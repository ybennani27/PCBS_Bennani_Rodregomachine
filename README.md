# Final Project - Yasmine Bennani
### Programming a Rodrego machine according to Dennett's chapter "The seven secrets of computer power revealed"



## Introduction
In his 24th chapter "The seven secrets of computer power revealed", Daniel Dennett aims at demystifying how machines work. He argues against these criticisms that presuppose that machines cannot do what minds can do. If the argument is just saying that machines, today, are not able to imitate human brain's capacities, then they are just stating the obvious, according to Dennett.
Dennett's claim is that even a very basic machine, what he calls the "Register machine" or the "Rodrego machine" is able to do what more elaborated ones, such as the Turing machine and the Von Neumann machine, can do.



## Aim of the project
My aim in the current project is to program a Rodrego machine, as conceived of by Daniel Dennett.

The core principle of the program follows two instructions.
The first one is the instruction "Increment" (e.g. "inc" in my code) and the second one is the instruction "Decrement". The "inc" instruction simply means "add 1" to the current register (a register being "a memory location" or, more metaphorically, "a box" that contains any number of small items, or to keep on stealing Dennett's examples, any number of "beans" p. 111).
Whereas the "Dec" instruction means "subtract 1" to the current register. Starting from this, many questions emerge: how can one deal with situations where the "Dec" instruction cannot occur, namely what happens when a register is empty? How could the algorithm know how to deal with items? How could the algorithm determine which register to execute the instructions over? All are questions that I address in the following section.



## I. Explaining the algorithm
### (1) Registers
For formulating the Rodrego machine algorithm, I started by imagining the machine's area of execution as being a large table with many distinct registers (e.g. boxes).


### (2) Deb
There is, indeed, a problem when reviewing the simple two instructions "Inc" and "Dec". What happens when the register is empty? Because, as Dennett notices it, "you can't take a bean out of an empty box" (p. 111).

The answer also explains why my code contains the "deb" instruction instead of "dec". It is because the instruction "deb" (e.g. branch) includes the solution to the problem of "finding an empty register". When the register is empty, the instruction is to go directly to the next step. This is formulated as follows: "Decrement register n (subtract 1 from the contents of register n) if you can and go to step m OR if you can't decrement register n (namely if it is empty), Branch to step p".


### (3) Program
The line of action of my algorithm is defined by "program".

In order to conceive of program precisely, I copied Dennett's way of imagining the machine's actions, i.e. :
```
program= """
inc 1 2
deb 2 1 3
end
"""
```

But this, in its current state, is hardly usable. I needed to make it clear that each element of program is isolated from one another, in order to use it. This is what the following line of the program helped me to do:
'prg = [l.split() for l in program.splitlines()]'
(This is a line I quote from Christophe Pallier's solutions to exercises).
This line was hard to understand for me.
I proceeded by trial and error. I first tried understanding the different tools of the line by testing what each one was doing:
```
prg1 = [l for l in program]
print(prg1)
prg2 = [l for l in program.splitlines()]
print(prg2)
prg3 = [l.split() for l in program.splitlines()]
print(prg3)
```
It gave me this:
 ```
 ['\n', 'i', 'n', 'c', ' ', '1', ' ', '2', '\n', 'd', 'e', 'b', ' ', '2', ' ', '1', ' ', '3', '\n', 'e', 'n', 'd', '\n']
['', 'inc 1 2', 'deb 2 1 3', 'end']
[[], ['inc', '1', '2'], ['deb', '2', '1', '3'], ['end']]
```

I then understood that the first prg1 was not recognizing correctly each element. For prg1, the delimiting object was the number of element: if there was a coming back to the next line, prg1 was counting it as "/n", if there was one letter prg1 was counting it as an element "i", etc.
For prg2, the delimiting object was the lines. It counted different elements each time they were separated by a new line (ex: "inc 1 2 ", "deb 2 1 3", etc).
Fortunately, prg3 gives the right solution (and I finally understood). The delimiting object was the spaces, namely it counted different elements each time they were separated by a space "inc", "1", "2", etc.
Thus, I understood the "prg" line was there to help isolate the different elements constituting the "program" I put in the very beginning of my code. This is the easiest way to make the machine "understand" what to do and deal with the elements and instructions given to it.

Having distinct lines has a specific role: lines mark the new step to follow (whether the next line or the previous line).  


### (4) IP
One question was: how do I make it clear what current instruction to follow? IP is the solution: it is my instruction pointer. I just needed to store in a variable (e.g. the instruction to follow).

```
IP = 1
instruction = prg[IP][0]
```
means the instruction is to go at the second line, first column (considering the first line of the program is an empty line and considering the first column, namely "inc / deb // end").


### (5) Representation of the key instructions
One challenging question for me was: "how could I represent my two key instructions 'Inc' and 'Dec'?"
Here, I decided to write a while loop including both instructions "inc" and "deb".
The while loop is divided into two options: either instruction "inc" or instruction "deb".
The "deb" part is also divided into two options: either the number of beans in the register is > 0, in which case (if registers > 0 then dec) the instruction is in fact the equivalent of "dec", namely subtract 1; or the number of beans in the register is = 0, in which case ("else") the instruction becomes "end".


### (6) All the machine can do
After writing my code, I wanted to show how any of Dennett's programs (ex: "MOVE", "COPY", etc) can work.

From two very basic instructions, "inc" and "deb", depending on the combinations of these two, can make powerful things.
(Understanding Dennett's programs took me a great deal of re-doing and making sense of his diagrams on paper)

- "ADD[1,2]""

For instance the "ADD" program "takes" the beans inside register 1 and "moves" them into register 2.
```
program= """
deb 1 2 3
inc 2 1
end
"""
```
Solutions to Exercise 1 p. 113
a) It will take 5 steps for the Registermachine to add 2+5 (counting end as a step).
b) It will take 11 steps for the Registermachine to add 5+2.
The conclusion to draw being that when register 1 is fuller (ex: 5 beans instead of 2), it takes more steps (more time) for the Registermachine to transfer the content of register 1 to register 2.


- "MOVE[4,5]"

The "MOVE" program empties register 5. It decrements from register 4 and increments register 5, then goes back to register 4 and does the same... So, it is the equivalent of taking what's in register 4 and puts in in register 5.
```
program= """
deb 5 1 2
deb 4 3 4
inc 5 2
end
"""
```

- "COPY[1,3]"

The "COPY" program empties register 3 and 4. Then it "empties" beans from register 1 and "copies" them in registers 3 and 4. Then, it "empties" register 4 and "copies" its content in register 1.   
```
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
```

- "Non-destructive ADD[1,2,3]"

The "non-destructive ADD" program first "empties" registers 3 and 4. It then "empties" and "copies" the content of registers 1 in register 3 and 4 and then "empties" and "copies" register 4 in 1. And "empties" and "copies" the content of register 2 in registers 3 and 4 and then "empties" and "copies" register 4 in 2. 4 is then a "storage" register. The final result being that register 3 contains the sum of contents of registers 1 and 2.
```
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
```

This is proving Dennett's claim that very elaborated machines, such as the Turing machine, are just following the same basics principles as the ones ruling my algorithm.



## Conclusion
To quote Dennett, "at first glance, you might not think such a simple machine could do anything very interesting; all it can do is put a bean in the box or take a bean out of the box" (p. 112). But in fact, as proven in the previous section, the machine can do all sorts of different things, which I checked and justified to be doable in the algorithm I propose.  


## Experience before the PCBS course
I had zero knowledge in programming (I come from a background in social science and philosophy). I was intimidated by the vocabulary and the apparent complexity of coding. To be honest, I think I had to overcome two difficulties: first, starting with no priori programming knowledge, and -most importantly- overcoming my huge bias vis-à-vis coding as a social science student.
The exercises we needed to do every week for the course were very hard for me. It used to take me very long to understand them and try doing some of them. I was happy to have "Automating the boring stuff" as a guideline; it was fun to read and it helped me get familiar with the concepts.

This project was really perfect for me. Coming to the Cogmaster, my aim was to gain the basic vocabulary in computer science and basic machine learning to get a better grasp on the philosophy of mind debates. Whether machines could ever replicate what minds can do is exactly the type of questions I am interested in.
I was very happy to actually "build" an argument, "from my own hands", to argue that very basic machines could do very complex things (and perhaps one day, do what minds can do).


## After the PCBS course
I hope I have learned to write a code properly, that is, I feel that I now learned what procedure to follow in order to write a program that responds to a specific problem.
I have also learned:
python's basic tools such as lists, dictionaries, etc
How to write loops
But also pandas and Numpy
How to use the shell
How to use Github

This project made me feel more confident that I could understand the basic principles of a code and the conceptual depth of it. Here, it took me a great deal of time to, first, understand Dennett's chapter, second write a corresponding script (for this, I spent days in a row to write it ! I am grateful I had the code from the course as a guideline) and third, to really understand all the implications of the code (by doing the exercises of the chapter - and some were really hard for me). It was both a programming and logical challenge for me. But I am very happy I did it.


## Feedbacks for the course
The programing course was actually the one I was the most looking for when entering the Cogmaster - as I want to specialize in questions related to AI and, thus, because it was one of my highest motivation to reorient my curriculum towards cognitive sciences to complete my background in social sciences and philosophy of mind.

In terms of feedbacks, I would first say that it is important to separate groups by level because I felt horribly demotivated siting next to people who had a very high level in programing. I was always censuring myself to ask questions because they were way too "beginner level". I think I needed more time to assimilate the vocabulary and the general logic.
Maybe it could have been more helpful to merge this course with the datacamp one or to integrate both in a way that makes one complete the other; for example make one be the lecture and the other the "application" session. Or just give more time to both courses.
