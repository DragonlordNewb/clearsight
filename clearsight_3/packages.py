import os
import sys

dependencies = ["nltk", "--upgrade pip"]

def installPackage(pkg):
    print("[clearsight_3.packages] Installing package \"" + pkg + "\" ...", end="")
    sys.stdout.flush()
    out = os.system("python3 -m pip install " + pkg + " -q --no-warn-script-location")
    if not out:
        print("done.")
        return True
    out = os.system("py -m pip install " + pkg + " -q --no-warn-script-location")
    if not out:
        print("done.")
        return True
    out = os.system("pip install " + pkg + "")
    if not out:
        print("done.")
        return True
    print("failed.")
    return False

def installDependencies():
    for pkg in dependencies:
        installPackage(pkg)
