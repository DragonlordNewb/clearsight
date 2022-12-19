print("[clearsight_3] Loading ...")

import time
import psutil

st = time.time()

print("  Importing packages ...")
from clearsight_3 import packages
packages.installDependencies()
print("  Importing interface ...")
from clearsight_3 import interface
print("  Importing misc ...")
from clearsight_3 import misc
print("  Importing patternmatching ...")
from clearsight_3 import patternmatching
print("  Importing datasets ...")
from clearsight_3 import datasets
print("  Importing states ...")
from clearsight_3 import states
print("  Importing memory ...")
from clearsight_3 import memory
print("  Importing unification ...")
from clearsight_3 import unification
print("  Importing vocaloid ...")
from clearsight_3 import vocaloid

try:
    patternmatching.unittest_numericalMatching()
    patternmatching.unittest_naturalLanguageMatching_1()
    patternmatching.unittest_superintelligence()
except AssertionError:
    print("[clearsight_3] Unit test failure; please note that this may be indicative of future performance.")
except Exception as e:
    raise e

et = time.time()

print("[clearsight_3] Done.")
print("  Consumed memory starting up: " + str(round(psutil.virtual_memory()[3]/1000000000, 3)) + " GB")
print("  Startup time: " + str(round(et - st, 2)) + " seconds")

def initialize():
    pass