"""
Checkpoint 1b

*First complete the steps in checkpoint1a.pdf

Here you will create a script to preprocess the data given in starbucks.csv. You may want to use
a jupyter notebook or python terminal to develop your code and test each function as you go... 
you can import this file and its functions directly:

    - jupyter notebook: include the lines `%autoreload 2` and `import preprocess`
                        then just call preprocess.remove_percents(df) to test
                        
    - python terminal: run `from importlib import reload` and `import preprocess`
                       each time you modify this file, run `reload(preprocess)`

Once you are finished with this program, you should run `python preprocess.py` from the terminal.
This should load the data, perform preprocessing, and save the output to the data folder.

"""

def remove_percents(df, col):
    df[col].replace('%','',regex=True,inplace=True)
    return df

def fill_zero_iron(df):
    df.fillna(0,inplace=True)
    return df
    
def fix_caffeine(df):
    df_1 = df[df['Caffeine (mg)'] != 'Varies']
    df_2 = df_1[df_1['Caffeine (mg)'] != 'varies']
    df_3 = df_2[df_2['Caffeine (mg)'] != 'nan']
    median_replace= df_3['Caffeine (mg)'].median()
    df['Caffeine (mg)'].replace(['Varies','vaires','nan'],median_replace,inplace=True)
    
    return df

def standardize_names(df):
    df.columns= ['beverage category', 'beverage', 'beverage prep', 'calories',
       'total fat', 'trans fat', 'saturated fat', 'sodium',
       'total carbohydrates', 'cholesterol', 'dietary fiber',
       'sugars', 'protein', 'vitamin a', 'vitamin c',
       'calcium', 'iron', 'caffeine']
    return df

def fix_strings(df, col):
    df[col].replace('[^A-Za-z0-9 ]+','',regex=True,inplace=True)
    return df


def main():
    
    # first, read in the raw data
    import pandas as pd
    df = pd.read_csv('/Users/Chris/Documents/00.Data_science/00.MADS/git_MDST/data/starbucks.csv')
    
    # the columns below represent percent daily value and are stored as strings with a percent sign, e.g. '0%'
    # complete the remove_percents function to remove the percent symbol and convert the columns to a numeric type
    pct_DV = ['Vitamin A (% DV)', 'Vitamin C (% DV)', 'Calcium (% DV)', 'Iron (% DV)']
    for col in pct_DV:
        df = remove_percents(df, col)
    
    # the column 'Iron (% DV)' has missing values when the drink has no iron
    # complete the fill_zero_iron function to fix this
    df = fill_zero_iron(df)

    # the column 'Caffeine (mg)' has some missing values and some 'varies' values
    # complete the fix_caffeine function to deal with these values
    # note: you may choose to fill in the values with the mean/median, or drop those values, etc.
    df = fix_caffeine(df)
    
    # the columns below are string columns... starbucks being starbucks there are some fancy characters and symbols in their names
    # complete the fix_strings function to convert these strings to lowercase and remove non-alphabet characters
    names = ['Beverage_category', 'Beverage']
    for col in names:
        df = fix_strings(df, col)
    
    # the column names in this data are clear but inconsistent
    # complete the standardize_names function to convert all column names to lower case and remove the units (in parentheses)
    df = standardize_names(df)
    
    # now that the data is all clean, save your output to the `data` folder as 'starbucks_clean.csv'
    # you will use this file in checkpoint 2
    df.to_csv('/Users/Chris/Documents/00.Data_science/00.MADS/git_MDST/data/starbucks_clean.csv')
    

if __name__ == "__main__":
    main()
