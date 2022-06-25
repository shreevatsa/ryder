(TeX-add-style-hook "book1"
 (lambda ()
    (LaTeX-add-environments
     "pverse")
    (TeX-add-symbols
     '("story" 1)
     '("attrib" 1)
     '("sk" 1))
    (TeX-run-style-hooks
     "verse"
     "latex2e"
     "bk10"
     "book")))

