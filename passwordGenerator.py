import random
import string

print("Password for life")

digits = string.digits
lowerLetters = string.ascii_lowercase
upperLetters = string.ascii_uppercase
symbols = string.punctuation

lenghts =int(input("Entered length of password"))

jumbledPass = digits+symbols+lowerLetters+upperLetters
onlyChar= random.choices(lowerLetters+upperLetters)
passes =  random.sample(jumbledPass,lenghts-1)
password = ''.join(onlyChar)+''.join(passes)

print(password)




