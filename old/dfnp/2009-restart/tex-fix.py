#!/usr/bin/env python

import sys, re

assert len(sys.argv)==2
images = {'--with-images' : True, '--without-images' : False}[sys.argv[1]]
imageStarted = False

for l in sys.stdin.readlines():
    n = l
    #Fix emdashes
    n = n.replace('---', r'{\textemdash}')
    n = n.replace('--', r'{\textemdash}')
    #and italics, like _in extremis_, but don't touch underscores in URLs
    if n.find('href') == -1:
        n = re.sub('_(.*)_', '\emph{\\1}', n)
    #Change "section", "subsection", "subsubsection" to "part", "chapter", "section"
    n = n.replace(r'\section', r'\part')
    n = n.replace(r'\subsection', r'\chapter')
    n = n.replace(r'\subsubsection', r'\section')

    #Sorry, have to special-case this
    n = n.replace(r'\chapter{Introduction}', r'\newpage\chapter{Introduction}')

    #Finally, what to do about the images?
    pages = re.findall('\[(\d+)\][^{]', n) #They may not be at the end of line after Pandoc's done with it
    plain = re.sub('\s*\[\d+\]([^{])', r'\1', n)
    if pages and images:
        #head = ('}\\ParallelRText{ ' + pages[0] + '}\\end{Parallel}\n''' if imageStarted else '')
        #head = ('}\\ParallelRText{\includegraphics{hertel/resized/00000' + pages[0] + '}}\\end{Parallel}\n''' if imageStarted else '')
        #n =  head + '\\begin{Parallel}[p]{}{}\n' + '\\ParallelLText{' + plain

        #n = r'\begin{figure}[p]\includegraphics[width=\textwidth]{hertel/resized/00000' + pages[0] + '}\end{figure}' + plain
        n = r'\includepdf[pages=' + pages[0] + r']{hertel/all.pdf}' + plain
        imageStarted = True
    elif pages:
        #n = r'\newpage' + '\n' + plain
        n = plain
    else:
        n = plain

    sys.stdout.write(n)
