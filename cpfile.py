#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 14:53:22 2017

@author: henryzhang
"""

import os  
import os.path  
import shutil
current_path = os.getcwd()
label_path = os.path.join(current_path, 'label')
resources_path = os.path.join(current_path, 'resources')

label_filelist = [f for f in os.listdir(label_path) if os.path.isfile(os.path.join(label_path, f))]
#resources_filelist = [f for f in os.listdir(resources_path) if os.path.isfile(os.path.join(resources_path, f))]

#filelist = os.listdir(path) #该文件夹下所有的文件（包括文件夹）

for label in label_filelist:
    filetype = os.path.splitext(label)[1]
    name = os.path.splitext(label)[0]
    image_path = os.path.join(resources_path, name + '.jpg')
    if not os.path.isfile(image_path):
        print("Could not find image file %s, skipping\n" % (image_path))
        continue
    dest = os.path.join(current_path, 'out')
    if not os.path.isdir(dest):
        os.mkdir(dest)
    shutil.copy(image_path, dest)
    

#count={ }
#for name in filelist:   #遍历所有文件
#    video_name = name.split('.')[0]
#    Olddir = os.path.join(path,video_name)   #原来的文件路径    
#    if not os.path.isdir(Olddir):   #如果不存在该视频文件夹
#        os.makedirs(Olddir)
#        count[video_name] = 0
#
#    src = os.path.join(path, name)
#    dst = os.path.join(Olddir,video_name +'_' + str(count[video_name]) + '.png')
#    os.rename(src, dst)
#    count[video_name] = count[video_name] + 1