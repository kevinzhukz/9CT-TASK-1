
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

import time

def typewrite(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)
    print()
 

 
 
def main_menu():
    print()
    typewrite("╔══════════════════════════════════════╗")
    typewrite("║     Welcome to School Rankings!      ║")
    typewrite("╚══════════════════════════════════════╝")
    while True:
        print()
        typewrite("╔══════════════════════════════════════╗")
        typewrite("║   NSW HSC School Rankings Viewer     ║")
        typewrite("╠══════════════════════════════════════╣")
        typewrite("║  1. View dataset                     ║")
        typewrite("║  2. Summary statistics               ║")
        typewrite("║  3. Search for a school              ║")
        typewrite("║  4. View chart                       ║")
        typewrite("║  5. Update a school                  ║")
        typewrite("║  6. Save changes                     ║")
        typewrite("║  7. Exit                             ║")
        typewrite("╚══════════════════════════════════════╝")

        choice = input("\nSelect an option (1-7): ").strip()
 #prints full data set
        if choice == "1":
            display_dataset_preview()
#Shows total schools + average success rate per school type
        elif choice == "2":
            display_summary_statistics()
 #Asks for a name, finds matching schools
        elif choice == "3":
            search_data()
 #Bar chart of top 10 schools
        elif choice == "4":
            display_visualisation()
 #Find a school, pick a column, change the value
        elif choice == "5":
            update_data_entry()
 #Writes the changes back to your CSV file
        elif choice == "6":
            save_changes()
 
        elif choice == "7":
            print("\nGoodbye!")
            break
 
        else:
            print("Invalid selection — please enter a number between 1 and 7.")
 

if __name__ == "__main__":
    main_menu()
