counterPDF=1
counterTXT=1
STR=""
STR_noES=""
emptyspace=" "
for file in /Users/Motoki/Desktop/git/PDFtoText/PDFs/*.pdf
do
  echo $file
 # do something on "$file"
 #cat "$file" >> /var/www/cdn.example.com/cache/large.css
 #newfile=${file:32}
 #path=/Users/UMBC/MedicalJournals/Texts/
 path=/Users/Motoki/Desktop/git/PDFtoText/Texts/temp
 extension=.txt
 #outfile=$path$newfile$extension
 outfile=$path$newfile$counterPDF$extension
 #echo $outfile
 python pdf2txt.py "$file" >> $outfile
 counterPDF=$((counterPDF+1))
done
for file in /Users/Motoki/Desktop/git/PDFtoText/Texts/*.txt
do
  extension=.txt
  temp=temp
  name="$temp$counterTXT$extension"
  STR_noES="$STR$name"
  STR="$STR_noES$emptyspace"
  counterTXT=$((counterTXT+1))
done
python convert.py $STR_noES
