Title: Let's build an emulator - Part 2: Starting our CPU
Date: 2014-03-02 02:47:39.283950+00:00
Category: computing

The first place we want to start when writing an emulator is the CPU itself.  The Apple 1 is of course powered by the [6502]. Thankfully this is a pretty simple processor to wrap your head around, which makes it a good first platform for emulation.

I've started to work on the CPU code, which you can find at [Github](https://github.com/rsayers/py-apple1/blob/part1/cpu.py).  For now I'd like to do a walkthrough of what the code does and how it work.

At a glance, this is pretty simple Python code, so it should be easy to follow.  Line 6 declares an array called memory.  As its name would suggest, this is for storing our program and data for the cpu to read.  Lines 9,10,11 declare our general purpose registers.  A register is a byte of memory that exists in the cpu itself and is used for immediate data manipulation.  When adding two numbers for instance, you would add them to the A register (which stands for accumulator for this reason) and once your calculaton is complete, you would store the value of the A register in memory.  Line 14 declares a stack pointer.  We wont be using the stack in this example, so i'll save the explanation for later.

On line 17 we have the program counter, or PC.  This is merely a special register that stores the address of our current instruction so the CPU knows what to do next.  Changing this also allows us to alter the flow of a program while it is running.

The next section are the CPU flags.  Again, since we arent using them in this article, I'll save the explanation for later.

Finally we get to a dictionary of our CPU instructions, or opcodes as they are often called. You can think of these as functions in a way.  Most of them take in arguments (called operands in the assembly world) and do something with them.  For our first milestone, we want to be able to run a really simple assembly program, one that will swap two values in memory.  For this, we only need 4 instructions.

The program we want to run looks like this in assembly:

    LDA 00 ; Store the value at 0x00 in the A register
    LDX 01 ; Store the value at 0x01 in the X register
    STA 01 ; Store the value in the A register in location 0x01
    STX 00 ; Store the value in the X register in location 0x00
    
The program will read whatever data is in memory locations 0x00 and 0x01 and swap them.  By the way, now would be a great time to  brush up on [hexidecimal](http://en.wikipedia.org/wiki/Hexadecimal) since we're going to be seeing it a lot.  You're probably aware that computers deal natively with binary,  but most of the times when we work with them on a low level, we're dealing with hexidecimal.  If you're lost, don't worry,  until you get to the number 9,  decimal and hexidecimal are the same,  that "0x" before the number is just to let us know we are indeed dealing with hex.  But for now,  know that Im talking about the first two memory locations, numbered 0 and 1.

So let's look at those instructions.  LDA is a mnemonic for "Load A", and this takes the operand, finds the value stored in that location, and stores it in our A register.  On our second line we see LDX, which as you can guess means "Load X" and does the exact same thing.

STA and STX do the opposite.  They stand for "Store A" and "Store X" respectively.  They take the value in the register, and store it in the location specified.  So we can see that our program reads location 0 into a, and then writes it to location 1,  while location 1 is read into x, and then written to location 0, this swapping their values.  It's not an exciting program by any means, but its easy to understand, and a great first test of our new emulated cpu.

Again looking at [our cpu](https://github.com/rsayers/py-apple1/blob/part1/cpu.py), take a look at the "run" function on line 48.  All this function does is run the current instruction by calling our "step" function, as long as we have not reaced the end of memory, and as long as we have not signaled a break.

The real fun begins on line 60 with the "step" method. It pulls out the value in memory where our program counted is pointing, and then tries to run an instruction that matches that name. And by name I mean a hexidecimal value.  If you've done a little assembly or are at least familiar with it,  you've probably read that assembly is the processors native langauge and is as low as you can go.  Actually that's not true.  All our great names such as LDA or STA, are called mnemomics and when you run them through an assembler, they get converted to the hex value that the cou actually understands.  So LDA actually becomes the hex value 0xA5, and LDX becomes 0xA6.  So when the step method reads 0xA5 from memory, it looks in the dictionary we defined on line 35 and sees that it points to "ins_a5" which we define on line 69.

If we take a look at ins_a5, it does pretty much what you expect:

    def ins_a5(self):
        self.a=self.memory[self.memory[self.pc+1]]
        self.pc+=1

It loads the A register (which in our code is self.a) with the memory location pointed to by the program counter + 1.  At this point our program counter still points to the current instruction, so we have to look ahead by one to get the operand we want.  The next line increments our program counter by one so the cpu knows where to look for the next instruction.  Of course that actually just moves it to the value we just stored in our A register, but once this method completes, we are brought back to our "run" method where the very next thing we do on line 58 is increment the value again.

We do this here because every single instruction will take at least 1 value in memory.  Some instructions such as "NOP" which means no operation, and literally does nothing when it is encounter, takes no operands, so it doesnt need to advance the program counter more than 1.  LDA does take an operand, so we depend on it to increment the counter in preperation for the next one.

Now take a look at [apple1.py](https://github.com/rsayers/py-apple1/blob/part1/apple1.py) which is our main computer emulator.  Of course if you take a look you'll realize that it's not emulating much of anything right now, but this code will grow as the series continues.  Right now its purpose is to load our cpu code,  put our test program in memory, and run it.

On line 5 you can see that I am entering our test program manually into memory.  Location 0 and 1 have the value 6502 and 42 respectively.  And starting with location 2, we have the hex values for our instructions.  Line 16 tells our cpu to start executing code at location 0x02.  If it started at 0, the first value it pulled would be 6502, and would not be a valid instruction.  We then have a line printing out those memory values right before we tell our cpu to run it. 

We have the same line after which just lets us validate that what we expected did indeed happen:

    rsayers@ideapad:~/pyapple1$ python apple1.py 
    Before -- 0x00: 6502 0x01: 42
    After  -- 0x00: 42 0x01: 6502
    
Success!  While this was not at all an impressive example, it does lay down some fundamentals and proves that we can load up programs into memory and run them.  The next step is to finish up our cpu and add in all the instructions.  This will free us up to start working on programming the parts that are specific to the Apple1.


[6502]:http://en.wikipedia.org/wiki/MOS_Technology_6502