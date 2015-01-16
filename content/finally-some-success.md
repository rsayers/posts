Title: Finally some progress
Date: 2015-01-15 19:33:00+06:00
Category: retrochallenge

![Talking to my laptop](http://media.robsayers.com/IMG_20150115_182111202.jpg)

My LCD and USB to Serial adapter showed up a day late,  but regardless, I was able to get a little hacking done tonight.

It looks like my Disk drive I found was not good after all.  I might end up scratching the idea of getting full fledged terminal software on this machine for now.  I discovered that the Super Serial Card has a terminal mode built it.  It's a dumb terminal, which limits things a bit, but it's still something I can work with.

I'm running into 2 issues right now.  First of all, the backspace key on the Apple produces the same character that the normal flashing prompt is (no idea what that character is called), and doesn't actually erase anything.

Secondly, when I connect the Apple to my laptop and do the procedure to enter terminal mode,  anything I type on the Linux side echos on the Apple screen perfectly... but anything I type on the Apple comes out incorrectly on the Linux side.  What's more, I have to type a character twice before it shows up in picocom (dumb terminal software I'm using).  Having to type it twice makes me think it's a settings issue, but I have both ends set to 19200, 8N1, no flow control.  And if there was an issue like that, I don't think that the PC would be able to send over text fine, I would think it would be garbled in both directions.

I decided to call it a night at this point and see what I could play on the [Apple2 Game Server](http://asciiexpress.net/gameserver/).  This game is harder than I remember

![Frogger!](http://media.robsayers.com/frogger.jpg)
