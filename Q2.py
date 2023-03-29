# Bar Girafi - 316582758
###############Q2

def revword(word):
    word = word[::-1].lower()
    return word


xfile = open('C:/Users/Admin/Downloads/text.txt')  
   
def countword(word):
    dicti={}
    first_word = None
    for i in word:
        i=i.split()
        dicti[i[0]] = 1
        for word in i:
            if first_word is None:
                first_word = word
        for x in i:
             x = revword(x)
             if x in dicti:
                dicti[x] += 1
             else:
                dicti[x]=1
    return dicti.get(first_word,0)

print(countword(xfile))

