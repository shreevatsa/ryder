#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Remove <code> from file
'''

import sys, re, codecs

# sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)

# for l in sys.stdin.readlines():
#     n = l.decode('UTF-8')
#     pages = re.findall('\(\d+\)$', n)
#     if pages:
#         assert len(pages)==1
#         n = n.replace(pages[0], '').rstrip()
#         n = n + ' '*(70 - len(n)) + pages[0]
#     sys.stdout.write(n)


for l in sys.stdin.readlines():
    n = l
    n = n.replace('<code>', '')
    n = n.replace('</code>', '')
    n = re.sub('_([^_]*)_', '<i>\\1</i>', n) #Italics _in extremis_
    sys.stdout.write(n)
