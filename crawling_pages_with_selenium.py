from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time
import pandas as pd

# Open up a Chrome browser and navigate to web page.
PATH = "C:\Program Files (x86)\chromedriver.exe" # PATH chromedriver.exe
driver = webdriver.Chrome(PATH)
driver.get("https://www.vietnamworks.com/")

job_details = []

# Enter search keywords on vietnamwork
def search(word):
    search_word = driver.find_element_by_name("keyword")
    search_word.send_keys(word)
    search_word.send_keys(Keys.RETURN)

# Get data from vietnamwork
def get_data():
    page_item = driver.find_elements_by_xpath("//li[@class='page-item' or @class='page-item active']/a  ")
    for page in range(0, len(page_item)-1):
        page_item[page].click() #  move to the next page get data
        time.sleep(5)
        job_list = driver.find_elements_by_xpath("//div[@class='job-info-wrapper ']")
        for each_job in job_list:
            job_title =  each_job.find_element_by_xpath('.//a[@class="job-title " or @class="job-title priorityJob"]')
            job_company =  each_job.find_element_by_xpath('.//a[@class="mt-1 company-name"]')
            job_location = each_job.find_element_by_xpath('.//div[@class="location"]')
            job_info = [job_title.text, job_company.text, job_location.text]
            job_details.append(job_info)  # save data 
    return job_details

# Save data as CSV
def save_data(data):
    job_details_df = pd.DataFrame(data)
    job_details_df.columns = ['title', 'company', 'location']
    job_details_df.to_csv('job_details.csv', index=False)

if __name__ == "__main__":
    search("Python")
    data_job = get_data()
    save_data(data_job)
