"""
shell utils
"""
from subprocess import Popen

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
