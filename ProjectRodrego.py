#Program Workline
program= """
inc 1 2
deb 2 1 3
end
"""

registers=[0]*10
registers[1]=5
registers[2]=6
print("Le tab registers avant modification: ")
print(registers)
prg = [l.split() for l in program.splitlines()]
print(prg)
IP = 1
instruction = prg[IP][0]

while instruction == 'inc' or instruction == 'deb':

    if instruction == 'inc':     #Start increment()
        registers[int(prg[int(IP)][1])]+=1     #On ajoute 1 à la case sélectionnée (n)
        IP = prg[int(IP)][2]     #Pointe sur la prochaine étape à suivre
        instruction = prg[int(IP)][0]    #Go to step m

    elif instruction == 'deb':     #Start decrement

        if registers[int(prg[int(IP)][1])]>0:     #Condtion de passage = valeurs non nulles
            registers[int(prg[int(IP)][1])]-=1     #On soustrait 1 à la case sélectionnée (n)
            IP = prg[int(IP)][2]     #Pointe sur la prochaine étape à suivre
            instruction = prg[int(IP)][0]     #Go to step m
            print(registers[int(prg[int(IP)][1])])
        else:
            IP = prg[int(IP)][3]    #IP pointe sur la ligne de sortie
            instruction = prg[int(IP)][0]     #Break command (ie go to step p)

print("Le tab registers après modification:")
print(registers)
