# ShapeDetection

Design a function that takes in a 2D structure of size 200x200 which represents the intensity of pixels of a 200x200 pixel image and it returns details about the contents. 

## Part 1 - slope-intercept equation line detection 
The function will detect lines on the image and return a line struct which provides the equation of the line in the form y = mx + b. 
Assumptions: -10 < m < 10 and -1000 < b < 1000 , image contains black lines on white background , there is noise and randomness in the image

## Part 2 - counting number of circles in an image 
The function takes as inputs a 200x200 pixel image and the radius of circles to be detected. It detects all complete circles of that radius without any overlapping and returns this integer number. 
