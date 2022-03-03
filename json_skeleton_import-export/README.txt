'''''''''''''''''''''''''''''''''''''''''''''''''''
Rigging Pose Joints to JSON (Export/Import)  
Copyright February 2022 Keven Fazio
'''''''''''''''''''''''''''''''''''''''''''''''''''

In this .zip file, you will find a custom shelf file labeled 'shelf_SR_ProblemOne.mel' and this 'README.txt' file.

INSTALLATION
-Locate the 'shelves' folder in your version of Maya. (i.e. C:\Users\...\Documents\maya\2022\prefs\shelves).
-Copy the 'shelf_SR_ProblemOne.mel' file to that folder.
-Open that version of Maya and if your shelf is visible, you will see the 'SR_ProblemOne' tab at the end of the shelf window with a tool icon labled 'json SK'.
-You may view and make changes to the shelf and tool in the 'Shelf Editor' (Windows->Settings/Preferences->Shelf Editor). 

HOW THE TOOL WORKS
This tool was created to take a selected hierarchy of joints from a skeleton and do two things:

1) Import a .json file with the joint names and transform information into the same skeleton the .json file was created from.
	This will overwrite the current transform settings for all the selected joints. Not the names.
	*NOTE: Changing of joint names either on the skeleton or in the file may break the functionality of this tool and cause unexpected results.

2) Export the hierarchy of joints with their names and transform information into a .json file to be used with the same skeleton.

TO IMPORT .JSON FILE
1) Select the root joint (which will include all of it's children) that you wish to overwrite with the information in the .json file. 
2) Enter the file path of the .json file you wish to use into the designated text field.
3) Click 'Import JSON', the changes will take effect immediately, and a prompt will appear notifying you of it's success or if there was an error.

TO EXPORT .JSON FILE
1) Select the root joint (which will include all of it's children) that you wish to write to the file.
	*NOTE: It is recommended to choose the first root joint to allow more flexibility when importing later.
2) Enter the file path of the folder where you wish to save the file too and add what you wish to name the file to the end (i.e. '...\problemOne.json').
3) Click the 'Export JSON' button. A prompt will appear notifying you of it's success or if there was an error.
4) Although I have confidence in the tool, it is always recommended to check that the file was created and the correct information is there. 


