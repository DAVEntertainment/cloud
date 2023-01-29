"""
EnvConfig
"""


class EnvConfig:
    """
    environment config
    """

    toolset_shortcut_map = {
        "Visual Studio 16 2019": "msvc16",  # based on CMake definition
        "Visual Studio 2019": "msvc16",  # based on CMake definition
        "Visual Studio 16": "msvc16",  # based on CMake definition
    }

    runtime_shortcut_map = {
        "Multithreaded": "mt",
        "Multithreaded Debug": "mtd",
        "Multithreaded Dll": "md",
        "Multithreaded Dll Debug": "mdd",
    }

    def __init__(self):
        self.system = "Windows"
        # *Windows
        # Ubuntu
        # CentOS
        self.architecture = "x86"
        # *x86
        self.address_mode = "64"
        # 32
        # *64
        self.toolset = "Visual Studio 16 2019"
        # *Visual Studio 16 2019
        # gcc 4
        self.runtime = "Multithreaded"
        # *Multithreaded (mtD will be available in debug)
        # Multithreaded Dll (mdD will be available in debug)
        self.static = None
        # *None - build static library
        # True - build static library
        # False - build shared library
        self.debug = None
        # *None - debug && release binaries in the same directory
        # True - only contains debug binaries
        # False - only contains release binaries

    @property
    def toolset_shortcut(self):
        """
        get toolset short name
        """
        return self.toolset_shortcut_map.get(self.toolset, self.toolset)

    @property
    def runtime_shortcut(self):
        """
        get runtime  short name
        """
        return self.runtime_shortcut_map.get(self.runtime, self.runtime)


class EnvNameRule:
    """
    environment name rule
    """
    @staticmethod
    def get_name_rule():
        """
        get environment name rule
        """
        return r"{sys}_{arch}_{addr_mod}_{toolset}_{runtime}"

    @staticmethod
    def get_name(env_config):
        """
        get environment name from given configuration by environment name rule
        """
        name = EnvNameRule.get_name_rule().format(
            sys = env_config.system.lower(),
            arch = env_config.architecture,
            addr_mod = env_config.address_mode,
            toolset = env_config.toolset_shortcut,
            runtime = env_config.runtime_shortcut,
        )
        return name
