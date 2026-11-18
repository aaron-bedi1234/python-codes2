def matchw(words):
    ch=0
    list=[]
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            ch+=1
            list.append(word)
    print("list words with the first and last character same  \n",list)
    return ch
count=matchw(["abc","der","ghi","jkl","2222","aaa","eee"])
print("number of words with the first and last letter the same  ",count)