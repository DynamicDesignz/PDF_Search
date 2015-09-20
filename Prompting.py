keywords = []
keyword = ""

while True: 
	keyword = raw_input("Enter a new a new keyword and then write "quit" :\n")
	if keyword == "quit" :
		break
	else :
		keywords.append(keyword)
	
for words in keywords:
	print words
