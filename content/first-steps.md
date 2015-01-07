Title: First Steps
Date: 2013-07-03 22:32:53+00:00
Category: retrochallenge

After a few days hacking this together, i've made some progress! If you want
to take a look at the project so far, I have it up at
[http://www.robsayers.com/kim1.html](http://www.robsayers.com/kim1.html).
Right now the only opcodes that work are LDA, LDX, STA, and STX. That said,
input works fine... start out by hitting the "RS" (reset) button which will
start you at memory location 0x0000. Hit "AD" (address) to enter another
address, or just hit "DA" (data) to enter in the data for that address. The +
key will jump you to the next address while keeping you in data mode. So
here's the thing... I don't really know assembly, or how processors work or
anything like that. Minor details when emulating a machine right? What I do
have are some books on programming this beast. What I am doing is starting
with the basic examples and working on getting the simulator to run them. I
don't know if this strategy will come back to bite me or not, but so far the
first example program from "[The First Book of
Kim](http://users.telenet.be/kim1-6502/6502/fbok.html)" runs quite well! That
program is:

    
    
    0200 A5 10    START LDA 10   address 10 to A
    0202 A6 11          LDX 11   address 11 to x
    0204 85 11          STA 11   A to address 11
    0206 86 10          STX 10   X to address 10
    0208 00             BRK      stop the program

BRK is technically in there, but since right now it only runs programs step by
step, it's kinda pointless. Don't count on this site being stable, as this is
also where I'm doing development.

