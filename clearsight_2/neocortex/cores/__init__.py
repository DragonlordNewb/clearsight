from clearsight_2.neocortex.cores import dataacquisition
from clearsight_2.neocortex.cores import test

coresById = {
    "dataacquisition": dataacquisition,
    "test": test
}

currentCore = None

def loadCore(cid):
    global currentCore
    global coresById

    if cid in coresById.keys():
        currentCore = coresById[cid]
    else:
        print("No such core with ID \"" + str(cid) + "\".")
