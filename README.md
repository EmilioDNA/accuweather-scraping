# Accuweather Scraping
A basic project that gets data from the Weather website each certain period of time.

# Description

This is a basic App that uses Scrapy,Python and Pymongo to get weather data from the accuweather site for three different cities in Mexico: Sonora, Mérida and Comitán.

This information is saved in MongoDB, and updated every 20 seconds (just for demostrative purposes). The idea of this script is to crawl the website and update the data daily.


## Getting Started

### Installing Dependencies

#### Python 3.7 

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### MongoDB 

Follow instructions to install the latest version of mongoDB for your platform in the [mongoDB docs](https://docs.mongodb.com/manual/administration/install-community/)

#### Virtual Enviornment

I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### Pip Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/accuweather-scraping` directory and running:

```bash
pip install -r requirements.txt
```
I included all the needed dependencies for this project in the `requirements.txt` file.

##### Key Dependencies

- [Scrapy](https://scrapy.org/)  is an open source and collaborative framework for extracting data from websites.

- [Pymongo](https://pymongo.readthedocs.io/en/stable/)  is a Python distribution containing tools for working with MongoDB.


## Running the script

From within the `accuweather-scraping` directory
ensure you are working using your created virtual environment.

To run the script, execute:

```bash
python3 accuweather-scraping.py
```

Press the `CTRL + C` when you decide to stop the script.



