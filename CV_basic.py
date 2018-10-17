# -*- coding: utf-8 -*-

# import cv2
# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import misc

# 读入图片：默认为彩色图（cv2.IMREAD_COLOR），灰度图（cv2.IMREAD_GRAYSCALE）
# img_array = cv2.imread('data/test.png', cv2.IMREAD_GRAYSCALE)
# img_array = cv2.imread('data/test.png')
# 也可以先读入彩色图，再转灰度图
# img_array = cv2.imread('data/test.png')
# img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

# 图片展示：src为展示窗口name，img_array为数组
# cv2.imshow('src', img_array)
# print(img_array)
# print(img_array.shape)  # 如果以彩色图读入，shape为(h,w,c)；如果以灰度图读入，shape为(h,w)
# print(img_array.size)  # 像素总数目
# print(img_array.dtype)  # 数组类型
# cv2.waitKey()  # 线程wait

# img_array = img_array.astype("float") / 255.0  # 这一步可省略
# img_array = img_array / 255.0
# print(img_array.dtype)
# print(img_array)

# 图片存储
# cv2.imwrite('data/test1.jpg', img_array)  # 归一化后得到的是全黑的图片
# cv2.imwrite('data/test2.jpg', img_array * 255)  # 这样就还原了原图片

# roi操作
# roi = img_array[200:550, 100:450, :]
# cv2.imshow('roi', roi)
#
# b, g, r = cv2.split(img_array)  # 通道拆分
# img_array = cv2.merge((b, g, r))  # 通道合并
# img_array[:, :, 2] = 0  # 将红色通道值全部设0

# img = Image.open('data/test.png')
# print(img.format)  # PNG
# print(img.size)  # 输出(w，h)，省略了c
# print(img.mode)  # 输出RGBA。L为灰度图，RGB为真彩色，RGBA为加了透明通道
# img.show()  # 显示图片

# gray = img.convert('L')
# print(gray.format)  # None
# print(gray.size)  # 输出(w，h)
# print(gray.mode)  # L
# gray.show()

# pillow读进来的图片不是numpy array，而是一个对象，用下面方式将图片转numpy array
# arr = np.array(img)
# print(arr.shape)  # (h, w, c)，即(740, 1352, 4)
# print(arr.dtype)  # uint8

# 图像存储
# new_im = Image.fromarray(arr)
# new_im.save('data/test_1.jpg')

# image = plt.imread('data/test.png')
# plt.imshow(image)  # 优化图窗、坐标区和图像对象属性以便显示图像，相当于预热，调用show方法前必须先执行这一步动作
# plt.show()  # 图像展示
#
# # plt.imread读入后就是一个矩阵，跟opencv一样，但彩图的格式是RGB或RGBA，这是与opencv的区别
# print(image.shape)  # (h,w,c)
# print(image.dtype)  # float32
# # [[[0.28627452 0.29411766 0.37254903 1.        ]
# #   [0.21176471 0.22352941 0.32941177 1.        ]
# #   [0.21176471 0.22352941 0.32941177 1.        ]
# #   ...
# # ]]]
# print(image)

# im = misc.imread('data/test.png')  # plt.imread读入后就是一个矩阵
# # [[[ 73  75  95 255]
# #   [ 54  57  84 255]
# #   [ 54  57  84 255]
# #   ...
# # ]]]
# print(im)
# print(im.dtype)  # uint8
# print(im.size)  # 4001920
# print(im.shape)  # (740, 1352, 4)
# misc.imsave('data/test0_1.png', im)  # 图像存储

