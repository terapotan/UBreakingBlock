# coding: utf-8
import os
import json

class managementPredictedValueFile:

    def __init__(self):
        '''jsonファイルが作成されていない時には、jsonファイルを新規作成し
    既に新規作成されている時にはjsonファイルのパースを行います。
    '''
        currentPath = os.path.dirname(__file__)
        self.fileName = "mileStoneID.json"
        #jsonファイルが作成されていない場合は空のjsonファイルを作成
        if(not os.path.exists(currentPath + '\\'+ self.fileName)):
            self.jsonWriteFile = open(currentPath + '\\'+ self.fileName,'w+')
            self.jsonWriteFile.write('{\n')
            self.jsonWriteFile.write('\"data\":{\n')

            self.jsonWriteFile.write('\"milestoneID\":\"defaultID\"\n')
            self.jsonWriteFile.write("}\n")
            self.jsonWriteFile.write("}")
            self.jsonWriteFile.close()
        
        self.jsonWriteFile = open(currentPath + '\\'+ self.fileName,'a')
        self.jsonReadFile = open(currentPath + '\\'+ self.fileName,'r')
        self.predictedValueFileData_json = json.load(self.jsonReadFile)

    def showFileAllLine(self):
        print("{}".format(json.dumps(self.predictedValueFileData_json,indent=4)))
        
    def getmileStoneID(self):
        return self.predictedValueFileData_json["data"]["milestoneID"]
    def setmileStoneID(self,setValue):
        self.predictedValueFileData_json["data"]["milestoneID"] = setValue
        self.clearFileContents()
        json.dump(self.predictedValueFileData_json,self.jsonWriteFile,indent=4)
    def clearFileContents(self):
        tmpFile = open(os.path.dirname(__file__) + '\\'+ self.fileName,'w')
        tmpFile.close()
    def __del__(self):
        self.jsonWriteFile.close()
        self.jsonReadFile.close()
    

