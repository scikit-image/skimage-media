.PHONY: all

all: clean handout

clean:
	find . -name "*.pytxcode" -type f -delete			\
	find . -name "*.lopytx" -type f -delete				\
	find . -name "pythontex-files-*" -type f -delete	\
	find . -name "*.aux" -type f -delete;				\
	find . -name "*.toc" -type f -delete;				\
	find . -name "*.lot" -type f -delete;				\
	find . -name "*.lof" -type f -delete;				\
	find . -name "*.blg" -type f -delete;				\
	find . -name "*.bbl" -type f -delete;				\
	find . -name "*.brf" -type f -delete;				\
	find . -name "*.synctex.gz" -type f -delete;		\
	find . -name "*.fdb_latexmk" -type f -delete;		\
	find . -name "*.fls" -type f -delete;				\
	find . -name "*.out" -type f -delete;				\
	find . -name "*.out" -type f -delete;				\
	find . -name "*.run.xml" -type f -delete;			\
	find . -name "*.bcf" -type f -delete;

handout:
	pdflatex handout
	bibtex handout
	pythontex handout
	pdflatex handout
	pdflatex handout

update:
	pdflatex handout
