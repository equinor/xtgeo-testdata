#!/usr/bin/env python
import sys
import pandas as pd
import xtgeo

efile = sys.argv[1]

print("Efile is ", efile)

df = xtgeo.grid3d.GridProperties.scan_keywords(efile, dataframe=True,
                                               dates=True)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)
