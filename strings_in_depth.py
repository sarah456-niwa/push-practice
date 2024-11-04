#strings array like structured
#arrays in python are lists
#example
#marks=[90,40,80]#eg of a list in python (arrays)
#in arrays the first index must be a zero
name="sarah"
print(name[0])
print(name[4])
#Looping through strings
#we loop through strings using a key word "for"
#example
for character in name:
    print(character)

address="Kamwokya"
for item in address:
    print(item)

#3.Slicing in strings
#This is accessing of a range of a character
#example
name="sarah"
print(name[1:3])#ar
print(name[1:5])#arah
print(name[1:4])#ara
print(name[0:2])#sa
print(name[ :4])#sara

#negative indexing
message="hello"
print(message[-1:-5])
print(message[-1:-4])
print(message[-5:-3])
print(message[-4: ])

print(message[-1])

#4.f strigs(formatted strings)
#for f strings we embed variables in curly brackets.
name="sarah"
age="21"
weight="56"
print(f"my name is {name}, i am {age} years old, my weight is {weight}")
total_cost=300000
print(f"a new car is {total_cost:,}")

#string methods
#1.length #len()
name="niwahereza"
print(len(name))
print(name.upper())

address='fromkamwokya'
print(len(address))
#the space left on a word to a word is also counted.
name='sarah\t niwahereza\n'
print(name)


