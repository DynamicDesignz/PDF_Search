"""
	Make_report.py takes the plain txt search report and converts it into a readable html file. The code breaks into two parts:
	(1) Modify the source code to markdown to make headings and such
	(2) Convert the markdown to
"""
import os, sys, inspect
cmd_markdown = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"deps/markdown/")))
sys.path.append(cmd_markdown)
import markdown 		# Convert markdown to html
import codecs			# Markdown require UTF-8 encoding of the .md file
import time				# Print the date on the report
import re				# Regular expressions
from sets import Set	# We'll need the 'Set' object

txt_report = open("./output.txt", 'r')							# .txt version of the report from convert.py
report = open("./report.md", 'w')								# .md version of the report to be written

# Title and Top Matter
report.write("#Search Report\n")							# Title
date_string = time.strftime("%d/%m/%Y")						# Date
report.write("Report generated: " + date_string + "\n")		# Write the Date generated
report.write("Report generaged by: PDF Search\n")			# Software name

# Summary of the Search
report.write("##Search Summary\n")
string_of_txt_report = txt_report.read()					# Convert report to a single string for regex work
txt_report.close()
summary_list = re.findall(r'Keyword (\w+) found in file: (\S+) (\d+) times', string_of_txt_report)	# Find tuples of (Keyword, filename, hits)

keywords = Set([])						# Make a set of keyowords
for Tuple in summary_list:
	keywords.add(Tuple[0])

report.write("Search Keywords: \n\n")	# Print out the keywords
for keyword in keywords:
	report.write("- *"+keyword+"* \n")
report.write("\n")

filenames = Set([])						# Make a set of filenames
for Tuple in summary_list:
	filenames.add(Tuple[1])

report.write("Files searched: \n")		# Print out the filenames
for filename in filenames:
	report.write("- *"+filename+"*\n")
report.write("\n")

# Fine details
report.write("##Findings\n")
txt_report = open("output.txt", 'r')
result = []
section = []
for line in txt_report:					# Structure the report as list of keyword hits starting with the keyword string
	if "Keyword" in line:
		if section != [] :
			result.append(section)
			section = []
			section.append(line)
		else:
			section.append(line)
	else:
		section.append(line)
else:
	result.append(section)
txt_report.close()

for filename in filenames:				# For each pdf filename:
	report.write("### Findings in " + filename + "\n")			# Subtitle for filename
	for keyword in keywords:									# For each search keyword
		for hit in result:										# Search through the hits
			if keyword in hit[0] and filename in hit[0]:		# if the hit is the right keyword and filename
				for line in hit:								# print all the lines of the hit to the markdown report
					if line == hit[0]:
						report.write(line)
					else:
						report.write(">"+line)

report.close()

# Convert to html
mdreport = open("./report.md", 'r')
markdown.markdownFromFile("./report.md", "report.html")
mdreport.close()
