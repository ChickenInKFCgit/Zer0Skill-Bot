# Zer0Skill 
Zer0 est un bot discord, qui a pour utilité de relier différents projets réalisés précédemment comme :

- Flaggergaster
- AnnoyingText
- (autres)

Ces projets sont reliés via le module GitPython (et sont ici appellés _services_).
Chacun de ces projets correspond en réalité à un clone du repository du projet associé.
Figurent ci-dessous les commandes associées :
| Commande                | Description     |
| ----------------------- | --------------- |
| /services_introuvables  | Donne la liste de tous les services qui n'ont pas pu être lancés.    | 
| /services_obtain  | Charge tous les services introuvables depuis github. Requiert un redémarrage pour prendre effet. (_correspond à une série de clone_)  | 
| /services_update  | Met à jour chacun des services à la version disponible sur github. (_correspond à une série de pull_)  | 
| /restart  | pour redémarrer le bot afin d'actualiser les nouveaux services clonés   | 
| /services_force  | /service_obtain → /service_update → /restart (_permet d'assurer la bonne mise à jour des services_)  | 

Ce projet a une structure modulaire, avec comme entry point [bot.py](link:bot/bot.py)

Permet d'exécuter plusieurs actions reliées à ces programmes via des commandes, telles que :

- text-randomize pour appliquer la fonction d'AnnoyingText sur un texte choisi
- scrapper-dashboard pour afficher la dashboard du scrapper, donc analyser les résultats, relancer une recherche, récupérer la sélection, etc
