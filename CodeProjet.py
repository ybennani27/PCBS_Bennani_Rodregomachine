#Programing Dennett's Rodrego machine

# Define the three possible instructions
## Inc: increment register n (add 1 to the contents of register n) and go to step m
## Deb: decrement register n (substract 1 from the contents of register n) and go to step m
## End

program = """
Deb 2 3
Inc 1
End
"""

DEBUG = TRUE
