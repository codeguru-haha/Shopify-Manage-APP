from config import *
import shopify


# Create and activate a new session
session = shopify.Session(SHOP_URL, API_VERSION, ADMIN_API)

shopify.ShopifyResource.activate_session(session)
print(session)
# products = shopify.Product.find()
# print(products)



shopify.ShopifyResource.set_site(f'https://{API_KEY}:{SECRET_KEY}@{SHOP_URL}/admin/api/{API_VERSION}')

# products = shopify.Product.find()
# for product in products:
#     print(product.title)