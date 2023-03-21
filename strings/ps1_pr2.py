letter = ''' Dear <|NAME|>,
Greetings from ABC tech. I am Happy to declear that
Congratulations You are selected!
Have a good day.
Date: <|DATE|>
'''

name = input("Enter candidate Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)