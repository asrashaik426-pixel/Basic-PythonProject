import string
import random
length=int(input("enter size of password:"))
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowwer_case="abcdefghijklmnopqrstuvwxyz"
digit="1234567890"
extra="!@#$%^"
combine=upper_case+lowwer_case+digit+extra
password = ''.join(random.choice(combine) for _ in range(length))

print("your generated password is:",password)
