# CracklePop Program by Rajiv Wallace

numbers = []

for i in range (1,101):
    numbers.append(i)

crackle_pop = []

for i in numbers:
    if i % 3 == 0 and i % 5 == 0:
        crackle_pop.append(str('CracklePop'))
    elif i % 3 == 0:
        crackle_pop.append(str('Crackle'))
    elif i % 5 == 0:
        crackle_pop.append(str('Pop'))
    else:
        crackle_pop.append(str(i))

print (numbers)

print (crackle_pop)