# make sure up to date
import git
import os
import subprocess
import sys
from PyQt5.QtWidgets import QMessageBox

class Installer:
    @staticmethod
    def install():
        # Prompt user to restart the application
        msg_box = QMessageBox()
        msg_box.setText("it's installing/updating. i have no loading bar sorry. close this message, i'll tell you when it's done")
        msg_box.exec_()

        try:
            subprocess.run(["pyinstaller", "--onefile", "--clean", "--noconsole", "./GUI/main.py"])
        except subprocess.CalledProcessError as e:
            pass

    @staticmethod
    def update(repo_path):
        if not os.path.exists(repo_path):
            # Repository doesn't exist, clone it
            git.Repo.clone_from("https://github.com/rukadev/audio.git", repo_path)
            Installer.install()
            return True
        else:
            repo = git.Repo(repo_path)
            
            # Fetch latest changes from remote
            repo.remotes.origin.fetch()
            
            # Get the local and remote commit hashes
            local_hash = repo.head.commit.hexsha
            remote_hash = repo.remotes.origin.refs.main.commit.hexsha
            
            # Compare local and remote commit hashes
            if local_hash != remote_hash:
                print("There are new updates available.")
                
                # Pull the updates
                repo.remotes.origin.pull()
                
                print("Updates have been pulled successfully.")
                Installer.install()
                return True
            else:
                print("Your repository is up to date.")

    
