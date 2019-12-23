# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 11:37:10 2019

@author: Ken
"""


#Things you need: Player & Team IDs

#eswan18

# find player Ids 
from nba_api.stats.static import players
player_dict = players.get_players()

# Use ternary operator or write function 
bron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
bron_id = bron['id']

# find team Ids
from nba_api.stats.static import teams 
teams = teams.get_teams()
GSW = [x for x in teams if x['full_name'] == 'Golden State Warriors'][0]
GSW_id = GSW['id']

#game_stats_player
#could not get DateFrom to work, just use loop with years if necessary 
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playergamelog
import pandas as pd 

gamelog_bron = playergamelog.PlayerGameLog(player_id='2544', season = '2018')
df_bron_games_2018 = gamelog_bron.get_data_frames()

gamelog_bron_all = playergamelog.PlayerGameLog(player_id='2544', season = SeasonAll.all)
df_bron_games_all = gamelog_bron_all.get_data_frames()

#find games played by a team or player
from nba_api.stats.endpoints import leaguegamefinder
GSW_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=GSW_id).get_data_frames()[0]

# game play by play data 
from nba_api.stats.endpoints import playbyplay
pbp = playbyplay.PlayByPlay('0021900429').get_data_frames()[0]





