"""This script uses my 'sng' package to create a machine learning model.

It will then be hosted as an API via the `05_ML-model-API.py` script.

The script will save its output, the folder `model`.

I committed the files to the repository, so it's not necessary to run
this script. It would take a few minutes.
"""

import sng

cfg = sng.Config(
    epochs=500
)

wordlist = sng.load_builtin_wordlist('gallic.txt')

gen = sng.Generator(wordlist=wordlist, config=cfg)
gen.fit()
gen.simulate(n=4)
gen.save('model', overwrite=True)
