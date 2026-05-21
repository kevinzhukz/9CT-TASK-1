import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt

dataset_df = pd.read_csv('Data/schoolrank.csv')

def display_hypothesis():
    print("\n========  HYPOTHESIS ========")
    print("Note: Success rate = percentage of HSC exam entries that scored Band 6 (90+)")
    print("Selective schools achieve higher HSC success rates")
    print("than private schools due to their academically")
    print("selective enrolment process.")
    print()
    selective = dataset_df[dataset_df["Type of School"] == "Selective"]["Success Rate (%)"].mean()
    private = dataset_df[dataset_df["Type of School"] == "Private"]["Success Rate (%)"].mean()
    print("Average Selective school success rate:", round(selective, 2), "%")
    print("Average Private school success rate:", round(private, 2), "%")
    if selective > private:
        print("\nResult: Hypothesis is supported ")
    else:
        print("\nResult: Hypothesis is not supported")

def _display_table(table,df):
    print(f"\n{table}")
    print("-" * len(table))
    print(df.to_string(index=False))
    print()

def display_dataset_preview():
    _display_table("2023-2025 School Rankings Dataset",dataset_df)
 
def display_summary_statistics():
    print("note: Success rate = percentage of HSC exam entries that scored Band 6 (90+)")
    print("Total schools:", len(dataset_df))
    print("Average success rate:", round(dataset_df["Success Rate (%)"].mean(), 2), "%")
 
def search_data():
    name = input("Enter school name: ")
    print(dataset_df[dataset_df["School"].str.contains(name, case=False)])
 
def display_visualisation():
    print("\n1. Top 10 Schools")
    print("2. Selective vs Private")
    print("3. Rankings Over 3 Years")
    print("Delete graph after viewing to ensure it works properly")
    
    choice = input("Choose a graph (1-3): ")

    if choice == '1':
        top10 = dataset_df.head(10)
        plt.bar(top10["School"], top10["Success Rate (%)"])
        plt.xticks(rotation=45, ha="right")
        plt.title("Top 10 Schools")
        plt.ylabel("Success Rate (%)")
        plt.tight_layout()
        plt.savefig("chart.png")
        print("Chart saved as chart.png!")

    elif choice == '2':
        avg = dataset_df.groupby("Type of School")["Success Rate (%)"].mean().dropna()
        plt.pie(avg, labels=avg.index)
        plt.title("Success Rate by School Type")
        plt.savefig("chart.png")
        print("Chart saved as chart.png")

    elif choice == '3':
        top5 = dataset_df.head(5).copy()
        top5["2025 School Ranking"] = pd.to_numeric(top5["2025 School Ranking"], errors='coerce')
        top5["2024 School Ranking"] = pd.to_numeric(top5["2024 School Ranking"], errors='coerce')
        top5["2023 School Ranking"] = pd.to_numeric(top5["2023 School Ranking"], errors='coerce')
        avg_rank = (top5["2025 School Ranking"] + top5["2024 School Ranking"] + top5["2023 School Ranking"]) / 3
        plt.bar(top5["School"], avg_rank)
        plt.xticks(rotation=45, ha="right")
        plt.title("Top 5 Schools - Average Ranking 2023-2025")
        plt.ylabel("Average Ranking")
        plt.tight_layout()
        plt.savefig("chart.png")
        print("Chart saved as chart.png")

    else:
        print('Not a Option')
    
def update_data_entry():
    name = input("Enter school name: ")
    new_rate = input("Enter new success rate: ")
    dataset_df.loc[dataset_df["School"] == name, "Success Rate (%)"] = new_rate
    print("Updated")
 
def save_changes():
    dataset_df.to_csv('Data/schoolrank.csv', index=False)
    print("Saved")



