print ("Welcome to the Rodrego machine programs. Here are many programs to discover:")

print("Program 1: ADD [1,2]")

#Program Workline (quoted from Christophe Pallier's code)
program= """
deb 1 2 3
inc 2 1
end
"""

registers=[0]*10
registers[0]=5
registers[2]=6
print("Register's tab before modification: ")
print(registers)

#prg isolates the different elements of program (quoted from Christophe Pallier's code)
prg = [l.split() for l in program.splitlines()]

#IP, instruction pointer, is the step to follow
IP = 1
instruction = prg[IP][0]

while instruction == 'inc' or instruction == 'deb':

#Start increment()
    if instruction == 'inc':
#Add 1 to the selected register(n)
        registers[int(prg[int(IP)][1])-1]+=1
#Point at next step to follow
        IP = prg[int(IP)][2]
#Go to step m
        instruction = prg[int(IP)][0]

#Start decrement
    elif instruction == 'deb':
#Step's conditions = value not 0
        if registers[int(prg[int(IP)][1])-1]>0:
#Take 1 out of the selected register (n)
            registers[int(prg[int(IP)][1])-1]-=1
            IP = prg[int(IP)][2]
#Point at next step to follow
            instruction = prg[int(IP)][0]
        else:
#IP points at the ending line
            IP = prg[int(IP)][3]
#Break command (ie go to step p)
            instruction = prg[int(IP)][0]

print("Register's tab after modification:")
print(registers)



print ("Program 2: MOVE[4,5]")

program= """
deb 5 1 2
deb 4 3 4
inc 5 2
end
"""

registers=[0]*10
registers[4]=5
registers[5]=6
print("Register's tab before modification: ")
print(registers)

#prg isolates the different elements of program (quoted from Christophe Pallier's code)
prg = [l.split() for l in program.splitlines()]

#IP, instruction pointer, is the step to follow
IP = 1
instruction = prg[IP][0]

while instruction == 'inc' or instruction == 'deb':

#Start increment()
    if instruction == 'inc':
#Add 1 to the selected register(n)
        registers[int(prg[int(IP)][1])-1]+=1
#Point at next step to follow
        IP = prg[int(IP)][2]
#Go to step m
        instruction = prg[int(IP)][0]

#Start decrement
    elif instruction == 'deb':
#Step's conditions = value not 0
        if registers[int(prg[int(IP)][1])-1]>0:
#Take 1 out of the selected register (n)
            registers[int(prg[int(IP)][1])-1]-=1
            IP = prg[int(IP)][2]
#Point at next step to follow
            instruction = prg[int(IP)][0]
        else:
#IP points at the ending line
            IP = prg[int(IP)][3]
#Break command (ie go to step p)
            instruction = prg[int(IP)][0]

print("Register's tab after modification:")
print(registers)



print ("Program 3: COPY[1,3]")

program= """
deb 3 1 2
deb 4 2 3
deb 1 4 6
inc 3 5
inc 4 3
deb 4 7 8
inc 1 6
end
"""

registers=[0]*10
registers[3]=2
registers[4]=3
registers[1]=4
print("Register's tab before modification: ")
print(registers)

#prg isolates the different elements of program (quoted from Christophe Pallier's code)
prg = [l.split() for l in program.splitlines()]

#IP, instruction pointer, is the step to follow
IP = 1
instruction = prg[IP][0]

while instruction == 'inc' or instruction == 'deb':

#Start increment()
    if instruction == 'inc':
#Add 1 to the selected register(n)
        registers[int(prg[int(IP)][1])-1]+=1
#Point at next step to follow
        IP = prg[int(IP)][2]
#Go to step m
        instruction = prg[int(IP)][0]

#Start decrement
    elif instruction == 'deb':
#Step's conditions = value not 0
        if registers[int(prg[int(IP)][1])-1]>0:
#Take 1 out of the selected register (n)
            registers[int(prg[int(IP)][1])-1]-=1
            IP = prg[int(IP)][2]
#Point at next step to follow
            instruction = prg[int(IP)][0]
        else:
#IP points at the ending line
            IP = prg[int(IP)][3]
#Break command (ie go to step p)
            instruction = prg[int(IP)][0]

print("Register's tab after modification:")
print(registers)



print ("Program 4: Non-destructive ADD[1,2,3]")

program= """
deb 3 1 2
deb 4 2 3
deb 1 4 6
inc 3 5
inc 4 3
deb 4 7 8
inc 1 6
deb 2 9 11
inc 3 10
inc 4 11
deb 4 12 13
inc 2 11
end
"""

registers=[0]*10
registers[3]=2
registers[4]=3
registers[1]=4
print("Register's tab before modification: ")
print(registers)

#prg isolates the different elements of program (quoted from Christophe Pallier's code)
prg = [l.split() for l in program.splitlines()]

#IP, instruction pointer, is the step to follow
IP = 1
instruction = prg[IP][0]

while instruction == 'inc' or instruction == 'deb':

#Start increment()
    if instruction == 'inc':
#Add 1 to the selected register(n)
        registers[int(prg[int(IP)][1])-1]+=1
#Point at next step to follow
        IP = prg[int(IP)][2]
#Go to step m
        instruction = prg[int(IP)][0]

#Start decrement
    elif instruction == 'deb':
#Step's conditions = value not 0
        if registers[int(prg[int(IP)][1])-1]>0:
#Take 1 out of the selected register (n)
            registers[int(prg[int(IP)][1])-1]-=1
            IP = prg[int(IP)][2]
#Point at next step to follow
            instruction = prg[int(IP)][0]
        else:
#IP points at the ending line
            IP = prg[int(IP)][3]
#Break command (ie go to step p)
            instruction = prg[int(IP)][0]

print("Register's tab after modification:")
print(registers)
