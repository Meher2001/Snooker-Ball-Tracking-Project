# Snooker-Ball-Tracking-Project
Snooker Ball Tracking Project
This project demonstrates a computer vision solution for tracking snooker balls in a video using OpenCV. The solution allows tracking moving balls on a snooker table and includes the capability to track a particular ball based on its color.

Features:

- Track Moving Balls: Detects and tracks balls moving on a snooker table.
- Color-Based Detection: Tracks a specific ball using its color in the HSV color space.
- Real-Time Visualization: Draws bounding boxes around detected balls and labels them.
- Flexible Input: Works with any video of a snooker table.

Requirements:

Ensure you have the following installed before running the code:
- Python 3.7+
- OpenCV (cv2)
- NumPy

To install the dependencies, run:
  pip install opencv-python numpy

Usage:

1. Clone this repository or download the code.
2. Place your snooker video in the project directory.
3. Define the HSV color range for the ball you want to track (e.g., blue).
4. Run the script with the path to the video file.

Working:

1. Video Reading: The video is loaded frame by frame using OpenCV.
2. Color Filtering: The frames are converted to HSV color space, and a mask is applied to isolate the target ball's color.
3. Contour Detection: Contours are found on the mask, and bounding rectangles are drawn around significant contours.
4. Real-Time Display: The processed frames are displayed in a window with the detected ball highlighted.
5. Exit: Press q to exit the program.

Input: 

- A video of a snooker game in .mp4 or other supported formats.
- HSV color range for the target ball (adjustable).

Output:
- A real-time visualization of the detected ball, highlighted with a bounding box and label.





