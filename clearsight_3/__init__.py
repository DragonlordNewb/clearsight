print("[clearsight_3] Loading ...")

print("  Importing misc ...")
from clearsight_3 import misc
print("  Importing packages ...")
from clearsight_3 import packages
print("  Importing patternmatching ...")
from clearsight_3 import patternmatching
print("  Importing tokenization ...")
from clearsight_3 import tokenization
print("  Importing datasets ...")
from clearsight_3 import datasets

packages.installDependencies()

patternmatching.unittest_numericalMatching()
patternmatching.unittest_naturalLanguageMatching_1()

print("[clearsight_3] Done.")