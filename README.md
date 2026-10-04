# What's monofetch and why did you made it?
I always didn't like fastfetch. It looked too heavy and too popular. And it didn't support a lot of linux distributions. As an example, on RaspberrypiOS it showed Debian logo instead of RaspberryPiOS logo. And this happened to most linux distros, that aren't in the "MOST POPULAR DISTROS" list. So, I made this. This fetch doesn't use any imports(even import os isn't allowed here). It works with system files instead "import os", use colour codes instead "import colorama", etc.

# How to use it?
First, download "monofetch.py". Then, type <python3 "$(xdg-user-dir DOWNLOAD)/monofetch.py">. Soon, I should make an installer for this, so you can run it by only type "monofetch" in your terminal.

# When you should release an installer and add more distro logotypes?
I should make an installer in May, I think. With every new release monofech will have more logotypes.

If you're still have any questions, contact me using the contact in my profile. Enjoy monofetch!

# Updates
UPD 0.3 announcement

 Yeah, after almost half of year, I'm back. So, in this update I'll add support for three new distros(Mint, Alpine and openSUSE). Also I'll clean the output: no more unnesessary components of /etc/os-release — now only the information that you need.
 I'm also thinking about rewriting monofetch in C. But firstly I need to make it polished in python. Because of it will never use imports, it's better to rewrite it in clear C for faster work and the ability to use keys(eg. --color). Once I'll make a website for it. Also, I'll delete the "Updates" section and post everything in Releases.

 ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
 
UPD 0.2:
3 new distros logos are added.
No more imports.
Battery info is now avaiable. Device's temperature is now shows.
Installer will be added in version 0.3

![ ](./IMG_20260403_150304_296.jpg)
