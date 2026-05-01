# Assessment Task 1
Does selective schools or private schools or regular schools achieve higher scores in HSC (NSW)
hypothesis: Selective schools achieve higher better than other schools in average in HSC

## Identifying and Defining 


### Mind Map


#### Functional Requirements

Data Loading: Consider aspects such as ability to load certain file types and handling errors in file loading (e.g. incorrect format, missing files).

Data Cleaning: Does the system need to handle missing values or allow for filtering, sorting and grouping of data?

Data Analysis: What kind of statistical analysis does the system need to allow for (e.g. mean, median, mode)?

Data Visualisation: How will the data need to be visualised (e.g. Pandas dataframes / Matplotlib chart types)?

Data Reporting: What output should the system include, and do we need to store the final dataset somewhere (e.g. .csv or .txt file)?


#### Non function requirements

Typically non-functional requirements would focus on performance, usability, reliability, scalability and security. However, for this task we are going to focus on usability and reliability, as the performance and scalability will not vary much due to only working with one or two datasets and security was a bit much to cram into the short time we have to complete the task. You are of course welcome to add a security layer (e.g. username + password) to your UI if you feel it's appropriate, and if you have time.

For now, focus on the following:

Usability: What is required from the User Interface and a 'README' document?

Reliability: What is required from the system when providing information to the user on errors and ensuring data integrity?

#### Use-Case
Now we need to a develop a use-case to outline how a user might access information from the system. Remember that the user will need to be able to access the program via a user interface (text-based is fine) to look at the data itself, any visualisations and perhaps even update data depending on the system.

Here is an example of how this might look - keep in mind you will need to tailor this to your system and be more specific. 

Actor: User

Goal: To access and interact with existing data through the program’s user interface.

Preconditions:

The dataset has already been preloaded into the system by an administrator / programmer.

The user has access to the system interface.

Main Flow:

User opens the program and is presented with a text-based menu.

User selects one of the following options:
a. View visualisation (e.g., chart or graph of selected data)
b. Search or filter data based on specific criteria
c. Update a data entry (e.g., change a value or correct an error)

System performs the requested action and outputs to user.

Postconditions:

User has viewed and/or interacted with the data.

Any valid updates are saved by the system.

Data remains available for further queries or analysis.