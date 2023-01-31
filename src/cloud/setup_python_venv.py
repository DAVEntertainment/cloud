"""
setup python virtual environment path
"""
import sys
from platform import system
from os.path import exists as existspath
from os.path import join as joinpath
from os.path import abspath, dirname


class WritePathFailed(Exception):
    """
    Write virtual environment path(.pth) file failed
    """

def get_path_file_path(env_root, path_file_name):
    """
    get path file path form given environment root
    """
    if system() == "Windows":
        site_package = joinpath(env_root, "Lib", "site-packages")
    else:
        print(f"system \"{system()}\" not supported")
        raise WritePathFailed(f"system \"{system()}\" not supported")
    return abspath(joinpath(site_package, path_file_name))

def write_path_file(env_root, path_file_name, paths = None):
    """
    write .path file for a virtual env
    """
    if paths is None:
        paths = []

    path_file_path = get_path_file_path(env_root, path_file_name)
    if existspath(path_file_path):
        with open(path_file_path, mode = 'r', encoding = 'utf-8') as stream:
            loaded = stream.read()
        for line in loaded.splitlines():
            if len(line) == 0:
                continue
            if existspath(line):
                print(f"found path {line} from {path_file_path}")
            else:
                print(f"path {line} from {path_file_path} not exists")
            if line not in paths:
                paths.append(line)
    print(f"write path to {path_file_path} ...")
    with open(path_file_path, mode = 'w', encoding = 'utf-8') as stream:
        for index, path in enumerate(paths):
            if index != 0:
                stream.write('\n')
            stream.write(path)

def main(args):
    """
    entry for setup venv (.pth)
    """
    paths = [
        abspath(joinpath(dirname(__file__), '..', '..'))
    ]
    for env_root in args:
        write_path_file(env_root, 'cloud.pth', paths)


if '__main__' == __name__:
    main(sys.argv[1:])

    print(r"system paths:")
    for p in sys.path:
        print(f"    {p}")
