counterPDF=1
counterTXT=1
counterDEL=1
STR=""
STR_noES=""
emptyspace=" "
for file in $PWD/PDFs/*.pdf
do
  echo $file
  temp=temp
 # do something on "$file"
 #cat "$file" >> /var/www/cdn.example.com/cache/large.css
 #newfile=${file:32}
 #path=/Users/UMBC/MedicalJournals/Texts/
 extension=.txt
 path=$PWD/$temp
 #outfile=$path$newfile$extension
 outfile=$path$counterPDF$extension
 #echo $outfile
 python pdf2txt.py "$file" >> $outfile
 counterPDF=$((counterPDF+1))
done
for file in $PWD/*.txt
do
  extension=.txt
  name="$temp$counterTXT$extension"
  STR_noES="$STR$name"
  STR="$STR_noES$emptyspace"
  counterTXT=$((counterTXT+1))
done
python convert.py $STR_noES

for file in $PWD/*.txt
do
  extension=.txt
  name="$temp$counterDEL$extension"
  rm $name
  counterDEL=$((counterDEL+1))
done
