This program extracts "icons" of images used in posts on 
www.reddit.com/r/all.

The most common color value in each image is then
found using Image.

The images and their most common colors are displayed
in "view_images.html"

You will need Beautiful Soup 4 and PIL to run this script.

This is an early version and very messy, so I apologize.

You can easily modify this code to be used with other pages
by changing the string value in the initialization of "html".

This code is not intended for commercial use and I used advice
or pieces of code from each of these sites:

http://blog.zeevgilovitz.com/detecting-dominant-colours-in-python/

http://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa