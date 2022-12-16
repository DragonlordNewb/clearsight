import os
import sys

dependencies = ["nltk", "--upgrade pip", "blessed"]
nltkPackages = ["punkt", "omw-1.4", "averaged_perceptron_tagger", "wordnet", "opinion_lexicon"]

def installPackage(pkg):
    print("[clearsight_3.packages] Installing package \"" + pkg + "\" ...", end="")
    sys.stdout.flush()
    out = os.system("py -m pip install " + pkg + " -q --no-warn-script-location")
    if not out:
        print("done.")
        return True
    out = os.system("python3 -m pip install " + pkg + " -q --no-warn-script-location")
    if not out:
        print("done.")
        return True
    out = os.system("pip install " + pkg + "")
    if not out:
        print("done.")
        return True
    print("failed.")
    return False

def installNLTKData(name):
    import nltk
    nltk.download(name)

def installDependencies():
    for pkg in dependencies:
        installPackage(pkg)
    for data in nltkPackages:
        installNLTKData(data)
