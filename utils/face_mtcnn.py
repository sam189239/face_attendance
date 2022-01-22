import cv2
import matplotlib
from matplotlib import pyplot as plt
from mtcnn.mtcnn import MTCNN
import numpy as np
from math import floor


dir = 'H:\\Code\\current_files\\pics\\'
filename = '123.jpg'

def detect_Faces_img(img):
    detector = MTCNN()
    faces = detector.detect_faces(img)
    return faces

def detect_Faces(filedir):
    img = plt.imread(filedir)
    detector = MTCNN()
    faces = detector.detect_faces(img)
    return faces

def draw_Boxes(filedir,box_list):
    img = plt.imread(filedir)
    plt.imshow(img)
    context = plt.gca()
    for box in box_list:
        x,y,width,height = box['box']
        rect = matplotlib.patches.Rectangle((x,y), width, height, fill = False, color = 'blue')
        context.add_patch(rect)
    plt.show()

def draw_Keypoints(filedir, box_list):
    img = plt.imread(filedir)
    plt.imshow(img)
    context = plt.gca()
    for box in box_list:
        for key, value in box['keypoints'].items():
            circle = matplotlib.patches.Circle(value, radius = 1, color = 'red')
            context.add_patch(circle)
    plt.show()

def draw_Box_and_Keypoints(filedir, box_list):
    img = plt.imread(filedir)
    plt.imshow(img)
    context = plt.gca()
    for box in box_list:
        for key, value in box['keypoints'].items():
            circle = matplotlib.patches.Circle(value, radius = 1, color = 'red')
            x,y,width,height = box['box']
            rect = matplotlib.patches.Rectangle((x,y), width, height, fill = False, color = 'blue')
            context.add_patch(rect)
            context.add_patch(circle)
    plt.show()

def extract_Faces(filedir, box_list):
    img = plt.imread(filedir)
    plt.imshow(img)
    num = 3
    for i in range(len(box_list)):
        x1, y1, width, height = box_list[i]['box']
        if width>height:
            l = floor((width/2) * 1.2)
        else:
            l = floor((height/2) *1.2)
        cy = floor(y1+height/2)
        cx = floor(x1+width/2)
        print(cy-l,cy+l, max(cx-l,0),cx+l)
        x2, y2 = x1 + width, y1 + height
        face = img[max(cy-l,0):cy+l, max(cx-l,0):cx+l]
        plt.subplot(1,len(box_list),i+1)
        plt.axis('off')
        plt.imshow(face)
        face = cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
        #cv2.imwrite('H:\\Code\\current_files\\pics\\' + str(num) +'.jpg',face)
        num +=1
        
    plt.show()

def extract_Faces_Save(filedir, box_list, save = False, destdir = ''):
    img = plt.imread(filedir)
    plt.imshow(img)
    num = 3
    # for i in range(len(box_list)):
    #     x1, y1, width, height = box_list[i]['box']

    #     x2, y2 = floor(x1 + height*1.2),floor(y1 + height*1.2)
    #     face = img[y1:y2, x1:x2]
    #     plt.subplot(1,len(box_list),i+1)
    #     plt.axis('off')
    #     plt.imshow(face)
    #     face = cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
    #     if save:
    #         cv2.imwrite(destdir + str(num) +'.jpg',face)
    #     num +=1
    for i in range(len(box_list)):
        x1, y1, width, height = box_list[i]['box']
        if width>height:
            l = floor((width/2) * 1.2)
        else:
            l = floor((height/2) *1.2)
        cy = floor(y1+height/2)
        cx = floor(x1+width/2)
        print(cy-l,cy+l, max(cx-l,0),cx+l)
        x2, y2 = x1 + width, y1 + height
        face = img[max(cy-l,0):cy+l, max(cx-l,0):cx+l]
        plt.subplot(1,len(box_list),i+1)
        plt.axis('off')
        plt.imshow(face)
        face = cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
        if save:
            cv2.imwrite(destdir + str(num) +'.jpg',face)
        num +=1
        
    plt.show()


# filedir = dir + '/' + filename
# img = plt.imread(filedir)
# detector = MTCNN()
# faces = detector.detect_faces(img)
# for face in faces:
#     print(face)
# draw_Boxes(filedir, faces)
# draw_Keypoints(filedir, faces)
# draw_Box_and_Keypoints(filedir, faces)
# extract_Faces(filedir, faces)
