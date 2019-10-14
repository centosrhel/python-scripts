import os, sys
f1 = open('mappings.txt','w')
root_dir = ''
items = os.listdir(root_dir)
for item in items:
    files = os.listdir(root_dir+'/'+item)
    for filename in files:
        if os.path.splitext(filename)[1]=='.jpg':
            f1.write(root_dir+'/'+item+'/'+filename+' '+root_dir+'/../lfw_aligned_dlib/'+item+'/'+os.path.splitext(filename)[0]+'.png\n')
f1.close()
