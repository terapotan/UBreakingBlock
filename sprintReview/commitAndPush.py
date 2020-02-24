# coding: utf-8
import subprocess

class commitAndPush:
    def executeMenuScene(self):
        try:
                commitMessage=input("Please enter a commit message.")
                allAdd = subprocess.run("git add --all",shell=True)
                moveDevelopBranch = subprocess.check_call("git commit -m"+commitMessage,shell=True)
                checkOK = input("Are all tests successful?(Allow push?)(y/n)>")

                if checkOK == "y":
                        pass
                else:
                        return
                
                currentBranch = subprocess.check_output("git rev-parse --abbrev-ref @").decode('utf-8')
                push = subprocess.run("git push -u origin " + currentBranch,shell=True)
        except subprocess.CalledProcessError:
                pass
