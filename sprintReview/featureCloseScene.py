import subprocess

class featureCloseScene:
    def executeMenuScene(self):
        inputIssueNum = input("Please enter featureNumber (issue number)>")

        moveDevelopBranch = subprocess.run("git checkout develop",shell=True)
        makeLocalFeatureBranch = subprocess.run("git merge feature" + inputIssueNum + " --no-ff",shell=True)
        pushLocalFeatureBranch = subprocess.run("git push -u origin develop",shell=True)
        deleteRemoteFeatureBranch = subprocess.run("git push --delete origin feature" + inputIssueNum,shell=True)
        deleteLocalFeatureBranch = subprocess.run("git branch -d feature" + inputIssueNum,shell=True)
        