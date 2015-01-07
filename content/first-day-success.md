Title: First day success
Date: 2014-01-02 00:40:02+00:00
Category: retrochallenge
Tags: retrocomputing,retrochallenge,computing


The day after Christmas I received a box from Jameco... it was most of the
parts I needed for my homebrew computer project. Today I finally had a chance
to mess around with it a bit. 

I turns out that instead of simply ordering a
crystal for the oscillator circuit, I ordered a complete oscillator. I took a
quick peak at the datasheet for what I did order, and it looked like it would
work. I put it on the breadboard, powered it up, and using my Arduino as a
poor-man's scope, I was able to see that it was in fact putting out the square
wave I needed. 

Next I hooked the cpu up to it, I put it in free-run mode so
that the data lines always gave the NOP instruction, so the cpu would simply
read that, then increment the value to the address lines. From what I can tell
this worked as expected. At 1mhz, it's a bit too fast for the Arduino to get
an accurate reading, but I read the value of the most significant bit, which
should stay low for most of the time, and go high briefly, and this is what I
was seeing on the screen. 

So it turns out that I neglected to get a USB->TTL
cable to actually let me communicate with the machine once it's done, I also
did not order the breadboards I needed and am already out of space on the tiny
one I have. Those are on order now. 

The big issue I have is that my cheap
Chinese eprom programmer does not want to work with my pc. It's a Top853 which
appears to be an older model. I can't get the software to run at all in
Windows 8 or in Linux under Wine. I can get it running in an XP VM, but it
fails to recognize the programmer. I'm investigating other options now,
including getting a friend with a working programmer to do it for me. I've
also had the idea of using a micro-controller to read the address bus and
output the correct values to the data bus in place of a rom. This would not
only give me the ability to easily rewrite the rom as needed, but could give
me some good debugging capabilities as well. As this is a retro themed
project, I'm leaning away from the idea of using a modern device to get an
ancient-styled rig going... but it is tempting. 

So far so good though, I've
already learned a ton about what actually goes on in a computer, and how
ram/rom/devices all talk to the cpu. Good luck to all the other participants!

