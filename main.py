import scrape
import attributes
import display

def driver(user_input):
    search = create_url(user_input)
    websites = scrape.scrape_search(search)
    item_list = []
    for url in websites:
        item = attributes.Details(scrape.get_soup(url))
        item_list.append(item)
    print(item_list)
    display.start_display(item_list)
    
#Format input to search url through Tractor Supply website
def create_url(user_input):
    search_request_split = user_input.split()
    search = "%20".join(search_request_split) + "?"
    return search
    

if __name__ == "__main__":
    user_input = input("What product would you like to search?\n")
    driver(user_input)