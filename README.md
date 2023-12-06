[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Ch92Y567)
# Museum-Project
## To Do list:

| Museum-Project Description |

1) Database Design and Initialization

- Database Creation:
      ArtCollection
- Table Structure: 
      Artist: artist ID, name, birth year, nationality
      Artwork: artwork ID, title, artist ID, creation year, medium, collection name, category, status
- Data insertion:
      Script inserts sample of data for artists and artworks
- Foreign Key Relationship: 
      Foreign key relationship between Artists and Artwork

2) SQL Queries and Database Operations

- Queries:
      Includes queries for listing tables, details about foreign key constraints, selecting artists and artworks, joining data from tables. 
- Specialized queries:
      Queries to retrieve artwork based on creation year and delete artists based on artwork status
- Database triggers
      Use of triggers to handle dynamic data changes like updating birth years

3) Graphical User Interface (GUI | Python)
      
- GUI application:
      Developed with Tkinter, GUI enables users to interact with database
- Database connectivity:
      Application connects to MySQL database with user-provided credentials
- Functionality:
      Executing SQL script to set up database, viewing artists and artwork, handling specific data operations
- Interactive elements:
      GUI features buttons, entry fields and data display in table format. Includes user-friendly elements like button color change on mouse hover.


 | Group members and their roles |


      Mohit Kaila 
            -> Developing the Python Application 
            -> Populating the database 
      Shalin Wickremeratna 
            -> EER Diagram 
            -> Relational Data Model
            -> Writing SQL queries
      Rajdeep Das 
            -> Helping populating the database


| Features List and General Info |

- User-friendly interface:
      Tkinter features accessible and easily traversable interface
- Dynamic Data Interaction:
      Users can view, sort, interact with data dynamically
- Data Integrity:
      SQL triggers ensure data consistency, such as when updating or deleting records
- Comprehensive Data Management:
      System covers various aspects of art management


- Important info :

      Make sure the SQL server is running and the user inputs the correct username and password connected to the server
      Anytime if the user wishes to go back to the previous window, the user can just close the current window.

  
- Include any features you have added beyond the minimum requirements in a features list

## Organization:
- code folder: contains your main python application code
- sql scripts folder: contains all sql scripts required (database creation and initialization, sql script with query tasks in the handout, etc...)
- database design folder: EERD and relational schema
- optional data folder: has data files that you can sue to load data to your application if you use this optional implementation requirement
