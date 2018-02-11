# from skimage import filter
from skimage import filter
import scipy.misc
import Image, numpy



######################################################################################################3
#this is code created by me for search image files in directory 
import os
import re
files=os.listdir('./')
k=[]
v=[]
for f in files:
    
#    print f[-2:]   #one method of stripping
     a=f.split('.') # method of spitting
     if len(a)==2:
        
        b=dict(zip(a[0:1],a[-1:])) #creating individual dictionaries
        k.append(a[0])
        v.append(a[1])

fin=dict(zip(k,v))    

for i in fin.keys():
    if fin[i]=='jpg':
       #print i
       for m in files:
           if i in m:
              print m
##########################################################################################
     
              # opening the image and converting it to grayscale
              a = Image.open(m).convert('L')
              # a is converted to an ndarray
              a = scipy.misc.fromimage(a)
              # performing adaptive thresholding
              b = filter.threshold_adaptive(a,51,offset = 10)##yahan par second argument odd hona chahiye even nahi


              # b is converted from an ndarray to an image
              b = scipy.misc.toimage(b) 
              # saving the image as adaptive_output.png
              # in the folder Figurespb
              b.save(m)
              
