import re
import datetime


def decoder(text):
    hsh = abs(hash(text))
    res = list(str(hsh))[:6]

    char = ['.',
              'a',
              'b',
              'c',
              'd',
              'e',
              'f',
              'g',
              'h',
              'i',
              'j',
              'k',
              'l',
              'm',
              'n',
              'o',
              'p',
              'q',
              'r',
              't',
              'u',
              'v',
              'w',
              'x',
              'y',
              'z']

    new_hash = []

    for x in range(len(res)-1):
        if x == 0:
            new_hash += char[int(res[x])]
        new_hash[0] += res[x]
    return new_hash[:5]


def search(text):
    pattern1 = r'^.*\.\w+/'
    result1 = re.findall(pattern1, text)

    pattern2 = r'\.\w+/(.+$)'
    result2 = re.findall(pattern2, text)

    return result1 + result2

# now = datetime.datetime.now()
# then = now + datetime.timedelta(hours=1)
# if now.time() < then.time():
#     print('Yes')

