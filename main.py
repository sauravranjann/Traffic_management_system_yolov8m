# main.py

import cv2
import numpy as np
from config import *
from vehicle_detector import VehicleDetector
from lane_detector import LaneDetector
from traffic_analyzer import TrafficAnalyzer

def process_image(image_path, vehicle_detector, lane_detector, traffic_analyzer):
    # Load image
    frame = cv2.imread(image_path)
    if frame is None:
        print(f"Error: Could not load image at {image_path}.")
        return None, {"car": 0, "bus": 0, "truck": 0, "motorbike": 0}, 0

    # Detect vehicles
    results = vehicle_detector.detect_vehicles(frame)
    vehicle_counts = {"car": 0, "bus": 0, "truck": 0, "motorbike": 0}

    for result in results:
        filtered_boxes = lane_detector.filter_vehicles(frame, result.boxes)
        for box in filtered_boxes:
            class_id = int(box.cls[0])
            if class_id == 2:  # Car
                vehicle_type = "car"
            elif class_id == 3:  # Motorbike
                vehicle_type = "motorbike"
            elif class_id == 5:  # Bus
                vehicle_type = "bus"
            elif class_id == 7:  # Truck
                vehicle_type = "truck"
            else:
                continue  # Skip other classes

            # Update vehicle count
            vehicle_counts[vehicle_type] += 1

            # Draw bounding box and label
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            color = VEHICLE_COLORS[vehicle_type]
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, vehicle_type.capitalize(), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Calculate green time
    green_time = traffic_analyzer.calculate_green_time(vehicle_counts)

    # Display green time on the frame
    cv2.putText(frame, f"Green Time: {green_time}s", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

    return frame, vehicle_counts, green_time

def main():
    # Initialize modules
    vehicle_detector = VehicleDetector(MODEL_PATH)
    lane_detector = LaneDetector(LANE_DETECTION_THRESHOLD)
    traffic_analyzer = TrafficAnalyzer(BASE_GREEN_TIME, MAX_GREEN_TIME, TIME_INCREMENT, LOG_FILE)

    # Process all images
    frames = []
    for image_path in IMAGE_PATHS:
        frame, vehicle_counts, green_time = process_image(image_path, vehicle_detector, lane_detector, traffic_analyzer)
        if frame is not None:
            frames.append(frame)

    # Combine frames into a grid layout
    if len(frames) == 4:
        # Resize frames to the same size (optional)
        resized_frames = [cv2.resize(frame, (400, 300)) for frame in frames]

        # Create a 2x2 grid
        top_row = np.hstack((resized_frames[0], resized_frames[1]))
        bottom_row = np.hstack((resized_frames[2], resized_frames[3]))
        grid = np.vstack((top_row, bottom_row))

        # Display the grid
        cv2.imshow("Traffic Management System - 4 Frames", grid)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Expected 4 images, but found", len(frames))

if __name__ == "__main__":
    main()