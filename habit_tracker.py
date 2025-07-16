import datetime

# Function to show the menu
def show_menu():
    print("\n=== Habit Tracker ===")
    print("1. Add New Habit")
    print("2. Mark Habit as Done")
    print("3. View Progress")
    print("4. Exit")

# Function to add a new habit
def add_habit():
    habit = input("Enter the new habit name: ")
    with open("habits.txt", "a") as file:
        file.write(f"{habit}\n")
    print(f"Habit '{habit}' added successfully!")

# Function to mark habit as done for today
def mark_habit_done():
    today = datetime.date.today().isoformat()
    habit = input("Enter the habit you completed today: ")
    with open("progress.txt", "a") as file:
        file.write(f"{today} - {habit} - Done\n")
    print(f"Marked '{habit}' as done for {today}.")

# Function to view progress
def view_progress():
    try:
        with open("progress.txt", "r") as file:
            print("\n--- Habit Progress ---")
            print(file.read())
    except FileNotFoundError:
        print("No progress recorded yet.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_habit()
    elif choice == "2":
        mark_habit_done()
    elif choice == "3":
        view_progress()
    elif choice == "4":
        print("Goodbye! Keep building good habits 😊")
        break
    else:
        print("Invalid choice. Try again.")
