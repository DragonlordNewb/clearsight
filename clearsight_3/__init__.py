from clearsight_3 import misc
from clearsight_3 import packages
from clearsight_3 import patternmatching
from clearsight_3 import tokenization
from clearsight_3 import datasets

packages.installDependencies()

patternmatching.unittest_numericalMatching()
patternmatching.unittest_naturalLanguageMatching_1()
