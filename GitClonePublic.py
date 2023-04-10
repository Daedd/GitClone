from git import Repo
from github import Github

g = Github()

ORG = input("USER/ORG: ")

user = g.get_user(ORG)
repos = user.get_repos()

for repo in user.get_repos():
    if repo.private is False:
        print("Cloning: ", repo.full_name, repo.url)
        Repo.clone_from(f"https://github.com/{ORG}/{repo.name}", f"/temp/CLONED/{repo.full_name}")
