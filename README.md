Creates Bigbluebutton participant lists based on the production.log files in greenlight.

First the programm reads the logfiles and caches the data in an array-list. Afterwards the array list will be 
processed to a dictionary. The dictionary has following key, values:
key: "room_id" value: [logfiles][...][...]

Based on the dictionary all data will be processed to seperated room_id .csv files
Now we have login/logout lists of all rooms on our bigbluebutton server