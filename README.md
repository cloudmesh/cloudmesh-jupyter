Documentation
=============


[![image](https://img.shields.io/travis/TankerHQ/cloudmesh-jupyter.svg?branch=main)](https://travis-ci.org/TankerHQ/cloudmesn-jupyter)

[![image](https://img.shields.io/pypi/pyversions/cloudmesh-jupyter.svg)](https://pypi.org/project/cloudmesh-jupyter)

[![image](https://img.shields.io/pypi/v/cloudmesh-jupyter.svg)](https://pypi.org/project/cloudmesh-jupyter/)

[![image](https://img.shields.io/github/license/TankerHQ/python-cloudmesh-jupyter.svg)](https://github.com/TankerHQ/python-cloudmesh-jupyter/blob/main/LICENSE)

see cloudmesh.cmd5

* https://github.com/cloudmesh/cloudmesh.cmd5


```python
$ pip install cloudmesh-jupyter
$ cms help jupyter
```


```
cms jupyter

  Usage:
        jupyter start USER HOST PORT [DIR]
        jupyter tunnel USER HOST PORT
        jupyter stop USER HOST
        jupyter open PORT

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

        Thsi command will aslo establich an SSH tunel and open in
        the web browser jupyter lab

```