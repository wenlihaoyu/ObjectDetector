import sys
sys.path.append("/Users/Gale/.virtualenvs/cv/lib/python2.7/site-packages")

import cv2

# Get user supplied values
imagePath = sys.argv[1]
cascPath = sys.argv[2]

wallclockCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

wallclocks = wallclockCascade.detectMultiScale(
    gray,
    scaleFactor=1.24,
    minNeighbors=3,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print "Found {0} wallclocks!".format(len(wallclocks))

i = 1
for (x, y, w, h) in wallclocks:
    imgcrop = image[y:(y+h), x:(x+w)]
    cv2.imwrite("/Users/Gale/Documents/ObjectDetector/return-wallclock/found-clocks/wallclock" + str(i) + ".jpg", imgcrop)
    i = i + 1
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.namedWindow('WallClocks found', cv2.WINDOW_NORMAL)
image2 = cv2.resize(image, (1000, 550))
cv2.imshow("output", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
