import random

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

char = ["@", "$", "&"]

password =  ""
for _ in range(12):

 alpa = random.choice(alphabet)
 charecter = random.choice(char)
 digit = str(random.randint(0, 9))
 password += alpa + charecter + digit 
 

print(password[:12] )