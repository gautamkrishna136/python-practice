import random as m
import string as s
pass_len=int(input("enter the len of the password:--"))
charvalues=s.ascii_letters+s.digits+s.punctuation
password="".join([m.choice(charvalues)for i in range(pass_len)])
print("your password is:",password)
