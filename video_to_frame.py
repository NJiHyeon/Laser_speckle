import cv2
import os

#####CLASS1#####
# class1의 동영상에 대한 경로
class1 = []
for c in ['1', '1_2'] :
    for p in ['pos_1', 'pos_2', 'pos_3', 'pos_4', 'pos_5']:
        PATH = os.path.join('./data/', c, p)
        videofiles = os.listdir(PATH)
        for v in videofiles :
            videofiles_path = os.path.join('./data/', c, p, v)
            print(videofiles_path)
            class1.append(videofiles_path)
          
# class1의 동영상을 frame으로 추출 
for c1 in class1 :
    vidcap = cv2.VideoCapture(c1)
    success, image = vidcap.read()
    count = 0
    fn = c1.split('/')
    class_name = fn[2]
    pos_name = fn[3]
    video_name = fn[4]
    foldername = class_name + '_' + pos_name + '_' + video_name
    while success :
        if int(vidcap.get(1))%1==0:
            framename = "f_{number:05}".format(number=count)
            #if not os.path.exists(f'./frames/1/{foldername}'):
                #os.makedirs(f'./frames/1/{foldername}')
            if not os.path.exists(f'./frames/{foldername}'):
                os.makedirs(f'./frames/{foldername}')
            cv2.imwrite(f'./frames/{foldername}/' + framename + '.jpg', image)
            #cv2.imwrite(f'./frames/1/{foldername}/' + framename + '.jpg', image)
            success, image = vidcap.read()
            count += 1
        else :
            success,image = vidcap.read()
            count += 1

#=======================================================================================================
#####CLASS3#####        
# class3의 동영상에 대한 경로
class3 = []
for c in ['3', '3_2'] :
    for p in ['pos_1', 'pos_2', 'pos_3', 'pos_4', 'pos_5']:
        PATH = os.path.join('./data/', c, p)
        videofiles = os.listdir(PATH)
        for v in videofiles :
            videofiles_path = os.path.join('./data', c, p, v)
            class3.append(videofiles_path)
            
# class3의 동영상을 frame으로 추출
for c3 in class3 :
    vidcap = cv2.VideoCapture(c3)
    success, image = vidcap.read()
    count = 0
    fn = c3.split('/')
    class_name = fn[2]
    pos_name = fn[3]
    video_name = fn[4]
    foldername = class_name + '_' + pos_name + '_' + video_name
    while success :
        if int(vidcap.get(1))%1==0:
            framename = "f_{number:05}".format(number=count)
            if not os.path.exists(f'./frames/{foldername}'):
                os.makedirs(f'./frames/{foldername}')
            #if not os.path.exists(f'./frames/3/{foldername}'):
                #os.makedirs(f'./frames/3/{foldername}')
            cv2.imwrite(f'./frames/{foldername}/' + framename + '.jpg', image)
            #cv2.imwrite(f'./frames/3/{foldername}/' + framename + '.jpg', image)
            success, image = vidcap.read()
            count += 1
        else :
            success,image = vidcap.read()
            count += 1
            

#하나씩#
'''
./data/1/pos_1/Basler_acA640-750um__24616320__20240215_10112438.avi
'''
'''
a = './data/1/pos_1/Basler_acA640-750um__24616320__20240215_10112438.avi'
a.split('/')
vidcap = cv2.VideoCapture(a)
success, image = vidcap.read()
count = 0
fn = a.split('/')
class_name = fn[2]
pos_name = fn[3]
video_name = fn[4]
foldername = class_name + '_' + pos_name + '_' + video_name
framename = "f_{number:05}".format(number=count)
while success :
    if int(vidcap.get(1))%1==0:
        framename = "f_{number:05}".format(number=count)
        if not os.path.exists(f'./frames/1/{foldername}'):
            os.makedirs(f'./frames/1/{foldername}')
        cv2.imwrite(f'./frames/1/{foldername}/' + framename + '.jpg', image)
        success, image = vidcap.read()
        count += 1
    else :
        success,image = vidcap.read()
        count += 1
'''