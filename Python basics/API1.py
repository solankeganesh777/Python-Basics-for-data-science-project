#API

#REST API Basic

#Install API for NBA.com
!pip install nba_api

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict    

print("\n")
#Pandas as an API
import pandas as pd
import matplotlib.pyplot as plt

a={'a':[11,21,31],'b':[12,26,32]}
df=pd.DataFrame(a)
print(df)
print(type(df))
print(df.head())
print(df.mean())


print("\n")
#REST APIs

"""
In the nba api to make a request for a specific team,
it's quite simple, we don't require a JSON all we require is an id. 
This information is stored locally in the API we import the module teams
"""
from nba_api.stats.static import teams
nba_teams=teams.get_teams()
print(nba_teams[0:4])
print(type(nba_teams))

#Convert dictionary into dataframe
dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)
print(df_teams.head())

print("\n")
df_warriors=df_teams[df_teams['nickname']=='Warriors']
df_warriors

war_id=df_warriors[['id']].values[0][0]
print(war_id)

#The function "League Game Finder " will make an API call, its in the module stats.endpoints
from nba_api.stats.endpoints import leaguegamefinder

#The information requested is provided and is transmitted via an HTTP response this is assigned to the object gamefinder
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=war_id)

#we can see the json file by running the following line of code.
gamefinder.get_json()

#The game finder object has a method get_data_frames(), that returns a dataframe
games = gamefinder.get_data_frames()[0]
games.head()

#download the dataframe from the API call for Golden State and run the rest like a video
! wget https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl
    
file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
games.head()
    
#We can create two dataframes,
#one for the games that the Warriors faced the raptors at home and the second for away games.    
games_home=games [games ['MATCHUP']=='GSW vs. TOR']
games_away=games [games ['MATCHUP']=='GSW @ TOR']

#Calculate the mean for the columns
games_home.mean()['PLUS_MINUS']
games_away.mean()['PLUS_MINUS']

#plot out the PLUS MINUS column for for the dataframes games_home and  games_away
fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()
