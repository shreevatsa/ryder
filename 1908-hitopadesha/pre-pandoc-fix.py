#!/usr/bin/env python

from optparse import OptionParser
import sys
import re

parser = OptionParser()
parser.set_defaults(strip_pagenum = False)
parser.add_option("-t", action="store_true", dest="for_tex")
(options, args) = parser.parse_args()

justblank = False
seen = []
level = 0
nlabels = 0
labels = []
for l in sys.stdin.readlines():
    n = l
    seen.append(n)
    assert(n)

    if justblank and n[0]!=' ': #Blankline followed by non-verse
        if options.for_tex:
            sys.stdout.write('\n\n')
        else:
            sys.stdout.write('<p class="parbreak"><br/></p>\n\n')

    #Deal with the {} metadata
    if not options.for_tex:
        n = re.sub('\s+[{]+','',n)
        n = re.sub('\s+[}]+','',n)
    else:
        if '{' in n:
            level += 1
            labels.append('s'+str(nlabels)); nlabels += 1
            n = re.sub('\s+[{]+','',n)
            n += '\label{'+labels[-1]+'}'
        elif '}' in n:
            n = re.sub('\s+[}]+',r'\\hyperref['+labels.pop()+r']{\qed}',n)
            level -= 1

    #Finally, what to do about the images?
    if options.for_tex:
        pages = re.findall('\[\d+\]$', n)
#         plain = re.sub('\s+\[\d+\]$', '', n)
#         if pages:
#             n = plain

    sys.stdout.write(n)
    justblank = n=='\n'
    if len(seen)>5:
        seen.pop(0)
