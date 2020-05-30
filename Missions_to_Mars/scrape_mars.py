from splinter import Browser
from bs4 import BeautifulSoup
import requests
import datetime as dt
import time
# import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": 'C:/Users/pli.TELOS/Desktop/web-scraping-challenge/Missions_to_Mars/chromedriver.exe'}
    # executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
#  code from jupyter notebook  
  

    browser = init_browser()
    # *********Scrape Title & Paragraph*********************************
   
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title_tag = soup.find('div',class_='list_text')
    # find title and assign to variable news_title
    new_title = title_tag.find('a').text
    # find paragraph text and assign to variable news_p
    news_p = soup.find('div', class_='article_teaser_body').text



    # *********Full Image*********************************
    
    
    browser = init_browser()
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    time.sleep(5)
    browser.click_link_by_id('full_image')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    time.sleep(5)
    html = browser.html
    image_soup = BeautifulSoup(html,'html.parser')
    suffix_ur = image_soup.find(class_="lede")
    suffix_inner = suffix_ur.find('a').get('href')
    featured_image_url = "https://www.jpl.nasa.gov" + suffix_inner 
    
    
 # *********Mars Hemisphere*********************************

    browser = init_browser()
    # browser = Browser('chrome', **executable_path, headless=False) 
    image_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(image_url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    element_item = soup.find_all('div', class_='item')
    image_list = []
    base_url = "https://astrogeology.usgs.gov" 
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    for x in element_item:
        h3_title=x.find('h3').text
        sub_page_url = x.find('a').get('href')
        browser.visit(base_url + sub_page_url)
        time.sleep(5)
        url_extension = browser.html
        soup = BeautifulSoup(url_extension,'html.parser')
        wide_image_suffix = soup.find('img', class_='wide-image')
        x = base_url + wide_image_suffix.get('src')
        image_list.append({'title':h3_title,'image_url':x})   
             
    image_list   


# **************************************************************
    # browser.quit() 
    mars_dict = {"header": new_title,"paragraph": news_p, "full_image":featured_image_url,"hemisphere":image_list}
    # "full_image":featured_image_url
    return mars_dict



# No need to run flask on this py, so we can omit below. 
# if __name__ == "__main__":
#     app.run(debug=True)
