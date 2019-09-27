# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:49:01 2019

@author: Administrator
"""
#! encoding: UTF-8

import os

import cv2
#import cv

#videos='lei.mp4'
#
#for each_video in videos:
#    print (each_video)
#
#    # get the name of each video, and make the directory to save frames
#    each_video_name, _ = each_video.split('.')
#    os.mkdir(videos_save_path + '/' + each_video_name)               
#
#    each_video_save_full_path = os.path.join(videos_save_path, each_video_name) + '/'
#
#    # get the full path of each video, which will open the video tp extract frames
#    each_video_full_path = os.path.join(videos_src_path, each_video)
#
#    cap  = cv2.VideoCapture(each_video_full_path)
#    frame_count = 1
#    success = True
#    while(success):
#        success, frame = cap.read()
#        print 'Read a new frame: ', success
#
#        params = []
#        params.append(cv.CV_IMWRITE_PXM_BINARY)
#        params.append(1)
#        cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.ppm" % frame_count, frame, params)
#
#        frame_count = frame_count + 1

#cap.release()

#video_path='lei.mp4'
#video_save_path='lei_save_frame'
#cap  = cv2.VideoCapture(video_path)
#frame_count = 1
#success = True
#while(success):
#    success, frame = cap.read()
#    print ('Read a new frame: ', success)
#    params = []
#    params.append(cv.CV_IMWRITE_PXM_BINARY)
#    params.append(1)
#    cv2.imwrite(video_save_path + "_%d.ppm" % frame_count, frame, params)
#    frame_count = frame_count + 1
#cap.release()



#
#import pylab
#import imageio
##注释的代码执行一次就好，以后都会默认下载完成
##imageio.plugins.ffmpeg.download()
#import skimage
#import numpy as np
# 
##视频的绝对路径
#filename = 'lei.mp4'
##可以选择解码工具
#vid = imageio.get_reader(filename,  'ffmpeg')
#for num,im in enumerate(vid):
#    #image的类型是mageio.core.util.Image可用下面这一注释行转换为arrary
#    print (im.mean())
#    image = skimage.img_as_float(im).astype(np.float64)
#    fig = pylab.figure()
#    fig.suptitle('image #{}'.format(num), fontsize=20)
#    pylab.imshow(im)


cap = cv2.VideoCapture("lei.mp4")#名为'003.mp4'的文件
c=0                             #文件名从0开始
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    cv2.imwrite('image/'+str(c) + '.jpg',frame) #存储为图像
    c=c+1
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
