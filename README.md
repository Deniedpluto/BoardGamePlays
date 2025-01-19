# BoardGamePlays

## Overview
The data for this project comes from [BG Stats app](https://www.bgstatsapp.com/).

### Key Files
1. BGStatsExport.json - an export from the BG Stats app.
2. Manual Coop Overwrite - a csv file for overwriting the base 50% win rate assumed by BG Stats app for calculating expected win rates.
3. Play History.pbix - A Power BI file that uses both of the above files as sources.
4. BGStatsParser.py - A python script for parsing the json export and converting it into normalized tables in parquet and csv*.

*The csv export currently does not handle newlines in comments.

Boardgame Stats ERD shows the data model in Power BI.

## How to Use This Project

### Without Python
To use this project without Python, do the following steps:
1. Download the Power BI file and the Manual Coop Overwrite.
2. Export you data from the BG Stats app and save it in the same folder as the Manual Coop Overwrite. Name it BGStatsExport.json
3. In Power BI, click transform data top open the Power Query Editor.
4. Find the FileLocation parameter and update it to the path of the folder you saved your BG Stats Export file.
5. Update the Manual Coop Overwrite with what you want to use for your expected win rates for coop games.

### With Python
To use this with Python, do the following steps:
1. Download the BGStatsParser.py python script.
2. Export you data from the BG Stats app and save it in the same folder as the python script. Name it BGStatsExport.json
3. Create two subfolders where you saved the python script called ParquetFiles and CSVFiles.
4. Run the python script *requires [Polars](https://docs.pola.rs)
