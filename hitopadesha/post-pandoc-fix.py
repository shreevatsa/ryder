#!/usr/bin/env python

import sys, re

assert len(sys.argv)==2
images = {'--with-images' : True, '--without-images' : False}[sys.argv[1]]

#Replace <pre><code> blocks with just <pre> blocks. Also re-add smart dashes to them, and images
incode = False
for l in sys.stdin.readlines():
    n = l
    if "<code>" in n:
        assert incode == False
        incode = True
        n = n.replace('<code>', '')
    elif "</code>" in n:
        assert incode == True
        incode = False
        if n=="</code>\n": continue
        n = n.replace('</code>', '')

    if incode:
        n = n.replace('--', '&mdash;')
        n = re.sub('_([^_]*)_', '<i>\\1</i>', n) #Italics _in extremis_

    if images:
        n = re.sub("\[(.*)\]",
                   '</div><div class="page"><span class="pagenum"><img src="H-\\1.png" alt="page image \\1"/></span>',
                   n)
    else:
        n = re.sub("\[(.*)\]", "", n)

    sys.stdout.write(n)
