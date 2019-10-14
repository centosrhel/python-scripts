import os, sys
items = os.listdir('/data/work-data/raw-data/PAKJ/NEW')
for item in items:
	os.mkdir('/data/work-data/align-data/pakj-new/'+item)
