# coding: utf-8

import sprintReviewRunScene 
import makeNewFeatureScene
import featureCloseScene
import makeNewreleaseScene
import closeReleaseScene
import commitAndPush

class startUpScene:
    def executeStartUpScene(self):
        userSelectNum = "-100"
        while(1):
            print("git-flow support tool ver1.0")
            print("Select the operation you want to perform. To end, enter -1.\n")
            print("0: Execute sprint review")
            print("1: Create new feature branch")
            print("2: feature branch completed")
            print("3: Create new release branch")
            print("4: release branch completed (tag also add)")
            print("5: Commit & push execute\n")
            
            #返ってきたuserSelectNumは文字列あつかいになる
            userSelectNum = input("Please fill in the value>")

            if(int(userSelectNum) == -1):
                break

            callClassList = [sprintReviewRunScene.sprintReviewRunScene(),
                    makeNewFeatureScene.makeNewFeatureScene(),
                    featureCloseScene.featureCloseScene(),
                    makeNewreleaseScene.makeNewreleaseScene(),
                    closeReleaseScene.closeReleaseScene(),
                    commitAndPush.commitAndPush()]

            callClassList[int(userSelectNum)].executeMenuScene()

        print("Exit.\n")
        
        return
