import subprocess

class makeNewreleaseScene:
    def executeMenuScene(self):
        releaseName = input("Enter the release name (ex.prealpha2.1). >")

        moveDevelopBranch = subprocess.run("git checkout develop",shell=True)
        makeLocalNewRelease = subprocess.run("git checkout -b release-" + releaseName,shell=True)
        pushLocalReleaseBranch = subprocess.run("git push -u origin release-" + releaseName,shell=True)
