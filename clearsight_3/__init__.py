print("[clearsight_3] Loading ...")

import time

print("  Importing interface ...")
from clearsight_3 import interface
print("  Importing misc ...")
from clearsight_3 import misc
print("  Importing packages ...")
from clearsight_3 import packages
print("  Importing patternmatching ...")
from clearsight_3 import patternmatching
# print("  Importing tokenization ...")
# from clearsight_3 import tokenization
print("  Importing datasets ...")
from clearsight_3 import datasets

packages.installDependencies()

try:
    patternmatching.unittest_numericalMatching()
    patternmatching.unittest_naturalLanguageMatching_1()
    patternmatching.unittest_superintelligence()
except AssertionError:
    print("[clearsight_3] Unit test failure; please note that this may be indicative of future performance.")
except Exception as e:
    raise e

print("[clearsight_3] Done.")
