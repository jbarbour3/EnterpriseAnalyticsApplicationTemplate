# EnterpriseAnalyticsApplicationTemplate
MVP for deploying python/tkinter code as a standalone EXE within an enterprise(build process for windows 10). 


DETAILS:
What this is: This is the bare minimum you need to get your python+tkinter code turned into a .exe file that you can then distribute / use on other windows systems without having any additionnal requirements.

How its used once you've got it set up successfully:
1. Execute the "launch build.bat" file(do this by opening the file and running it, maybe as admin if required). This will do the following...
1.1 start a small local "Build process" by  looking at your "Main.py" or equivalent file
1.2 It will recursively copy libraries you reference in your code so that they are packaged up nicely
1.3 Then it will do some cleanup and movement of files. Most importantly, everything will be output to the "Builds" folder, in a seperate folder named as Date-Time so that you know what build it is.

![alt text](https://raw.githubusercontent.com/jbarbour3/EnterpriseAnalyticsApplicationTemplate/master/Capture.JPG)
