import subprocess
import makeNewreleaseScene
import closeReleaseScene
import makeNewFeatureScene
import webbrowser
import featureCloseScene
import managementPredictedValueFile
import shutil

class sprintReviewRunScene:
    def executeMenuScene(self):
                
        #Document/sprintReviewDocumentに現在のスプリント名のファイルを作成し
        #作成したmdファイルを開く
        jsonFileInstance = managementPredictedValueFile.managementPredictedValueFile()
        webbrowser.open("https://github.com/terapotan/BreakingBlocks#workspaces/-5d0cc4b925117c7c06ea41d7/reports/burndown?milestoneId="+jsonFileInstance.getmileStoneID())
        
        openFile = subprocess.run("start .././Document/sprintReviewDocument/スプリントレビュー.md",shell=True)
        
        print("スプリントレビューを行ってください。")
        input("作業が終了したらEnterキーを押してください...\n")
        
        print("現在開かれているマイルストーンを閉じてください。")
        input("作業が終了したらEnterキーを押してください...\n")

        print("プロジェクト管理ツールを開きます。")
        opens=subprocess.run("start .././projectManagement/main.py",shell=True)

        input("ストーリポイントの追加を行ってください。終了したらEnterキーを押してください。")
        input("予測値の更新を行ってください。終了したらEnterキーを押してください。")
        input("プロジェクト管理ツールを終了してください。\n")

        webbrowser.open("https://github.com/terapotan/BreakingBlocks#workspaces/-5d0cc4b925117c7c06ea41d7/board?repos=192507024")
        
        opens=subprocess.run("start supportEmistate.py",shell=True)
        
        print("現在存在するイシューのストーリポイントを調整してください。")
        input("作業が終了したらEnterキーを押してください...\n")

        print("イシューの削除・変更・追加を行ってください。")
        input("作業が終了したらEnterキーを押してください...\n")

        webbrowser.open("https://github.com/terapotan/BreakingBlocks#workspaces/-5d0cc4b925117c7c06ea41d7/reports/burndown?milestoneId="+jsonFileInstance.getmileStoneID())        
        
        print("新たにマイルストーンを作成し、開いてください。")
        input("作業が終了したらEnterキーを押してください...\n")

        newMileStoneId = input("新たに作成したマイルストーンのIDを入力してください。")
        jsonFileInstance.setmileStoneID(newMileStoneId)

        webbrowser.open("https://github.com/terapotan/BreakingBlocks#workspaces/-5d0cc4b925117c7c06ea41d7/board?repos=192507024")
        
        print("作成したマイルストーンに次回行うイシューを設定してください。")
        input("作業が終了したらEnterキーを押してください...\n") 

        print("全てのfeatureブランチを完了させてください。")
        showBranchList = subprocess.run("git branch",shell=True)
        while(1):
            featureCloseScene.featureCloseScene().executeMenuScene()
            isContinue = input("作業を続行しますか?(y/n)")        
            if(isContinue == "n"):
                break

        print("リリース作業を行ってください。")
        
        #以下を自動化
        #MSBuildを用いてプロジェクトをRelease構成でビルドする
        buildProject = subprocess.run("msbuild /p:Configuration=Release .././NewBreakingBlocks/NewBreakingBlocks/NewBreakingBlocks.vcxproj",shell=True)
        #その後ReleaseSoftwareにNewBreakingBlocks.exeをコピーし置き換え
        shutil.copy2(".././NewBreakingBlocks/NewBreakingBlocks/Release/NewBreakingBlocks.exe", ".././NewBreakingBlocks/ReleaseSoftware/NewBreakingBlocks.exe")
        #続いてREADME.mdを開き、NewBreakingBlocks.exeを起動する
        openREADME = subprocess.run("start ../README.md",shell=True)
        startNewBreakingBlocks = subprocess.run("start NewBreakingBlocks.lnk",shell=True)

        input("作業が終了したらEnterキーを押してください...\n") 
        makeNewreleaseScene.makeNewreleaseScene().makeNewreleaseScene()
        print("新規featureブランチを作成してください。")
        makeNewFeatureScene.makeNewFeatureScene().executeMenuScene()
        print("スプリントレビューを終了します。\n")