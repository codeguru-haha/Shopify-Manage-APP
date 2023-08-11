from config import *
import shopify
import csv


# Create and activate a new session
session = shopify.Session(SHOP_URL, API_VERSION, ADMIN_API)

shopify.ShopifyResource.activate_session(session)

# shopify.ShopifyResource.set_site(f'https://{API_KEY}:{SECRET_KEY}@{SHOP_URL}/admin/api/{API_VERSION}')

products = shopify.Product.find()

# Specify the path and filename for the CSV file
csv_file_path = 'products.csv'

# Open the CSV file in 'write' mode

with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)
    
    # Write the header row
    csv_writer.writerow(['Title', 'ID', 'ItemCode', 'Available'])
    
    # Iterate over the products and write the title and ID to each row
    for product in products:
        print(dir(product))
        csv_writer.writerow([product.title, product.id, product.ItemCode, product.Available])

print('Data has been successfully written to', csv_file_path)

