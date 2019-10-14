import sys
import os
from PIL import Image
def resize(im_path,save_path):
    im=None
    global size_im
    try:
        im=Image.open(im_path)
    except:
        return
    print im_path
    filename=os.path.basename(im_path)
    save_dir=None
    if save_path==None:
        save_dir=im_path
    else:
	save_dir="%s/%s" %(save_path,filename)
    out=im.resize((size_im,size_im))
    out.save(save_dir)
def rgb2gray(im_path,save_path):
    global size_im
    try:
        im=Image.open(im_path)
    except:
        return
    im=im.convert('L')
    filename=os.path.basename(im_path)
    save_dir=None
    if save_path==None:
        save_dir=im_path
    else:
	save_dir="%s/%s" %(save_path,filename)
    out=im.resize((size_im,size_im))
    out.save(save_dir)

 
if __name__ == '__main__':

    if len(sys.argv)<3:
        print('usage image_size filelist savepath')
        exit(0)
    size_im=int(sys.argv[1])
    file=open(sys.argv[2])
    save=None
    if len(sys.argv)==4:
        save=sys.argv[3] 
    for x in file:
        x=x.strip()
	rgb2gray(x,save)	

