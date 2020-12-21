from typing import TextIO

from pcfg import PCFG
import os

BASEPATH: str = os.path.dirname(__file__)

f: TextIO
with open(os.path.join(BASEPATH, "swedish_grammar.txt")) as f:
    pcfg: PCFG = PCFG.fromstring(f.read())

n: int = int(input("How many sentences do you want generated? "))
sentence: str
for sentence in pcfg.generate(n):
    print()
    print(sentence.capitalize())