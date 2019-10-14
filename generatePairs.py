#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hu@wondershare'

import os
import random

mainDir = '/data/DP/datatmp/WS_Cap29/Capture-29-align-5pt'
subDirs = os.listdir(mainDir)

genuine = []
#imposter = []
#p = 0
for subDir in subDirs:
	files = os.listdir(os.path.join(mainDir,subDir))
	fileNum = len(files)
	Seq = range(fileNum)
	for i in Seq:
		for j in range(i+1, fileNum):
			genuine.append("{} {} {}".format(subDir, files[i], files[j]))
random.shuffle(genuine)
with open('./genuine.txt', 'w') as f:
	for item in genuine:
		f.write(item+'\n')

imposter = []
folderNum = len(subDirs)
Seq = range(folderNum)
for i in Seq:
	files1 = os.listdir(os.path.join(mainDir, subDirs[i]))
	fileNum1 = len(files1)
	Seq1 = range(fileNum1)
	for j in range(i+1, folderNum):
		files2 = os.listdir(os.path.join(mainDir, subDirs[j]))
		fileNum2 = len(files2)
		Seq2 = range(fileNum2)
		for m in Seq1:
			for n in Seq2:
				imposter.append("{} {} {} {}".format(subDirs[i], files1[m], subDirs[j], files2[n]))
random.shuffle(imposter)
with open('./imposter.txt', 'w') as f:
	for item in imposter:
		f.write(item+'\n')

f1 = open('genuine-Cap29.txt','r')
f2 = open('imposter-Cap29.txt','r')
f3 = open('pairsCap.txt','w')
list1 = f1.readlines()
list2 = f2.readlines()
i = 0 #10
interval = 300
while i < 10: #20
	tlist1 = list1[i*interval:(i+1)*interval]
	tlist2 = list2[i*interval:(i+1)*interval]
	for line in tlist1:
		f3.write(line)
	for line in tlist2:
		f3.write(line)
	i += 1
f1.close()
f2.close()
f3.close()
