# nfl-schedule-scraper
## Description
During my internship at Zoomph, I took on the responsibility of scraping the 2023 NFL schedule to enhance their broadcast reports. The goal was to provide comprehensive broadcast information for each game, combining data from a JSON file containing the prospective schedule as of August 2023 with Zoomph's broadcast details. The result was the creation of detailed spreadsheets reflecting the scheduled events.

## Implementation
I successfully imported a JSON file containing the 2023 NFL schedule and integrated it with Zoomph's broadcast information. This process allowed me to generate spreadsheets that captured key details for each game, including location, parent channel, market, call sign, channel ID, start time, end time, sport, home team, and away team. By importing a new JSON file reflecting the latest changes to the NFL season schedule, the system automatically updates the existing data. This ensures that the generated spreadsheets are always up-to-date and accurately represent the current state of the schedule.

## Example Week


| Week | Location | Parent Channel  | Market | Call Sign  | Channel ID | Start Time  | End Time | Sport | Home Team  | Away Team |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1  | GEHA Field at Arrowhead Stadium, Kansas City, MO  | NBC  | Kansas City  | KSHB  | KSHB(NBC)-8223  | 2023-09-07 23:50:00  | 2023-09-08 03:50:00  | Football  | Kansas City Chiefs  | Detroit Lions  |
| 1  | GEHA Field at Arrowhead Stadium, Kansas City, MO  | NBC  | Detroit  | WDIV  | WDIV(NBC)-8288  | 2023-09-07 23:50:00  | 2023-09-08 03:50:00  | Football  | Kansas City Chiefs   | Detroit Lions  |
| 1  | Caesars Superdome, New Orleans, LA  | CBS  | New Orleans  | WWL | WWL(CBS)-8418  | 2023-09-10 16:30:00  | 2023-09-10 20:30:00  | Football  | New Orleans Saints  | Tennessee Titans  |
| 1  | Caesars Superdome, New Orleans, LA  | CBS  | Nashville  | WTVF  | WTVF(CBS)-8402 | 2023-09-10 16:30:00  | 2023-09-10 20:30:00  | Football  | New Orleans Saints  | Tennessee Titans  |
| 1  | Lucas Oil Stadium, Indianapolis, IN  | FOX  | Indianapolis  | WXIN  | WXIN(Fox)-8421  | 2023-09-10 16:30:00  | 2023-09-10 20:30:00  | Football  | Indianapolis Colts  | Jacksonville Jaguars  |
| 1  | Lucas Oil Stadium, Indianapolis, IN  | FOX  | Jacksonville  | WFOX  | WFOX(Fox)-442  | 2023-09-10 16:30:00  | 2023-09-10 20:30:00  | Football  | Indianapolis Colts  |  Jacksonville Jaguars  |
| 1  | U.S. Bank Stadium, Minneapolis, MN  | CBS | Minneapolis  | WCCO  | WCCO(CBS)-8276l  | 2023-09-10 16:30:00  | 2023-09-10 20:30:00  | Football  | Minnesota Vikings  |  Tampa Bay Buccaneers  |
| 1  | U.S. Bank Stadium, Minneapolis, MN  | CBS  | Tampa  | WTSP  | WTSP(CBS)-8127  | 2023-09-10 16:30:00  | 2023-09-10 20:30:00  | Football  | Minnesota Vikings  | Tampa Bay Buccaneers  |


