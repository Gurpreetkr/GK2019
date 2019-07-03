technologies = ["AI","Android","Hadoop","JEE"]
technologies[1] ="Mobile Apps" # Update/Set Operation in List
print(technologies)

print()

del technologies[2]

print(technologies)
print(technologies[2])

#print(technologies[-2])

data =[1,2,3,4,5,"john","jennie","jim","jack","joe"]
data.pop(3) # Removes on the basis of index
print(data)

data.remove(3) #Remove the matching element

print(data)

data.remove("john")
print(data)

print(len(data))