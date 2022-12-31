# Program To Read video
# and Extract Frames
import cv2

# Function to extract frames
def FrameCapture(path):
  
  # Path to video file
  vidObj = cv2.VideoCapture(path)

  # Used as counter variable
  count = 0
  # checks whether frames were extracted
  success = 1

  while success:

    # vidObj object calls read
    # function extract frames
    success, image = vidObj.read()
    
    cv2.imwrite("yolo//1000%d.jpg" % count, image)
    count += 1


# Driver Code
if __name__ == '__main__':

  # Calling the function
  FrameCapture("yolo.mp4")
