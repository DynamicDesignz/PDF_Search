import sys

#keyword = input("Enter your keyword: ")
keyword = "have"
def search (keyword):
    for x in range (1,len(sys.argv)):
        f = open(sys.argv[x], 'r')
        text = f.read().lower().split()
        appear = False
        counter = 0
        where_appear = []
        for i in range(0, len(text)):
            if text[i] == keyword.lower():
                counter = counter + 1
                where_appear.append(i)
                appear = True
        if appear == True:
            out = open('output.txt', 'w')
            out.write(sys.argv[x])
            out.write("\n")
            out.write(keyword)
            out.write("\n")
            out.write(str(counter))
            out.write("\n")
            out.write("\n")
            for i in range(0,len(where_appear)):
                for j in range (-25,25):
                    if text[where_appear[i] + j] == keyword:
                        out.write(keyword.upper() + " ")
                    else:
                        out.write(text[where_appear[i] + j] + " ",)
                out.write("\n")
                out.write("\n")


search(keyword)
