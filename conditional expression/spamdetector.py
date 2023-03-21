text = input("Enter the text\n")
spam = False

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
               
elif("suscribe now" in text):
    spam = True
else :
    spam = False    

if(spam):
    print("This is a spam\n")
else:
    print("This is not a spam\n")    
