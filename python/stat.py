"""
Compute the chi-squared
"""

import pandas as pd
from scipy.stats import chi2_contingency

def chisq_test(x_in,y_in):
    if (x_in.dtype!='O'):
       x_in=x_in.apply(str)
    elif (y_in.dtype!='O'):
      y_in=y_in.apply(str)
    tab =pd.crosstab(x_in,y_in)
    stat, p, dof, expected = chi2_contingency(tab)
    print('Pearsons\' Chi-squared test with Yates\' continuity correction')
    print('Data: %s,%s' % (x_in.name, y_in.name))
    print('X-squared =%.3f, df=%.3f, p-value=%.3f' % (stat, dof, p))

import numpy as np
def outliers(df, threshold, columns):
    for col in columns: 
        mask = df[col] > float(threshold)*df[col].std()+df[col].mean()
        df.loc[mask == True,col] = np.nan
        mean_property = df.loc[:,col].mean()
        df.loc[mask == True,col] = mean_property
    return df

def freq(x,n): 
    from collections import Counter
    c=Counter(x)
    c.most_common(n)