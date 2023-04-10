from git import Repo
from github import Github

g = Github()

# USERNAME HERE
ORG = ("USERNAME/ORG")

user = g.get_user(ORG)
repos = user.get_repos()

public = []
for repo in user.get_repos():
    if repo.private is False:
        public.append(repo.name)
        Repo.clone_from(f"https://github.com/{ORG}/{repo.name}", repo.name)

print("DEBUG:>>> PUBLIC REPOS>>> ", public)

