class EnvConfig:
    """
    """
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
        return ToolsetShortcut.GetShortcut(self.toolset)

    @property
    def runtime_shortcut(self):
        return RuntimeShortcut.GetShortcut(self.runtime)



class ToolsetShortcut:
    shortcut_map = {
        "Visual Studio 16 2019": "msvc16",  # based on CMake definition
        "Visual Studio 2019": "msvc16",  # based on CMake definition
        "Visual Studio 16": "msvc16",  # based on CMake definition
    }
    @classmethod
    def GetShortcut(cls, toolset):
        return cls.shortcut_map.get(toolset, toolset)


class RuntimeShortcut:
    shortcut_map = {
        "Multithreaded": "mt",
        "Multithreaded Debug": "mtd",
        "Multithreaded Dll": "md",
        "Multithreaded Dll Debug": "mdd",
    }
    @classmethod
    def GetShortcut(cls, runtime):
        return cls.shortcut_map.get(runtime, runtime)


class EnvNameRule:

    @staticmethod
    def GetNameRule():
        return r"{sys}_{arch}_{addr_mod}_{toolset}_{runtime}"

    @staticmethod
    def GetName(env_config):
        name = EnvNameRule.GetNameRule().format(
            sys = env_config.system.lower(),
            arch = env_config.architecture,
            addr_mod = env_config.address_mode,
            toolset = env_config.toolset_shortcut,
            runtime = env_config.runtime_shortcut,
        )
        return name
