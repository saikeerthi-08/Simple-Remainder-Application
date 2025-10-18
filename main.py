import time
import threading
from datetime import datetime

reminders = []  # List to store reminders


def add_reminder():
    """Add a new reminder."""
    try:
        message = input("Enter reminder message: ")
        time_str = input("Enter reminder time (HH:MM in 24-hour format): ")
        reminder_time = datetime.strptime(time_str, "%H:%M").time()
        reminders.append({"time": reminder_time, "message": message})
        print(f"Reminder set for {reminder_time} ✅")
    except ValueError:
        print("Invalid time format! Please use HH:MM (24-hour format).")


def view_reminders():
    """View all reminders."""
    if not reminders:
        print("No reminders set yet.")
        return
    print("\n----- Reminders -----")
    for i, rem in enumerate(reminders, start=1):
        print(f"{i}. Time: {rem['time']}, Message: {rem['message']}")
    print("--------------------")


def reminder_checker():
    """Background thread that checks and triggers reminders."""
    while True:
        now = datetime.now().time()
        for rem in reminders:
            if rem["time"].hour == now.hour and rem["time"].minute == now.minute:
                print(f"\n⏰ Reminder: {rem['message']}")
                reminders.remove(rem)  # Remove after triggering
        time.sleep(30)  # Check every 30 seconds


def main():
    """Main menu for the reminder application."""
    # Start background reminder checker
    thread = threading.Thread(target=reminder_checker, daemon=True)
    thread.start()

    while True:
        print("\n===== Simple Reminder Application =====")
        print("1. Add Reminder")
        print("2. View Reminders")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_reminder()
        elif choice == '2':
            view_reminders()
        elif choice == '3':
            print("Exiting Reminder Application. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-3.")


if __name__ == "__main__":
    main()
