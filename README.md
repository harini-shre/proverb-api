# Proverbb API
### Proverbs for life

This is an app that consists of API (Application Programming Interface) to access proverbs.
You can serach a proverb by and their URLS:
- Read a Random Provern - /Random_Proverb
- Search the proverbs written by an Author - /Author_Search/"Author_name"
- Search proverbs based on keyword - /Keyword_Search/"keyword"

### Tools Used

- Python 
- Flask Package in Python
 
Note:
- The "app.py" is the main Flask file
- The "web_scrapping.py" is used scrape proverb from website and store it in csv.
- The "create_table.py" is used put the proverbs from generated csv file to a table in database (Sqlite) 