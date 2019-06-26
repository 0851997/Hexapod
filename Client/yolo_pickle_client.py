# USAGE COMMAND:
# python yolo_pickle_client.py --yolo yolo-coco
# -IP 192.168.43.189 -p 10000

import numpy as np
import argparse
import imutils
from imutils.video import VideoStream
import time
import cv2
import os
import socket
import pickle

# Parameters to run this program
ap = argparse.ArgumentParser()
ap.add_argument("-y", "--yolo", required=True,
	help="base path to YOLO directory")
# ap.add_argument("-IP", "--ip_address", type=str, required=True,
# 				help="Set the IP address of the BeagleBone")
# ap.add_argument("-p", "--port", type=int, required=True,
# 				help="Set the port of the BeagleBone")
ap.add_argument("-c", "--confidence", type=float, default=0.8, #0.5
	help="minimum probability to filter weak detections")
ap.add_argument("-t", "--threshold", type=float, default=0.3, #0.3
	help="threshold when applyong non-maxima suppression")
args = vars(ap.parse_args())

labelsPath = os.path.sep.join([args["yolo"], "coco.names"])
LABELS = open(labelsPath).read().strip().split("\n")

np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
	dtype="uint8")

weightsPath = os.path.sep.join([args["yolo"], "yolov3-tiny.weights"])
configPath = os.path.sep.join([args["yolo"], "yolov3-tiny.cfg"])

print("[INFO] loading YOLO from disk...")
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

vs = VideoStream(src=0).start()
time.sleep(1.0)
(W, H) = (None, None)

lastPosition = (0, 0)

IP = "192.168.43.31"
PORT = 9000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

while True:
    frame = vs.read()
    if W is None or H is None:
        (H, W) = frame.shape[:2]
        print("[INFO] Height:", H, "Width:", W)

    # Making a blob and putting it through the layers of the yolo detection
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
        swapRB=True, crop=False)
    net.setInput(blob)
    start = time.time()
    layerOutputs = net.forward(ln)
    end = time.time()

    boxes = []
    confidences = []
    classIDs = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            if LABELS[classID] in 'person': # Filter out off all the detected things to only persons
                if confidence > args["confidence"]:
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")

                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))

                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

    idxs = cv2.dnn.NMSBoxes(boxes, confidences, args["confidence"],
        args["threshold"])

    if len(idxs) > 0:  # If there is more than 0 persons detected draw it on the screen
        for i in idxs.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            rectCenter = (int((x + x + w) / 2), int((y + y + h) / 2))
            print("[INFO] Rectangle Center		:", rectCenter)
            print("[INFO] Last know position	:", lastPosition)
            if lastPosition[0] == 0 and lastPosition[1] == 0:  # The first person detected will be saved and followed.
                color = [int(c) for c in COLORS[classIDs[i]]]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                dimensionsRectangle = (((x+w)-x), ((y+h)-y))
                lastPosition = rectCenter
                distanceCenterToBorder = (dimensionsRectangle[0]/2, dimensionsRectangle[1]/2)
                cv2.circle(frame, rectCenter, 5, (0, 0, 210), 5)
                print("")
                print("[INFO] Width and Height of the found person   			:", dimensionsRectangle) 		#<---- dimensionsRectangle is the width and height of the box around the person
                print("[INFO] Center coordinates of the found person 			:", rectCenter) 				#<---- rectCenter is the center point of the found person
                print("[INFO] From the center to the border of the rectangle 	:", distanceCenterToBorder) 	#<---- distanceCenterToBorder is the distance between the found person center and the drawn border around it
                print("")
                
                widthDimension, heightDimension = dimensionsRectangle
                rectWidth, rectHeight = rectCenter

                if (rectWidth != None or widthDimension != None):
                    tup = (rectWidth, widthDimension)
                    data_string = pickle.dumps(tup)
                    s.send(data_string)

                data = s.recv(4096)
                data_arr = pickle.loads(data)
                print('Received', repr(data_arr))

                cv2.putText(frame, "Tracked Person", (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            if (rectCenter[0] - 80) <= lastPosition[0] <= (rectCenter[0] + 80):   # Check if the x point is too far away from the last x point
                if (rectCenter[1] - 80) <= lastPosition[1] <= (rectCenter[1] + 80):  # Check if the y point is too far away from the last y point
                    color = [int(c) for c in COLORS[classIDs[i]]]
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                    dimensionsRectangle = (((x + w) - x), ((y + h) - y))
                    lastPosition = rectCenter
                    distanceCenterToBorder = (dimensionsRectangle[0] / 2, dimensionsRectangle[1] / 2)
                    cv2.circle(frame, rectCenter, 5, (0, 0, 210), 5)
                    print("")
                    print("[INFO] Width and Height of the found person   			:", dimensionsRectangle)
                    print("[INFO] Center coordinates of the found person 			:", rectCenter)
                    print("[INFO] From the center to the border of the rectangle 	:", distanceCenterToBorder)
                    print("")

                    widthDimension, heightDimension = dimensionsRectangle
                    rectWidth, rectHeight = rectCenter

                    if (rectWidth != None or widthDimension != None):
                        tup2 = (rectWidth, widthDimension)
                        data_string2 = pickle.dumps(tup2)
                        s.send(data_string2)

                    data2 = s.recv(4096)
                    data_arr2 = pickle.loads(data2)
                    print('Received', repr(data_arr2))

                    cv2.putText(frame, "Tracked Person", (x, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            else:
                print("")
                print("The person has disappeared")
                print("")
    cv2.imshow("Little Heavy Mathametics", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
cv2.destroyAllWindows()
vs.stop()