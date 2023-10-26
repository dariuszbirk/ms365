# Scripts for Microsoft 365 administrators
## Script #1 - Adding multiple users in MS365 admin center from .csv file
### Problem description
During the Covid-19 pandemic, schools were forced to conduct classes remotely. 
MS Teams was often used for this purpose, because Microsoft provided this and many other tools practically free of charge as part of the Office 365 Education service. 
However, to use these services, an individual account had to be created for each student and teacher. 
Entering all users individually was difficult, so Microsoft made it possible to import data from a properly prepared .csv file.

The purpose of this script is to help you generate such a file correctly.

### Preparation of input data
To create an individual user account in MS365, you need the user's name and surname and school domain in MS365. 
It is good to complete other data such as position, school address, etc., but they are not necessary and are usually constant for a group of users. 
Therefore, constant data for a given group is now declared as variables directly in the code. 
Individual data, i.e. name and surname, are imported from a .txt file.

Since school secretariats provide administrators with this data in files of various formats, it is necessary to use generally available tools appropriate for these files to transform the data into such a form that the student's surname and first name appear in one line. 
The data prepared in this way should be saved in a text file called input.txt in the directory where the script is located.
A sample input.txt file is available in the repository.

### Script execution
The script in its current form should be run in the terminal by issuing the command:

`python3 ms365_export_file.py`

As a result, a ready-made export.csv file should appear in the same directory.
This file can be moved to another target directory, or at least renamed.
You can then import data from this file in the MS365 admin center.

### Comments and possibilities for script development

The script is very simple but extremely useful - it can save administrators a lot of time.
However, it requires basic programming knowledge in terms of the ability to run Python scripts and prepare data in a text file.
It also assumes that the data will be correctly prepared in the manner described.
It has not been tested or prepared for cases of incorrect use - it was created "quickly" to help me perform my personal duties - not for general use.
In the future, it may be expanded and adapted for general use by making it available via a website or adding a graphical interface and introducing additional lines of code used in such cases.
