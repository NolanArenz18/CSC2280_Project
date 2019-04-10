# cipher.py
# Implement a Caesar cipher.


def cipher(txt, key):
    x = []
    for i in range(len(txt)):
        y = txt[i]
        x += chr((ord(y) + key))
    return x


# Test the function
# (You do not need to edit the code below, but you should examine what it does!)
txt = "weekend"
key = 1
print("({}, {}) --> {}".format(txt, key, cipher(txt, key)))

txt = "secret"
key = 2
print("({}, {}) --> {}".format(txt, key, cipher(txt, key)))

txt = "tfdsfu"
key = -1
print("({}, {}) --> {}".format(txt, key, cipher(txt, key)))

txt = "ugetgv"
key = -2
print("({}, {}) --> {}".format(txt, key, cipher(txt, key)))
