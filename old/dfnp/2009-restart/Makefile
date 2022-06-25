web:
	python pre-pandoc-fix.py < complete-ryder.txt > 1-for-pandoc.txt
	pandoc -Ss -c mystyle.css --toc 1-for-pandoc.txt -o 2-pandoc2tidy.html
	tidy -utf8 -icq -o 3-tidy2post.html 2-pandoc2tidy.html
	python post-pandoc-fix.py --without-images <3-tidy2post.html > ryder.html
	python post-pandoc-fix.py --with-images < 3-tidy2post.html > ryder-hertel.html
# 	python post-pandoc-fix.py --with-images < 3-tidy2post.html > test.html

tex:
	python pre-pandoc-fix.py -t < complete-ryder.txt > 1-for-pandoc-tex.txt
	pandoc -Ss --toc -w latex -C header.txt 1-for-pandoc-tex.txt -o 2-pandoc2tex.tex
# 	python tex-fix.py --with-images < 2-pandoc2tex.tex > 3-fixed.tex
	python tex-fix.py --without-images < 2-pandoc2tex.tex > 3-fixed.tex

clean:
	rm 3-fixed.{aux,log,out,pdf,synctex.gz*(N),toc}

%.html: %.txt
	python pre-pandoc-fix.py < $< > 1-for-pandoc.txt
	pandoc -Ss -c mystyle.css --toc 1-for-pandoc.txt -o 2-pandoc2tidy.html
	tidy -utf8 -icq -o 3-tidy2post.html 2-pandoc2tidy.html
	python post-pandoc-fix.py --with-images < 3-tidy2post.html > $@

separate:
	python split.py < complete-ryder.txt
