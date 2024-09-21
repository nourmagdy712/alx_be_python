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
    while True:
        # Prompt for a single task
        task = input("Enter your task: ")
        priority = input("Priority (high/medium/low): ").lower()
        time_bound = input("Is it time-bound? (yes/no): ").lower()

        # Initialize the reminder message
        if time_bound == "yes":
            immediate_attention = "requires immediate attention today!"
        else:
            immediate_attention = "Consider completing it when you have free time."

        # Process the task based on priority using match-case statement
        match priority:
            case "high":
                reminder_message = f"Reminder: '{task}' is a high priority task that {immediate_attention}"
            case "medium":
                reminder_message = f"Reminder: '{task}' is a medium priority task that {immediate_attention}"
            case "low":
                reminder_message = f"Reminder: '{task}' is a low priority task that {immediate_attention}"
            case _:
                reminder_message = "Invalid priority level entered."

        # Print the customized reminder
        print(reminder_message)

        # Ask if the user wants to enter another task
        another = input("Would you like to enter another task? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()