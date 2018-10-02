import re

line_re = re.compile(r'(.+)\t(.*)\t(.*)', re.I)

def parse_text() -> str:
    with open('tg-api-methods.txt', 'r') as f:
        lines = f.read().split('\n')

    res = []

    for line in lines:
        match = line_re.match(line)
        a, b, c = match.groups()

        assert b != '' or c != ''

        if b == 'ao':
            res.append(f"{a} = method_array_of_entity('{a}', {c})")
        elif b == 'raw':
            res.append(f"{a} = method_raw('{a}')")
        else:
            res.append(f"{a} = method_entity('{a}', {c})")

    return '\n'.join(res)

def main():
    print(parse_text())

if __name__ == '__main__':
    main()