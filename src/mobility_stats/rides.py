import csv
import os
from collections import defaultdict


def load_rides(csv_path: str) -> list[dict[str, object]]:
    """Load ride data from rides CSV file."""
    rides_dict = []
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Could not find file: {csv_path}")
    with open(csv_path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for rides in r:
            rides.copy()
            rides_dict.append(
                {
                    "ride_id": rides["ride_id"],
                    "start_station": rides["start_station"],
                    "end_station": rides["end_station"],
                    "duration_min": float(rides["duration_min"]),
                    "rider_type": rides["rider_type"],
                }
            )
    return rides_dict


def average_duration(rides):
    """Return the average ride duration in minutes."""
    if len(rides) == 0:
        return 0.0
    total_duration = 0.0
    for c in rides:
        total_duration += c["duration_min"]
    return total_duration / len(rides)


def count_by_rider_type(rides):
    """Count rides for each rider type."""
    total_duration = defaultdict(int)
    for ride in rides:
        total_duration[ride["rider_type"]] += 1
    return dict(total_duration)


def busiest_start_station(rides):
    """Return the start station with the most rides."""
    if rides == None:
        raise ValueError("rides must not be None")
    if len(rides) == 0:
        raise ValueError("rides must not be empty")
    total_duration = {}
    for ride in rides:
        start_station = ride["start_station"]
        total_duration[start_station] = total_duration.get(start_station, 0) + 1
    return max(total_duration, key=total_duration.get)


def filter_long_rides(rides, total_duration=30):
    """Return all rides with duration greater than or equal to b minutes."""
    long_rides = []
    for ride in rides:
        if ride["duration_min"] >= total_duration:
            long_rides.append(ride)
    return long_rides
