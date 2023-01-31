"""
lint utils
"""
from os import walk
from os.path import join as joinpath

def split_modules(roots):
    """
    Split modules into submodules

    signature:
        split_modules(roots)

    params:
        roots           root list to search
    """
    submodules = []
    for module_root in roots:
        for _, module_subs, _ in walk(module_root):
            for sub in module_subs:
                submodules.append(joinpath(module_root, sub))
            break
    return submodules
