# Makes the Isochrone Files
from spisea import IsochroneMakerReformattedVersion2
from spisea.IsochroneMakerReformattedVersion2 import extractorO, reformatterO
from spisea import IsochroneMakerReformattedVersionNew
from spisea.IsochroneMakerReformattedVersionNew import reformatter, extractor
import time
import math
import sys
def main():
    fit_dirO = sys.argv[1]
    fit_dir = sys.argv[2]
    iso_dirO = sys.argv[3]
    iso_dir = sys.argv[4]
    # Note: O exists in order to confuse between the extractors and reformatters
    # from the two functions
    # O stands for old
    reformatterO(fit_dirO, ["z020"])
    reformatter(fit_dir, ["z020"])
    for x in range(30):
        t1 = time.time()
        extractorO(round(7.0 + 0.1 * x,1),"z020", fit_dirO,
                   iso_dirO, 0.05)
        t2 = time.time()
        print(t2 - t1)
    print("Begin New Method")
    for x in range(30):
        t1 = time.time()
        extractor(round(7.0 + 0.1 * x,1),"z020",fit_dir, iso_dir, 0.05)
        t2 = time.time()
        print(t2 - t1)
if __name__ == '__main__':
    main()