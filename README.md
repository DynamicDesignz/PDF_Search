# PDF Search

Welcome to PDF Search. This repository as tools perform automated searchs of large PDF documents. 

## pdf2txt.py

pdf2txt.py converts pdf documents to plain text. Given a pdf in "mypdf.pdf" it will be converted to  plain text in the standard output. For example:

```bash    
    $python pdf2txt.py "mypdf.pdf"
```
    
will return the file to the screen and

```bash 
    $python pdf2txt.py "mypdf.pdf">>output.txt
```

will write the plain text version of the file to a text file "output.txt" in the current directory.

## Acknowledgements

This is fork of gangopad/PDFtoText. Check out the original project here: https://github.com/gangopad/PDFtoText



