"""
setup cloud
"""
from os import walk
from os.path import join as joinpath
from os.path import exists as existspath
from os.path import abspath, dirname
from types import SimpleNamespace
from subprocess import Popen


class SetupFailed(Exception):
    """
    setup cloud failed
    """


def run_cmd(cmd):
    """
    run cmd with log

    signature:
        run_cmd(cmd)

    params:
        cmd         command to execute
    """
    print(cmd)
    with Popen(cmd) as proc:
        proc.communicate()
        print(f"return code {proc.returncode}")
        return proc.returncode


def setup(config):
    """
    setup
    """
    for root, dirs, files in walk(config.packages_root):
        for file in files:
            if file.endswith('.7z'):
                ret = run_cmd(
                    f"{config.tool7z}"
                    + r" x -y"
                    + f" -o{config.extract_root}"
                    + f" {joinpath(root, file)}"
                )
                if 0 != ret:
                    raise SetupFailed(f"failed to extract {file}")


def default_builder_config():
    """
    default setup config
    """
    config = SimpleNamespace()

    # procedure control
    config.packages_root = abspath(dirname(__file__))
    config.repo_root = abspath(joinpath(config.packages_root, '..'))
    config.extract_root = config.repo_root
    config.tools_root = joinpath(config.repo_root, 'tools')
    config.tool7z = joinpath(config.tools_root, '7z-22.01.exe')

    return config

def main():
    """
    setup cloud main
    """
    print("start from cloud setup entry")
    config = default_builder_config()
    setup(config)


if "__main__" == __name__:
    main()
