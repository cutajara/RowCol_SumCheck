# Fusion File Checking: Checks Dataframe from any Rows or Columns that are empty

def RowColCheck(df):
    zerosrows = (df.sum(axis=1)==0)[(df.sum(axis=1)==0) == True] # Rows that sum == 0 
    if len(zerosrows) > 0: # If there are rows that sum == 0
        print("Warning, Zero Sum Respondnet:")
        print(zerosrows) # Print rows that sum == 0
    
    zeroscols = (df.sum(axis=0)==0)[(df.sum(axis=0)==0) == True] # Columns that sum == 0
    if len(zeroscols) > 0: # If there are columns that sum == 0
        print("Warning, Zero Sum Column:")
        print(zeroscols) # Print columns that sum == 0
            
           
