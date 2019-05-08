import pandas as pd
import pprint

df_fixtures = pd.read_csv('short_league_fixtures.csv')
df_table = pd.read_csv('short_league_table.csv')

#Add new column to check team that won, value is 1 if home team won, 0 if tie, -1 if away team won
import numpy as np

#Remove rows of matches that haven't occured yet
df_fixtures = df_fixtures[df_fixtures.events__homeScore != 'null']
#Merge home team stats to fixtures
df_final = pd.merge(df_fixtures, df_table, how='inner', left_on = 'events__homeTeam__name', right_on = 'teamName')
#Merge away team stats to fixtures
df_final = pd.merge(df_final, df_table, how='inner', left_on = 'events__awayTeam__name', right_on = 'teamName', suffixes = ('_homeTeam','_awayTeam'))

#Small function that determines winner
def setWinner(row):
    if(row['events__homeScore'] > row['events__awayScore']):
        return 1
    elif(row['events__homeScore'] == row['events__awayScore']):
        return 0
    else:
        return -1
    
#Apply function to DataFrame
df_final.apply(lambda row: setWinner(row), axis=1)
#New column winner created
df_final['winner'] = df_final.apply(lambda row: setWinner(row), axis=1)

#Remove unnecessary columns
df_final = df_final.drop(['roundNumber', 'events__startTime', 'events__startTimestamp', 'events__matchID', 'events__timeLive', 'events__homeTeam__name', 'events__homeTeam__teamID', 'events__awayTeam__name', 'events__awayTeam__teamID', 'teamID_homeTeam', 'teamID_awayTeam'], axis=1)

#Remove goal scores
df_final = df_final.drop(['events__homeScore', 'events__awayScore'], axis=1)

#Convert team names to categories and then to unique IDs to keep track of them
df_final['teamName_homeTeam'] = df_final['teamName_homeTeam'].astype('category')
df_final['teamName_awayTeam'] = df_final['teamName_awayTeam'].astype('category')
cat_columns = df_final.select_dtypes(['category']).columns

#Create categoryTeamDict to keep track of team names after they are switched to id's
categoryTeamDict = dict( enumerate(df_final['teamName_homeTeam'].cat.categories))

#Replace team names with id's
df_final[cat_columns] = df_final[cat_columns].apply(lambda x: x.cat.codes)

from sklearn.model_selection import train_test_split
X = df_final.drop('winner', axis=1)
y = df_final['winner']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()
dtree.fit(X_train,y_train)

predictions = dtree.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix
##print(classification_report(y_test,predictions))
##print(confusion_matrix(y_test,predictions))

#Expect two strings
def whoWins(homeTeam, awayTeam): 
    #Get home team stats to fixtures
    df_home = df_table.loc[df_table['teamName'] == homeTeam]
    df_home = df_home.add_suffix('_homeTeam')
    #Get away team stats to fixtures
    df_away = df_table.loc[df_table['teamName'] == awayTeam]
    df_away = df_away.add_suffix('_awayTeam')

    df_awayDict = df_away.to_dict()
    awaySmallDict = df_awayDict['teamName_awayTeam']
    awayIndex = 0
    for key, value in awaySmallDict.items():
        awayIndex = key
    print(df_awayDict)
    for key, value in df_awayDict.items():
        df_home[key] = value[awayIndex]
    #Remove unneeded columns
    df_home = df_home.drop(['teamID_homeTeam', 'teamID_awayTeam'], axis=1)
    df_home['teamName_homeTeam'] = pd.to_numeric(df_home['teamName_homeTeam'], errors='coerce')
    df_home['teamName_awayTeam'] = pd.to_numeric(df_home['teamName_awayTeam'], errors='coerce')
    print(df_home)
    for number, teamName in categoryTeamDict.items():
        if(teamName == homeTeam):
            df_home.set_value(df_home['positionOverall_homeTeam'].values[0]-1, 'teamName_homeTeam', int(number))
        if(teamName == awayTeam):
            df_home.set_value(df_home['positionOverall_homeTeam'].values[0]-1, 'teamName_awayTeam', int(number))
    #Calculate winner
    winner = dtree.predict(df_home)
    return {'homeTeam':homeTeam, 'awayTeam': awayTeam, 'matchResult': int(winner[0])}

result = whoWins('Southampton', 'Fulham')
print(result['matchResult'])
