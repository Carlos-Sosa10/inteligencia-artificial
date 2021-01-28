import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while(1):

	ret,frame=cap.read() 
	grayImage=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	dimensions = frame.shape
 
	
	height = frame.shape[0]
	width = frame.shape[1]
	channels = frame.shape[2]

	largo=height/2
	ancho=width/2
	

	print(largo)
	print(ancho)
	print(width)
	print(channels)

	output=frame.copy()
	circles=cv2.HoughCircles(grayImage,cv2.HOUGH_GRADIENT,2,4000, param1=50,param2=30,minRadius=40, maxRadius=90)
	circles=np.uint16(np.around(circles))
	for circuloActual in circles[0,:]:
		centroX=circuloActual[0]
		centroY=circuloActual[1]
		radio=circuloActual[2]
		cv2.circle(output,(centroX,centroY),radio,(0,255,0),2)
	cv2.imshow('Video',output)
	
	#print('X= ',centroX)
	#print('Y= ',centroY)
	

	
	
	#moments = cv2.circuloActual(mask)
	#area = centroX['0']
	
	#moments1 = cv2.circuloActual(mask1)
	#area1 = centroY['0']
	
	#moments2 = cv2.circuloActual(mask2)
	#area2 = radio['0']

	#if(area > 200):
		#ser.write('h')
	
	
	
	#if(area1 > 200):
		#ser.write('a')

	#if(area2 > 200): 
		#ser.write('b')
	
	#else:
		#ser.write('n')
	
	#cv2.imshow('mask', mask)
	#cv2.imshow('Camara', imagen)
	tecla = cv2.waitKey(5) & 0xFF
	if tecla == 27:
		break
cap.release()
cv2.destroyAllWindows()
    
    

   
