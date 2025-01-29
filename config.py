# config.py

# YOLO Model Path
MODEL_PATH = "yolov8m.pt"  # Switch to a more powerful model


# Video Path
# config.py

# Image Paths
IMAGE_PATHS = [
    "C:\\Users\\Lenovo\\Downloads\\1651869427801first.png",
    "C:\\Users\\Lenovo\\Downloads\\image22.jpg",
    "C:\\Users\\Lenovo\\Downloads\\image3.jpg",
    "C:\\Users\\Lenovo\\Downloads\\images4.jpeg"
]
VEHICLE_COLORS = {
    "car": (0, 255, 0),      # Green
    "bus": (255, 0, 0),      # Blue
    "truck": (0, 0, 255),    # Red
    "motorbike": (0, 255, 255)  # Yellow
}

# Green Time Parameters
BASE_GREEN_TIME = 10  # Base green time in seconds
MAX_GREEN_TIME = 60  # Maximum green time in seconds
TIME_INCREMENT = {"car": 2, "bus": 2, "truck": 2, "motorbike": 1}  # Time increments per vehicle type

# Lane Detection Parameters
LANE_DETECTION_THRESHOLD = 0.2  # Percentage of frame width to consider as the lane

# Logging Parameters
LOG_FILE = "traffic_log.csv"

# Display Parameters
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
