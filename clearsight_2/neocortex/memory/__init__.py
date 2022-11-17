import os

cacheDirectory = os.getcwd() + "/clearsight_2/neocortex/memory/"
currentMemoryCacheName = None

def loadMemoryCache(mcid):
    global cacheDirectory
    global currentMemoryCacheName

    if os.path.exists(cacheDirectory + mcid + "/key.mek"):
        currentMemoryCacheName = mcid + "/"
    else:
        print("No such memory cache with name \"" + str(mcid) + "\" (not exists " + str(cacheDirectory + mcid + "/key.mek") + ").")

def commit(filename, data):
    try:
        if os.path.exists(cacheDirectory + currentMemoryCacheName + filename + ".mem"):
            with open(cacheDirectory + currentMemoryCacheName + filename + ".mem", "a") as f:
                f.write("\n")
                f.write(data)
                return True
        else:
            with open(cacheDirectory + currentMemoryCacheName + filename + ".mem", "w") as f:
                f.write(data)
                return False

    except FileExistsError:
        with open(cacheDirectory + currentMemoryCacheName + filename + ".mem", "a") as f:
            f.write("\n")
            f.write(data)
            return FileExistsError

    except FileNotFoundError:
        with open(cacheDirectory + currentMemoryCacheName + filename + ".mem", "w") as f:
            f.write(data)
            return FileNotFoundError

    except TypeError:
        print("No memory cache loaded.")
        return None

    except Exception as e:
        raise e

def remember(data):
    locatedContent = {}
    for root, dirs, files in os.walk(cacheDirectory + currentMemoryCacheName, topdown=False):
       for name in files:
          path = os.path.join(root, name)
          with open(path, "r") as f:
              content = f.read()
              if data in content:
                  if name not in locatedContent.keys():
                      locatedContent.keys = []
                  locatedContent[name].append(data)
    return locatedContent
