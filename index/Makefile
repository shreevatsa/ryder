all:
	# pandoc -c style.css -s index.txt | tidy -utf8 -icq > index.html
	pandoc -s index.txt --variable=linestretch:1.5 --variable=mainfont:"Georgia, serif" --variable=fontsize:"20px" > index.html
	# echo index.txt | entr -s "pandoc -s index.txt > index.html"


