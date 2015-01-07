Title: I'm Done!
Date: 2013-07-23 22:37:57+00:00
Category: retrochallenge

This Retrochallenge, I did something I have not done in a while... finished! I
present to you the [Javascript Kim-1
Emulator](http://www.robsayers.com/kim1.html). 

If you are not familiar with
programming one of these, I suggest peeking at [The First Book of
Kim](http://users.telenet.be/kim1-6502/6502/fbok.html). I've played with a few
random bits of 6502 machine code and it seems to do well. I'm pretty pleased
with how it turned out. 

Machine specific addresses currently do nothing, which
is unfortunate since the real machine would let you independently control each
segment of the six, 7-segment displays it has. That is a project for another
day however. 

The ROM code from the manual is loaded, however the number of
subroutines that really work is a mystery. As a toy that can enter and execute
raw 6502 opcodes however, it seems fully functional. All of the keys should
work as expected. Hitting go will execute starting with the currently selected
address, if SST is selected, hitting go will execute one instruction at a
time. If you do create a program that end up going out of control,
unfortunately ST does not seem to save the day as the page will become
unresponsive. This is something else I will fix in the near future. 

If you are
familiar with these beasts and can offer me andy advice, I'd [certainly
appreciate it](mailto:rsayers@robsayers.com). Good luck to all the other
participants as we enter the home stretch!

