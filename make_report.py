"""
	Make_report.py takes the plain txt search report and converts it into a readable html file. The code breaks into two parts:
	(1) Modify the source code to markdown to make headings and such
	(2) Convert the markdown to
"""
import os, sys, inspect
cmd_markdown = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"deps/markdown/")))
sys.path.append(cmd_markdown)
import markdown 		# Convert markdown to html
import time				# Print the date on the report
import re				# Regular expressions
from sets import Set	# We'll need the 'Set' object

txt_report = open("output.txt", 'r')
report = open("report.md", 'w')

# Title and Top Matter
report.write("#Search Report\n")
date_string = time.strftime("%d/%m/%Y")
report.write("Report generated: " + date_string + "\n")
report.write("Report generaged by: PDF Search\n")

# Summary of the Search
report.write("##Search Summary\n")
string_of_txt_report = txt_report.read()
summary_list = re.findall(r'Keyword (\w+) found in file: (\S+) (\d+) times', string_of_txt_report)

keywords = Set([])
for Tuple in summary_list:
	keywords.add(Tuple[0])

report.write("Search Keywords: \n\n")
for keyword in keywords:
	report.write("- *"+keyword+"* \n")
report.write("\n")

filenames = Set([])
for Tuple in summary_list:
	filenames.add(Tuple[1])

report.write("Files searched: \n")
for filename in filenames:
	report.write("- *"+filename+"*\n")
report.write("\n")

# Fine details
report.write("##Findings\n")

for filename in filenames:
	report.write("### Hits in "+filename+"\n")
	for keyword in keywords:
		for Tuple in summary_list:
			if Tuple[0] == keyword and Tuple[1] == filename:
				report.write("Keyword *"+keyword+"* found "+str(Tuple[2])+" times: \n")
				findings = re.findall(str(Tuple[2])+r' times: (.*?) Keyword', string_of_txt_report, re.DOTALL)
				print findings


report.close()
txt_report.close()
