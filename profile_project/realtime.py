import cv2
import face_recognition as fr

known_image = fr.load_image_file("glen.jpg")
glen_encoding=fr.face_encodings(known_image)[0]

cap=cv2.VideoCapture(0)

while True:
	print("scanning....")
	ret,frame=cap.read()
	cv2.imshow("feed",frame)
	if cv2.waitKey(1)==27:
		break
	face=fr.face_locations(frame)
	
	if face:
		print("face detected")
		for top,right,bottom,left in face:
			cv2.rectangle(frame,(left,top),(right,bottom),(255,0,0),2)
		
		break
	
	
try:
	print("Searching databse...")
	cam_encoding=fr.face_encodings(frame)[0]
	results = fr.compare_faces([glen_encoding], cam_encoding)
	if results:
		print("Authenticated as glen")
		
	else:
		print("Access denied")
except Exception:
	print("error")
	
cv2.destroyAllWindows()