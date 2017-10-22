# stubhub-price-scraper

Python script that scrapes the min, max, average, and median prices for event listings.  It scrapes prices at the time of program execution.

## Intructions

To use the price scraper, there are a couple of set up items you need to address.

### Set up stubhub developer account and get api token

1. To scrape data, you need an account for the stubhub api. You can sign up at the following link. [https://developer.stubhub.com/store/site/pages/index.jag](https://developer.stubhub.com/store/site/pages/index.jag)
2. Navigate to the APIs tab and create a new application.
3. Generate api keys for your access token.
4. Profit

### Configure scraper

1. Clone/fork the repository and install it on your local machine.
2. Open the api_config.py and input the following configuration items:
⋅⋅* Stubhub username
⋅⋅* Stubhub password
⋅⋅* API Key
⋅⋅* Ids for events you'd like to scrape ( Can be found in their respective stubhub urls )
3. Run the script by executing 'python index.py'

## Notes

This script requires python3.  If you'd like to get data over time, schedule periodic execution using crontab or the like.  There are some external dependencies that are required.  Install them with pip as you encounter errors.

## Credits

Big thanks to Ozzie Liu who provided much of the direction in getting this script set up in his tutorial.  You can visit that here [http://ozzieliu.com/2016/06/21/scraping-ticket-data-with-stubhub-api/](http://ozzieliu.com/2016/06/21/scraping-ticket-data-with-stubhub-api/)


