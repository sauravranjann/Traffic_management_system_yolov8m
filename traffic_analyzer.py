# traffic_analyzer.py

import time
import csv

class TrafficAnalyzer:
    def __init__(self, base_green_time, max_green_time, time_increment, log_file):
        self.base_green_time = base_green_time
        self.max_green_time = max_green_time
        self.time_increment = time_increment
        self.log_file = log_file

    def calculate_green_time(self, vehicle_counts):
        total_time = sum(vehicle_counts[vehicle] * self.time_increment[vehicle] for vehicle in vehicle_counts)
        green_time = min(self.base_green_time + total_time, self.max_green_time)
        return green_time

    def log_data(self, vehicle_counts, green_time):
        with open(self.log_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                time.strftime("%Y-%m-%d %H:%M:%S"),
                vehicle_counts["car"],
                vehicle_counts["bus"],
                vehicle_counts["truck"],
                vehicle_counts["motorbike"],
                green_time
            ])