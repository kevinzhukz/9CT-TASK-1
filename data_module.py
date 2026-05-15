import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt

dataset_df = pd.read_csv('Data/schoolrank.csv')

def display_dataset_preview():
    print(dataset_df)
 
def display_summary_statistics():
    print("Total schools:", len(dataset_df))
    print("Average success rate:", dataset_df["Success Rate (%)"].mean())
 
def search_data():
    name = input("Enter school name: ")
    print(dataset_df[dataset_df["School"].str.contains(name, case=False)])
 
def display_visualisation():
    print("\n1. Top Ten Schools")
    print("2. Selective vs Private")
    print("3. Top 5 Schools Over 3 Years")
    
    choice = input("Choose a graph (1-3): ")

    if choice == '1':

        gaming_data = dataset_df['schoolrank'].value_counts()

        gaming_data.plot(kind='bar')

        plt.title("Top 10 Schools based on HSC results")
        plt.xlabel("Schools")
        plt.ylabel("Success Rate")
        plt.xticks(rotation=90)
        plt.show()

    # english improvement graph
    elif choice == '2':

        improvement_data = dataset_df['Data/schoolrank.csv'].value_counts()

        improvement_data.plot(kind='pie', autopct='%1.1f%%')

        plt.title("English Improvement")
        plt.ylabel("")

        plt.show()

    # grades graph
    elif choice == '3':

        grades_data = dataset_df['Data/schoolrank.csv'].value_counts()

        grades_data.plot(kind='bar')

        plt.title("Gaming Affecting Grades")
        plt.xlabel("Answer")
        plt.ylabel("Students")

        plt.show()

    else:
        print("Invalid option")
    
def update_data_entry():
    name = input("Enter school name: ")
    new_rate = input("Enter new success rate: ")
    dataset_df.loc[dataset_df["School"] == name, "Success Rate (%)"] = new_rate
    print("Updated!")
 
def save_changes():
    dataset_df.to_csv('Data/schoolrank.csv', index=False)
    print("Saved!")