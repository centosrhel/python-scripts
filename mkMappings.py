import os, sys
f1 = open('filelist.txt','w')
root_dir = '/data/work-data/raw-data/PAKJ/NEW'
items = os.listdir(root_dir)
for item in items:
	new_item = item + ' '
	files = os.listdir(root_dir+'/'+item)
	for filename in files:
		if os.path.splitext(filename)[1]=='.jpg':
			new_new_item = new_item + filename
			f1.write(new_new_item+'\n')
f1.close()
