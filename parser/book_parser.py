import re
from locators.book_locator import BookLocators

class BookParser:
    RATINGS={
        'One':1,
        'Two':2,
        'Three':3,
        'Four':4,
        'Five':5
    }
    def __init__(self,parent):
        self.parent=parent

    @property
    def itemname(self):
        locator=BookLocators.NAMELOCATORS
        item_link=self.parent.select_one(locator)
        item=item_link.attrs['title']
        return item

    @property
    def itemlink(self):
        locator=ParserBookLocators.LINK_LOCATORS
        item_link=self.parent.select_one(locator)
        item=item_link.attrs['href']
        return item
    @property
    def price(self):
        locator=BookLocators.PRICE_LOCATORS
        price_link=self.parent.select_one(locator).string
        expression='£([0-9]+\.[0-9]+)'
        matches=re.search(expression,price_link)
        print(matches.group(0))
        print(matches.group(1))
        price_number=float(matches.group(1))
        return price_number
    @property
    def rating(self):
        locator=BookLocators.RATING_LOCATORS
        star_rating=self.soup.select_one(locator)
        classes=star_rating.attrs['class']
        class_rating=[p for p in classes if p!= 'star-rating']
        rating_number=BookParer.RATINGS.get(class_rating[0])
        return rating_number

