import sys
keyword = ["what", "are", "you", "have", "talking"]
def search (keyword):
    appear = False

    where_appear = []
    out = open('output.txt', 'w')

    #Search through every inputted pdf
    for pdf_loop in range (1,len(sys.argv)):
        f = open(sys.argv[pdf_loop], 'r')
        text = f.read().lower().split()

        #Search through every inputted keyword
        for keyword_loop in range (0, len(keyword)):
            counter = 0

            #Search through individual pdf's text
            for i in range(0, len(text)):
                if text[i] == keyword[keyword_loop].lower():
                    counter = counter + 1
                    where_appear.append(i)

            out.write("Keywords found in file: " + sys.argv[pdf_loop] + "\n")
            out.write("Hits encountered for " +keyword[keyword_loop] + ": " + str(counter) + "\n")

            #Start creating summary
            for i in range(0,len(where_appear)):
                if where_appear[i] < 25:
                    for j in range (0,50):
                        out.write(text[where_appear[i] + j] + " ",)
                elif where_appear[i] > len(text)-25:
                    for j in range (len(text) - 50, len(text)):
                        out.write(text[j] + " ",)
                else:
                    for j in range (-25,25):
                        if text[where_appear[i] + j] == keyword[keyword_loop]:
                            out.write(keyword[keyword_loop].upper() + " ")
                        else:
                            out.write(text[where_appear[i] + j] + " ",)
            out.write("\n" + "\n")

search(keyword)
