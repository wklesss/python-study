s1 = 'hello, world!'
s2 = 'hello, python!'
s3 = """
hello,
world!
"""

print(s1, s2, s3, end='')

# 转义符
s4 = '\'hello, world!\''
s5 = '\n\\hello, world!\\\n'
print(s4, s5, end='')

s6 = '\141\142\143\x61\x62\x63'
s7 = '\u9a86\u660a'
print(s6, s7)

s8 = r'\'hello, world!\''
s9 = r'\n\\hello, world!\\\n'
print(s8, s9, end='')