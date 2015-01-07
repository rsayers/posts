Title: An assembler for the Gakken GMC4
Date: 2013-09-26 18:25:38+00:00
Category: programming
Tags: programming, computing


I've wanted to write an assembler for a while. After playing with my GMC4 and
getting a handle on its simple architecture, I decided to give it a go. [The
result can be found here.](https://github.com/rsayers/gmc4asm) 

Since there's
no IO on the device aside from a seven-segment display, 7 leds, and a keypad,
the assembler outputs a format that the user can easily read to input into the
device. I added two output modes, one that lists the address, opcodes and
operands, and the original assembly statement line by line. The second should
be easier for output as it provides the address according to which LEDs should
be lit, and every nibble is on its own line. 

This was a fun little project
hacked together over two lunch breaks, but it should be useful for programming
the device going forward. I think my next project will be a higher level
language that targets assembly.

