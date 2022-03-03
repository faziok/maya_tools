#'''''''''''''''''''''''''''''''''''''''''''''''''''
#Rigging Pose Joints to JSON (Export/Import) 
#Copyright 2022 Keven Fazio
#'''''''''''''''''''''''''''''''''''''''''''''''''''

import maya.cmds as cmds
import json

class JSON(object):
        
    #constructor
    def __init__(self):
        self.size = (500, 500)
        self.window = "JSON"
        self.title = "Skeleton JSON Import/Export"
        self.instructions = "\nChoose to Import or Export a JSON file of the selected joints with their Tranform Attributes.\nBegin by selecting the Root joint in the hierarchy."
        self.browserFilter = "*.json"
            
        # close old window is open
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window=True)
            
        #create new window
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        
        cmds.columnLayout( adjustableColumn = True, columnAttach=('both', 5), rowSpacing=10)
        cmds.text(self.instructions)
        cmds.separator(height=20)
        cmds.button(label="Import JSON", command=self.importBtn)
        cmds.button(label="Export JSON", command=self.exportBtn)
        self.errorText = cmds.textFieldGrp(visible=False, adjustableColumn=1)

        #display new window
        cmds.showWindow()        
    
    #import button    
    def importBtn(self, *args):
        #try that a joint is selected
        try:
            selectedJointRoot = cmds.joint(q=True, n=True)
        except:
            cmds.textFieldGrp(self.errorText, visible=True, e=True, text="Please select a root joint and try again.")
            return
            
        #get filepath from user
        try:
            path = cmds.fileDialog2(fileMode=1, fileFilter=self.browserFilter, dialogStyle=2)
            importFilePath = path[0]
        except:
            cmds.textFieldGrp(self.errorText, visible=True, e=True, text="No import file selected.")
            return
        
        #try to open file
        try:
            with open(importFilePath, 'r') as f:
                data = json.load(f)
        except:
            cmds.textFieldGrp(self.errorText, visible=True, e=True, text="Import file path not valid.")
            return                 
        
        #setting the attributes        
        def set_data(data):
            joints = cmds.ls(dagObjects=True, allPaths=True, selection=True, type="joint")
                       
            for j in joints:
                #Translate
                cmds.setAttr(j+'.translateX', data[j]["Translate"][0])
                cmds.setAttr(j+'.translateY', data[j]["Translate"][1])
                cmds.setAttr(j+'.translateZ', data[j]["Translate"][2])
                #Rotate
                cmds.setAttr(j+'.rotateX', data[j]['Rotate'][0])
                cmds.setAttr(j+'.rotateY', data[j]['Rotate'][1])
                cmds.setAttr(j+'.rotateZ', data[j]['Rotate'][2])        
                #Scale
                cmds.setAttr(j+'.scaleX', data[j]['Scale'][0])
                cmds.setAttr(j+'.scaleY', data[j]['Scale'][1])
                cmds.setAttr(j+'.scaleZ', data[j]['Scale'][2])
                #Shear
                cmds.setAttr(j+'.shearXY', data[j]['Shear'][0])
                cmds.setAttr(j+'.shearXZ', data[j]['Shear'][1])
                cmds.setAttr(j+'.shearYZ', data[j]['Shear'][2])
                #Rotate Order
                cmds.setAttr(j+'.rotateOrder', data[j]['Rotate Order'][0])
                #Rotate Axis
                cmds.setAttr(j+'.rotateAxisX', data[j]['Rotate Axis'][0])
                cmds.setAttr(j+'.rotateAxisY', data[j]['Rotate Axis'][1])
                cmds.setAttr(j+'.rotateAxisZ', data[j]['Rotate Axis'][2])        

        #set selected joints
        try:
            set_data(data)
        except:
            cmds.textFieldGrp(self.errorText, visible=True, e=True, text="***Selected root not found in file.***")
            return
        
        #success message
        cmds.textFieldGrp(self.errorText, visible=True, e=True, text="File IMPORTED successfully!")
    
    #export button    
    def exportBtn(self, *args):
        #try that a joint is selected
        try:
            selectedJointRoot = cmds.joint(q=True, n=True)
        except:
            cmds.textFieldGrp(self.errorText, visible=True, e=True, text="Please select a root joint and try again.")
            return
        
        #create tree of joints   
        def hierarchyTree(tree):
            joints = cmds.ls(dagObjects=True, allPaths=True, selection=True, type="joint")
            
            for j in joints:
                t = [cmds.getAttr(j+'.translateX'), cmds.getAttr(j+'.translateY'), cmds.getAttr(j+'.translateZ')]
                r = [cmds.getAttr(j+'.rotateX'), cmds.getAttr(j+'.rotateY'), cmds.getAttr(j+'.rotateZ')]
                s = [cmds.getAttr(j+'.scaleX'), cmds.getAttr(j+'.scaleY'), cmds.getAttr(j+'.scaleZ')]
                sh = [cmds.getAttr(j+'.shearXY') ,cmds.getAttr(j+'.shearXZ'), cmds.getAttr(j+'.shearYZ')]
                ro = [cmds.getAttr(j+'.rotateOrder')]
                ra = [cmds.getAttr(j+'.rotateAxisX'), cmds.getAttr(j+'.rotateAxisY'), cmds.getAttr(j+'.rotateAxisZ')]
                tree[j] = {"Translate": t, "Rotate": r, "Scale": s, "Shear": sh, "Rotate Order": ro, "Rotate Axis": ra}
        
        #get filepath from user
        try:
            path = cmds.fileDialog2(fileFilter=self.browserFilter, dialogStyle=2)
            exportFilePath = path[0]
            print (exportFilePath)
        except:
            cmds.textFieldGrp(self.errorText, visible=True, e=True, text="No export file selected.")
            return
        
        #create Dict of joints and fill it
        hierarchy_tree = {}
        hierarchyTree(hierarchy_tree)
        
        #try to open and write to file
        try:
            with open(exportFilePath, 'w+') as p:
                json.dump(hierarchy_tree, p, indent = 4)
        except:
            cmds.textFieldGrp(self.errorText, visible=True, e=True, text="Export file path not valid")
            return
        
        #success message                  
        cmds.textFieldGrp(self.errorText, visible=True, e=True, text="File EXPORTED successfully!")
                                   
myWindow = JSON()