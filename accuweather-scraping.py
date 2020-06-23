# Impoorting all the required modules
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from scrapy.crawler import CrawlerRunner
from scrapy.spiders import Spider
from pymongo import MongoClient

# Instantiate the mongo client and create the db and collection directly
client = MongoClient('localhost')
db = client['weather']
col  = db['accuweather_forecast']

# Create the class to crawl accuweather
class WeatherSpider(Spider):
    name = "WeatherCrawler"
    # The custom settings that define the user agent, max num of requests and the display of the log in the console
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
        'CLOSESPIDER_PAGECOUNT': 20,
        'LOG_ENABLED': False
    }
    """
    For this exercise I considered three important cities in México (Mérida, Sonora and Comitán (my born city))
    """
    start_urls = [
        "https://www.accuweather.com/es/mx/m%c3%a9rida/246574/weather-forecast/246574",
        "https://www.accuweather.com/es/mx/sonora/3586188/weather-forecast/3586188",
        "https://www.accuweather.com/es/mx/comit%c3%a1n-de-dom%c3%adnguez/231934/weather-forecast/231934"
    ]
    # Defined the main callback
    def parse(self, response):
        print(response)
        # Get the city, current weather and real feel with xPath
        city = response.xpath('//h1/text()').get()
        current = response.xpath('//a[contains(@class, "card current")]//div[@class="temp"]/span[1]/text()').get()
        real_feel = response.xpath('//a[contains(@class, "card current")]//div[@class="real-feel"]/text()').get()
        # Perfomed a simple clean up of the values to remove spaces and trailing characters
        city = city.replace('\n', '').replace('\r', '').strip()
        current = current.replace('°', '').replace('\n', '').replace('\r', '').strip()
        real_feel = real_feel.replace('RealFeel®', '').replace('°', '').replace('\n', '').replace('\r', '').strip()

        # Use the command update_one of Mongo where the city is equals to itself
        col.update_one({
            'ciudad': city 
        }, {
            '$set': { # If there is no document, a new one will be created
                'ciudad': city, # In case the document already exists, this will be updated
                'current': current,
                'real_feel': real_feel
            }
        }, upsert=True) # Upsert to true

# The next portion of code uses a looping call to perform the crawl every determined period of time
runner = CrawlerRunner()
task = LoopingCall(lambda: runner.crawl(WeatherSpider))
task.start(20) # set 20 seconds as example to evaluate the results
reactor.run()