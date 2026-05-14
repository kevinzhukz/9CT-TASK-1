# 9CT-TASK-1
 
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
 
 
# Only run the menu when this file is executed directly.
# If data_module imports main, this block will NOT run.
if __name__ == "__main__":
    main_menu()
