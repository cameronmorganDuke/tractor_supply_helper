import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

headers = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_search(search):
    url = "https://www.tractorsupply.com/tsc/search/" + search #search the requested search
    response = requests.get(url, headers=headers) #connect to the search
    soup = BeautifulSoup(response.text, 'html.parser') #parse the website's response
    
    website_list = [] #initialize the list of the first three websites 

    # Find all divs with the class 'all-components' 
    div_tags = soup.find_all('div', class_='all-components')
    
    for each in div_tags[0:3]:  # Limiting to the first three divs
        # Find the first 'a' tag inside the div and get the href attribute
        a_tag = each.find('a', href=True)
        if a_tag:
            website_list.append(urljoin("https://www.tractorsupply.com", a_tag['href']))
    
    return website_list

def get_soup(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_name(soup):
    h1_tag = soup.find('h1')
    if h1_tag:
        heading_text = h1_tag.text.strip()
        return(heading_text)
    else:
        return("h1 tag not found")
    
def get_image(soup):
    img_tag = soup.find('img', attrs={'itemprop': 'image', 'loading': 'lazy'})
    if img_tag:
        image_url = img_tag.get('src')
        return image_url
    else:
        return("Image tag not found or attributes not matched")
    
def get_sku(soup):
    span_tag = soup.find('span', id='sku')
    if span_tag:
        sku_number = span_tag.text.strip()[:-2]
        return sku_number
    else:
        print("Span tag not found or id 'sku' not matched")
        
def get_stock(soup):
    element = soup.find('strong', id="in-stock", class_="in-stock-qty")
    if element:
        return(element.text.strip())
    else:
        return("Element not found")
    
