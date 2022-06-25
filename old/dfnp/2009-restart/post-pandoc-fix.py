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
        if '[' in n:
            n = re.sub("^(.*)\[(.*)\]",
                       #'<span class="pagenum"><a href="hertel/resized/00000\\2.png"><img src="hertel/00000\\2.png"/></a></span>\\1',
                       #'</div><div class="page"><span class="pagenum"><a href="hertel/resized/00000\\2.png"><img src="hertel/00000\\2.png"/></a></span>\\1',
                       '<span class="pagenum"><a href="hertel/resized/00000\\2.png">[f]</a><br/><img id="x\\2" src="hertel/00000001.png" onclick=\'document.getElementById("x\\2").src = "hertel/00000\\2.png";\'/></span>\\1',
                       n)
    else:
        n = re.sub("\[(.*)\]", "", n)

    sys.stdout.write(n)
