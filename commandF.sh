#File and Folder placement:::
# BASE FOLDER PWD MUST contain files "commandF.sh", "convert.py",
#"README.md", "pdf2txt.py", "make_report.py"
# All PDFs to be searched are in a folder of PWD called "PDFs"

counterPDF=1
counterTXT=1
counterDEL=1
STR=""
STR_noES=""
emptyspace=" "
pdfname=""
for file in $PWD/PDFs/*.pdf
do
  #echo $file
  extension=.txt
  path=$PWD/
filename="%%$file.pdf"
echo $filename
 outfile=$path$counterPDF$extension
 python pdf2txt.py "$file" >> $outfile
 counterPDF=$((counterPDF+1))
done
for file in $PWD/*.txt
do
  #echo "$file"
  extension=.txt
  name="$counterTXT$extension"
  STR_noES="$STR$name"
  STR="$STR_noES$emptyspace"
  counterTXT=$((counterTXT+1))
done
python convert.py $STR_noES
#python make_report.py
#rm *.txt
