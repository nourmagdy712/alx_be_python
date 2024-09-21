'''
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
'''
def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Initialize the reminder message
    reminder_message = f"'{task}' is a {priority} priority task."

    # Process the task based on priority using match-case statement
    match priority:
        case "high":
            reminder_message += " that requires immediate attention today!"
        case "medium":
            reminder_message += " It would be good to get this done soon."
        case "low":
            reminder_message += " Consider completing it when you have free time."
        case _:
            reminder_message = "Invalid priority level entered."

    # Modify the reminder if the task is time-bound
    if time_bound == "yes" and priority in ["high", "medium"]:
        reminder_message = f"'{task}' is a {priority} priority task that requires immediate attention today!"
    
    # Print the customized reminder
    print(reminder_message)

if __name__ == "__main__":
    main()