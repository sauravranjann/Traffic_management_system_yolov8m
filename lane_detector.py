# lane_detector.py

import cv2

class LaneDetector:
    def __init__(self, lane_threshold):
        self.lane_threshold = lane_threshold

    def filter_vehicles(self, frame, boxes):
        frame_width = frame.shape[1]
        filtered_boxes = []
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            if x1 > frame_width * self.lane_threshold * 0.5:  # Only consider vehicles in the correct lane
                filtered_boxes.append(box)
        return filtered_boxes