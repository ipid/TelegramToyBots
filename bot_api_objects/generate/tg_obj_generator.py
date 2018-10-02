from typing import Dict, List, Tuple
import json, keyword

def text_parse() -> Dict[str, Dict[str, str]]:
    with open('telegram-api-types.txt', 'r') as f:
        lines = f.read().split('\n')

    res: Dict[str, Dict[str, str]] = dict()
    target: Dict[str, str] = None
    target_name: str = ''

    for line_row in lines:
        line = line_row.strip()
        if line == '':
            res[target_name] = target
        elif '\t' not in line:
            if line in res:
                raise ValueError(f"{line} duplicated")
            target = dict()
            target_name = line
        else:
            prop_ptype: List[str] = line.split('\t')
            target[prop_ptype[0]] = prop_ptype[1]

    return res

def raw_to_pytype(t: str) -> Tuple[str, bool]:
    if ' ' in t:
        raise ValueError("Space in type.")

    lookup = {
        'String': 'str',
        'Integer': 'int',
        'Float': 'float',
        'True': 'bool',
        'Boolean': 'bool'
    }

    parsed_type = lookup.get(t)
    if parsed_type is not None:
        return parsed_type, True

    return t, False

def purge_member_name(name: str, raw_type: str) -> str:
    if name in keyword.kwlist:
        return name + '_' + raw_type.lower()
    return name

def generate_class_code(name: str, members: Dict[str, str]) -> str:
    slots = tuple(purge_member_name(x, y) for x, y in members.items())
    res = f'''class {name}(TelegramObject):
    __slots__ = {slots}

    def __init__(self, params: Dict[str, Any]) -> None:
'''

    for member, raw_type in members.items():
        if 'Array of Array of ' in raw_type:
            pytype, is_builtin = raw_to_pytype(raw_type[len('Array of Array of '):])
            hint = f"List[List[{pytype}]]"
            if not is_builtin:
                val = f"array_of_array_of({pytype}, params.get('{member}'))"
            else:
                val = f"params.get('{member}')"
        elif 'Array of ' in raw_type:
            pytype, is_builtin = raw_to_pytype(raw_type[len('Array of '):])
            hint = f"List[{pytype}]"
            if not is_builtin:
                val = f"array_of({pytype}, params.get('{member}'))"
            else:
                val = f"params.get('{member}')"
        else:
            pytype, is_builtin = raw_to_pytype(raw_type)
            hint = f"{pytype}"
            if not is_builtin:
                val = f"{pytype}(params.get('{member}'))"
            else:
                val = f"params.get('{member}')"

        res += f"        self.{purge_member_name(member, raw_type)}: Optional[{hint}] = {val} if '{member}' in params else None\n"

    res += '\n'
    return res

def main() -> None:
    types = text_parse()

    with open('../__init__.py', 'w') as f:
        f.write('''from typing import Dict, Any, List, Optional
from .array_parser import *

class TelegramObject:
    pass

''')
        for name, members in types.items():
            f.write(''.join(generate_class_code(name, members)))

def debug():
    print(json.dumps(text_parse()))

if __name__ == '__main__':
    # debug()
    main()
