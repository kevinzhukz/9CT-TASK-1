import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  
import matplotlib.pyplot as plt

 
dataset_df = pd.read_csv('Data/schoolrank.csv')
 
def display_dataset_preview():
    print(dataset_df)
 
def display_summary_statistics():
    print("Total schools:", len(dataset_df))
    print("Average success rate:", dataset_df["Success Rate (%)"].mean())
 
def search_data():
    name = input("Enter school name: ")
    print(dataset_df[dataset_df["School"] == name])
 
def display_visualisation():
    top10 = dataset_df.head(10)
    plt.bar(top10["School"], top10["Success Rate (%)"])
    plt.xticks(rotation=45, ha="right")
    plt.title("Top 10 Schools")
    plt.ylabel("Success Rate (%)")
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x}%"))  # adds % to numbers
    plt.tight_layout()
    plt.savefig("chart.png")
    print("Chart saved as chart.png!")
 
def update_data_entry():
    name = input("Enter school name: ")
    new_rate = input("Enter new success rate: ")
    dataset_df.loc[dataset_df["School"] == name, "Success Rate (%)"] = new_rate
    print("Updated!")
 
def save_changes():
    dataset_df.to_csv('Data/schoolrank.csv', index=False)
    print("Saved!")