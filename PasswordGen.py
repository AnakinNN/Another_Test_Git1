import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWZYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,_-"
all = lower+upper+numbers+symbols
length = 4*9
password = "".join(random.sample(all,length))
print('This is your effective password: ',password)



