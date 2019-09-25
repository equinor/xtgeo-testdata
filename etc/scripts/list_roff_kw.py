#!/usr/bin/env python
import sys
import pandas as pd
import xtgeo

rfile = sys.argv[1]

print("Roff file is ", rfile)

df = xtgeo.grid3d.GridProperties.scan_keywords(rfile, dataframe=True,
                                               fformat='roff')

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)
