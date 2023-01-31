"""
shell utils
"""
import shlex

from subprocess import Popen, PIPE
from platform import system


def __black_hole(*args, **kwars):
    pass


def run_cmd(cmd, print_func = print, **kwargs):
    """
    run cmd with log

    signature:
        run_cmd(cmd)

    params:
        cmd         command to execute
    """
    print_func = __black_hole if print_func is None else print_func
    print_func(cmd)
    with Popen(
        cmd if system() == "Windows" else shlex.split(cmd),
        **kwargs
    ) as proc:
        proc.communicate()
        print_func(f"return {proc.returncode}")
        return proc.returncode

def run_cmd_with_log(cmd, print_func = print, **kwargs):
    """
    run cmd with log

    signature:
        run_cmd_with_log(cmd)

    params:
        cmd         command to execute
    """
    print_func = __black_hole if print_func is None else print_func
    print_func(cmd)
    with Popen(
        cmd if system() == "Windows" else shlex.split(cmd),
        stdout = PIPE, stderr = PIPE,
        shell = (system() == "Windows"),
        **kwargs
    ) as proc:
        stdout, stderr = proc.communicate()
        print_func(f"return {proc.returncode}")
        print_func(f"stdout {stdout}")
        print_func(f"stderr {stderr}")
        return proc.returncode, stdout, stderr
