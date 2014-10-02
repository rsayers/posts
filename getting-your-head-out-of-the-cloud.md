Title: Getting your head out of the cloud
Date: 2009-01-26 16:52:00+00:00
Category: computing

Thanks to Google, storing your digital "life" in the cloud is the thing to do,
and with good reason. Current web browsers deliver usability equal to that of
desktop apps and untie you from a certain machine.

  
  
  
What happens though when these services go under? The way the economy is going
now, more and more tech shops are closing up, even Google has not been immune
to layoffs and axing products. Google notebook was a recent casualty. While
it's unlikely that Gmail is going away any time soon, what about other
services which might be important to you?

  
  
  
Some time ago, this (along with other concerns I will voice in a future post)
made me decide to consolidate the cloud and get it firmly in my control. I
rent a virtual private server from [Linode](http://www.linode.com/). [Slice
Host](http://www.slicehost.com/) is a similar service which is also popular.
For only $20 per month I get a virtualized Linux server with root access, I
can pick which distro I want, and exactly what software I want to run. I'm
currently hosting web, email, Jabber/Xmpp, OpenID and a couple other misc
services.

  
  
  
For email I'm using postfix/courier. With a standard smtp/imap server running,
I can then install the webmail client of my choosing. While nothing I've found
works quite as well as the Gmail interface, [Roundcube](http://roundcube.net/)
works extremely well. I actually use Mutt as my primary client, but having
webmail setup is handy when I'm at a computer without ssh access.

  
  
  
For Office/Calendar type apps, there are things like
[eyeOS](http://eyeos.org/) and [OpenGOO](http://www.opengoo.org/). Both have
strengths and weaknesses, but seem to work well.

  
  
  
Net based file storage is as simple as setting up [WebDAV in
Apache](http://www.howtoforge.com/setting-up-webdav-with-apache2-on-debian-
etch) giving you lots of storage space in a format that can be mounted from a
Linux, Windows, or OSX client.

  
  
  
Setting up a blog a website is easy as well. I recommend
[Wordpress](http://www.wordpress.org/) as it allows you to create a pretty
complete website with a blog and regular pages.

  
  
  
I'm running Jabberd 1.4 for instant messaging. Since it is able to federate
with other XMPP servers, I can login to my local server and add friends who
use gtalk as if I were on that service already. By using transports I can also
log into AIM without needing to use multiple clients or accounts, anywhere I
am I just login to my main account to talk to anyone.

  
  
  
While this setup is not for anyone, my point was to prove that it's not
impossible to get your data and communications into your own control. By
renting an inexpensive virtual server, you get full control on a machine you
can manage and backup as you wish and never have to worry about a third party
managing your data again.

