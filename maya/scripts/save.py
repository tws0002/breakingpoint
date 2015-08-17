#*************************************************************
# title:        Save
#
# software:     Maya
#
# content:      automaticly saves work and publish files
#               automaticly executes other script on publish
#
# dependencies: "PYTHONPATH=%SOFTWARE_PATH%;%PYTHONPATH%"
#
# author:       Alexander Richter 
# email:        alexander.richter@filmakademie.de
#*************************************************************
# -*- coding: utf-8 -*-

import os, sys
import shutil
import webbrowser

from PySide.QtGui import *
from PySide.QtCore import *

from scripts.ui import save

import maya.cmds as cmds
import maya.mel as mel

import settings as s
sys.path.append(s.PATH['lib'])
import libMessageBox as msg


#**********************
# RUN DOS RUN
#**********************
saveW   = QWidget()
ui      = save.Ui_save()


#**********************
# VARIABLE
#**********************
VERSION         = "v0.45"
CURRENT_USER    = os.getenv('username')

FILE_NAME       = ['140', 'SHD', 'v001', 'ar']
FILE_FORMAT     = 'ma'
SAVE_DIR        = ''

SHOT_DEFAULT    = '000'

SCENE_SHD_PATH  = s.PATH_EXTRA["scene_shd"]
META_DATA       = "Resolution:  2048 x 1152\n\nFPS:           25 FPS\n\nFrames:       1001 - "


#**********************
# CLICKED_TRIGGER
#**********************
def clicked_btnSave():
    saveFile()


def clicked_btnCancel():
    saveW.close() 


def clicked_btnHelp():
    webbrowser.open(s.LINK["software"])


def clicked_btnEmail():
    print ("clicked_btnEmail")


def clicked_btnReport():
    print ("clicked_btnReport")
    from scripts import report
    report.start()


def clicked_btnMsgFolder():
    print("clicked_btnMsgFolder")
    output = msg.folderMsgBox(saveW, "Maya Files (*.mb *.ma)", "Choose Maya file to open")
    print "OUTPUT: " + str(output)
    
    initPath(output)


def clicked_btnVersionUp():
    global FILE_NAME

    if('v' in FILE_NAME[2]): 
        FILE_NAME[2] = FILE_NAME[2].replace('v', '')
        FILE_NAME[2] = 'v' + str('{0:03d}'.format(int(FILE_NAME[2]) + 1))

    ui.edtSavePath.setText(('_').join(FILE_NAME) + '.' + FILE_FORMAT)
    changed_edtComment()


def clicked_btnVersionDown():
    global FILE_NAME

    if('v' in FILE_NAME[2] and FILE_NAME[2] != "v000"): 
        FILE_NAME[2] = FILE_NAME[2].replace('v', '')
        FILE_NAME[2] = 'v' + str('{0:03d}'.format(int(FILE_NAME[2]) - 1))

    ui.edtSavePath.setText(('_').join(FILE_NAME) + '.' + FILE_FORMAT)
    changed_edtComment()


#**********************
# CHANGED_TRIGGER
#**********************
def changed_user():
    global FILE_FORMAT
    
    # CHANGE USER IMG
    changeUserImg(ui.cbxUser.currentText())

    # CHANGE USER TOKEN
    FILE_NAME[3] = ui.cbxUser.currentText()[:2]
    ui.edtSavePath.setText(('_').join(FILE_NAME) + '.' + FILE_FORMAT)
    ui.edtPath.setText(os.path.join(SAVE_DIR, ui.edtSavePath.text()))
    changed_edtComment()


def changed_publish():
    global SAVE_DIR

    if(ui.cbxPublish.isChecked()):
        ui.edtComment.setEnabled(False)
        ui.edtComment.setPlainText('')
        ui.lblStatus.setText("PUBLISH")

    else:
        ui.edtComment.setEnabled(True)
        ui.lblStatus.setText("WORK")
       

def changed_edtComment():
    if(len(ui.edtComment.toPlainText()) < 20):
        if not (ui.edtComment.toPlainText() == ''):
            ui.edtSavePath.setText(('_').join(FILE_NAME) + '_' + ui.edtComment.toPlainText() + '.' + FILE_FORMAT)   
        else:
            ui.edtSavePath.setText(('_').join(FILE_NAME) + '.' + FILE_FORMAT)   
    else:
        ui.edtComment.textCursor().deletePreviousChar()
       

def changed_edtSavePath():
    currentFile     = ui.edtPath.text()

    if(len(currentFile.split('.')) > 1):
        (FILE_NAME, FILE_FORMAT) = currentFile.split('.')

        if (len(FILE_NAME.split('_')) > 4):
            FILE_NAME = FILE_NAME.split('_')
        else:
            ui.edtPath.setText('NAME CONVENTION: Not conform name setting - 010_SHD_v001_ar.' + FILE_FORMAT)

    ui.edtPath.setText(os.path.join(SAVE_DIR, ui.edtSavePath.text()))


#**********************
# FUNCTIONS
#**********************
def changeUserImg(user):
    currentImgPath = os.path.join(s.PATH['img'], 'user', user + ".png")
    if(os.path.isfile(currentImgPath)):
        ui.lblUser.setPixmap(QPixmap(QImage(currentImgPath)))
    else:
        ui.lblUser.setPixmap(QPixmap(QImage(os.path.join(s.PATH['img'], 'user', "_default.png"))))


def setMetaData():
    ui.edtMetaData.setPlainText(META_DATA)


def initPath(filePath = ''):
    global FILE_NAME, FILE_FORMAT, SAVE_DIR

    if(filePath == ''):
        filePath = cmds.file(q=True,sn=True)

    SAVE_DIR        = os.path.dirname(filePath).replace('/','\\')
    currentFile     = os.path.basename(filePath)

    print SAVE_DIR
    print currentFile

    if not (SAVE_DIR):
        SAVE_DIR =  os.path.join(s.PATH['shots'], '000_TEMPLATE\\40_LIGHT\\WORK')
        currentFile = '000_LIGHT_v000_ar.' + FILE_FORMAT

    if(SAVE_DIR.startswith("\\\\bigfoot\\breakingpoint")):
        SAVE_DIR = SAVE_DIR.replace("\\\\bigfoot\\breakingpoint", "P:")

    (FILE_NAME, FILE_FORMAT) = currentFile.split('.')

    if (len(FILE_NAME.split('_')) == 5):
        (shot, task, version, user, comment) = FILE_NAME.split('_')
    
    elif(len(FILE_NAME.split('_')) == 4):
        (shot, task, version, user) = FILE_NAME.split('_')
   
    else:
        (shot, task) = FILE_NAME.split('_')
        version = "v000"

    user = ui.cbxUser.currentText()[:2]

    if('v' in version): 
        version = version.replace('v', '')
        version = 'v' + str('{0:03d}'.format(int(version) + 1))

    FILE_NAME = [shot, task, version, user]

    ui.lblBanner.setPixmap(QPixmap(QImage(os.path.join(s.PATH['img'], 'banner', task + ".png"))))
    
    imgShotPath = os.path.join(s.PATH['img'], 'shot', shot + ".png")
    if not os.path.isfile(imgShotPath): 
        imgShotPath = os.path.join(s.PATH['img'], 'shot', SHOT_DEFAULT + ".png")

    ui.lblImage.setPixmap(QPixmap(QImage(imgShotPath)))

    ui.edtSavePath.setText(('_').join(FILE_NAME) + '.' + FILE_FORMAT)
    ui.lblShotNr.setText(shot)

    if("PUBLISH" in SAVE_DIR):
        SAVE_DIR = SAVE_DIR.replace("PUBLISH", "WORK")

    ui.edtPath.setText(os.path.join(SAVE_DIR, ui.edtSavePath.text()))
    setMetaData()


def saveFile():
    global SAVE_DIR, FILE_FORMAT, FILE_NAME

    msgText         = "File was saved!\n\n"
    sceneReference  = []

    # SAVE FILE:
    tmpSavePath = ui.edtPath.text()
    

    if(ui.cbxPublish.isChecked()):

        msgText = "File was published!\n\n"

        try:

            # CUSTOM TASK SCRIPTS
            if("MODEL" == FILE_NAME[1]):
                print ("PUBLISH: MODEL")


            if("SHD" == FILE_NAME[1]):
                print ("PUBLISH: SHD")

                try:
                    mel.eval('file -removeReference -referenceNode "SCENE_SHDRN";')
                except:
                    print("** FAIL | SAVE: Cant remove SCENE_SHD reference **")

                try:
                    from scripts.SHD import uniteShaderGroup
                    uniteShaderGroup.start()
                except:
                    print ("** FAIL | Unite Shader and Shader Group **")

                sceneFile = mel.eval('file -q -l;') [1:]

                for files in sceneFile:
                    if(files.endswith("."+ FILE_FORMAT)):

                        tmpReference = os.path.basename(files).split(".")[0] + "RN"
                        sceneReference.append(tmpReference)

                        try:
                            cmds.file(unloadReference=tmpReference)
                        except:
                            print ("FAIL | SAVE: Reference not exists: " + tmpReference)


            if("RIG" == FILE_NAME[1]):
                print ("PUBLISH: RIG")    


            if("LIGHT" == FILE_NAME[1]):
                print ("PUBLISH: LIGHT")
                
        except:
            msgFailed = "** SORRY | SAVE: One helping script failed! **"
            print(msgFailed)
            msgText = msgText + msgFailed


    try:    
        cmds.file( rename=tmpSavePath)
        cmds.file( save=True, type='mayaAscii' )

    except:
        msgText = "FAIL | SAVE: Couldnt save file!"

    print ("SAVE: " + tmpSavePath)


    if(ui.cbxPublish.isChecked()):

        # COPY FILE WITH _PUBLISH
        tmpCopyWork = os.path.join(SAVE_DIR, ('_').join(FILE_NAME) + '_PUBLISH' + '.' + FILE_FORMAT)
        shutil.copy(tmpSavePath, tmpCopyWork)
        print ("COPY: " + tmpCopyWork)
        
        if('WORK' in SAVE_DIR):
            SAVE_DIR = SAVE_DIR.replace('WORK', 'PUBLISH')

        # PUBLISH FILE
        if("ANIM" == FILE_NAME[1]):
            print ("ANIM PUBLISH")
            from scripts.ANIM import alembicExport
            msgText = "File was saved!\n\n" + alembicExport.start()
            print ("PUBLISH: ALEMBIC") 

        else:
            tmpCopyPublish = os.path.join(SAVE_DIR, ('_').join(FILE_NAME[:2]) + '.' + FILE_FORMAT)
            shutil.copy(tmpSavePath, tmpCopyPublish)
            print ("PUBLISH: " + tmpCopyPublish)

        if("SHD" == FILE_NAME[1]): 
            from scripts.SHD import referenceSCENE_SHD
            referenceSCENE_SHD.start()

            for tmpReference in sceneReference:
                if not (sceneReference == ""):
                    cmds.file(loadReference=tmpReference)

            cmds.file(s = True)


    QMessageBox.information( saveW, "Save", msgText.replace("**", "") ) 

    print ("** DONE | SAVE: Save File **")
    saveW.close() 


#**********************
# START PROZESS
#**********************
def setSave():
    global CURRENT_USER
    CURRENT_USER = os.getenv('username')

    userList = os.listdir(s.PATH['data_user'])
    ui.cbxUser.addItems(sorted(userList))
    
    if(os.getenv('username') in userList):      
        ui.cbxUser.setCurrentIndex(ui.cbxUser.findText(os.getenv('username')))

    #setLOGO IMG
    initPath()


#**********************
# START UI
#**********************
def start():
    ui.setupUi(saveW)

    ui.lblVersion.setText(VERSION)
    
    saveW.connect(ui.btnSave, SIGNAL("clicked()"), clicked_btnSave)
    saveW.connect(ui.btnCancel, SIGNAL("clicked()"), clicked_btnCancel)
    saveW.connect(ui.btnHelp, SIGNAL("clicked()"), clicked_btnHelp)
    saveW.connect(ui.btnEmail, SIGNAL("clicked()"), clicked_btnEmail)
    saveW.connect(ui.btnReport, SIGNAL("clicked()"), clicked_btnReport)
    saveW.connect(ui.btnFolder, SIGNAL("clicked()"), clicked_btnMsgFolder)
    saveW.connect(ui.btnVersionUp, SIGNAL("clicked()"), clicked_btnVersionUp)
    saveW.connect(ui.btnVersionDown, SIGNAL("clicked()"), clicked_btnVersionDown)

    saveW.connect(ui.cbxUser, SIGNAL("currentIndexChanged(const QString&)"), changed_user)

    # ui.btnReport.hide()
    ui.btnEmail.hide()

    ui.cbxPublish.toggled.connect(changed_publish)  
    ui.edtSavePath.textChanged.connect(changed_edtSavePath)
    ui.edtComment.textChanged.connect(changed_edtComment)

    setSave()

    # ui.edtQuestionNr.returnPressed.connect(changed_questionNr)
    # ui.edtQuestionNr.lostFocus.connect(changed_questionNr)

    saveW.show()    