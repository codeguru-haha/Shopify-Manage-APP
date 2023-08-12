# Shopify-Product-Management-APP-Sample

I created this extremely simplistic, but hollistic, app for Shopify using Python to help you learn the basics of the process. I recently created my first Shopify app and while the documentation from Shopify was great, I found it tough to fully grok the entire process. I found many community examples to be somewhat opinionated or built more as an SDK, which are great for some but I prefer a more basic approach, learning a very barebones understanding of the mechanics of the entire app lifecycle, so that's what I focused on for this project.

## What does this sample do?

Very simply, this sample will create the server-side component for your Shopify app and provide you some basic tools which you can build on to create a ~~more~~ robust commercial application.

## Setup
1. Install dependencies
```
pip3 install -r requirements.txt
```


2. Set up your Shopify app, following [these](https://github.com/StarSolution1221/Shopify-Manage-APP#recieve-admin-api-key) steps.


3. Run the app locally. If you are located in the root directory:
```
python "shopify inventory management.py"
```
From this running you can control the shopify product's properties.


5. Run the app onto a Shopify test store, you can manage the all property of product using CSV file, following [these](https://github.com/StarSolution1221/Shopify-Manage-APP#product-management)


### `config.py`

This is where you will place your app-specific configuration values. For a production application **DO NOT** keep your sensitive values (i.e. `SHOP_URL`, `API_VERSION`, `API_KEY`, `SECRET_KEY`, `ADMIN_API`) in your source code.

### `shopify inventory management.py`

This app allows you to get product names, IDs, counts, and more in your Shopify store. After importing the data, it will all be output as a CSV file.
You can make any changes to this CSV file and upload it to your Shopify store using this app. So, this app gives you simple control over all the products in your Shopify store.

## Recieve Admin API Key

Whatever you use to host your app, you have to login to https://shopify.com (https://admin.shopify.com/store/{SHOPIFY NAME}). From this window you can set the app and admin api key etc. as following steps

![](images/img1.png)

![](images/img2.png)

![](images/img3.png)

![](images/img4.png)

![](images/img5.png)

![](images/img6.png)

![](images/img7.png)

![](images/img8.png)

Your `config` file can be fully configured! You should now run the app.

## Product Management



## Conclusion

That's it, you've successfully created your first Shopify product management app using Python! Congrats! 

I hope you found this sample app helpful. If I messed anything up, just let me know and I will try to resolve as soon as I can, I'm also open to contributions. 

I used the APACHE 2.0 license which is very liberal, feel free to use any of the code in this project, I don't require attribution but would love to know if you found it helpful.

