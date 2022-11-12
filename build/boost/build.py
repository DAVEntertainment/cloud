"""
boost build entry
"""
import json
import sys
from types import SimpleNamespace
from subprocess import Popen
from os import chdir
from os.path import join as joinpath
from os.path import exists as existspath
from os.path import abspath, dirname
from logging import DEBUG, StreamHandler, FileHandler, getLogger


class BuildFailed(Exception):
    """
    Build Failed Exception
    """

class BoostBuilder:
    """
    Boost Builder
    """

    script_dir = abspath(dirname(__file__))
    config_file = joinpath(script_dir, 'boost.json')
    log_file = joinpath(script_dir, 'build.log')
    components = [
        'atomic',
        'chrono',
        'container',
        'context',
        'contract',
        'coroutine',
        'date_time',
        'exception',
        'fiber',
        'filesystem',
        'graph',
        'graph_parallel',
        'headers',
        'iostreams',
        'json',
        'locale',
        'log',
        'math',
        'mpi',
        'nowide',
        'program_options',
        # 'python',
        'random',
        'regex',
        'serialization',
        'stacktrace',
        'system',
        'test',
        'thread',
        'timer',
        'type_erasure',
        'wave',
    ]

    def __init__(self):
        self.args = ()
        self.config = self.get_default_config()
        self.__setup_logger()

    def __setup_logger(self):
        logger = self.__logger = getLogger('boost_builder')
        logger.addHandler(StreamHandler())
        logger.addHandler(FileHandler(self.log_file, mode = 'w', encoding = 'utf-8'))
        logger.level = DEBUG

    def __dump_config(self):
        with open(self.config_file, mode = 'w', encoding = 'utf-8') as stream:
            json.dump(self.config.__dict__, stream, indent = 4)

    def __load_config(self):
        config = self.config
        with open(self.config_file, mode = 'r', encoding = 'utf-8') as stream:
            str_loaded = stream.read()
        if len(str_loaded) == 0:
            str_loaded = r"{}"
        config_loaded = json.loads(str_loaded)
        config.__dict__.update(config_loaded)
        return config

    def __format_config(self):
        return json.dumps(self.config.__dict__, indent = 4)

    def __confirm_and_continue(self):
        confirm = input(r"confirm and continue? [Y]/N ")
        if confirm in ('Y', 'y', ''):
            return True
        return False

    def __make_b2_cmd(self, build_dir, install_dir, config):
        b2_cmd = [
            'b2',
            f'toolset={config.toolset}',
            f'threading={config.threading}',
            f'architecture={config.architecture}',
            f'address-model={config.address_model}'
        ]

        if config.build_static:
            b2_cmd.append('link=static')
        else:
            b2_cmd.append('link=shared')

        if config.link_static:
            b2_cmd.append('runtime-link=static')
        else:
            b2_cmd.append('runtime-link=shared')

        b2_cmd.append(f'--prefix={install_dir}')
        b2_cmd.append(f'--build-dir={build_dir}')
        b2_cmd.append('--build-type=complete')

        for component in self.components:
            b2_cmd.append(f'--with-{component}')

        return b2_cmd

    def __format_b2_cmd(self, b2_cmd, indent = 4):
        indent_str = ('{:' + str(indent) + '}').format('')
        return ('\n' + indent_str).join(b2_cmd)

    def get_default_config(self):
        """
        get default config of builder
        """
        config = SimpleNamespace()

        # build config
        config.whole_procedure = True
        config.do_nothing = False
        config.run_bootstrap = False
        config.clean = False
        config.build_static = False
        config.link_static = False
        config.toolset = 'msvc-14.2'
        config.threading = 'multi'
        config.architecture = 'x86'
        config.address_model = '64'
        # for toolset, we have
        #  Visual Studio 2019-14.2
        #  Visual Studio 2017-14.1
        #  Visual Studio 2015-14.0
        #  Visual Studio 2013-12.0
        #  Visual Studio 2012-11.0
        #  Visual Studio 2010-10.0
        #  Visual Studio 2008-9.0
        #  Visual Studio 2005-8.0
        #  Visual Studio .NET 2003-7.1
        #  Visual Studio .NET-7.0
        #  Visual Studio 6.0, Service Pack 5-6.5
        # see more:
        # https://www.boost.org/doc/libs/1_78_0/tools/build/doc/html/index.html#bbv2.reference.tools.compiler.msvc

        # boost repo config
        config.repo = r"https://github.com/boostorg/boost.git"
        config.tag = r"boost-1.80.0"
        config.version = r"1.80.0"
        config.install_dir_name = f"boost-{config.version}"

        # flow control
        config.ask_before_continue = True
        return config

    def setup(self, args):
        """
        setup builder
        """
        self.args = args
        self.__load_config()
        self.__dump_config()
        return self

    def log(self, msg):
        """
        log
        """
        self.__logger.info(msg)

    def run_cmd(self, cmd):
        """
        run cmd with log
        """
        self.log(f"running cmd: {cmd}")
        if self.config.do_nothing:
            self.log("skipping cause --do-nothing detected")
            return
        with Popen(cmd) as proc:
            proc.communicate()
            self.log(f"return code {proc.returncode}")
            if proc.returncode != 0:
                raise BuildFailed(f"run cmd \"{cmd}\" failed with code {proc.returncode}")

    def main(self):
        """
        main procedure of building boost
        """
        config = self.config
        run_cmd = self.run_cmd
        log = self.log

        repo_dir = joinpath(self.script_dir, f"boost-{config.version}")
        build_dir = joinpath(repo_dir, 'build')
        install_dir = abspath(joinpath(self.script_dir, '..', '..', config.install_dir_name))
        b2_cmd = self.__make_b2_cmd(build_dir, install_dir, config)

        log(f"starting with: {self.args}")
        log(f"repo {config.repo}")
        log(f"source {repo_dir}")
        log(f"build in {build_dir}")
        log(f"install to {install_dir}")
        log(f"log into {self.log_file}")
        log(f"config: {self.__format_config()}")
        log(f"b2 command: {self.__format_b2_cmd(b2_cmd)}")
        log(r"")

        if config.ask_before_continue and not self.__confirm_and_continue():
            return

        if config.whole_procedure:
            if not existspath(repo_dir):
                run_cmd([
                    'git', 'clone', config.repo,
                    '--single-branch', '--branch', config.tag,
                    repo_dir
                ])

        log(f"Entering {repo_dir}")
        chdir(repo_dir)

        if config.whole_procedure or config.clean:
            run_cmd(['git', 'clean', '-dfx'])
            run_cmd(['git', 'submodule', 'foreach', 'git', 'clean', '-dfx'])

        run_cmd(['git', 'checkout', config.tag])
        run_cmd(['git', 'reset', '--hard'])
        run_cmd(['git', 'submodule', 'update', '--init', '--recursive'])
        run_cmd(['git', 'submodule', 'foreach', 'git', 'reset', '--hard'])

        if config.run_bootstrap or config.whole_procedure or config.clean:
            run_cmd(['bootstrap.bat'])

        run_cmd(b2_cmd + ['variant=release','install'])
        run_cmd(b2_cmd + ['variant=debug', 'install'])


if '__main__' == __name__:
    BoostBuilder().setup(sys.argv[1:]).main()
