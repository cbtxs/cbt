
all: git_use.pdf \


git_use.pdf: git_use.tex
	xelatex -shell-escape git_use.tex
	bibtex git_use.aux
	xelatex -shell-escape git_use.tex
	xelatex -shell-escape git_use.tex
	evince git_use.pdf&

.PHONY:clean  
clean:
	-rm -fr *.ps *.dvi *.aux *.toc *.idx *.ind *.ilg *.log *.out *~ *.tid *.tms *.pdf *.bak *.blg *.bbl *.gz *.snm *.nav _minted *.fls *.fdb_latexmk

