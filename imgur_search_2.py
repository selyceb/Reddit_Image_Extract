from sys import argv
from bs4 import BeautifulSoup
from PIL import Image
import urllib2, cStringIO, re, csv, os, datetime

def get_html(f):
	response = urllib2.urlopen(f)
	html = response.read()
	return html

#from: http://blog.zeevgilovitz.com/detecting-dominant-colours-in-python/	
def most_frequent_color(image):
	w, h = image.size
	pixels = image.getcolors(w * h)
	most_frequent_pixel = pixels[0]
	
	for count, color in pixels:
		if count > most_frequent_pixel[0]:
			most_frequent_pixel = (count, color)
	
	return most_frequent_pixel[1]
	
def most_frequent_color_count(image):
		w, h = image.size
		pixels = image.getcolors(w * h)
		most_frequent_pixel = pixels[0]
	
		for count, color in pixels:
			if count > most_frequent_pixel[0]:
				most_frequent_pixel = (count, color)
		
		return most_frequent_pixel
	
def url_to_file(url):
	file = cStringIO.StringIO(urllib2.urlopen(url).read())
	return file
	
#from: http://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

#Write RGB Value, Pixel Count, and Time to CSV File
def write_to_csv(out_file, rgb, count):
	with open(out_file, "a") as csv_out:
		fieldnames = ['Count', 'RGB', 'Time', 'Date']
		writer = csv.DictWriter(csv_out, fieldnames = fieldnames)
		#Write header if file is empty
		if os.stat(out_file).st_size == 0:
			writer.writeheader()
		time = datetime.datetime.now().time().isoformat()
		date = datetime.datetime.now().date().isoformat()	
		writer.writerow({'Count': count, 'RGB': rgb, 'Time': time, 'Date': date}) 
		#Excel formula: =INDEX(B2:B22,MODE(MATCH(B2:B22, B2:B22, 0)))	
		csv_out.close()

output = open('view_images.html', 'w')	
html = get_html('http://www.reddit.com/r/all')	
soup = BeautifulSoup(html)
outstring = ''

#Write html file ( to be cleaned up)
outstring += "<!DOCTYPE HTML><html><head><title>Imgur Links</title></head><body>"
#write each link to html file
for link in soup.findAll('img'):
	links = link.get('src')
	image_string = ''
	outstring += '<img src="http:'
	outstring += links
	outstring += '">'
	outstring += '\n'
	image_string += "http:"
	image_string += links
	im = Image.open(url_to_file(image_string))
	hex = rgb_to_hex(most_frequent_color(im))

	write_to_csv("output.csv", most_frequent_color_count(im)[1], most_frequent_color_count(im)[0])
	
#display color and hex value of each color in html
	outstring += '<p style="color:'
	outstring += hex.upper()
	outstring += '">'
	outstring += hex.upper()
	outstring += '</p>'
	outstring += '\n'

#write and close html file
outstring += "</body></html>"
output.write(outstring);
output.close()