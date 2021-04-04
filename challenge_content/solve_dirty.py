import os
import re
from functools import partial
from pprint import pprint

base2 = partial(int, base=2)
file_contents = []

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

file_dir = 'kartaca'
for filename in os.listdir(file_dir):
    with open(os.path.join(file_dir, filename)) as f:
        content = ''.join(map(chr, map(base2, f.read().split())))
        file_contents.append((filename, content))



def key_func(tup):

    word = tup[0]
    second_char = 'AQ'
    third_char = 'AEIMQUYcgk'
    fourth_char = 'wxyz012345'
    return word[:2], third_char.find(word[2]), fourth_char.find(word[3])


file_contents.sort(key=key_func)

keys = ('\t'.join(key for key, word in file_contents if 'k' in key))
words = ('\t'.join(word for key, word in file_contents if 'k' in key))

for kl, wl in zip(keys.split('\t'), words.split('\t')):
    print(kl, wl)

words = (''.join(word for key, word in file_contents if '=' in key[-2] ))
print(words)
words = (''.join(word for key, word in file_contents if '=' in key[-1] and '=' not in key[-2] ))
print(words)
words = (''.join(word for key, word in file_contents if '=' not in key ))
print(words)
pprint({word[2] for word, _ in file_contents})
pprint({word[3] for word, _ in file_contents})
words = {}
di = dict(file_contents)
for k, v in dict(file_contents).items():
    words[v] = words.get(v, []) + [k]
# words = (''.join(word if key!="NDc5" else key for key, word in file_contents if all(i not in key for i in '=')))
# words = (''.join(f'{key} {word}\n' for key, word in file_contents if all(i not in key for i in '=')))
# pprint(file_contents)
# def join_if_matches(li, pattern):
    # new_li = []
    # for i, (k, v) in enumerate(li):
        # if re.match(pattern, k):
            # new_li[-1] = new_li[-1][0], new_li[-1][1]+v
        # else:
            # new_li.append((k, v))

    # return new_li

# file_contents.sort()
# result = join_if_matches(file_contents, r'.*[12345]$')
# result = join_if_matches(result, r'.*[wxyz]$') 
