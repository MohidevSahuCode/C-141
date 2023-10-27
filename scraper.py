# help for interaction of web browser
from selenium import webdriver
from selenium.webdriver.common.by import By
# conver into HTML code to understabe for python ( Parsing )
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver read website
browser = webdriver.Chrome("C:/Users/mohid/OneDrive/Desktop/Python Files/Web Scraping/C-141 project/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

stars_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):

        soup = BeautifulSoup(browser.page_source,"html.parser")
        print(f'Scrapping page {i+1} ...' )
        for ul_tag in soup.find.all("ul",attrs={"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index,li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
        stars_data.append(temp_list)
    browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

        




        
# Calling Method    
scrape()

# Define Header
headers = ["name", "distance", "mass", "radius"]

# Define pandas DataFrame   
stars_df = pd.DataFrame(stars_data,columns=headers)

# Convert to CSV
stars_df.to_csv("Scrapped.csv",index=True,index_label="id")
    


