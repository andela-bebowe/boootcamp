import webbrowser
import time

def list_browser(web_array):
	p = 0
	for x in web_array:
		while p < 2:
			webbrowser.open (x[0])
			time.sleep(x[1])
			p += 1
	if p == 2:
		webbrowser.open (x[0])

weblist = [["http://p102.sci.website/docs/shell/", 10], ["http://p102.sci.website/docs/shell/", 10], ["http://p102.sci.website/docs/shell/", 10]]

list_browser(weblist)