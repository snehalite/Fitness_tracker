# Fitness_tracker
# Fitness Tracker

A simple Python program to log physical activities, calculate calories burned, and keep track of your fitness progress.

## Features

- **Log Activities**: Track your workout activities, including their duration.
- **Calorie Calculation**: Calculates the estimated calories burned for each activity based on predefined rates.
- **Fitness Log**: View a detailed log of all recorded activities.
- **Total Calories**: Display the total calories burned from all logged activities.

## Activities Supported

The program includes the following predefined activities with estimated calorie burns per hour:

- **Running**: 600 calories/hour
- **Cycling**: 400 calories/hour
- **Walking**: 250 calories/hour
- **Swimming**: 500 calories/hour
- **Yoga**: 200 calories/hour

## Usage

1. **Run the Program**  
   Execute the script in a Python environment:
   ```bash
   python fitness_tracker.py

Enter activity (e.g., running, cycling): running
Enter duration in minutes: 30
Logged: running for 30 minutes, burned 300.00 calories.

Fitness Log:
2024-11-25 15:30:00: running - 30 minutes, 300.00 calories burned

Total calories burned: 300.00

ACTIVITIES = {
    "dancing": 350,  # calories/hour
    ...
}
