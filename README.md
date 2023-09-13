# Cost & Schedule Analysis
This is a public repository for Cost Esimating &amp; Schedulding professionals to share code ideas

## General Tools
This folder will contain items that fall into a general project analysis category and do not specifically apply to one or more of the project analysis, estimating, or scheduling disciplines 

### Document Log
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

## Estimating
This folder will contain all items that pertain primarily to cost estimating and analysis for projects.

### Simulation
This folder contains two MS excel sheets formatted based on the masterformat 50 division format. The script contained in this folder is a basic monte carlo simulation used to assist in quantifying risk.[^1] 

The two sheets are for one and three point estimates, once these are populated the script can be ran and the parameters choosen, the output will be the raw simulation data, a basic general statics table, and a histogram of the simulation. 

## Scheduling
This folder will contain all items that pertain primarily to project scheduling and analysis. 



[^1]: Author makes no warranty or guarantee express or implied that these simulations will produce accurate resulsts, it is up to the user to ensure that the data is properly analyzed and the simulation is producing accepatble results. 