from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.flipkart.com/search?q=asus+vivobook&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_9_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_9_na_na_na&as-pos=2&as-type=HISTORY&suggestionId=asus+vivobook%7CLaptops&requestId=c359b93d-2a8f-492b-80de-1d524f6460d6'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"_3O0U0u"})
#print(len(containers))

#print(soup.prettify(containers[1]))

container = containers[0]
#print(container.div.img["alt"])

price = container.findAll("div", {"class": "_1vC4OE _2rQ-NK"})
#print(price[0].text)

ratings = container.findAll("div",{"class": "niH0FQ"})
#print(ratings[0].text)

filename = "products.csv"
f= open(filename,"w")

headers = "Product_Name.Pricing.Ratings\n"
f.write(headers)

for container in containers:
    try:
         product_name = container.div.img["alt"]

         price_container = container.findAll("div", {"class": "_1vC4OE _2rQ-NK"})
         price = price_container[0].text.strip()

         ratings_container = container.findAll("div", {"class": "niH0FQ"})
         rating = ratings_container[0].text

         print("product_name: " + product_name)
         print("price:" + price)
         print("rating:" + rating)


         trim_price = ''.join(price.split(','))
         rm_rupee = trim_price.split("₹")
         add_rs_price = "Rs." + rm_rupee[1]
         split_price = add_rs_price.split('E')
         final_price = split_price[0]


         split_rating = rating.split(" ")
         final_rating = split_rating[0]

         print(product_name.replace("," , "|") + final_price + "," + final_rating + "\n")
         f.write(product_name.replace("," , "|") + final_price + "," + final_rating + "\n")
    except IndexError:
       break

f.close()