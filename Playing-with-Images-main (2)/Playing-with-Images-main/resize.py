import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Landscape.jpeg", 1)
# Loading the image

half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1) #resizes the image to 10% of its original size.
bigger = cv2.resize(image, (1050, 1610))  #resizes the image to a specific width and height of 1050 and 1610,

stretch_near = cv2.resize(image, (780, 540),
			interpolation = cv2.INTER_NEAREST)  #resizes the image to a specific width and height of 780 and 540, respectively, using the cv2.INTER_NEAREST interpolation method.


Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[image, half, bigger, stretch_near]
count = 4

for i in range(count):     #These lists are used to create a 2x2 grid of subplots using the plt.subplot() function. For each image in the list, a subplot is created and the title and image are set using plt.title() and plt.imshow() functions, respectively.
	plt.subplot(2, 2, i + 1)
	plt.title(Titles[i])
	plt.imshow(images[i])

plt.show()
