import subprocess

class closeReleaseScene:
    def executeMenuScene(self):
        releaseName = input("Enter the release name (ex.prealpha2.1). (Commit or not)>")

        addFiles = subprocess.run("git add --all",shell=True)
        commitFeatureFile = subprocess.run("git commit -m \"release commit\"",shell=True)
        moveMasterBranch = subprocess.run("git checkout master",shell=True)
        mergeReleaseBranch = subprocess.run("git merge release-" + releaseName,shell=True)
        pushLocalMasterBranch = subprocess.run("git push origin master",shell=True)
        addTagToLocalReleaseBranch = subprocess.run("git tag " + releaseName,shell=True)
        pushAllTag  = subprocess.run("git push origin "+ releaseName,shell=True)
        moveDevelopBranch = subprocess.run("git checkout develop",shell=True)
        mergeMasterToDevelop = subprocess.run("git merge --no-ff master",shell=True)
        pushDevelopBranch = subprocess.run("git push origin develop")
        deleteLocalReleaseBranch = subprocess.run("git branch -d release-" + releaseName,shell=True)
        deleteRemoteReleaseBranch = subprocess.run("git push --delete origin release-" + releaseName,shell=True)

