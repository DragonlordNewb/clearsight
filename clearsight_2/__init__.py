# Copyright 2022-2023 Lux Bodell
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

print("Installing packages ... (1/2)", end="")
sys.stdout.flush()
os.system("pip install nltk -q -q")
print("\rInstalling packages ... (2/2)")
sys.stdout.flush()
os.system("pip install blessed -q -q")
print("Downloading NLTK packages ...")
import nltk 
nltk.download("omw-1.4")
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

from clearsight_2 import neocortex
from clearsight_2 import states
from clearsight_2 import utils
from blessed import Terminal

term = Terminal()

def initialize():
    print(term.clear())
    print("".join(["\n" for x in range(term.height)]))
    print(term.center("Clearsight-2 Artificial General Intelligence Engine"))
    print(term.center("Connection will now begin."))
    print("".join(["_" for x in range(term.width)]) + "\n")

    while True:

        user = input("<User> ")

        if user[:16] == "system command: ":
            cmd = user[16:].split(" ")
            if cmd[0] in ["exit", "terminate"]:
                print("Are you sure you want to terminate the Clearsight-2 connection? (y/n)")
                while True:
                    with term.cbreak(), term.hidden_cursor():
                        k = term.inkey()
                    if k == "y":
                        exit()
                    elif k == "n":
                        break
            elif cmd[0] == "load":
                if cmd[1] == "core":
                    neocortex.cores.loadCore(cmd[2])
                elif cmd[1] in ["mc", "memorycache", "memory"]:
                    neocortex.memory.loadMemoryCache(cmd[2])

            elif cmd[0] == "run":
                if cmd[1] in ["sr", "subroutine"]:
                    if cmd[2] == "1":
                        neocortex.cores.loadCore("dataacquisition")
                        neocortex.memory.loadMemoryCache("main")
                        neocortex.memory.eraseMemoryFile("MAIN")

        else:
            if neocortex.cores.currentCore == None:
                print("<Clearsight-2> ... [no core loaded]")
            else:
                print("<Clearsight-2> " + str(neocortex.feed(user)))
