import hashlib

key = "iwrupvqb"
n = 1

while True:
    test = key + str(n)
    h = hashlib.md5(test.encode()).hexdigest()
    if h.startswith("000000"):
        print("Answer:", n)
        break
    n += 1

