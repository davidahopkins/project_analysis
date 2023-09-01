# Cost & Schedule Analysis
This is a public repository for Cost Esimating &amp; Schedulding professionals to share code ideas

## Example Folder
The example folder contains, well, an example, a small piece of code that can take a string of feet & inches and convert it to a float value.
As new project get introduced each can have its own folder containing all the elements of that project. 
Please feel free to create folders as needed for different ideas.

## Document Log
The document log folder contains two file, the python file and a jupyter notebook. The script will look through a directory and extract the names and file paths of all files in the directory, then create an excel workbook with the name of the files as hyperlinks to their locations. 

When the script is run it will ask where your directory is, where you want to save the new workbook, and what your project number is. 

The excel workbook will have the following columns:
- index: from the dataframe
- Date: user define once the workbook is made
- Document Type: user defined once the workbook is made
- Name: this is the file name from the directory
- Path: this is the full path of the files from the directory
- Name Match: this is a formula that takes the file name from the path and is used for the error checking
- Error Checking: this is a formula that checks is the file name from the path and the file name match, if the value is true the files and paths are in correct order, if it is false there is an error.
- Document: this is a formala that lists the file names and creates a hyperlink to the file path, these will not show up blue underlined like a typical link, but click on one of the cells and it should open the file from that path