def daily_reminder():
    task = input("Enter the task description: ")
    priority = input("Enter the task's priority (high, medium, low): ").strip().lower()
    time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

    # Generate the reminder based on priority and time sensitivity
    match priority:
        case "high":
            reminder = f"[High Priority] You need to: {task}."
        case "medium":
            reminder = f"[Medium Priority] You should: {task}."
        case "low":
            reminder = f"[Low Priority] Consider: {task}."
        case _:
            reminder = "Error: Invalid priority level."

    # Modify the reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " That requires immediate attention today!"

    # Print the customized reminder
    print(reminder)

# Run the reminder function
if __name__ == "__main__"
    daily_reminder()
