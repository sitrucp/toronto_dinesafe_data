# toronto_dinesafe_data
The City of Toronto’s open data site includes the results of the city’s Dine Safe restaurant inspections. 

Data is available in XML format. This project converts XML data to CSV format and transform for use in Tableau visualization.

dinesafe_csv_geocode.py 
Used to geocode the dinesafe addresses to get lat and lon. This uses MapQuest's open Nominatim server. This free service has daily record limits. This code creates cache so code can be run on successive days to geocode large datasets over a period of days. Can set up as cron job etc.

dinesafe_explore_xml.py
Just used to quickly view selected XML elements

dinesafe_xml_to_csv.py
Converts Dinesafe data from XML to CSV format for use in Tableau visualizations.

dinesafe_word_freq.py
Create tokens from Dinesafe data citation descriptions for word frequency analysis.

Read blog post for more details https://009co.com/?p=146
