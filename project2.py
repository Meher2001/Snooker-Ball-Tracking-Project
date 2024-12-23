import cv2
import numpy as np

def track_ball(video_path, target_color_range=None, show_numbered_ball=None):
    """
    Tracks moving balls in a snooker table video.

    :param video_path: Path to the input video.
    :param target_color_range: Tuple of HSV color range for the target ball (low, high).
    :param show_numbered_ball: Number of the ball to track (if using pre-trained detection).
    """
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Exit when video ends

        # Resize for faster processing
        frame = cv2.resize(frame, (800, 450))

        # Convert to HSV color space for color detection
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        if target_color_range:
            # Mask for the target color
            mask = cv2.inRange(hsv, target_color_range[0], target_color_range[1])
            result = cv2.bitwise_and(frame, frame, mask=mask)

            # Find contours for the masked area
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                if cv2.contourArea(contour) > 500:  # Filter small contours
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue rectangle
                    cv2.putText(frame, "Target Ball", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        if show_numbered_ball:
            # Placeholder for detecting numbered balls (requires object detection model)
            pass

        # Display the result
        cv2.imshow("Snooker Ball Tracking", frame)

        # Exit on 'q' key
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Example usage
# Define the HSV color range for blue (adjust based on your video)
blue_hsv_range = (np.array([100, 150, 50]), np.array([140, 255, 255]))

# Provide path to your video
video_path = "assets/video.mp4"
track_ball(video_path, target_color_range=blue_hsv_range)
