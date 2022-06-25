(TeX-add-style-hook "3-fixed"
 (lambda ()
    (TeX-run-style-hooks
     "hyperref"
     "alltt"
     "microtype"
     "pdfpages"
     "graphicx"
     "parallel"
     "inputenc"
     "utf8x"
     "ucs"
     "mathletters"
     "latex2e"
     "memoir10"
     "memoir"
     "article"
     "twoside"
     "10pt")))

