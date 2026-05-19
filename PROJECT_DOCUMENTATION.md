# Assessment Task 1
Does selective schools or private schools or regular schools achieve higher scores in HSC (NSW 2023-2025)
hypothesis: Selective schools achieve higher better than other schools in average in HSC

## Identifying and Defining 


### Mind Map


#### Functional Requirements

Data Loading: the system loads a CSV file (schoolrank.csv) containing NSW HSC school ranking data from 2023-2025. It handles missing values using pandas pd.to_numeric(errors='coerce').

Data Cleaning:The system handles missing values in the 2023 and 2024 ranking columns. data can be filtered by school type (selective, private or public).

Data Analysis: The system calculates mean success rates grouped by school type to test the hypothesis. It also calculates average rankings across 3 years.

Data Visualisation: Three matplotlib charts: a bar chart of top 10 schools, a pie chart comparing school types, and a bar chart of average rankings 2023-2025. 

Data Reporting: Results are displayed in the terminal. Charts are saved as chart.png. Updated data is saved back to schoolrank.csv.


#### Non function requirements

Usability: Text-based menu with numbered options 1-8. typewriter used because its more interesting and is more aestetic. Clear labels and prompts for user input.

Reliability: Invalid menu selections show an error message. Search returns "No school found" if nothing matches or if there is an incorrect spelling.

#### Use-Case
Actor: User
Goal: To access and interact with NSW HSC school ranking data (2023-2025) through the program's text-based menu.
Preconditions:

schoolrank.csv has been loaded into the Data/ folder
The user runs main.py in the terminal
pandas and matplotlib are installed

Main Flow:

User runs the program and sees the welcome message and numbered menu
User selects one of the following options:

View hypothesis and see if selective schools outperform private schools
View the full dataset
View summary statistics (total schools, average success rate)
Search for a specific school by name
View one of three charts (top 10, school type comparison, 3 year average)
Update a school's success rate
Save changes back to the CSV


System performs the action and displays the result in the terminal. Charts are saved as chart.png.

Postconditions:

User has viewed and/or interacted with the data
Any updates made are saved to schoolrank.csv
Data remains available for further queries



##### SEE-I PARAGRAPH
Statement: Selective schools perform better than private schools in the HSC.

Elaborate: This is likely because selective schools only accept students who pass an entry exam, meaning their student cohort is already academically strong before they even start high school.

Example: The data shows that selective schools have an average success rate of 37.84%, compared to private schools at 24.19%. This is a difference of over 13%.

Illustrate: In other words, if you picked a random HSC exam entry from a selective school, it is significantly more likely to be a Band 6 than one from a private school.