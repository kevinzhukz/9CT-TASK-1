import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt

dataset_df = pd.read_csv('Data/schoolrank.csv')

def display_hypothesis():
    print("\n======== HYPOTHESIS ========")
    print("Note: Success rate = % of HSC entries that scored Band 6 (90+)")
    print("Selective schools achieve higher HSC success rates than private schools.")
    print()
    selective = dataset_df[dataset_df["Type of School"] == "Selective"]["Success Rate (%)"].mean()
    private = dataset_df[dataset_df["Type of School"] == "Private"]["Success Rate (%)"].mean()
    print("Average Selective school success rate:", round(selective, 2), "%")
    print("Average Private school success rate:", round(private, 2), "%")
    if selective > private:
        print("Hypothesis is supported")
    else:
        print("Hypothesis is not supported")

def display_dataset_preview():
    print("\n======== DATASET ========")
    pd.set_option('display.max_columns', None)
    print(dataset_df.to_string())

def display_summary_statistics():
    print("\n======== SUMMARY ========")
    print("Note: Success rate = % of HSC entries that scored Band 6 (90+)")
    print("Total schools:", len(dataset_df))
    print("Average success rate:", round(dataset_df["Success Rate (%)"].mean(), 2), "%")

def search_data():
    name = input("Enter school name: ")
    results = dataset_df[dataset_df["School"].str.contains(name, case=False)]
    if results.empty:
        print("No school found.")
    else:
        print(results.to_string())

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
        print("Invalid option")

def compare_schools():
    name1 = input("Enter first school name: ")
    name2 = input("Enter second school name: ")
    school1 = dataset_df[dataset_df["School"].str.contains(name1, case=False)]
    school2 = dataset_df[dataset_df["School"].str.contains(name2, case=False)]
    if school1.empty or school2.empty:
        print("School not found.")
    else:
        print("\n======== COMPARISON ========")
        print(school1["School"].values[0], "vs", school2["School"].values[0])
        print("2025 Ranking:", school1["2025 School Ranking"].values[0], "vs", school2["2025 School Ranking"].values[0])
        print("Success Rate:", school1["Success Rate (%)"].values[0], "vs", school2["Success Rate (%)"].values[0])
        print("Type:", school1["Type of School"].values[0], "vs", school2["Type of School"].values[0])

def show_ranking_change():
    name = input("Enter school name: ")

    results = dataset_df[dataset_df["School"].str.contains(name, case=False)]

    if results.empty:
        print("No school found.")

    else:
        rank2024 = int(results["2024 School Ranking"].values[0])
        rank2025 = int(results["2025 School Ranking"].values[0])

        print("2024 Ranking:", rank2024)
        print("2025 Ranking:", rank2025)

        if rank2025 < rank2024:
            print("Went up", rank2024 - rank2025, "places")

        elif rank2025 > rank2024:
            print("Went down", rank2025 - rank2024, "places")

        else:
            print("No change")