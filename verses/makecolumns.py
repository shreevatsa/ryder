# -*- coding: utf-8 -*-

'''
Turn the {}{}{}{} thing into tables (for now).
'''

import re
import sys
import json

# def tupleFromString(s):
#     match = re.search(r'(\d).(.*)', s)
#     t = (int(match.group(1)), float(match.group(2)))
#     return t

# def stringFromTuple(t):
#     s = str(t[0]) + '.'
#     if int(t[1])==t[1]:
#         s += str(int(t[1]))
#     else:
#         s += str(t[1])
#     return s

def loadFromOrig(s):
    d = json.loads(s)
#     realkeys = [tupleFromString(n) for n in d.keys()]
#     for key in sorted(realkeys):
#         n = stringFromTuple(key)
#         #print '%s:' % n
#         dn = d[n].split('\n')
#         #for l in dn:
#         #    print '    %s' % l
    assert len(d)==324
    return d

def startTd(classname):
    return '<td>\n' + '<pre class="' + classname + '">\n'

def endTd():
    return '</pre>\n</td>\n'

curRyder = ''
def cleanUp():
    global curRyder
    if curRyder:
        #sys.stdout.write(startTd('Ryder') + curRyder + endTd())
        sys.stdout.write(curRyder + endTd())
        curRyder = ''

state = 0
intr = False
d = loadFromOrig(open('../bhartrhari/verses.json').read())
cur = ''
for l in sys.stdin.readlines():
    if state%2 == 0:            # Not inside a {}
        if l[0]=='\n':          # Blank line
            cleanUp()
            if intr:
                sys.stdout.write('</tr>\n')
                intr = False
            state = 0
        if l[0]=='{':
            if state==0:
                sys.stdout.write('<tr>\n')
                intr = True
            if state>-1:
                sys.stdout.write(startTd(['Ryder', 'Sanskrit', 'Other'][state/2]))
            state += 1
        else:
            sys.stdout.write(l) # The introductory sentences
    else:                       # Inside a {}
        if l[0]=='}':
            if state==2:
                #cleanUp()
                #sys.stdout.write(startTd('Sanskrit'))
                pass
            if state==1:        # Closed Ryder
                curRyder = cur; cur=''
                cleanUp()
            else:               # Closed something else
                sys.stdout.write(cur); cur = ''
                sys.stdout.write(endTd())
            state += 1
        else:
            match = re.search(r'^\|\| BharSt_(\d).(.*) \|\|', l)
            if match:
                name = match.group(1) + '.' + match.group(2)
                lines = d[name]['sa'].splitlines()
                cur += '  ' + ('\n  '.join(l.encode('UTF-8') for l in lines))
            else:
                cur += l
