
import re

def toName(number):
        list = {}
        for line in open('ethernettype.txt'):
                result = re.findall(r'([^\t\n]+)+',line)
                list[int(result[0],16)] = result[1]
        return list[number]
