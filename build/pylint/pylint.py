"""
pylint entry
"""
import sys
from os.path import exists as existspath
from os.path import join as joinpath
from os.path import abspath, dirname
from types import SimpleNamespace
from build.pyutils.path_utils import glob_files
from build.pyutils.lint_utils import split_modules
from build.pyutils.shell_utils import run_cmd


class LintFailed(Exception):
    """
    lint failed
    """


def run_lint(config):
    """
    run pylint
    """
    statistics = {}
    for module in config.modules:
        print(f"pylint running for {module.root}")
        module_stats = statistics[module.root] = {}

        files = glob_files(
            roots = (module.root, ),
            check_postfix = config.post_fix,
            skip_dirs = config.skip_dirs,
            skip_files = config.skip_files,
            depth = module.depth
        )

        module_stats['files'] = len(files)
        if len(files) > 0:
            module_stats['code'] = run_cmd(f"{sys.executable} -m pylint {' '.join(files)}")
        else:
            print(r"no files found for pylint")
            module_stats['code'] = 0
    return statistics

def analyze_summary(statistics):
    """
    analyze pylint summary
    """
    summary = SimpleNamespace()
    summary.summary = SimpleNamespace()
    summary.modules = statistics

    for module, module_stats in statistics.items():
        module_stats['success'] = module_stats['code'] == 0

    summary.summary.modules = len(statistics)
    summary.summary.success = sum((
        module_stats['code'] == 0 for module, module_stats in statistics.items()
    ))

    return summary

def print_summary(summary):
    """
    print summary
    """
    print(r"pylint summary:")
    print(r"  summary:")
    print(f"    modules: {summary.summary.modules}")
    print(f"    success: {summary.summary.success}")
    for module, module_stas in summary.modules.items():
        print(f"  module {module}")
        print(f"    code   : {module_stas['code']}")
        print(f"    success: {module_stas['success']}")
        print(f"    files  : {module_stas['files']}")

def main():
    """
    pylint entry
    """
    print("start from cloud pylint entry")

    config = SimpleNamespace()
    config.repo_root = abspath(joinpath(dirname(__file__), '..', '..'))
    config.packages_root = abspath(joinpath(config.repo_root, 'packages'))

    config.build_root = joinpath(config.repo_root, 'build')
    config.modules = []

    for module in split_modules((config.build_root, )):
        lint_module = SimpleNamespace()
        lint_module.root = module
        if existspath(joinpath(module, '.util')):
            lint_module.depth = 9999
            print(f"found util module: {module}")
        else:
            lint_module.depth = 1
            print(f"found repo module: {module}")
        config.modules.append(lint_module)

    packages_module = SimpleNamespace()
    packages_module.root = config.packages_root
    packages_module.depth = 1
    config.modules.append(packages_module)

    config.post_fix = ('.py', )
    config.skip_dirs = ('__pycache__', )
    config.skip_files = ()

    statistics = run_lint(config)
    summary = analyze_summary(statistics)
    print_summary(summary)

    if summary.summary.modules != summary.summary.success:
        raise LintFailed()


if "__main__" == __name__:
    main()
