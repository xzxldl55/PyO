# -*- coding:utf-8 -*-

'''
PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。
'''
from PIL import Image, ImageFilter, ImageDraw, ImageFont

# 1.demo缩放图片
# im = Image.open('big99007.jpg')
# # 获得尺寸
# w, h = im.size
# print('Original image size: %sx%s' % (w, h))
# # 缩放到50%
# im.thumbnail((w // 2, h // 2))
# print('Resize image to: %sx%s' % (w // 2, h // 2))
# # 重新保存 --> 图片就被压缩掉了
# im.save('thumbnail.jpg', 'jpeg')

# 2.滤镜...
# im = Image.open('big99007.jpg')
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg', 'jpeg')

# 3.绘图-->生成字母验证码
import random

# 随机字母


def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色


def rndColor():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 随机颜色2:


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240 * 60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())  # 随机填充颜色

# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
