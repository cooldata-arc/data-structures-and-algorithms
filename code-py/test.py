print("Hello World")

a = dict()
a[2] = 0
a[3] = 1
print("a.get(3, default=None): ", a.get(3, -1))
print("a[4]: ", a.get(4, -1))