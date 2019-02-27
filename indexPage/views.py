from django.shortcuts import render
# Create your views here.
from github import Github
import numpy as np
from indexPage.models import repo
import urllib.request
import shutil

def getGitRepos():
    g = Github()
    return g.get_user("furkankykc").get_repos()


def getRepos():
    return repo.objects.all()


def saveRepos():
    go = getGitRepos()
    repo.objects.all().delete()
    for r in go:
        if r.language is not None:
            instance = repo.objects.create(name=r.name, lang=r.language)
            print(instance.name,'created ')
            try:
                picture = urllib.request.urlretrieve(r.get_file_contents("/test-output/picture.png").download_url,"static/img/projects/"+r.name+".png")
                instance.picture = "static/img/projects/"+r.name+".png"

                print(instance.picture)
                # picture = urllib.request.urlretrieve(r.get_file_contents("/screenshots/splash.png").download_url,"static/img/projects/"+r.name+".png")
            except Exception as ex:
                print(ex)
                picture = "static/img/github.png"
                instance.picture = picture
                # shutil.copy2("static/img/projects/"+r.name+".png",picture ,follow_symlinks=True)
            instance.save()


def runIndex(request):
    repos = getRepos()
    uniqueLangs = []
    uniqueLangs = ([x.lang.replace('#', 's').replace('+', 'p') for x in repos])
    uniqueLangs = np.unique(uniqueLangs)
    print(uniqueLangs)
    uniqueLangs = np.array(uniqueLangs)
    # for repo in repos:
    #     repo.myimage = None
    #     try:
    #         repo.myimage = "static/img/projects"+repo.name+".png"
    #         # repo.myimage = (repo.get_file_contents("/outputs/ex1.png").download_url)
    #     except:
    #         repo.myimage = "static/img/github.png"
    #         # repo.myimage = "https://raw.githubusercontent.com/furkankykc/MarketPlacePredictor/master/outputs/ex1.png"

    # myimage = "https://raw.githubusercontent.com/furkankykc/MarketPlacePredictor/master/outputs/ex1.png"
    return render(request, 'index.html', {"projects": repos, "langs": uniqueLangs})
    # return render(request,'index.html')
