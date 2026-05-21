from data_module import (
    display_dataset_preview,
    display_summary_statistics,
    search_data,
    display_visualisation,
    compare_schools,
    show_ranking_change,
    display_hypothesis,
)

import time

def typewrite(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)
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
        typewrite("║  1. View hypothesis                  ║")
        typewrite("║  2. View dataset                     ║")
        typewrite("║  3. Summary statistics               ║")
        typewrite("║  4. Search for a school              ║")
        typewrite("║  5. View chart                       ║")
        typewrite("║  6. Compare two schools              ║")
        typewrite("║  7. Show rank change for a school    ║")
        typewrite("║  8. Exit                             ║")
        typewrite("╚══════════════════════════════════════╝")

        choice = input("\nSelect an option (1-8): ").strip()
        if choice == "1":
            display_hypothesis()
        elif choice == "2":
            display_dataset_preview()
        elif choice == "3":
            display_summary_statistics()
        elif choice == "4":
            search_data()
        elif choice == "5":
            display_visualisation()
        elif choice == "6":
            compare_schools()
        elif choice == "7":
            show_ranking_change()
        elif choice == "8":
            print("\nGoodbye!")
            break
        else:
            print("Invalid selection — please enter a number between 1 and 8.")

if __name__ == "__main__":
    main_menu()