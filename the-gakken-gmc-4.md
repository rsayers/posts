Title: The Gakken GMC-4
Date: 2013-09-22 02:25:36+00:00
Category: computing
Tags: retrocomputing,programming,computing

After completing my Retrochallenge project in July, I became a bit obsessed
with computers similar to the Kim-1.  Punching in machine code and getting our
results on a seven segment display is just fun.  It turns out there's quite a
few computers like this,  aside from the Kim, there's the Z80 Based MPF-1,
and due to its popularity as a training platform, there are quite a few boards
like this based on the Intel 8085 (Which powers my Tandy Model 100).

 The
problem is that these devices were either old and rare,  or new and expensive.
Considering I just wanted one to goof around with, I sort of gave up on the
idea until I came across the [Gakken GMC4](http://otonanokagaku.net/magazine/vol24/index.html).

![888d7860219211e3979522000a9f309d_7](http://www.robsayers.com/wp-content/uploads/888d7860219211e3979522000a9f309d_7.jpg)

Gakken produces a series of
educational magazinze/books which contain kits.  This one happened to contain
a 4 bit CPU board that is quite fun to program.  There's a really [great blog post by Alexander Demin](http://demin.ws/blog/english/2012/07/04/gmc-4/) which
goes into more detail on the machine. Some resources I've found handy so far:

  * [Programming Guide](http://tsoj.manga.org/gakken/otona_gmc.html)
  * [Optimizing Assembler](http://terus.jp/engineering/gmc4cc/gmc4as.html)
  * [C Compiler](http://terus.jp/engineering/gmc4cc/)
  * [Basic Compiler](http://softyasu.net/g4cbasic.html), It's a windows EXE, but runs under wine with no issue.
  
So of course I got the thing to program, and lately generating the Fibonacci
sequence has become my new "Hello World" so I thought I would start there. 

I'm
not a great assembly developer, and still have trouble getting my brain to
think correctly at that level, but here's what I've come up with.

    
    ; Setup the initial sequence of 0 1 1 to 0x50, 0x51, and 0x52 respectively
    ; 0x53 will also be used later as a temp variable
    START:
    
    	; mem[0] = 0
    	TIA 0 
    	TIY 0
    	AM   
    
    	; mem[1] = 1
    	TIA 1 
    	TIY 1  
    	AM    
    
    	; mem[2] = 1
    	TIY 2 
    	AM   
    
    LOOP:
    
    	; A = mem[2]
    	TIY 2
    	MA
    
    	; print A
    	AO
    
    	; initialize A to zero
    	TIA 0
    
    	; A += mem[2]
    	M+
    
    	; A += mem[2]	
    	TIY 1
    	M+	
    
    	; mem[3] = A
    	TIY 3
    	AM
    
    	; A = mem[1]
    	TIY 1
    	MA
    
    	; mem[0] = A
    	TIY 0
    	AM
    
    	; A = mem[2]
    	TIY 2
    	MA
    
    	; mem[1] = A
    	TIY 1
    	AM
    
    	; a = mem[3]
    	TIY 3
    	MA
    
    	; mem[2] = a
    	TIY 2
    	AM
    
    	; Pause for a bit
    	TIA 9
    	CAL TIMR
    
    	; A = mem[2]
    	TIY 2
    	MA
    
    	; if A != D, jump to the top
    	CIA D
    	JUMP LOOP
    
    	; Otherwise, print the last value
    	AO
    
    END: ; Infinite loop to end the program
    	JUMP END

Instead of recursing (Which is impossible on this machine) or filling an
array, I decided to use 3 memory locations (+ 1 temp) to keep up with each
iteration, and prefilled them for iteration #1. Also since this is a 4 bit
machine, the max value you can store is 15, so the highest value we can
calculate is 13, which will display as "d" since it's in hex.  I assembled it
with the assembler I linked above,  but the assembled code is: **8 0 A 0 4 8 1
A 1 4 A 2 4 A 2 5 1 8 0 6 A 1 6 A 3 4 A 1 5 A 0 4 A 2 5 A 1 4 A 3 5 A 2 4 8 9
E C 5 C D 1 F 3 7** 

This has been a lot of fun to play with.  Using the C
compiler and examining the assembly output, it's neat to see how things like
simple variable assignment work under the hood.  Even your assembler does
quite a bit of work for you. 

This computer was released in 2009 and I don't
believe it was made for that long.  Finding one was a bit of a challenge, the
first place I ordered from emailed me back to let me know it was out of stock
there. [ I eventually lucked out and found it for sale on J-List.](http://www.jbox.com/product/GAK024)
And as far as I know that's the
only place you can find them.  If you have trouble finding one in the future,
it turns out the GMC4 is a repackaged version of the old Tandy Microcomputer
Trainer.  And from what I've seen, the example programs from each machine will
run on the other.  The Tandy turns up on Ebay somewhat regularly, so that's an
option. 

