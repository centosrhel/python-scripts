'''rename all files in a folder'''
import os, sys
mappings = []
def search_file(path):
	i = 1
        items = [x for x in os.listdir(path)]
	for item in items:
		fullpath = os.path.join(path,item)
		if os.path.isdir(fullpath):
			search_file(fullpath)
		elif os.path.splitext(item)[1]=='.png':
			newname = os.path.join(path,os.path.split(path)[1]+'_'+str(i).zfill(4)+'.jpg')
			os.rename(fullpath,newname)
			i += 1
if __name__ == '__main__':
	args = sys.argv
	search_file(args[1])
