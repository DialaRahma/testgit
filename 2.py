ex21 = [2, 4, 6, 8, 10]
# List comprehension
ex211 = [i for i in range(0, 11) if i % 2 == 0]
ex212 = [i for i in range(0, 11, 2)]


print("ex21 ", ex21)
print("ex211 ", ex211)
print("ex212 ", ex212)

x22 = []
for i in range(1, 100):
    if (i % 15 == 0):
        x22.append(i)

print(x22)

ex221 = [i for i in range(0, 101) if i % 15 == 0]
print("ex221 ", ex221)


x23 = []
for i in range(0, 16):
    if (i % 2 != 0):
        x23.append(i)
x23.sort(reverse=True)
print(f"EX2.3 {x23}")

ex231 = [i for i in range(15, 0, -1) if i % 2 != 0]
print("ex231 ", ex231)


x24 = ["xx"] * 5
x241 = ["xx" for i in range(0, 5)]
print(f"EX2.4 {x24}")
print(f"EX2.41 {x241}")


x25 = []
for i in range(4, 15):
    x25.append(f"string{i}")
print(f"EX2.4 {x25}")

x251 = [f"string{i}" for i in range(5, 15)]
print(f"EX2.5 {x251}")


x26 = ["1", 2, 3.0, 4]
print(f"EX2.6 {x26}")


x27 = [i for i in range(0, 100) if str(i).find("3") != -1]
print(x27)
