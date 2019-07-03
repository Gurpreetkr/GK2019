application = []

item = input("Enter a item of your Choice: ")

application.append(item)

print()

application.append("Python")
print(application)

print("")

application.extend(["Whatsapp","Facebook"])
print(application)

print()

application.insert(1, "CamScanner")
print(application)

print()

application.pop(4)
print(application)

# HW: Use all the above operations by taking inputs from User