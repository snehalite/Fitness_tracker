import datetime

# Predefined activities with estimated calorie burn per hour
ACTIVITIES = {
    "running": 600,  # calories per hour
    "cycling": 400,
    "walking": 250,
    "swimming": 500,
    "yoga": 200,
}

# User's fitness log
fitness_log = []

def log_activity(activity, duration):
    """
    Log an activity with its duration.
    """
    if activity in ACTIVITIES:
        calories_burned = (ACTIVITIES[activity] * duration) / 60  # Convert to per minute
        log_entry = {
            "activity": activity,
            "duration": duration,
            "calories_burned": calories_burned,
            "timestamp": datetime.datetime.now()
        }
        fitness_log.append(log_entry)
        print(f"Logged: {activity} for {duration} minutes, burned {calories_burned:.2f} calories.")
    else:
        print(f"Activity '{activity}' is not recognized. Please choose from: {list(ACTIVITIES.keys())}")

def view_log():
    """
    Display the fitness log.
    """
    if not fitness_log:
        print("No activities logged yet!")
        return

    print("\nFitness Log:")
    for entry in fitness_log:
        print(f"{entry['timestamp']}: {entry['activity']} - {entry['duration']} minutes, "
              f"{entry['calories_burned']:.2f} calories burned")
    print()

def total_calories():
    """
    Calculate and display the total calories burned.
    """
    total = sum(entry['calories_burned'] for entry in fitness_log)
    print(f"Total calories burned: {total:.2f}")

def main():
    """
    Main function to interact with the user.
    """
    while True:
        print("\nFitness Tracker")
        print("1. Log Activity")
        print("2. View Log")
        print("3. View Total Calories Burned")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            activity = input("Enter activity (e.g., running, cycling): ").lower()
            try:
                duration = int(input("Enter duration in minutes: "))
                log_activity(activity, duration)
            except ValueError:
                print("Invalid input for duration. Please enter a number.")
        elif choice == "2":
            view_log()
        elif choice == "3":
            total_calories()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()