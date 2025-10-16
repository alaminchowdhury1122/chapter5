marks = {
    "al amin": 100, 
    "jhon": 55,
}

print(marks, type(marks))
print(marks["al amin"])
print(marks["jhon"])


print(marks.items())
marks.update({"al amin":99})
print(marks)
print(marks.get("smith"))
