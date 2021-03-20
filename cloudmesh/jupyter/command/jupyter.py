from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

from cloudmesh.jupyter.Jupyter import Jupyter

class JupyterCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_jupyter(self, args, arguments):
        """
        ::

          Usage:
                jupyter start USER HOST PORT [DIR]
                jupyter tunnel USER HOST PORT
                jupyter stop USER HOST
                jupyter open PORT
                jupyter test USER HOST PORT [DIR]

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

                cms jupyter start USER HOST PORT

            Step 3: Start the tunnel in a different terminal

                cms jupyter start USER HOST PORT

           Step 4: Open the jupyterlab

                copy the https address that you see in the terminal for step 1
                into your browser. It will look similar to

                    http://127.0.0.1:8888/lab?token=1234...abcd

                This does not  yet work
                cms jupyter open PORT

        """

        jupyter = Jupyter(arguments.USER, arguments.HOST, arguments.PORT, arguments.DIR)

        if arguments.start:

            jupyter.start()

        if arguments.tunnel:

            jupyter.tunnel()

        elif arguments.stop:
            jupyter.stop()

        elif arguments.open:
            jupyter.open()

        elif arguments.test:
            jupyter.test()

        return ""
