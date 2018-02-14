myPets = ['Zophie', 'Pooka', 'Fat-tail']
print ('Enter your pet\'s name: ')
name = input()
if name not in myPets:
    print ("You don't have such pet")
else:
    print ("Your pet is " + name)
