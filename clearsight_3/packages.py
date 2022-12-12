import os 

dependencies = []

def installPackage(pkg):
    print("[clearsight_3.packages] Installing package \"" + pkg + "\" ...", end="")
    out = os.system("py -m pip install " + pkg + " -q --no-warn-script-location")
    if not out:
        return True
        print("done.")
    out = os.system("python3 -m pip install " + pkg + " -q --no-warn-script-location")
    if not out:
        return True
        print("done.")
    out = os.system("pip install " + pkg + "")
    if not out:
        return True
        print("done.")
    print("failed.")
    return False

def installDependencies():
    for pkg in dependencies:
        installPackage(pkg)