import random
p = []
for i in range(127):
    p.append(chr(i))
    
password = ""
for i in range(8):
    r = random.randint(32,126)
    password += str(p[r])


print(password)