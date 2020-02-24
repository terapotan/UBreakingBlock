import subprocess

class makeNewFeatureScene:
    def executeMenuScene(self):
        inputIssueNum = input("Please enter featureNumber (issue number)>")

        moveDevelopBranch = subprocess.run("git checkout develop",shell=True)
        makeLocalFeatureBranch = subprocess.run("git checkout -b feature" + inputIssueNum,shell=True)
        makeRemoteFeatureBranch = subprocess.run("git push -u origin feature" + inputIssueNum,shell=True)
        

