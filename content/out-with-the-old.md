Title: Out with the old
Date: 2008-04-02 22:45:00+00:00
Category: computing

And in with Debian.

  
  
  
As i posted before I originally got my eeePc running with eeeDora (eeepc
specific version of Fedora Core 8). After becoming frusterated with not being
able to get certain things (webcam, wpa, skype, firefox 3) working I decided
to give Debian a shot. I followed the directions given
[here](http://wiki.debian.org/DebianEeePC). All the installer does is make it
easy to get a base system going from usb and includes drivers needed to get
acpi and wifi going right away so you can finish the install over a network.
Other than that it's a plain Debian install.

  
  
  
I opted to install a bare system because otherwise Gnome would be installed
with its many programs and getting rid of all of that would be a pain. Once I
had the base system up with the eeepc specific drivers, "aptitude install
desktop xfce4" installed xorg, xfce, and any other apps needed to get a
desktop running.

  
  
  
Certain things like Gimp and OpenOffice were also installed, but I removed
these and issued "apt-get autoremove" to clear out anything else not needed
once it was up and running. This left me with almost 2 gigs of free space on
the internal flash memory (i have a 4G).

  
  
  
It's pretty much perfect now and runs extremely fast on such modest hardware.

