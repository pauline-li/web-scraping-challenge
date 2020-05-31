from splinter import Browser
from bs4 import BeautifulSoup
import requests
import datetime as dt
import time

def init_browser():
    # Execute chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'} 
    # Set headless to True for chromedrive to run in background to avoid annoying pop ups. 
    return Browser("chrome", **executable_path, headless=True)
   

def scrape():
#  code tested in jupyter notebook  
  
    
    # *********Scrape <NASA Mars News Latest News Title and Paragraph Text>******************************************
   
    browser = init_browser()
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



    # *********Scrape <JPL Mars Space Images - Featured Image>**************************************************
     
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
    

     # *********Scrape <Mars Facts table>**********************************************************************
     
    
    
    
    # *********Scrape <Mars Hemispheres Image>******************************************************************

    browser = init_browser()
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
    

    # Append title and image url to list  
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


    # ********* Store results in dictionary ***************************************************************
    # ---browser.quit() 
    mars_dict = {"header": new_title,"paragraph": news_p, "full_image":featured_image_url,"hemisphere":image_list}
    return mars_dict


