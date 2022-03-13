# Email-info-alarmid
Create a db in sqlite : id name ip address office region
Suppose the alarm gives only the NE ID as a starting point information to the operator, and then he will need to collect other information in order to prepare a detailed situation report and send it by email.
Why using  database? In some cases the user may check the alarm and see the NE ID, and then he will have to collect different information from different locations before being able to prepare an email and send it, (some information may need to be checked from a GUI interface, some other part on the needed information may be present in a separate document like spreadsheet or other type of files, a database will gather all these information in one single db or even table and makes possible to collect all the needed information with one single sql query.

Next an email body template will be populated with the corresponding information of the NE ID, as well as the subject of the email, and to add some complexity, and in fact this is often the case in the real world and in big enough networks, there is not a fixed list of recipient, but the recipient will depend on which region our NE ID belongs to, each region has different people and responsible to deal with, and our table will help us for this point as well.
A display screen to input the id (from the alarm), the screen should display the recipient which will depend on the region, and need to be checked and modified by the user if needed (in case the receiver is replaced or in vacation for example)

Modules and libraries needed:
Sqlite3, Tkinter, 
First we create our db:
100 NEs 
ID    name   IP address    Office    
1      name1   10.0.0.1     office1   
2      name2    10.0.0.2    office1   
3      name3    10.0.0.3     office2   
.
.
100   name100   10.0.0.100  office10 

Table 2:
Office   Region   Owner
Office1 Region1   Owner1
Office2 Region1   Owner1
Office3 Region1   Owner1
Office4 Region1   Owner1
Office5 Region2   Owner2
Office6 Region2   Owner2
Office7 Region2   Owner2
Office8 Region3  Owner3
Office9 Region3   Owner3
Office10 Region3   Owner3

Steps:
Step 1: Create the database
Step 2: Design the application graphical interface
