@@ -0,0 +1,14 @@
import employees1
import string
import random

chars = string.ascii_letters + string.digits + '!@#$%^&*()'


username = random.choice(employees1.santana) + random.choice(string.digits)+ '@yahoo.com'
password = ''.join(random.choice(chars) for i in range(8))

print(username)
print(password)

