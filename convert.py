x = input("Enter your keyword: ")
def search (keyword):
    f = open('inputTextFile.txt', 'r')
    text = f.read().lower()
    print text
    if keyword.lower() in text:
        print True
    else:
        print False
search(x)
