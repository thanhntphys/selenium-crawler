# selenium-crawler
Setep 1:
Initializing the web driver
Selenium for doing its work opens a browser. The browser can be chrome or firefox that has UI or phantomjs browser that does not have UI. It's trivial that phanstomjs would be faster than the others, but we can see the process by our eyes. So it's a good way to do our develope and debugs with chrome or firefox, and for the final version of our code, we replace them with phantomjs to speed up our work. for this purpose, we should initialize the webdriver for our navigation in a web webpage. So first we import webdriver
from selenium import webdriver.
And then we initialize our driver with the path of our browser driver.

Step 2: pip install -r requirements.txt
Step 3: python crawling_pages_with_selenium.py
Data is saved job_details.css.
