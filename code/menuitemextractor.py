
import sys
sys.path.append('code')
from menuitem import FoodItem


def clean_price(price:str) -> float:
   return float(price.replace("$", "").replace(",", ""))


def clean_scraped_text(scraped_text: str) -> list[str]:
    raw_items = scraped_text.split("\n")
    data_list = []
    for item in raw_items:
        if item in ['GS',"V","S","P"]:
            continue
        if item.startswith("NEW"):
            continue
        if len(item.strip()) == 0:
            continue

        data_list.append(item)

    return data_list

def extract_menu_item(title:str, scraped_text: str) -> FoodItem:
    cleaned_items = clean_scraped_text(scraped_text)
    item = FoodItem(category=title, name="", price=0.0, description="")
    item.name = cleaned_items[0]
    item.price = clean_price(cleaned_items[1])
    if len(cleaned_items) > 2:
        item.description = cleaned_items[2]
    else:
        item.description = "No description available."
    return item



