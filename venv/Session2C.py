dishPrice = 100

#dishesPrice = 100, 200, 350, 500, 120

print(dishPrice, hex(id(dishPrice)), type(dishPrice))

dishesPrices = (100, 200, 350, 500, 120)    # Homogeneous

print(dishesPrices, hex(id(dishesPrices)), type(dishesPrices))

anotherDishesPrices = (100, 200.22, 350, 500, 120, "100") # Hetrogeneous

print(dishesPrices[1], hex(id(dishesPrices[1])), type(dishesPrices[1]))