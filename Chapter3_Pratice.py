# 3.1 Name
name = ['Aven','Avon','Eric','Jack']
print(name[0])
print(name[1])
print(name[2])
print(name[3])

# 3.2 Greeting
print("Hi " + name[0] + ", how are you?")
print("Hi " + name[1] + ", how are you?")
print("Hi " + name[2] + ", how are you?")
print("Hi " + name[3] + ", how are you?")

# 3.3 Own List
commute = ['motocrycle','car','ship']
print('I would like to own a Honda ' + commute[1] + '.') 

# 3.4
invite = ['Aven','Avon','Eric','Jack']
print('Come ' + invite[1] + ', have dinner with me.')
print('Come ' + invite[0] + ', have dinner with me.')
print('Come ' + invite[2] + ', have dinner with me.')
print('Come ' + invite[3] + ', have dinner with me.')

# 3.5 Changing List
print(invite[2] + " can't come for the dinner.")
invite[2] = 'Rick'
print('Come ' + invite[2] + ', have dinner with me.')

# 3.6 adding list
print('I found a bigger table')
invite.insert(0, 'Raymond') # front
invite.insert(3, 'Jimmy') # middle
invite.insert(6,'John') # end # using -1 unable to add John at the end
print('Come ' + invite[0] + ', have dinner with me.')
print('Come ' + invite[1] + ', have dinner with me.')
print('Come ' + invite[2] + ', have dinner with me.')
print('Come ' + invite[3] + ', have dinner with me.')
print('Come ' + invite[4] + ', have dinner with me.')
print('Come ' + invite[5] + ', have dinner with me.')
print('Come ' + invite[6] + ', have dinner with me.')


# 3.7 deleting list
print('Sorry, the table is broken, I can only inivite two people.')
one = invite.pop(2)
print('Sorry ' + one + ", my table is broken, the dinner is cancel")
two = invite.pop(2)
print('Sorry ' + two + ", my table is broken, the dinner is cancel")
three = invite.pop(2)
print('Sorry ' + three + ", my table is broken, the dinner is cancel")
four = invite.pop(2)
print('Sorry ' + four + ", my table is broken, the dinner is cancel")
five = invite.pop(2)
print('Sorry ' + five + ", my table is broken, the dinner is cancel")

print('Hi ' + invite[0] + ', you still can come with me for dinner')
print('Hi ' + invite[1] + ', you still can come with me for dinner')

del invite[0]
del invite[0] 
print(invite)
# position always change when you pop or delete

# 3.8 changing order of a list
world = ['Iceland','United Kingdom','Japan','Russia','Spain']
print(world)
print(sorted(world))
print(world)
print(sorted(world, reverse=True))
print(world)
world.reverse()
print(world)
world.reverse()
print(world)
world.sort()
print(world)
world.sort(reverse=True)
print(world)

invite = ['Aven','Avon','Eric','Jack','Jimmy']
print(len(invite))




