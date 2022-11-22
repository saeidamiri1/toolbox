def find_null(df):
    return(df[pd.isnull(df).any(axis=1)])

def split_colum(df,X,sep="_"):
# split a column into two columns
    return(df[[f'{X}_f',f'{X}_l']] = df.X.apply(lambda x: pd.Series(str(x).split(sep))))

def select_column_loc(df, in='B|A')
    return(run_cols = df.columns.str.contains( in, case=False)


def select_column(df, in_col=0:2 in='B|A')
    location_cols=[:, lambda df: df.columns.str.contains(in,case=False)]
    location_indi =[i for i, col in enumerate(location_cols) if col]
    return(df.iloc[:, np.r_[in_col,location_indi]])

def dollarizer_df(X): 
    df[X] = df[X].str.replace('$','').astype('float')


def column_list(): 
    col_mapping = [f"{c[0]}:{c[1]}" for c in enumerate(df.columns)]
    col_mapping_dict = {c[0]:c[1] for c in enumerate(df.columns)}
    return(col_mapping,col_mapping_dict )
