h = " Happy programming!"
print(len(h))
print(h.count("p"))
print(h.upper())
print(h.lower())
print(h.strip())
print(h.replace("Happy", "Funny"))
print(h.find("ap"))
print(h.rfind("a"))
print(h.find("Happy"))
print(h.find("fun"))
print("a" in h)
print("b" in h)

x = "01::23::ab::^^"
y = x.split("::")
print(y)
print(", ".join(y))