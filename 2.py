import sys
import os
import numpy as np
class ImageClass():
  "Stores the paths to images for a given class"
  def __init__(self, name, image_paths):
    self.name = name
    self.image_paths = image_paths

  def __str__(self):
    return self.name + ', ' + str(len(self.image_paths)) + ' images'

  def __len__(self):
    return len(self.image_paths)

def get_dataset(paths):
  dataset = []
  for path in paths.split(':'):
    path_exp = os.path.expanduser(path)
    classes = os.listdir(path_exp)
    classes.sort()
    nrof_classes = len(classes)
    for i in range(nrof_classes):
      class_name = classes[i]
      facedir = os.path.join(path_exp, class_name)
      images = os.listdir(facedir)
      image_paths = map(lambda x: os.path.join(facedir,x), images)
      dataset.append(ImageClass(class_name, image_paths))
  print("########dataset size:%d ###################" %(len(dataset)))
  return dataset

def split_dataset(dataset, split_ratio, mode):
  if mode=='SPLIT_CLASSES':
    nrof_classes = len(dataset)
    class_indices = np.arange(nrof_classes)
    np.random.shuffle(class_indices)
    split = int(round(nrof_classes*split_ratio))
    train_set = [dataset[i] for i in class_indices[0:split]]
    test_set = [dataset[i] for i in class_indices[split:-1]]
  elif mode=='SPLIT_IMAGES':
    train_set = []
    test_set = []
    min_nrof_images = 2
    for cls in dataset:
      paths = cls.image_paths
      np.random.shuffle(paths)
      split = int(round(len(paths)*split_ratio))
      if split<min_nrof_images:
        # If the number of train set images are too few we throw an exception
        raise ValueError('Too few images in train set (%d) for class "%s"' % (split, cls.name))
      if len(paths)-split<min_nrof_images:
        # If the number of test set images are too few we use all images for training
        split = len(paths)
      train_set.append(ImageClass(cls.name, paths[0:split]))
      if split<len(paths):
        test_set.append(ImageClass(cls.name, paths[split:-1]))
  else:
    raise ValueError('Invalid train/test split mode "%s"' % mode)
  return train_set, test_set
###choose the images classs with most size and two image left for test .
def choose_dataset_max_set(dataset, train_set_ratio,max_size):
    global saveout
    trainlist=saveout+"/train.list"
    testlist=saveout+"/test.list"
    f1=open(trainlist,'w')
    f2=open(testlist,'w')
    d={}
    nrof_classes=len(dataset)
    train_size=max_size
    if max_size>nrof_classes:
      train_size=int(round(nrof_classes*train_set_ratio))
    cnt=0
    for cls in dataset:
      paths = cls.image_paths
      size=len(paths)
      t={cnt:size}
      cnt+=1
      d.update(t)
    c=sorted(d.items(),key=lambda d:d[1],reverse =True)
    for i in xrange(train_size):
      idx=c[i][0]
      cls=dataset[idx]
      paths = cls.image_paths
      np.random.shuffle(paths)
      for j in xrange(len(paths)):
        if j>len(paths)-3:
	  ss="%s %d\n" %(paths[j],i)
	  f2.write(ss)
	else:
	  ss="%s %d\n" %(paths[j],i)
	  f1.write(ss)
if __name__ == '__main__':
    if len(sys.argv)<2:
        print 'usage datadir savedir'
	exit(0)
    saveout=sys.argv[2]
    dataset=get_dataset(sys.argv[1])
    choose_dataset_max_set(dataset,0.9,10000)
