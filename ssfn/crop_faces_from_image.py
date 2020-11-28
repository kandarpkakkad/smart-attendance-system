import cv2
import sys
import numpy as np
import datetime
import os
import glob
from ssfn.retinaface import RetinaFace
#from mtcnn.mtcnn import MTCNN

base_path = './ssfn/'

def get_faces():
	thresh = 0.8

	count = 1

	gpuid = 0
	detector = RetinaFace(base_path + 'models/R50', 0, gpuid, 'net3')
	index=1
	for file in glob.glob(base_path + "frames/*"):
		identity = os.path.splitext(os.path.basename(file))[0]
		#if not os.path.exists(('cropped/'+identity)):
			#os.mkdir(('cropped/'+identity))
		#for face in glob.glob((file+"/*")):
			#face=os.path.splitext(os.path.basename(face))
			#face=face[0]+face[1]
		scales = [1024, 1980]
		img = cv2.imread(file,1)
		print(img.shape)
		im_shape = img.shape
		target_size = scales[0]
		max_size = scales[1]
		im_size_min = np.min(im_shape[0:2])
		im_size_max = np.max(im_shape[0:2])
		#im_scale = 1.0
		#if im_size_min>target_size or im_size_max>max_size:
		im_scale = float(target_size) / float(im_size_min)
		# prevent bigger axis from being more than max_size:
		if np.round(im_scale * im_size_max) > max_size:
			im_scale = float(max_size) / float(im_size_max)

		print('im_scale', im_scale)

		scales = [im_scale]
		flip = False

		bboxes, landmarks = detector.detect(img, thresh, scales=scales, do_flip=flip)
		#print("111111111111111  ",bboxes)

		width = bboxes[:, 2] - bboxes[:, 0] + 1.0
		height = bboxes[:, 3] - bboxes[:, 1] + 1.0


		det = bboxes[:, 0:4]
		bb = np.zeros((bboxes.shape[0],4), dtype=np.int32)
		#cv2.imwrite("crop_images/frame.jpg",frame)
		for i in range(bboxes.shape[0]):
			bb[i][0] = det[i][0]-width[i]*0.3
			bb[i][1] = det[i][1]-height[i]*0.3
			bb[i][2] = det[i][2]+width[i]*0.3
			bb[i][3] = det[i][3]+height[i]*0.3
			if bb[i][0]<0:
				bb[i][0]=0
			if bb[i][1]<0:
				bb[i][1]=0
			if bb[i][2]>im_shape[1]:
				bb[i][2]=im_shape[1]-1
			if bb[i][3]>im_shape[0]:
				bb[i][3]=im_shape[0]-1

			#color = (0,255,0)
			#cv2.rectangle(img, (bb[i][0], bb[i][1]), (bb[i][2], bb[i][3]), color, 2)

			faces=img[bb[i][1]:bb[i][3], bb[i][0]:bb[i][2], :]
			faces=cv2.resize(faces,(112,112),interpolation = cv2.INTER_AREA)
			cv2.imwrite((base_path + "crop_images/"+str(index)+".jpg"),faces)
			index= index+1
		#cv2.imwrite(("frames/"+str(identity)+"_1"+".jpg"),img)
