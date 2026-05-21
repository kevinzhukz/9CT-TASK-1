# NSW HSC School Ranking Data System (2023–2025) Overview
This program is a data analysis tool that allows users to explore NSW HSC school performance from 2023–2025. It supports searching, comparison, statistical analysis, and visualisation of school ranking data.

The system is designed to investigate the research question:
Do selective, private, or public schools achieve higher HSC scores in NSW?

## How to Run
Run the program using:
python main.py
Follow the on screen menu and enter a number (1–8) to select an option.

## Menu Functions Explained

### 1. View Hypothesis
This option tests the hypothesis that selective schools perform better than private schools.

What it does:
- Calculates the average HSC success rate (Band 6 percentage) for selective schools
- Calculates the same average for private schools
- Compares both results
- Displays whether the hypothesis is supported or not

### 2. View Full Dataset
This option displays the entire dataset in the terminal

What it does:

- Shows all schools and their data
- Includes rankings, success rates, and school types
- Useful for inspecting raw data

Note: Output may be large.

### 3. Summary Statistics
This option provides a quick overview of the dataset.

What it shows:

- Total number of schools in the dataset
- Average HSC success rate across all schools

Purpose:
Gives a quick summary of overall performance trends.

### 4. Search School
This option allows the user to search for a specific school.

What it does:

- Accepts partial or full school name input
- Searches the dataset (not capital sensitive)
- Displays matching results

If no match is found, it displays “No school found”

### 5. Data Visualisations
This option displays graphs based on the dataset

Available graphs:

- Top 10 Schools
Displays the top 10 schools by success rate
Uses a bar chart

- Selective vs Private Schools
Compares average success rates
Displays a pie chart

- Rankings Over 2023–2025
Shows average ranking over three years
Uses a bar chart

Only one graph is displayed per selection.

### 6. Compare Two Schools
This option compares two selected schools.

What it compares:

- 2025 ranking
- HSC success rate
- Type of school

Purpose:
Allows direct comparison between two schools to identify differences in performance.

### 7. Ranking Change (2024–2025)

This option checks how a school’s ranking has changed.

What it does:

- Finds the selected school
- Compares 2024 ranking with 2025 ranking
- Displays whether the school:
- Went up in ranking
- Went down in ranking
- Had no change
- Data Information

The dataset includes:

- School names
- Rankings for 2023–2025
- HSC success rate (percentage of Band 6 results)
- Number of HSC students
- School type (Selective, Private, Public)
- Requirements



# This system allows users to analyse NSW HSC school performance through searching, comparisons, statistics, and visual graphs. It helps determine whether school type influences academic success using real data.