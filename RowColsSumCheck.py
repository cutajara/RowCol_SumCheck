# Fusion File Checking: Checks Dataframe from any Rows or Columns that are empty

def RowColCheck(df):
    # Check each row has data
    for i in range(0, df.shape[0]):
        if sum(df.iloc[i,:].values.tolist()) == 0:
            print("Warning, Zero Sum Respondnet: " + str(df.index[i]))
            
    # Check each column has data
    colx = df.columns
    for i in range(0, df.shape[1]):
        if sum(df.iloc[:,i].values.tolist()) == 0:
            print("Warning, Zero Sum Column: " + str(df.columns[i]))
            
            
RowColCheck(df)
