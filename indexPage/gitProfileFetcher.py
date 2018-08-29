from github import Github





def getRepos():
    g = Github("4b7caf300a3e3afaade1d62a467bb6649d2adfb5")
    return g.get_user().get_repos()


g = Github("4b7caf300a3e3afaade1d62a467bb6649d2adfb5")
for repo in g.get_user("furkankykc").get_repos():
    if(repo.name == "MarketPlacePredictor"):
        print(repo.get_file_contents("/outputs/ex1.png").download_url)
