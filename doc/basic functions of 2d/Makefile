
all: space-2d.pdf \


space-2d.pdf: space-2d.tex
	xelatex -shell-escape space-2d.tex
	bibtex space-2d.aux
	xelatex -shell-escape space-2d.tex
	xelatex -shell-escape space-2d.tex
	evince space-2d.pdf&

.PHONY:clean  
clean:
	-rm -fr *.ps *.dvi *.aux *.toc *.idx *.ind *.ilg *.log *.out *~ *.tid *.tms *.pdf *.bak *.blg *.bbl *.gz *.snm *.nav _minted*

