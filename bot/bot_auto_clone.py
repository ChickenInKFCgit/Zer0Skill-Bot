"""
Permet de récupérer des repositories via git, et ici via les serveurs de github.
Permet également l'update de ces repositories.

si module non trouvé : pip install gitpython
"""

from git import Repo 

def cloner(git_url:str, repo_dir:str):
    Repo.clone_from(git_url, repo_dir)