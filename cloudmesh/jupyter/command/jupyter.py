from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE


class JupyterCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_jupyter(self, args, arguments):
        """
        ::

          Usage:
                jupyter start USER HOST PORT
                jupyter stop
                jupyter open

          This command can start a jupyter notebook on a remote machine and
          use it in your browser.

          Arguments:
             USER   The username on the remote machine
             HOST   The hostname of the remote machine
             PORT   The port of the remote machine

        """

        if arguments.start:
            pass
        elif arguments.stop:
            pass
        elif arguments.open:
            pass
        return ""
