import polars
import fsspec

# Load in the json data
base_df = polars.read_json("BGStatsExport.json")

# Split the data into each of the subgroups
tags = base_df["tags"].explode()
groups = base_df["groups"].explode()
games = base_df["games"].explode()
players = base_df["players"].explode()
locations = base_df["locations"].explode()
plays = base_df["plays"].explode()
# challenges = base_df["challenges"].explode()
# deletedObjects = 
# userInfo = 

# Convert json structs to tables
tags = polars.DataFrame(tags).unnest('tags')
groups = polars.DataFrame(groups).unnest('groups')
games = polars.DataFrame(games).unnest('games')
players = polars.DataFrame(players).unnest('players')
locations = polars.DataFrame(locations).unnest('locations')
plays = polars.DataFrame(plays).unnest('plays')
# challenges = polars.DataFramgamee(challenges).unnest('challenges')

# Pull out subtables
gameCopies = games.select(polars.col(['uuid', 'copies']))
gameTags = games.select(polars.col(['uuid', 'tags']))
playScores = plays.select(polars.col(['uuid', 'playerScores']))

# Explode the subitems
gameCopies = gameCopies.explode('copies')
gameTags = gameTags.explode('tags')
playScores = playScores.explode('playerScores')

# Change uuid column name since copies also has a uuid column and the unnest breaks if it is not changed
gameCopies = gameCopies.rename({'uuid': 'game uuid'})

# Convert subtables to tables
gameCopies = gameCopies.unnest('copies')
gameTags = gameTags.unnest('tags')
playScores = playScores.unnest('playerScores')

# Drop subtable columns
games = games.drop('copies', 'tags')
plays = plays.drop('playerScores')

# Write out the data!
tags.write_parquet("DIM_Tags.parquet")
groups.write_parquet("DIM_Groups.parquet")
games.write_parquet("DIM_Games.parquet")
players.write_parquet("DIM_Players.parquet")
locations.write_parquet("DIM_Locations.parquet")
plays.write_parquet("FACT_Plays.parquet")
gameCopies.write_parquet("DIM_Game_Copies.parquet")
gameTags.write_parquet("DIM_Game_Tags.parquet")
playScores.write_parquet("FACT_Play_Scores.parquet")