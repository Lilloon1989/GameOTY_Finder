#Dictionary Training
#Game of the year information
#what year they won/Name of game/Dev/Pub/NA Release Date
#ex. 2014/Dragon Age/Inquisition/Bioware/Electronic Arts/November 18, 2014
import pandas as pd

GotyData = pd.read_excel('Game of the year.xlsx')
df = GotyData

def GOTY_Finder():
    u_year = int(input("enter the year and ill tell you who won Game of the Year! (2014 - present)" ))
    if u_year < 2014:
        print("Sorry, The Gaming Award started in 2014. Select a year 2014 and above.")
        GOTY_Finder()        
    for i in range(len(df)):
        if df.iloc[i,0] == u_year:
            result =df.iloc[[i]]
            print(result.to_string(index=False))
            break

GOTY_Finder()