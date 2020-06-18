
all: main.pdf \
	pull

main.pdf: main.tex
	xelatex -shell-escape main.tex
	bibtex main.aux
	xelatex -shell-escape main.tex
	xelatex -shell-escape main.tex
	evince main.pdf&
pull: 
	git add .
	git commit -m'update'
	git pull
	git push
	chenchunyu
	tongtong.123

.PHONY:clean  
clean:
	-rm -fr *.ps *.dvi *.aux *.toc *.idx *.ind *.ilg *.log *.out *~ *.tid *.tms *.pdf *.bak *.blg *.bbl *.gz *.snm *.nav _minted*

