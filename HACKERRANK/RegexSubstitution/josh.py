import re

n = int(input())
for i in range(n):
    line = input()
    pattern = r'(?<=\s)&&(?=\s)|(?<=\s)\|\|(?=\s)'
    output = re.sub(pattern,lambda x: 'and' if x.group() == '&&' else 'or',line)
    print(output)
