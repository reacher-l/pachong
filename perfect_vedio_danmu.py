# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 17:38:44 2019

@author: Administrator
"""


from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.fx import resize
from moviepy.video.tools.segmenting import findObjects

import numpy as np
import cv2

from PIL import Image, ImageDraw, ImageFont
 
if __name__ == "__main__":
    
    barrages_all = [
    ('ballankscovwvvevdfvvd', 1),
    ('blablablablablablablablablablablabla', 2),
    ('ooooooooooooo', 3),
    ('1500万.....', 12),
    ('发', 5),
    ('每日三刷', 1),
    ('建议赶紧出去，要不然一会就晚了', 7),
    ('可怕', 9),
    ('666', 4),
    ('小孩子才做选择，我全都要', 4),
    ('弹幕被清了好多', 21),
    ('颜表立', 2),
    ('可耻的播放量', 17),
    ('哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', 5),
    ('我没有', 12),
    ('38', 9),
    ('这毒，我！不！戒！', 15),
    ('还是小姨妈好看、', 27),
    ('我是来看腿的', 5),
    ('B站毒枭', 2),
    ('小孩才会选，我全都要！', 49),
    ('出不去了', 60),
    ('在现场 我是丝袜', 106),
    ('暂停成功', 218),
    ('开头见', 223),
    ('颜表立！', 17),
    ('颜表立！ 抱走猫酱', 92),
    ('突然害怕', 197),
    ('未来我的广场舞', 215),
    ('没弹幕', 18),
    ('白衣服的是我的，，', 155),
    ('这个我还是喜欢白衣服的，，', 117),
    ('白衣服是我的!', 177),
    ('我要表白白色，，，', 210),
    ('色表立', 40),
    ('C位终于浮现', 173),
    ('1600万助攻', 50),
    ('这么可爱怎么舍得拔头吃', 118),
    ('为了蕾丝', 29),
    ('1600万助攻', 14),
    ('颜表立', 51),
    ('喵酱我的！！！', 7),
    ('小孩子才全都要！我只要喵酱。', 80),
    ('极乐净土原作一出来就和大家一样很激动的喜欢上了，所以其实后面看到很多很多催稿极乐净土的评论，我都一直会想，啊，想默默练习给大家一个惊喜这件事恐怕是不行了～这支舞对于我非常有挑战，激发起了我全部的热情和', 93),
    ('颜表立', 32),
    ('欢迎回来，颜表立', 6),
    ('小孩子才做选择，我全都要', 14),
    ('全程看红色', 126),
    ('来考古的', 145),
    ('最高日第一emm', 18),
    ('哥仨不火天理难容', 19)]
    
    def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
        if (isinstance(img, np.ndarray)):  #判断是否OpenCV图片类型
            img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img)
        fontText = ImageFont.truetype(
                "font/simsun.ttc", textSize, encoding="utf-8")
        draw.text((left, top), text, textColor, font=fontText)
        return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    #step1: load in the video file
    videoCapture=cv2.VideoCapture('lei.mp4')
    
    #step2:get a frame
    sucess,frame=videoCapture.read()
    
    #step3:get frames in a loop and do process 
    i=0
    while(sucess):
        if i==51:
            i=0
        sucess,frame=videoCapture.read()
        displayImg=cv2.resize(frame,(1024,768)) #resize it to (1024,768)
#        cv2.putText(displayImg,barrages_all[i][0],(100,50),cv2.FONT_HERSHEY_PLAIN,2.0,(0,0,255),2)
        
        displayImg = cv2ImgAddText(displayImg, barrages_all[i][0], 20, 60, (255, 255, 0), 20)
        
        cv2.namedWindow('test Video')    
        cv2.imshow("test Video",displayImg)
        keycode=cv2.waitKey(10)
        i=i+1
        if keycode==27:
            cv2.destroyWindow('test Video')
            videoCapture.release()
            break
