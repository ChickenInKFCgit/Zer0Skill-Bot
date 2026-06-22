"""
Permet de récupérer des repositories via git, et ici via les serveurs de github.
Permet également l'update de ces repositories.

si module non trouvé : pip install gitpython
"""

from git import Repo 

def clone_service(servicename:str) -> str:
    """
    Clone un service.
    Renvoie le résultat d'exécution.
    """
    if (servicename in d_repos.keys()):
        urlrepo = d_repos[servicename]
        pathrepo = "services"
        if(__cloner(git_url=urlrepo, repo_dir=pathrepo) ):
            return f"Réussite du cloning du repository à l'adresse '{urlrepo}' dans '{pathrepo}'."
        else :
            return f"Echec du cloning du repository : '{urlrepo}' dans '{pathrepo}'."
    else:
        return f"'{servicename}' ne correspond à aucun repo enregistré dans 'repositories.tsv'."

def __cloner(git_url:str, repo_dir:str) -> bool:
    rep = Repo.clone_from(git_url, repo_dir)
    return rep != None

def load_repositories():
    f = open("services/repositories.tsv",mode="r",encoding="utf-8")

    d={}
    for ligne in f.read().split("\n"):
        nom_repo, url_repo = ligne.split("\t");
        d[nom_repo] = url_repo
    return d

d_repos = load_repositories()