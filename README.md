<div align="center">
<h1 align="center">MS4: Siopa Fia</h1>
<img src="https://res.cloudinary.com/elerel/image/upload/v1627641031/amiresponsive4_tijagt.png" alt="multi-device site display image"/>
<br>
</div>

# Project Overview

View the live project [here.](https://siopafia.herokuapp.com/)

Siopa Fia was created as my 4th and final milestone project as part of the Code Institute's Software Development Diploma Course. It is intended to be a full-stack e-commerce site using Python and Django frameworks and based on a fictional online Irish eco/sustainable women's clothing store. Visitors to the site would be able to browse across all products available (women's clothing, footwear and cosmetics), read blogs posted by users or the owner, register for an account to keep track of their recent purchases and in addition they can sign up to the company newsletter to avail of product discounts available in the future. Siopa Fia or "siopaFIA" (as it will appear throughout the documentation) is a fashion store that promotes sustainable fashion, for someone who likes to wear good quality clothing, that is made locally and supports local business.


The logic behind siopaFIA was to create an e-commerce based around a personal interest: eco-fashion. siopaFIA was created to incorporate every valuable takeaway learned from the [Code Institute's Full Stack Diploma in Web Development](https://codeinstitute.net/) course, maintaining a MVP approach to the site whilst creating a fully-functioning e-commerce site.


Primary functions of Siopa Fia:
- Product purchase functionality
- User authentication and authorisation for site subscribers and site admin
- Customer profile page which will contain purchase history and store customer details
- All CRUD functionalities


---

## Contents

- [UX](#ux)
    - [Strategy](#strategy)
        - [Business Logic](#business-logic)
        - [User Stories](#user-stories)
    - [Scope](#scope)
        - [Existing Features](#current-features)
            - [Base HTML](#base-html)
            - [Home Page](#home-page)
            - [All Products Page](#all-products-page)
            - [Product Detail Page](#product-detail-page)
            - [Shopping Bag Page](#shopping-bag-page)
            - [Checkout Page](#checkout-page)
            - [Checkout Success Page](#checkout-success-page)
            - [Profile Page](#profile-page)
            - [FAQs Page](#faqs-page)
            - [Profile Page](#profile-page)
            - [Product and Blog Management Page](#product-and-blog-management-page)
        - [Features Left To Implement](#features-left-to-implement)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
        - [Wireframes](#wireframes)
    - [Surface](#surface)
        - [Design](#design)
            - [Colour Scheme](#colour-scheme)
            - [Typography](#typography)
            - [Imagery](#imagery)
            - [Icons](#icons)
- [Information Architecture](#information-architecture)
    - [Database](#database)
    - [Data Modelling](#data-modelling)
- [Technologies used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-&-databases-used)
- [Testing](#testing)
- [Deployment](#deployment)
     - [Heroku Deployment with AWS](#heroku-deployment-with-aws)
     - [Amazon Web Services](#amazon-web-services)
     - [Local Deployment](#local-deployment)
- [Credits](#credits)
- [Disclaimer](#disclaimer)
- [Acknowledgements](#acknowledgements)

# User Experience (UX)

## Strategy

### Business Logic

- To make the site easy to navigate and create a positive user experience for the shopper
- To be able to add add, edit or delete products available
- To manage a blog circling the topics of discussion around ethical fashion, promoting awareness to users
- To encourage the user to understand the site owner's mission behind siopaFIA
- To support local fashion designers and promote ethical fashion
- To promote awareness of the impact of the fast-fashion industry and help the sustainable fashion grow or even take its place

### User Stories

|      As a/an...      |                         I want the ability to...                         |                        So that I can...                       |
|:--------------------:|:------------------------------------------------------------------------:|:-------------------------------------------------------------:|
|                      |                                                                          |                                                               |
|          ---         |                                    ---                                   |                              ---                              |
| First time user      | easily navigate the site;                                                | find what I am looking for quickly                            |
| First time user      | view the site on all screen sizes;                                       | view the store across all devices                             |
| First time user      | view a list of products                                                  | view items available to buy                                   |
| First time user      | view individual product details                                          | see exactly what I am buying                                  |
| First time user      | read about the company description                                       | gain trust in the company and support local business          |
| First time user      | search for categories of products                                        | find the best-rated/priced products in a specific category    |
| First time user      | search for a product by name or category                                 | easily find the exact product Im looking for                  |
| First time user      | view items selected in the shopping bag                                  | easily see how much I am spending                             |
| First time user      | adjust or remove items from the shopping bag                             | easily change my order in case I change my mind               |
| First time user      | access contact details;                                                  | get in touch with any questions                               |
| First time user      | access social media of the company;                                      | view their social media presence                 |
| First time user      | register for a user profile account by choosing a username and password; | store my own personal details and purchase history            |
| First time user      | make purchases as a guest user                                           | do not have to set up an account if I dont want to            |              
|          ---         |                                    ---                                   |                              ---                              |
| Registered user      | log in and log out of my profile account;                                | Safeguard my information whilst not active on the site        |
| Registered user      | update my details                                                        | update address and other details in case they change          |
| Registered user      | store my address for later use                                           | avoid having to retype it every time I make a purchase        |
| Registered user      | store my purchase history;                                               | access my previous purchase history                           |
| Registered user      | store my choices in checkout;                                            | go back to the site in case I wish to add more options        |
| Registered user      | Make secure payments                                                     | ensure my payments are securely handled                       |
| Registered user      | Receive email confirmation of payment                                    | confirm that my payment was made |
|          ---         |                                    ---                                   |                              ---                              |
| Site Owner           | add new items and category listings;                                     | continuously update the site with new items or specials       |
| Site Owner           | update items                                                             | change price or product criteria                              |
| Site Owner           | delete items                                                             | delete items that are no longer for sale                      |
| Site Owner           | view and manage orders made through siopaFIA                                                              | keep track of new and existing orders                      |
| Site Owner           | view and manage newsletter subscriptions                                                              | keep track of new and existing newsletter subscribers, potential customers                      |
| Site Owner           | view and manage users siopaFIA                                                              | keep track of new and existing users                      |
| Site Owner           | view and manage blog posts, add, edit and delete existing blog posts made through siopaFIA                                                              | keep track of blog post page                      |

 ---


## Scope

### Existing Features

### Base HTML

Features across all pages

### Navbar

The navbar for siopaFIA has two separate designs- one for mobile and tablet view and the other for larger/desktop screens. Like in the walkthrough project, Boutique Ado, for mobiles and smaller screens I used Bootstrap's [collapsible toggler](https://getbootstrap.com/docs/4.1/components/navbar/#external-content), once selected the user can be redirected to the main componenents in a drop-down view. The items in the dropdown menu are the same in the navbar on desktop view. Similar to the favicon, the company logo is present to act as a link to the homepage and alternatively, the user can find the home link on the top of the dropdown list via the hamburger icon. There is a search icon (replaced by the search bar) and a My Account link, where users can register, sign in or view their profile. The user can always track their spending by having the bag displaying the total amount of the items purchased- this is displayed across all pages of the site.

### Delivery Banner

Throughout the site, users will see the free delivery offer on spending anything over €75 using a [scroll-text animation](https://blog.hubspot.com/website/scrolling-text-css) feature.

![image](https://res.cloudinary.com/elerel/image/upload/v1627982832/deliverybanner_o0r8ix.png)

### Messages (Toasts)
   So that the user is kept aware of important interactions, such as adding items to their shopping bag, signing up to the newsletter/confirmation, logging in to their profile etc. importing 'messages' from 'django-contrib' the messages displayed (error, success, warning, info) are in [Bootstrap's Toast](https://getbootstrap.com/docs/5.0/components/toasts/) format:

![image](https://res.cloudinary.com/elerel/image/upload/v1627982581/toast_ay3j3h.png)

### Footer
 The company footer appears on all pages throughout the site and is divided into three separate parts: social links (where the user can follow the company via Facebook, Twitter etc), Shop and Company links and a sign-up to the company newsletter invitation where the user is required to enter their email address to receive the monthly newsletter. Below the newsletter form, the user can also unsubscribe should they wish.

 ![image](https://res.cloudinary.com/elerel/image/upload/v1628175943/footer_wjgzwr.png)
 

### Home Page
Upon entering the site, the user will get a feel of what the site is about with its catchy slogan above the call-to-action "Sale Now On!" button. The hero image of the girl snuggling into her "organic" sweater was chosen to convey the message of the siopaFIA's general mission statement of quality over quantity and promote sustainability. The sale button redirects the user to all products the website has to offer its customer. From there, the user will be able to view the selected items on sale and they can filter results using the sort by feature on the all products page. 


### All Products Page:
Similar to the walkthrough project, Boutique Ado, I followed the similar design of displaying four items across the page on large screens, 3 on medium screens, 2 on smaller tablet screens and 1 item for mobile devices. Each of the product cards show an image of the product itself, its name, price, category and rating. Without overloading the card with more text or buttons, the user simply clicks the image and can be redirected to the product detail page where they can view further detail of the product and add the item to their shopping bag.
As the product list may be plentisome, I included a scroll button so that the user can be brought to the top of the page when clicked. Once the user selects "All Clothing" via the navbar dropdown item, they are brought to the clothing items and can filter items again by selecting one of the three clothing categories.

### Product Detail Page:
Displaying a larger image and more detail information on the product, the user can select the item's size (if applicable), the quantity (within the set range) they wish to purchase. The user can either select the "Keep Shopping" button where they are redirected to the all products page or they can add the item to their bag by selecting "Add to Bag". The user will be informed they have selected the item with a toast success message alerting them of the items they have currently in their shopping bag, and how much (if applicable) they need to spend to avail of the free delivery offer.
The edit and delete links on the item card are only visible to the site's superuser.

### Shopping Bag Page:
This page is divided into 5 parts- a smaller rendered image of the item, the product name and SKU number, the price, quantity box selector with remove and update links and the subtotal- all displayed horizontally. Should the user wish to change their mind on any of the products added to the bag, they can update their order on this page below the quantity selector box using the remove or update buttons. The grand total is displayed, along with the delivery charge info (if applicable) towards the bottom of the page. The user can also return to the all products page by clicking on the "Keep Shopping" button, or they can proceed with their purchase by clicking "Secure Checkout".

### Checkout Page:

This page contains three forms (user's name, billing details and payment form) that the user is required to fill out before purchase. This is saved once the user is logged in and below the billing details, the user has the opportunity to create an account or login to save the information filled out. Below the credit card form they are once again informed how much their card will be charged and can proceed to confirm payment or they can adjust their bag and return to the shopping bag page:

![image](https://res.cloudinary.com/elerel/image/upload/v1628159157/checkoutpage_axvcmi.png)

### Checkout Success Page:

Once the purchase is completed, a success message appears with confirmation that the payment went through successfully, details of the order number, and a confirmation email will be sent to the user. All details of the order are displayed and a button redirecting to the new-arrivals category page is below:

![image](https://res.cloudinary.com/elerel/image/upload/v1628161345/checkoutsuccess_unqgxr.png)


### FAQs Page:

While any user can read any of the blog posts, only the superuser/site admin can add, edit or delete the featured blogposts. 
Accessible by clicking "blog" from the navbar, the user is redirected to the blog app. There is a brief description of the benefits of reading through the featured posts, the user can browse through the various topics that are formatted in a card-view, and once they click on "more" they are then brought to the blog_detail page where they can read the blog in full.
Once the super user is logged in, they can edit or delete the blog or click "Add Blog" button which is further down the page. There is also a scroll-to-top button to improve UX in case they post entries are lengthy.

### Blog Page:

- Accessible to any user to the site, which includes all CRUD functionalities if logged in as a superuser.
- Each blog is contained in its own card-style format and the user can read on by selecting "more" to open up the blog_detail page. The blog_detail page styling is kept basic with an image to upload should the user wish to include it (only the superuser can add any blog posts on user's behalf)
- Scroll-to button to the right of the page for lengthy pages to improve UX.
- The user can redirect back to the home page, products page or back to the blog page which are links below the blog post.

### Profile Page:

This page is only accessible to a registered user where the user can track their purchases and update their details should they need. Divided into two sections, the first shows the user's default delivery information. If they have just made their first order, their address will be automatically saved with the details of their order. Here they can edit their default information which will speed up the checking out process which therefore makes the user more likely to make a purchase.
The second section shows the user's order history which shows the order number, date, items purchased and order total. The user can click on the order number to view their past order. The user is notified by a toast message (alert) that they are looking at a previous order.

### Product and Blog Management Page
---

### Product Management Page

Accessible only to site admin, once logged in they can select "My Account" (dropdown in the navbar) and from there select Product Management where from here they can add any new product that fits into one of the categories listed (Clothing, Footwear, Skincare, etc.)


### Blog Management Page
Like Product Management, this page is also only available to site admin or the superuser. Should a new user wish to add a blog to siopaFIA, they must contact the site admin so that they can request to send in an article or piece written by themselves. Only the admin have access to this page so they wold upload on the user's behalf.
Like Product Management, there is a form to fill out - simply the subject and content with an image to upload should the user wish. Had I known at the time of creation, I would have included three content sections to make the content look more tidy, than one large block of text.

#### Error Pages:
- a custom 404 Error Page was designed to redirect the user back to the home page should they be met with a 404 error:
![image](https://res.cloudinary.com/elerel/image/upload/v1628627009/404_ihxslr.png)
- Much similar to the above 404 error page, a custom 500 Error Page was designed to redirect the user back to the home page should they be met with a 500 error.

### Features Left To Implement
- A welcome or discount offer, such as 10% off their first purchase to entice the user to register or spend straight away.
- A size guide on a separate HTML page
- A favourites or wishlist added by the customer- this could allow the customer to save what they would have like to purchase at the time but were unable to. It further invites the user to come back to the site and make these saved purchases and possibly more.
- Email notification to the user/customer that should their order prove unsuccessful, this is also confirmed by email. This way they can keep track of what they were originally seeking to purchase.
- Email notification to the business owner of any new order that is made- sent directly to the store's email rather than checking orders through admin.
- Additional payment providers such as Paypal or Apple Pay


## Structure
- I wanted to design siopaFIA in a way that seemed obvious to a new user; easy to navigate, find products easily and create a quick and fuss-free transaction. The site is divided into clear sections and created with Django using the following installed apps: Home, Products, Profiles, Bag, Checkout, Contact, About, Blog & FAQ. Having installed Django allauth, this addressed authentication, registration, account management as well as 3rd party (social) account authentication. Similar to the flow of e-commerce sites, like Boutique Ado, it created a natural transaction and with usage of the sticky navbar, footer, links to redirect across all pages, toast messages to guide the user of their interactions, siopaFIA should become an easy site to get around. 

## Information Architecture

### Database 
- As suggested in throughout the walkthrough project, SQLlite (that comes pre-installed with Django) was used for development.
- PostgreSQL was used when deployed through Heroku (as an additional add-on).
- The user model is provided by default with [Django's Authentication System](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/)

### Data Modelling

- All data related to Products was compiled in a JSON format and is stored in a fixtures folder, as does the FAQ data in its own fixtures folder.
- The Data Model below was created using [drawSQL](https://drawsql.app/):

![image](https://res.cloudinary.com/elerel/image/upload/v1626455309/drawSQL-export-2021-07-16_18_07_zniam0.png)

**Changes made to the Database Model since creation:**
- The one addition I made to the Blog Model was alter and create three further fields (intro, body_one, body_two, body_three) that contain TextFields. This was to allow more spacing and better paragraph usage in the blog_detail page thus avoiding long and chunky text that can be difficult to read.

#### [Back to Contents](#contents)
---

## Wireframes

### Desktop View:

- Home Page

![image](https://res.cloudinary.com/elerel/image/upload/v1626507220/desktop-home-new_d6svbt.png)

- All Products on offer through siopaFIA

![image](https://res.cloudinary.com/elerel/image/upload/v1626507354/desktop-all-products_zqzyz9.png)

- Product Detail Page

![image](https://res.cloudinary.com/elerel/image/upload/v1626507301/desktop-product-detail_zgdflo.png)

- Shopping Bag Page

![image](https://res.cloudinary.com/elerel/image/upload/v1626548287/desktop-shoppingbag_qxjfez.png)

- Checkout Page

![image](https://res.cloudinary.com/elerel/image/upload/v1626548341/desktop-checkout_otmkk9.png)

Full desktop wireframes can be access [here](static/readme/wireframes/siopafia_desktop_view.pdf)

## Tablet and Mobile View:

- Home Page

![image](https://res.cloudinary.com/elerel/image/upload/v1627305887/Tablet-Mobile-home_oc3xrf.png)

- All Products

![image](https://res.cloudinary.com/elerel/image/upload/v1627309060/Tablet-Mobile-allproducts_uexnho.png)

- Product Detail

![image](https://res.cloudinary.com/elerel/image/upload/v1627308976/Tablet-Mobile-productdetail_wrmm4z.png)

- Shopping Bag:
 
![image](https://res.cloudinary.com/elerel/image/upload/v1627309139/Tablet-Mobile-shoppingbag_huvo1o.png)

- Checkout:

![image](https://res.cloudinary.com/elerel/image/upload/v1627311530/Tablet-Mobile-checkout_phrzmc.png)

Full mobile and tablet wireframes can be access [here](static/readme/wireframes/siopafia_tabletmobile_view.pdf)

#### [Back to Contents](#contents)

## Surface
   
### Design
-   #### Colour Scheme
    As the colour green is the dominant colour throughout the site, I thought it was a good choice that suited the theme of the site. It is fresh, clean and most often the colour choice for use with the term, "eco" or "environment". The colour chart used is as below, taken from [Color-Hex:](https://www.color-hex.com/color-palette/112498)

    ![image](https://res.cloudinary.com/elerel/image/upload/v1628434425/darkrose_green_Color_Palette_-_color-hex.com_busqpd.png)

-   In addition to the colour chart chosen, primarily green, to add some diversity is #FFC107 - a strong, bold and mustard-toned yellow that I found eye catching and grabs the user's attention towards it. I used it for the CTA button on the home page, the submit button below the newsletter signup and when hovering over the links in the footer:

    ![image](https://res.cloudinary.com/elerel/image/upload/v1628435266/colors_muj5yj.png)



### Typography
[Cutive Mono](https://fonts.google.com/specimen/Cutive+Mono) font is the logo font used throughout the whole website for headers, navbar categories and dropdown list items partnered with [Monteserrat](https://fonts.google.com/specimen/Montserrat?query=mon) font for the bulk text/paragraph use. Sans Serif was the fallback font in case for 
any reason the font isn't being imported into the site correctly. I chose these fonts as I felt it fit well with the 'eco' theme of the business without overstyling the site with flambouyancy. I believe it has a modern feel, both fonts stand out and fit well throughout the site.

![image](https://res.cloudinary.com/elerel/image/upload/v1628189312/cutivemono_taxx12.png)

 ### Imagery
 For most of the product images, I compiled a list from [Kaggle](https://www.kaggle.com/paramaggarwal/fashion-product-images-small) and then sourced the rest of the images from [Pixabay](https://pixabay.com/), [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/)

### Icons
The icons used throughout the site are taken from [Font Awesome](https://fontawesome.com/).


---

# **Technologies used**

## **Languages**

-   [HTML5](https://en.wikipedia.org/wiki/HTML5): used for creating the structure of the project
-   [CSS3](https://en.wikipedia.org/wiki/CSS): used to style and position all pages
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript): used to create interactive elements on the relevant pages
-   [Python](https://www.python.org/): used as the primary backend framework

## **Frameworks, Libraries and Other Sources**

- [Balsamiq](https://balsamiq.com/) was used to create mockups or wireframes for the site.
- [Django](https://www.djangoproject.com/) was used as the primary framework for the project.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used for all forms on the site.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) was used for user authentication on the site.
- [Stripe](https://stripe.com/) was used to handle payments on the site.
- [Bootstrap4](https://getbootstrap.com/) was used to make the site responsive.
- [Amazon Web Services](https://aws.amazon.com/) S3 was used to store all static CSS and Javascript files, and images.
- [SQLite3](https://www.sqlite.org/index.html) is the database that was used in production.
- [PostgreSQL](https://www.postgresql.org/) is the database used by the deployed site.
- [Heroku](https://www.heroku.com/) is used as an online cloud platform service used to host the site.
- [JQuery](https://jquery.com/) was used primarily throughout the site, in order to provide functionality for Bootstrap elements and for use of Stripe. 
- [GitPod](https://gitpod.io/) was used as an IDE for this project. 
- [GitHub](https://github.com/) is where siopaFIA's repository is stored. Regular commits were made throughout, and code was pushed to GitHub from GitPod.

# **Testing**

Testing for siopaFIA has been documented in a separate file that can be accessed here: [TESTING.md](https://github.com/elerel/ms4-siopa-fia/blob/master/TESTING.md)

#### [Back to Contents](#contents)

---

# **Deployment**

## **Heroku Deployment with AWS**

In order to deploy the site onto [Heroku](https://dashboard.heroku.com/apps), I took the following steps:
1. Installed gunicorn, psycopg2-binary and dj-database-url using [PIP](https://pypi.org/project/pip/).
2. Created a requirements.txt file and froze all the required modules to this file using ```pip3 freeze > requirements.txt```
3. Created a Procfile and added ```web: gunicorn siopa_fia.wsgi:application```
4. ```git add```, ```git commit``` and ```git push``` to push these changes to my GitHub repository.
5. Logged into my Heroku account and created a new app, I selected Europe (eu-west-1) as my region.
6. Select Resources tab in Heroku, then in the Add-ons search bar added Heroku Postgres, select plan name **Hobby Dev - Free** then clicked 
Submit Order Form in order to add it to my project.
7. In the dashboard for the application, I clicked on Settings, then Reveal Config Vars and set the following values to appear as below:

|Key|Value|
|--|--|
|AWS_ACCESS_KEY_ID|```Your AWS Access Key```|
|AWS_SECRET_ACCESS_KEY|```Your AWS Secret Access Key```|
|DATABASE_URL	|```Your Postgres Database URL```|
|EMAIL_HOST_PASS|```Your Email Password (generated by Gmail)```|
|EMAIL_HOST_USER|```Your Email Address```|
|SECRET_KEY	|```Your Secret Key```|
|STRIPE_PUBLIC_KEY	|```Your Stripe Public Key```|
|STRIPE_SECRET_KEY	|```Your Stripe Secret Ke```y|
|STRIPE_WH_SECRET	|```Your Stripe WH Key```|
|USE_AWS	|```True```

8. In the Deploy tab, under Deployment method, selected GitHub and then set up automatic deploys. When the app has finished building, click **Open app** button on the top right of the page.
9. Commented out current DATABASE setting in settings.py, and add the following code instead:
``` 
DATABASES = {     
        'default': dj_database_url.parse("<your Postgres database URL here>")     
    }    
```

10. Back on the main dashboard, click on 'deploy', and then under the 'Deployment' method section, select GitHub and 'Automatic Deploys'.

11. In settings.py, the the following code is commented out:
```
Database
 https://docs.djangoproject.com/en/3.1/ref/settings/#databases
```
and then instead the following code is added:
```
DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
```
12. Plan for migration with the following command:
```
python3 manage.py makemigrations --dry-run
```

13. Make migrations using the following command:
```
python3 manage.py makemigrations
```
and migrate the database models to the Postgres database using the following command:
```
python3 manage.py migrate
```
13. Load the fixtures from the 'products.json' file and then from the 'products.json' file - which are contained in the 'fixtures' folder into the database. 
This is done by using the following command:
```
python3 manage.py loaddata <file name>
```
14. Create a new superuser with the following command:
```
python3 manage.py createsuperuser
```
proceed to then enter chosen email, username and password.

15. In settings.py, contain the previously entered database setting in an if statement, and add an else condition, so that different databases are 
used depending on the environment.
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```
16. Disable 'COLLECTSTATIC' with the fillowing code: ``` heroku config:set DISABLE_COLLECTSTATIC=1 ``` 
so that Heroku doesn't attempt to collect the static files.
17. Add ```ALLOWED_HOSTS = ['siopafia.herokuapp.com', 'localhost']``` to settings.py.
18. Add Stripe environment variables to settings.py.
19. Push to Heroku using the following command:
```git push heroku master```

---


## **Amazon Web Services**

I used AWS to host the static and media files for the deployed site kept in the siopafia S3 bucket. I created a new account, then a new S3 bucket
and uploaded the relevant static and media files. Detailed guidelines can be found [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
As guided in the Boutiquqe Ado walkthrough project, I used the following CORS configuration:
```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```

1. Returning to the IDE terminal, I installed boto3 and django-storages using the ```pip3 install``` and then froze them using ```pip3 freeze > requirements.txt```
in order to connect the S3 bucket to Django.
2. Added 'storages' to the list of ```INSTALLED_APPS``` in settings.py
3. Added the following also in settings.py:
```
if 'USE_AWS' in os.environ:
    if 'USE_AWS' in os.environ:
        # Cache control
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=94608000',
        }


    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'siopafia'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
4. Created a custom_storages.py file at the top level folder which includes the location of the Static Storage and Media Storage.
5. Removed DISABLE_COLLECTSTATIC from Heroku's Config Var.
6. Pushed all the changes to Github and thus Heroku.

## **Local Deployment**
In order to make a local clone of the siopaFIA website, enter ```git clone https://github.com/elerel/ms4-siopa-fia.git``` into the
terminal. 

Alternatively, you can follow these steps, which are detailed on the official 
[GitHub Documentation](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)

Next, create an .env.py file in the root directory of the project, and add it to the .gitignore file. This project will only run locally if an env.py file is set up containing the IP, PORT and SECRET_KEY. As per security measures advised, these details will not be shared on this documentation.
The following code to be added to the .env.py file:
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret Key>"
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public Key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret Key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH Secret Key>"   
```

Then make sure that the required packages are installed by running the following command: 
```pip install -r requirements.txt```

Make migrations and then migrate in order to create a database, by running the following commands:
```python3 manage.py makemigrations``` and ```python3 manage.py migrate```.

Load the fixtures from the 'products.json' and 'faq.json' files - which are contained in the 'fixtures' folder into the database. 
This is done by using the following command:
```
    python3 manage.py loaddata <file name> 
```

Create a superuser with the following command: ```python3 manage.py runserver``` and entering your credentials.

Run the app by entering the following command:
```python3 manage.py runserver```


### **Credits**

**Code:**
- The walkthrough project in the Full Stack Frameworks with Django Module, Boutique Ado, was used as the primary resource throughout this project.
- For the Newsletter sign-up View in the Contact App, I followed this tutorial by [Master Code Online](https://www.youtube.com/watch?v=Hy94jBBgvpk)
- To add an unsubscribe view to the Contact App, I followed this tutorial also by [Master Code Online](https://www.youtube.com/watch?v=q2B1VpjDjMQ)
- [Bootstrap](https://getbootstrap.com/docs/5.0/forms/layout/) on grid layout for the Blog and FAQs page
- [Stackoverflow](https://stackoverflow.com/questions/38062124/mobile-media-queries-in-landscape-mode) for help with fixing landscape orientation bug
- [Stackoverflow](https://stackoverflow.com/questions/29211115/adding-link-to-the-admin-index-page-in-django) on adding the Django admin index url
- [Django Docs](https://django-book.readthedocs.io/en/latest/chapter14.html) on users and sessions

**Content:**
- Snippets from blog post "Lets talk about going grey" is taken from [OhhByGum's Blog Page.](https://ohhbygum.ie/blogs/news/thinking-about-going-grey)
- Blog post named "Marci Zaroff: The woman we have to thank for eco fashion" is from [liveeco.co.za](http://www.liveeco.co.za/2016/08/09/marci-zaroff-woman-thank-eco-friendly-fashion/)
- Blog post named "Upcycled Fashion is Growing in India" is also taken from [liveeco.co.za](http://www.liveeco.co.za/2016/08/01/upcycled-fashion-growing-india/)
- Blog post named "How to Dress Sustainably" is from [Harpers Bazaar](https://www.harpersbazaar.com/uk/fashion/what-to-wear/a41158/how-to-be-sustainable-fashion/)

**Media:**
- All images were taken from [Unsplash](), [Pixels](), and [Pixabay](), and some images from [Kaggle]() which are all royalty-free.

### **Disclaimer** 
All images and content on this website is for educational purposes only.

### **Acknowledgements**
- My thanks to my mentor [**Nishant Kumar**](https://github.com/nishant8BITS/) for his time and support, the wonderful and helpful as ever Slack Community, CI tutor support (my special thanks to Scott, Igor, John and Cormac!) and last but not least, [Chris Z](https://github.com/ckz8780) for explaining everything so well and in-depth throughout the project.
- Thank you to my ever-supportive family in having the faith in me to keep going and to my two sweet little girls for letting Mummy "work"!


##### [Back to Contents](#contents)