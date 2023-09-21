#Names: Benjamin Liu and Abraham Medina
#Project: Data analytics

-----------------------How to use-----------------------
Open and run the program TeamProject_Stats.py 
A small window should appear prompting for a csv file.
The user can either manually type the file path to the csv file, or they can use the browse button to search for it.
Once a file path/name has been selected (it should appear in the entry box), press the process button.
If the file can be opened, the window will change.
In this new window, the bottom half of the screen displays all the data contained in the CSV file.
The very last rows (can scroll down if needed) will be the statstical analysis of each columns.
The statstical analysis performed are total, min, max, mean, meadian, and standard deviation.
If the user would like to visually represent the data with graphs, they can select the bar, pie, or lollipop graph buttons.
Upon selecting any of those buttons, a new window will appear.
Select one of the data options (may need to vertically resize window if there are a lot of data sets) and then press the confirm button.
Upon pressing the confirm button, the corressponding graph will be displayed.
To exit the graph, simply press the x on the top right window as you would with any other window.
The exit the data options window, simply select the exit graph button.
The user can go back to the previous window and select a different graph to view.
The reset button can be selected to take the user back to the file select screen, and they can input a different csv file.
To exit the program hit the x on the top right window similar to exiting the graph.  

-----------------------Notes and Design stipulations----------------------- 
The program expects a csv file, but a txt file could be accepted. As long as the txt file follows the same format as a csv file it should be fine.
But there could be unexpected results if the txt file does not follow the same format as a csv file.
For the csv files themselves we expect the first row to be the names of each column. 
We also expect the first column to be the names/labels of each row.
Refer to the Global Temperature Anomaly.csv and planets.csv file for how the program expects the csv file to be formatted. 
For the pie chart, it can only graph data if all the values in that data set are positive. A pie chart can not be created if there are negative values within the data set
and an error message should pop up, stating the pie chart could not be create because of this.
