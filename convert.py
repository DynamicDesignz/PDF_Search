import sys
keyword = ["what", "are", "you", "have", "talking"]
def search (keyword):
    out = open('output.txt', 'w')

    #Search through every inputted pdf
    for pdf_loop in range (1,len(sys.argv)):
        print pdf_loop
        f = open(sys.argv[pdf_loop], 'r')
        text = f.read().lower().split()

        #Search through every inputted keyword
        for keyword_loop in range (0, len(keyword)):
            counter = 0
            where_appear = []
            appear = False

            #Search through individual pdf's text
            for i in range(0, len(text)):
                if text[i] == keyword[keyword_loop].lower():
                    counter = counter + 1
                    where_appear.append(i)
                    appear = True
            if appear == True:
                out.write("Keyword " + keyword[keyword_loop].upper() + " found in file: " + sys.argv[pdf_loop] + " " + str(counter) + " times \n \n")
                #Start creating summary
                for i in range(0,len(where_appear)):
                    if where_appear[i] < 25:
                        out.write("\"",)
                        for j in range (0,50):
                            out.write(text[j] + " ",)
                        out.write("\"",)
                    elif where_appear[i] > len(text)-25:
                        out.write("\"",)
                        for j in range (len(text) - 50, len(text)):
                            out.write(text[j] + " ",)
                        out.write("\"",)
                    else:
                        out.write("\"",)
                        for j in range (-15,15):
                            if text[where_appear[i] + j] == keyword[keyword_loop]:
                                out.write(keyword[keyword_loop].upper() + " ")
                            else:
                                out.write(text[where_appear[i] + j] + " ",)
                        out.write("\"",)
                    out.write("\n" + "\n")
                appear = False
search(keyword)
