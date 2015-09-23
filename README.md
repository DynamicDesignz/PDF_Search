# PDF Search

Welcome to PDF Search, a search program for multiple PDF files. PDF Search hunts through a directory of pdf documents by for one or more keywords and returns an html report on what it found. PDF Search is implemented entirely in python and ships with its dependencies (python-markdown and python-pdfminer) so all you need to use it is a working python 2.x installation. 

## How-to

First clone the git repository and change directories to it

``` bash
    $ git clone https://github.com/nsmith5/PDF_SEARCH.git
    $ cd PDF_SEARCH
```

Add all the pdf documents you need to search the "PDFs" directory and then run the "PDF_SEARCH.py" script
    
```bash 
    $ python PDF_SEARCH.py
```

PDF Search will prompt you for keywords you'd like to search for in the terminal and afterwords you'll find an html file named "report.html" with the finds. 

```bash
    $ firefox report.html
```

## Bugs and Issues

Currently, PDF Search only accepts filenames with no spaces and only works on searchable pdf files. As a rule of thumb, if you can't highlight words in your pdf documents then PDF Search will not be able to search through them. 

## Acknowledgements

This is fork of gangopad/PDFtoText. Check out the original project here: https://github.com/gangopad/PDFtoText
