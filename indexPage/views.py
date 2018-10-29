from django.shortcuts import render
# Create your views here.
from github import Github
import numpy as np
from indexPage.models import repo
def getGitRepos():
    g = Github("4b7caf300a3e3afaade1d62a467bb6649d2adfb5")
    return g.get_user("furkankykc").get_repos() 
def getRepos():
	return repo.objects.all()
def saveRepos():
	go = getGitRepos()
	repo.objects.all().delete()
	for r in go:
		if r.language is not None:
			instance = repo.objects.create(name=r.name,lang=r.language)
			instance.save()
def runIndex(request):
    repos = getRepos()
    uniqueLangs = []
    uniqueLangs = ([x.lang.replace('#','s').replace('+','p') for x in repos])
    uniqueLangs = np.unique(uniqueLangs)
    print (uniqueLangs)
    uniqueLangs=np.array(uniqueLangs)
    for repo in repos:
        repo.myimage = None
        try:
            repo.myimage = (repo.get_file_contents("/screenshot/fav.png").download_url)
            #repo.myimage = (repo.get_file_contents("/outputs/ex1.png").download_url)
        except:
            repo.myimage = "static/img/github.png"
            #repo.myimage = "https://raw.githubusercontent.com/furkankykc/MarketPlacePredictor/master/outputs/ex1.png"

    myimage= "https://raw.githubusercontent.com/furkankykc/MarketPlacePredictor/master/outputs/ex1.png"
    return render(request, 'index.html', {"projects":repos, "langs":uniqueLangs, "myimage":myimage})
    #return render(request,'index.html')
