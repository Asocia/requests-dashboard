import os
from functools import partial

base2 = partial(int, base=2)
file_contents = []

file_dir = 'kartaca'
for filename in os.listdir(file_dir):
    with open(os.path.join(file_dir, filename)) as f:
        content = ''.join(map(chr, map(base2, f.read().split())))
        file_contents.append((filename, content))


def key_func(tup):
    word = tup[0]
    third_char = 'AEIMQUYcgk'
    fourth_char = 'wxyz012345'
    return word[:2], third_char.find(word[2]), fourth_char.find(word[3])


file_contents.sort(key=key_func)

words = (''.join(word for key, word in file_contents if '=' in key[-2]))
print(words)
words = (''.join(word for key, word in file_contents if '=' in key[-1] and '=' not in key[-2]))
print(words)
words = (''.join(word for key, word in file_contents if '=' not in key))
print(words)
