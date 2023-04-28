# Web-Scrapers
This is a repository for some of the various types of web-scrapers I have written for the purpose of data collection for various projects.

## PS4DealsScraper
This is a beautifulsoup4 scraper that goes to a website to scrape current sale prices of Ps4 games as well as their normal prices. It saves that data into a dataframe, from which you can produce a '.csv' file, and it also logs the data to a mysql database.

## Upwork Scraper
This is a jsoup scraper that goes to the job board for web-scraping on the popular website 'Upwork' and returns a json of the data it collects from the postings there.

## USC Football Scraper
This is a Python web scraper designed to collect statistics for the USC football team for the year 2020 from the website sports-reference.com. The script uses the BeautifulSoup library to extract data from the website and the Pandas library to organize the data into a table format. The output is saved as a CSV file named usc_football_stats.csv. The user can modify the school variable to scrape data for a different college football team.
