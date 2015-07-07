
import webbrowser
import time
def link_opener():
	x=0
	while x<3:
		webbrowser.open("https://docs.google.com/spreadsheets/d/1gd_wjNJTlGe821nME7yc5DEvZj_I5xTqtPE5CA5gap8/edit#gid=2037554563")
		time.sleep(5)
		x += 1
link_opener()