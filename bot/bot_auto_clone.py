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
        pathrepo = f"services/{servicename}"

        try: repo = __cloner(git_url=urlrepo, repo_dir=pathrepo)
        except Exception: return f"Echec : '{pathrepo}' existe déjà et n'est pas vide." 
        if(repo==None ):
            return f"Echec du cloning du repository : '{urlrepo}' dans '{pathrepo}'." 
        else:
            return f"Réussite du cloning du repository à l'adresse '{urlrepo}' dans '{pathrepo}'."
    else:
        return f"'{servicename}' ne correspond à aucun repo enregistré dans 'repositories.tsv'."

def __cloner(git_url:str, repo_dir:str) -> Repo:
    return Repo.clone_from(git_url, repo_dir) 

def load_repositories():
    f = open(PATH_REPOSITORIES,mode="r",encoding="utf-8")

    d={}
    for ligne in f.read().split("\n"):
        if ligne!='':
            valeurs = ligne.split("\t");
            nom_repo, url_repo = valeurs[0], valeurs[1]
            d[nom_repo] = url_repo
    return d
 

PATH_REPOSITORIES = "services/repositories.tsv"
d_repos = load_repositories()
