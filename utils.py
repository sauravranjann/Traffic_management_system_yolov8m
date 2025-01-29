# utils.py

import cv2

def display_frame(frame, vehicle_counts, green_time):
    cv2.putText(frame, f"Cars: {vehicle_counts['car']}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(frame, f"Buses: {vehicle_counts['bus']}", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(frame, f"Trucks: {vehicle_counts['truck']}", (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(frame, f"Motorbikes: {vehicle_counts['motorbike']}", (20, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(frame, f"Green Time: {green_time}s", (20, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
    cv2.imshow("Traffic Management System", frame)