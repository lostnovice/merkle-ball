import sys
import random
from collections import Counter
from hashlib import sha256

# take the args and make the tree
a = sha256(sys.argv[1].encode('utf-8')).hexdigest()
b = sha256(sys.argv[2].encode('utf-8')).hexdigest()
c = sha256(sys.argv[3].encode('utf-8')).hexdigest()
d = sha256(sys.argv[4].encode('utf-8')).hexdigest()

ab = sha256(a.encode('utf-8') + b.encode('utf-8')).hexdigest()
cd = sha256(c.encode('utf-8') + d.encode('utf-8')).hexdigest()

seedgen = sha256(ab.encode('utf-8') + cd.encode('utf-8')).hexdigest()
print("Using merkle root of", seedgen)
random.seed(seedgen)

# do the loop and get the most common numbers
numbers = []
numbers2 = []
count = 0
count2 = 0

# main numbers
while count < 10000:
    new = random.randint(1, 35)
    numbers.append(new)
    count += 1

x = Counter(numbers).most_common()
print(x)

# powerball number
while count2 < 10000:
    new = random.randint(1, 20)
    numbers2.append(new)
    count2 += 1

y = Counter(numbers2).most_common()
print(y)