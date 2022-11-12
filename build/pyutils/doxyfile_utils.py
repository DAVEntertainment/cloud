"""
doxyfile utils
"""
import re

def search_var(content, var_name):
    """
    Search variable string in doxyfile

    """
    matched = re.findall(
        r"(^\s*(" + var_name + r"\s*)=(\s*(\".*\"|[\w\-\.\*\+]+)\s*\\?$)*)",
        content,
        re.MULTILINE
    )
    # print(matched)

    if len(matched) == 0:
        print(f"doxyfile option {var_name} not found")
        return None, None, None

    if len(matched) > 1:
        print(f"doxyfile option {var_name} multiple found:")
        for match in matched:
            print(f"  {match[0].strip()}")
        return None, None, None

    full_str, var_name_prefix, _, value_str = matched[0]
    return full_str.strip(), var_name_prefix, value_str


def replace_vars(content, **kwargs):
    """
    Replace variable string with given value in doxyfile
    """
    for key, value in kwargs.items():
        full_str, prefix, _ = search_var(content, key)
        if full_str is None:
            continue
        if isinstance(value, list):
            value_str_gen = ''
            indent = ("{:" + str(len(prefix) + 2) + "}").format(" ")
            for index, item in enumerate(value):
                value_str_gen += ("" if index == 0 else indent) + "{}{}".format(
                    item,
                    "" if index == len(value)-1 else " \\\n"
                )
            full_str_gen = f"{prefix}= {value_str_gen}"
        else:
            full_str_gen = f"{prefix}= {value}"
        content = content.replace(full_str, full_str_gen)
    return content
