#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Fix indentation in file
'''

import sys, re

last = ''

for l in sys.stdin.readlines():

    #Type of line

    if l[0] in ['<','>',' ','\n','#']:
        #Not a verse line
        sys.stdout.write(l)
        last = 'ignore'

    else:
        #A verse line

        if last=='just':
            indent = ' '*6
            last = 'more'
        else:
            indent = ' '*4
            last = 'just'

        sys.stdout.write(indent+l)

#     elif l[0] in (['%c'%x for x in
#                   range(ord('a'),ord('z')+1)+
#                   range(ord('A'),ord('Z')+1)]+
#                   ['(', '"', '“', '*', "'"]):
#         pass
#     else:
#         sys.stdout.write('    '+l)





