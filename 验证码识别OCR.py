# -*- coding:utf-8 -*-
import pytesseract as pt
from PIL import Image

image = Image.open('验证码003.png')#第一步读取图片
chapter = pt.image_to_string(image) #第二步识别验证码
print(chapter)