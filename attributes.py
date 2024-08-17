import scrape
import locate_item

class Details:
    def __init__(self,soup):
        self.name = scrape.get_name(soup)
        self.image = scrape.get_image(soup)
        self.sku = scrape.get_sku(soup)
        self.stock_status = scrape.get_stock(soup)
        self.pog = locate_item.get_pog(self.sku)
    

    
    
    
        
    
        