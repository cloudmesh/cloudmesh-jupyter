from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from cloudmesh.common.util import backup_name
from cloudmesh.common.util import yn_choice
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.Printer import Printer
import os
from cloudmesh.jupyter.Jupyter import Jupyter

class JupyterCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_jupyter(self, args, arguments):
        """
        ::

          Usage:
                jupyter lab HOST PORT [DIR]
                jupyter tunnel HOST PORT
                jupyter stop HOST PORT
                jupyter open PORT
                jupyter info [PORT]
                jupyter backup

          This command can start a jupyter notebook on a remote machine and
          use it in your browser.

          Arguments:
             USER   The username on the remote machine
             HOST   The hostname of the remote machine
             PORT   The port of the remote machine
             DIR    The directory where the notebooks are located

          Description:

            Step 1: Setting up a .bash_profile file

             If you have your python venv set up you need to add it to the
             .bash_profile on your remote machine. A possible
             profile file could look as follows:

                if [ -f ~/.bash_aliases ]; then
                     . ~/.bash_aliases
                 fi

                 export PATH=$HOME/ENV3/bin:$PATH
                 source $HOME/ENV3/bin/activate

            Step 2: Start the remote notebook server in a terminal

                Note: After the start you will not be able to use that terminal

                cms jupyter start HOST PORT

                Thsi command will aslo establich an SSH tunel and open in
                the web browser jupyter lab

        """

        VERBOSE(arguments)

        jupyter = Jupyter(arguments.HOST, arguments.PORT, arguments.DIR)

        if arguments.lab:

            jupyter.start()

        if arguments.tunnel:

            jupyter.tunnel()

        elif arguments.stop:
            jupyter.stop()
            data = jupyter.info()
            print (Printer.attribute(data))

        elif arguments.open:
            jupyter.open()

        elif arguments.test:
            jupyter.test()

        elif arguments.info:
            data = jupyter.info()
            print (Printer.attribute(data))

        elif arguments.backup:

            data = jupyter.info()
            data.backup = backup_name(data['cwd'])
            print ("Generate backup")
            print (f"From: {data.cwd}")
            print (f"To:   {data.backup}")
            if yn_choice("Continue"):
                os.system(f"cp -r -v {data.cwd} {data.backup}")
                Console.ok(f"Backup created at: {data.backup}")

        return ""
