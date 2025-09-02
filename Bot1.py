import requests
import bs4

# URL of edikted's sales and promotions page
my_url = 'https://edikted.com/collections/on-sale'

#gets the HTML content of the specified URL, for certain tags and classes, and then prints them revealing all items on sale


#Parameters:
# my_url=  The URL of the webpage to scrape.
# tag = The HTML tag to search for.
# myclass = The class name to filter elements by.
#returns parsed_data.find_all(tag, class_=myclass)
def scrape_with__tags_and_class(my_url, tag, myclass):
        response = requests.get(my_url)  # gets the webpage
        html_data = response.content  # get the content
        code = response.status_code  # get the status code
        #print(html_data)  # print the raw data unformatted
        parsed_data = bs4.BeautifulSoup(html_data, "html.parser")  # parse it

        # find all the elemnts with the specified tag
        elements = parsed_data.find_all(tag, class_=myclass)
        # Extract text content from the elements
        return elements
#  Scrapes product discounts and names from the sales page, with certian tags and classes
#paramaters my_url
#returns parsed_data,names_of_products which is then replugged into the Print data function
def scrape_sales(my_url):

    parsed_data= scrape_with__tags_and_class(my_url, 'div',"product-badge product-badge--discount")
    names_of_products = scrape_with__tags_and_class(my_url,'div','product-card__title')
    return parsed_data,names_of_products

#   Prints the product names and their discount information.
def print_data(parsed_data,names_of_products):
    for i in range(0, len(names_of_products)):
        # For each product, print the text of its first child element and the associated parsed data
        print(names_of_products[i].findChildren()[0].get_text(),parsed_data[i].get_text())# Loop through the list of product names and corresponding parsed data

#return data scrape
parsed_data,names_of_products = scrape_sales (my_url)

#prints everything
print_data(parsed_data,names_of_products)

