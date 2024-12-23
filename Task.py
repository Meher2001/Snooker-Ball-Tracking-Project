import cv2
import numpy as np

def track_ball(video_path, target_color_range=None, show_numbered_ball=None):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break  

        frame = cv2.resize(frame, (800, 450))

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        if target_color_range:
            mask = cv2.inRange(hsv, target_color_range[0], target_color_range[1])
            result = cv2.bitwise_and(frame, frame, mask=mask)

            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                if cv2.contourArea(contour) > 500:  
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  
                    cv2.putText(frame, "Target Ball", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        if show_numbered_ball:           
            pass
       
        cv2.imshow("Snooker Ball Tracking", frame)
        
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

blue_hsv_range = (np.array([100, 150, 50]), np.array([140, 255, 255]))

video_path = "assets/video.mp4"
track_ball(video_path, target_color_range=blue_hsv_range)
