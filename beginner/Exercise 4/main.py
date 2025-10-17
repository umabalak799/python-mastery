#the program to converts a normal English message into a secret coded message

st = input("Enter the message: ")
words = st.split(" ")  #breaks the msg into a list of words 

coding = input("Enter 1 for Coding or 2 for Decoding: ")#the user select whether to encode or decode
coding = True if coding == "1" else False               #this is the boolean option fo encoding and decoding 

if coding:
    nwords = []
    for word in words:
        if len(word) >= 3:                              #checks if the word is bigger then 3
            r1 = "cba"                                  #random letters
            r2 = "zyx"
            stnew = r1 + word[1: ] + word[0] + r2       #1st is random word r1 + remove the 1st letter + add the first letter to  the last + r2 2nd random letter
            nwords.append(stnew)                        #add the decoded word to the nwords
        else:
            nwords.append(word[::-1])                   #if the word is less than 3 then they are just reversed
    print ("Coded message: ", " ".join(nwords))
else:
    nwords = []                                         # to store the decoded words
    for word in words:                                  #goes through each encoded word in the input 
        if len(word) >= 3:                              #checks if the word is bigger then 3
            stnew = word[3:-3]                          #removes the first 3 and last 3 random letters ie. r1 and r2
            stnew = stnew[-1] + stnew[:-1]              #removes the last word and swap it to the first 
            nwords.append(stnew)                        #add the decoded word to the nwords
        else:
            nwords.append(word[::-1])                   #if the word is less than 3 then they are just reversed 
    print("Decoded message:", ",".join(nwords)) 

