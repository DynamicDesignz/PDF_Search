# PDF Search

Welcome to PDF Search, a search program for multiple PDF files. PDF Search hunts through a directory of pdf documents by for one or more keywords and returns an html report on what it found. PDF Search is implemented entirely in python and ships with its dependencies (python-markdown and python-pdfminer) so all you need to use it is a working python 2.x installation. 

## How-to

Start by downloading the zip file from https://github.com/nsmith5/PDF_Search. You'll see the "Download Zip" link on the bottom right hand side of the page. 

### Windows

Once you've downloaded the zip file, extract it. The result will be a folder called "PDF_Search-master". Inside this folder there is another folder call "PDFs" where you can place all of the pdf files you want to search. Once your pdf files are inside this folder navigate to the "PDF_Search-master" folder once again. Now, press the SHIFT key and right click inside the the folder. You'll see a menu with option "Open command window here" available, which you should click. 

Inside of the command window type the following command:

```bash
    > python PDF_SEARCH.py
```

This will run the python program that performs the search. You should see messages telling you which files are begin converted to text and afterwords there will be a prompt asking you for keywords. Enter keywords seperated by spaces (Capitalization does not matter) and press <Enter> when you are finished. 

The python program will now automatically search through your pdf files and generate a report called "report.html" in the "PDF-Search-master" folder. Open this report in your favourite browser.

### Mac

Once you've downloaded the zip file, extract it. The result will be a folder called "PDF_Search-master". Inside this folder there is another folder call "PDFs" where you can place all of the pdf files you want to search. Once your pdf files are inside this folder navigate to the "PDF_Search-master" folder in Finder. Right click on the folder in Finder the select the "New Terminal at Folder" option under Services. If this option is not available to you, you can change your settings to make it available by heading into System Preferences and selecting Keyboard > Shortcuts > Services. Find "New Terminal at Folder" in the settings and click the box.

Inside of the terminal window type the following command:

```bash
    > python PDF_SEARCH.py
```

This will run the python program that performs the search. You should see messages telling you which files are begin converted to text and afterwords there will be a prompt asking you for keywords. Enter keywords seperated by spaces (Capitalization does not matter) and press <Enter> when you are finished. 

The python program will now automatically search through your pdf files and generate a report called "report.html" in the "PDF-Search-master" folder. Open this report in your favourite browser.


## Bugs and Issues

Currently, PDF Search only accepts filenames with no spaces and only works on searchable pdf files. As a rule of thumb, if you can't highlight words in your pdf documents then PDF Search will not be able to search through them. 

## Acknowledgements

This is fork of gangopad/PDFtoText. Check out the original project here: https://github.com/gangopad/PDFtoText
