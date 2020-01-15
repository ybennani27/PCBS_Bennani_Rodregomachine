# Final Project - Yasmine Bennani
### Programming a Rodrego machine according to Dennett's chapter "The seven secrets of computer power revealed"

## Introduction
In his 24th chapter "The seven secrets of computer power revealed", Daniel Dennett aims at demystifying how machines work. He argues against these criticisms that presuppose that machines cannot do what minds can do. If such argument is just saying that machines, today, are not able to imitate human brain's capacities, then they are just stating the obvious, according to Dennett. What is his more challenging claim is to argue that even a very basic machine, what he calls the "Register machine" or the "Rodrego machine" is able to do what more elaborated ones, such as the Turing machine and the Von Neumann machine, can.

## Aim of the project
My aim in the current project is to program a Rodrego machine, as conceived of by Daniel Dennett.
The core principle of the program follows two instructions.
The first one is the instruction "Increment" (e.g. "Inc" in my code) and the second one is the instruction "Decrement" (e.g. "Dec" in my code). The "Inc" instruction simply means "add 1" to the current register (a register being "a memory location" or, more metaphorically, "a large box" that contains any number of small items, or to keep on stealing Dennett's examples, any number of "beans" p. 111) whereas the "Dec" instruction means "subtract 1" to the current register. Starting from this, many questions emerge: how can one deal with situations where the "Dec" instruction cannot occur, namely what happens when a register is empty? And, how could the program determine which register to execute the instructions over?

## I. Explicating the algorithm
For formulating the Rodrego machine algorithm, I started by imagining the machine's area of execution as being a large board with many distinct registers (e.g. boxes). Let us say the board contains 10 registers in each board' line.
Now, the first question that puzzled me for a while is "How could I represent this board?".

(a) The board
This is where I thought I could represent each register as an element of a list.
The line "registers = [0] * 10" means I imagine a series of 10 registers. I then fill them up, for example the first register, with 5 beans and the second with 6 beans (this is "registers[1]=5" and the "registers[2]=6")
But creating a board also means creating distinct lines. This is where I borrowed from the course code's example and its method "program.splitlines()".
The creation of distinct lines would help me formulate transitions to the program's next steps.

(b) A third instruction : Branch
There is, indeed, a problem when reviewing the simple two instructions "Inc" and "Dec". What happens when the register is empty? Because, as Dennett notices it, "you can't take a been out of an empty box" (p. 111). This is when the third instruction comes in: Branch. Such instruction actually leads to the reformulation of the "Dec" instruction with regards to Branch, namely by putting it this way: "Decrement register n (subtract 1 from the contents of register n) if you can and go to step m OR if you can't decrement register n (namely if it is empty), Branch to step p".

(c) Representation of the key instructions
The second challenging question for me was: "how could I represent my two key instructions 'Inc' and 'Dec'?"

[... complete...]

(d) All the machine can do


## Conclusion
To quote Dennett, "at first glance, you might not think such a simple machine could do anything very interesting; all it can do is put a bean in the box or take a bean out of the box" (p. 112). But in fact, as proven in the previous section (d), the machine can do all sorts of different things, which I checked and proved to be doable in the algorithm I propose.  


## Experience before the PCBS course
I had no previous knowledge of programming whatsoever. I come from a background in social science and philosophy.

## After the PCBS course
I hope I have learned to write a code properly, that is, I feel that I now learned what procedure to follow in order to write a program that responds to a specific task, starting from a blank slate.
I have also learned:
python's basic tools such as lists, dictionaries, etc
How to write loops
But also pandas, Numpy, Expyriment
to use the shell
to use Github
to understand the basic vocabulary
