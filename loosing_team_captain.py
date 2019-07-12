# %%
teams = [['Paul', 'John', 'Ringo', 'George']]

#%%
def losing_team_captain(teams):
    losing_team = teams[len(teams) -1 ]

    captain = losing_team[1]

    return captain

#%%
print(losing_team_captain(teams))
