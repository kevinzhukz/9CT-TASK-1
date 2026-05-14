
# main.py
# Text-based menu UI for exploring NSW HSC School Rankings data.
# All data logic lives in data_module.py and is imported here.
 
from data_module import (
    display_dataset_preview,
    display_summary_statistics,
    search_data,
    display_visualisation,
    update_data_entry,
    save_changes,
)
 

 
 
def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. View dataset")
        print("2. Summary statistics by school type")
        print("3. Search or filter schools")
        print("4. View a visualisation / chart")
        print("5. Update a school's data")
        print("6. Save changes")
        print("7. Exit")
 
        choice = input("\nSelect an option (1-7): ").strip()
 
        if choice == "1":
            display_dataset_preview()

        elif choice == "2":
            display_summary_statistics()
 
        elif choice == "3":
            search_data()
 
        elif choice == "4":
            display_visualisation()
 
        elif choice == "5":
            update_data_entry()
 
        elif choice == "6":
            save_changes()
 
        elif choice == "7":
            print("\nGoodbye!")
            break
 
        else:
            print("Invalid selection — please enter a number between 1 and 7.")
 

if __name__ == "__main__":
    main_menu()
