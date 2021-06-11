import os
from cloudmesh.common.Shell import Shell
# from yamldb import YamlDB
from subprocess import Popen
from cloudmesh.common.util import path_expand
from subprocess import PIPE
from subprocess import STDOUT
from cloudmesh.common.dotdict import dotdict
import shlex
from pathlib import Path

class Jupyter:


    def __init__(self, host:str, port:int, directory:str):
        self.port = port
        self.host = host
        self.directory = directory or ""

        # self.db = YamlDB("~/.cloudmesh/jupyter.yml")

    def info(self):

        data = dotdict({
            "hostname": Shell.run("hostname"),
            "repo": Shell.run("git config --get remote.origin.url"),
            "python": Shell.run("which python"),
            "user": Shell.run("whoami"),
            "cwd": path_expand(os.curdir),
            "home": str(Path.home()),
            "port": self.port,
            "tunnel": None
        })

        data.workdir = data.cwd.replace(f"{data.home}/", "")

        if self.port is not None:
            netstat = Shell.run(f"netstat -tulpen")
            for line in  netstat.splitlines():
                if self.port in line and "127.0.0.1" in line:
                    data.tunnel = line.strip().split(" ")[-1].split("/")[0]

        return data

    def start(self):
        command = f"source .bash_profile; jupyter-lab {self.directory} --no-browser --port={self.port} 2>&1"
        print (command)
        p = Popen(['ssh', '-T', f'{self.host}', command],
                   stdin=PIPE, stdout=PIPE, stderr=PIPE,
                   universal_newlines=True)
        p.stdin.flush()
        while True:
            l = p.stdout.readline().strip()
            if l != None and l != "" and l.startswith("or http://127.0.0.1"):
                # print (f"{l}")
                url = l.split(" ")[1]
                self.tunnel()
                Shell.browser(url)

    def stop(self):
        os.system(f"ssh {self.host} killall jupyter-lab")
        data = self.info()
        if data.tunnel is not None:
            os.system(f"kill -9 {data.tunnel}")

    def tunnel(self):
        command = f"ssh -N -f -L localhost:{self.port}:localhost:{self.port} {self.host}"
        print (command)
        os.system(command)

    def open(self):
        location = f"https://localhost:{self.port}/lab?"
        print ("Open", location)
        Shell.browser(location)


    #  > /dev/null 2>&1 & echo $! > "dmr.pid"