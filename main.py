import cv2
import time

# Initialize video capture (0 for default webcam)
cap = cv2.VideoCapture(0)

# Give the camera some time to warm up
time.sleep(2)

# Initialize the first frame for comparison
first_frame = None

while True:
    ret, frame = cap.read()
    text = "No Motion"

    # Resize for faster processing
    frame = cv2.resize(frame, (500, 300))

    # Convert to grayscale and blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Set the first frame
    if first_frame is None:
        first_frame = gray
        continue

    # Compute difference between current and first frame
    frame_delta = cv2.absdiff(first_frame, gray)
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]

    # Dilate the thresholded image to fill holes
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Ignore small movements
        if cv2.contourArea(contour) < 1000:
            continue

        # If motion is detected
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Motion Detected"

    # Display status
    cv2.putText(frame, f"Status: {text}", (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Show the live feed
    cv2.imshow("Security Feed", frame)
    cv2.imshow("Threshold", thresh)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
