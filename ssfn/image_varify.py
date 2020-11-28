import cv2
from PIL import Image
import argparse
from pathlib import Path
from multiprocessing import Process, Pipe,Value,Array
import torch
from ssfn.config import get_config
from ssfn.mtcnn import MTCNN
from ssfn.Learner import face_learner
from ssfn.utils import load_facebank, draw_box_name, prepare_facebank
from ssfn.mtcnn_pytorch.src.align_trans import get_reference_facial_points, warp_and_crop_face
from ssfn.mtcnn_pytorch.src.box_utils import nms, calibrate_box, get_image_boxes, convert_to_square
from ssfn.crop_faces_from_image import get_faces

import sys
import numpy as np
import datetime
import os
import glob
import time
import pickle
from copy import deepcopy
from time import sleep
from matplotlib import pyplot

attendance = []

base_path = '../ssfn/'

def smart_attendance():
	get_faces()
	parser = argparse.ArgumentParser(description='for face verification')
	parser.add_argument("-s", "--save", help="whether save",action="store_true")
	parser.add_argument('-th','--threshold',help='threshold to decide identical faces',default=1.54, type=float)
	parser.add_argument("-u", "--update", help="whether perform update the facebank",action="store_true")
	parser.add_argument("-tta", "--tta", help="whether test time augmentation",action="store_true")
	parser.add_argument("-c", "--score", help="whether show the confidence score",action="store_true")
	args = parser.parse_args()

	conf = get_config(False)

	#mtcnn = MTCNN()
	print('mtcnn loaded')
	
	learner = face_learner(conf, True)
	learner.threshold = args.threshold
	if conf.device.type == 'cpu':
		learner.load_state(conf, 'cpu_final.pth', True, True)
	else:
		learner.load_state(conf, 'final.pth', True, True)
	learner.model.eval()
	print('learner loaded')
	
	#if args.update:
	if False :
		targets, names = prepare_facebank(conf, learner.model, mtcnn, tta = args.tta)
		print('facebank updated')
	else:
		targets, names = load_facebank(conf)
		print('facebank loaded')

	cnt=1
	for file in glob.glob(base_path + "crop_images/*"):            
		try:
			faces=[]
			img = cv2.imread(file)
			face=cv2.resize(img,(112,112))
			faces.append(face)  
			results, score = learner.infer(conf, faces, targets, args.tta)
			print("result ",results)
			print("score ",score)
			if not os.path.exists((base_path + 'results/'+names[results[0]+1])):
				os.mkdir((base_path + 'results/'+names[results[0]+1]))
			if results[0]==-1:
				cv2.imwrite((base_path + "results/"+names[results[0]+1]+"/"+names[results[0]+1]+"_"+str(cnt)+".jpg"),img)
			else:	
				cv2.imwrite((base_path + "results/"+names[results[0]+1]+"/"+names[results[0]+1]+"_"+str(cnt)+".jpg"),img)
				attendance.append(names[results[0]+1])

			cnt=cnt+1
			'''for idx,bbox in enumerate(bboxes):
				if args.score:
				frame = draw_box_name(bbox, names[results[idx] + 1] + '_{:.2f}'.format(score[idx]), frame)
				else:
				frame = draw_box_name(bbox, names[results[idx] + 1], frame)'''
		except Exception as e:
			print(e)
			#print('detect error')    
			
		#cv2.imshow('face Capture', frame)

		#if args.save:
			#video_writer.write(frame)

		#if cv2.waitKey(1)&0xFF == ord('q'):
		#	break

	#cap.release()
	#if args.save:
		#video_writer.release()
	#cv2.destroyAllWindows()  
	return set(attendance)  