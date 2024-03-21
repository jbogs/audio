import git
import os

def check_for_updates(repo_path):
    if not os.path.exists(repo_path):
        # Repository doesn't exist, clone it
        git.Repo.clone_from("https://github.com/rukadev/elixir2d.git", repo_path)
        print("Repository cloned successfully.")
    else:
        repo = git.Repo(repo_path)
        
        # Fetch latest changes from remote
        repo.remotes.origin.fetch()
        
        # Get the local and remote commit hashes
        local_hash = repo.head.commit.hexsha
        remote_hash = repo.remotes.origin.refs.master.commit.hexsha
        
        # Compare local and remote commit hashes
        if local_hash != remote_hash:
            print("There are new updates available.")
            
            # Pull the updates
            repo.remotes.origin.pull()
            
            print("Updates have been pulled successfully.")
        else:
            print("Your repository is up to date.")

# Example usage
repository_path = "./Path"
check_for_updates(repository_path)
