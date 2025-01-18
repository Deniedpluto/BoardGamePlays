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
# challenges = polars.DataFrame(challenges).unnest('challenges')

# Pull out subtables
gameCopies = games.get_column('copies').explode()
gameTags = games.get_column('tags').explode()
playScores = plays.get_column('playerScores').explode()

# Convert subtables to tables
gameCopies = polars.DataFrame(gameCopies).unnest('copies')
gameTags = polars.DataFrame(gameTags).unnest('tags')
playScores = polars.DataFrame(playScores).unnest('playerScores')

# Drop subtable columns
games.drop('copies', 'tags')
plays.drop('playerScores')

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