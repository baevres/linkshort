import re
from random import randrange


char = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
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
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
    ]
char2 = [i.upper() for i in char[10:len(char)]]
char = char + char2 # add to char list with uppercase letters


def generator():
    """
    Function will create list res (len(res) == 1) which have string (len(res[0]) == 6).
    Circle <for> create random range of one- or two-digit numbers and then res uses numbers as index for list char.
    Random have range from 0 to 61 - cause len(char) == 62. For example:
    rnd = [12, 5, 27, 49, 37, 61]
    res = ['c5rNBZ']
    """
    res = []

    for x in range(6):
        rnd = randrange(0, 62, 1)
        if x == 0:
            res += char[rnd]
        else:
            res[0] += char[rnd]
    yield res


def search(text):
    """
    Function divide url between domain and body. For example:
    origin_url = 'https://www.google.com.ua/webhp?tab=ww&ei=LltCVIvrDOrnygOd5IGABw&ved=0CAYQ1S4'
    search() will return list - ['https://www.google.com.ua/', 'webhp?tab=ww&ei=LltCVIvrDOrnygOd5IGABw&ved=0CAYQ1S4']
    """
    pattern1 = r'^.*\.\w+/'
    result1 = re.findall(pattern1, text)

    pattern2 = r'\.\w+/(.+$)'
    result2 = re.findall(pattern2, text)
    if result1 and result2:
        return result1 + result2
    return

