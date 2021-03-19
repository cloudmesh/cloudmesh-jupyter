import os
from cloudmesh.common.Shell import Shell

class Jupyter:

    def __init__(self, user:str, host:str, port:int, directory:str):
        self.user = user
        self.port = port
        self.host = host
        self.directory = directory or ""

    def start(self):
        command = f'ssh -t {self.user}@{self.host} "source .bash_profile; jupyter-lab {self.directory} --no-browser --port={self.port}"'
        print(command)
        os.system(command)

    def stop(self):
        ValueError("not yet implemented")

    def tunnel(self):
        command = f"ssh -N -f -L localhost:{self.port}:localhost:{self.port} {self.user}@{self.host}"
        print (command)
        os.system(command)

    def open(self):
        location = f"https://localhost:{self.port}/lab?"
        print ("Open", location)
        Shell.browser(location)


    #  > /dev/null 2>&1 & echo $! > "dmr.pid"