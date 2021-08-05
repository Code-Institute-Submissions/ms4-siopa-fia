<div align="center">
<h1 align="center">MS4: Siopa Fia</h1>
<img src="https://res.cloudinary.com/elerel/image/upload/v1627641031/amiresponsive4_tijagt.png" alt="multi-device site display image"/>
<br>
</div>

# Project Overview

View the live project [here.](https://siopafia.herokuapp.com/)

Siopa Fia was created as my 4th and final milestone project as part of the Code Institute's Software Development Diploma, intending to be full-stack site based on a fictional online Irish eco/sustainable women's clothing store. Visitors to the site would be able to browse across all products available (women's clothing, footwear and cosmetics), read blogs posted by users or the owner, register for an account to keep track of their recent purchases and they can sign up to the company newsletter to avail of product discounts available in the future. siopaFIA is a fashion store that promotes sustainable fashion, for someone who likes to wear good quality clothing, made locally and supports local business.


The logic behind siopaFIA was to create an e-commerce based around a personal interest: eco-fashion. siopaFIA was created to incorporate every valuable takeaway learned from the [Code Institute's Full Stack Diploma in Web Development](https://codeinstitute.net/) course, maintaining a MVP approach to the site and keeping it to the level that fits my abilities.


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
            - [Base HTML](#base-HTML)
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

## [Strategy](#strategy)

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
| First time user      | access social media of the company;                                      | join social media forums for news and updates                 |
| First time user      | register for a user profile account by choosing a username and password; | store my own personal details and purchase history            |
| First time user      | make purchases as a guest user                                           | do not have to set up an account if I dont want to            |              
|          ---         |                                    ---                                   |                              ---                              |
| Registered user      | log in and log out of my profile account;                                | Safeguard my information whilst not active on the site        |
| Registered user      | update my details                                                        | update address and other details in case they change          |
| Registered user      | store my address for later use;                                          | avoid having to retype it every time I make a purchase        |
| Registered user      | store my purchase history;                                               | access my previous purchase history                           |
| Registered user      | store my choices in checkout;                                            | go back to the site in case I wish to add more options        |
| Registered user      | Make secure payments                                                     | ensure my payments are securely handled                       |
| Registered user      | Receive email confirmation of payment                                    | confirm that my payment was made |
|          ---         |                                    ---                                   |                              ---                              |
| Site Owner           | add new items and category listings;                                     | continuously update the site with new items or specials       |
| Site Owner           | update items                                                             | change price or product criteria                              |
| Site Owner           | delete items                                                             | delete items that are no longer for sale                      |


 ---


## [Scope](#scope)

### [Existing Features](#existing-features)

### Base HTML 

Features across all pages:

#### Navbar

The navbar for siopaFIA has two separate designs- one for mobile and tablet view and the other for larger/desktop screens. Like in the walkthrough project, Boutique Ado, for mobiles and smaller screens I used Bootstrap's [collapsible toggler](https://getbootstrap.com/docs/4.1/components/navbar/#external-content), once selected the user can be redirected to the main componenents in a drop-down view. The items in the dropdown menu are the same in the navbar on desktop view. Similar to the favicon, the company logo is present to act as a link to the homepage and alternatively, the user can find the home link on the top of the dropdown list via the hamburger icon. There is a search icon (replaced by the search bar) and a My Account link, where users can register, sign in or view their profile. The user can always track their spending by having the bag displaying the total amount of the items purchased- this is displayed across all pages of the site.

#### Delivery Banner

Throughout the site, users will see the free delivery offer on spending anything over €75 using a [scroll-text animation](https://blog.hubspot.com/website/scrolling-text-css) feature.

![image](https://res.cloudinary.com/elerel/image/upload/v1627982832/deliverybanner_o0r8ix.png)

#### Messages (Toasts)
   So that the user is kept aware of important interactions, such as adding items to their shopping bag, signing up to the newsletter/confirmation, logging in to their profile etc. importing 'messages' from 'django-contrib' the messages displayed (error, success, warning, info) are in [Bootstrap's Toast](https://getbootstrap.com/docs/5.0/components/toasts/) format:

![image](https://res.cloudinary.com/elerel/image/upload/v1627982581/toast_ay3j3h.png)

#### Footer
 The company footer appears on all pages throughout the site and is divided into three separate parts: social links (where the user can follow the company via Facebook, Twitter etc), Shop and Company links and a sign-up to the company newsletter invitation where the user is required to enter their email address to receive the monthly newsletter. Below the newsletter form, the user can also unsubscribe should they wish.

 ![image](https://res.cloudinary.com/elerel/image/upload/v1628175943/footer_wjgzwr.png)
 

#### Home Page
Upon entering the site, the user will get a feel of what the site is about with its catchy slogan above the call-to-action "Sale Now On!" button. The hero image of the girl snuggling into her "organic" sweater was chosen to convey the message of the siopaFIA's general mission statement of quality over quantity and promote sustainability. The sale button redirects the user to all products the website has to offer its customer. From there, the user will be able to view the selected items on sale and they can filter results using the sort by feature on the all products page. 


#### All Products Page:
Similar to the walkthrough project, Boutique Ado, I followed the similar design of displaying four items across the page on large screens, 3 on medium screens, 2 on smaller tablet screens and 1 item for mobile devices. Each of the product cards show an image of the product itself, its name, price, category and rating. Without overloading the card with more text or buttons, the user simply clicks the image and can be redirected to the product detail page where they can view further detail of the product and add the item to their shopping bag.
As the product list may be plentisome, I included a scroll button so that the user can be brought to the top of the page when clicked. Once the user selects "All Clothing" via the navbar dropdown item, they are brought to the clothing items and can filter items again by selecting one of the three clothing categories.

#### Product Detail Page:
Displaying a larger image and more detail information on the product, the user can select the item's size (if applicable), the quantity (within the set range) they wish to purchase. The user can either select the "Keep Shopping" button where they are redirected to the all products page or they can add the item to their bag by selecting "Add to Bag". The user will be informed they have selected the item with a toast success message alerting them of the items they have currently in their shopping bag, and how much (if applicable) they need to spend to avail of the free delivery offer.
The edit and delete links on the item card are only visible to the site's superuser.

#### Shopping Bag Page:
This page is divided into 5 parts- a smaller rendered image of the item, the product name and SKU number, the price, quantity box selector with remove and update links and the subtotal- all displayed horizontally. Should the user wish to change their mind on any of the products added to the bag, they can update their order on this page below the quantity selector box using the remove or update buttons. The grand total is displayed, along with the delivery charge info (if applicable) towards the bottom of the page. The user can also return to the all products page by clicking on the "Keep Shopping" button, or they can proceed with their purchase by clicking "Secure Checkout".

#### Checkout Page:

This page contains three forms (user's name, billing details and payment form) that the user is required to fill out before purchase. This is saved once the user is logged in and below the billing details, the user has the opportunity to create an account or login to save the information filled out. Below the credit card form they are once again informed how much their card will be charged and can proceed to confirm payment or they can adjust their bag and return to the shopping bag page:

![image](https://res.cloudinary.com/elerel/image/upload/v1628159157/checkoutpage_axvcmi.png)

#### Checkout Success Page:

Once the purchase is completed, a success message appears with confirmation that the payment went through successfully, details of the order number, and a confirmation email will be sent to the user. All details of the order are displayed and a button redirecting to the new-arrivals category page is below:

![image](https://res.cloudinary.com/elerel/image/upload/v1628161345/checkoutsuccess_unqgxr.png)


#### FAQs Page:

While any user can read any of the blog posts, only the superuser/site admin can add, edit or delete the featured blogposts. 
Accessible by clicking "blog" from the navbar, the user is redirected to the blog app. There is a brief description of the benefits of reading through the featured posts, the user can browse through the various topics that are formatted in a card-view, and once they click on "more" they are then brought to the blog_detail page where they can read the blog in full.
Once the super user is logged in, they can edit or delete the blog or click "Add Blog" button which is further down the page. There is also a scroll-to-top button to improve UX in case they post entries are lengthy.

#### Blog Page:



#### Profile Page:

This page is only accessible to a registered user where the user can track their purchases and update their details should they need: 




### [Features Left to Implement](#features-left-to-implement):
- A welcome or discount offer, like 10% off their first purchase to entice the user to register or spend straight away.
- A size guide on a separate HTML page but time did not allow!
- 


## [Structure](structure)

### Database 
- As suggested in throughout the walkthrough project, SQLlite (that comes pre-installed with Django) was used for development.
- PostgreSQL was used when deployed through Heroku (as an additional add-on).
- The user model is provided by default with [Django's Authentication System](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/)

### Database Modelling

- All data related to Products was compiled in a JSON format and is stored in a fixtures folder, as does the FAQ data in its own fixtures folder.
- The Data Model below was created using [drawSQL](https://drawsql.app/):

![image](https://res.cloudinary.com/elerel/image/upload/v1626455309/drawSQL-export-2021-07-16_18_07_zniam0.png)

---

### Wireframes

#### Desktop View:

- Home Page:

![image](https://res.cloudinary.com/elerel/image/upload/v1626507220/desktop-home-new_d6svbt.png)

- All Products on offer through siopaFIA:

![image](https://res.cloudinary.com/elerel/image/upload/v1626507354/desktop-all-products_zqzyz9.png)

- Product Detail Page:

![image](https://res.cloudinary.com/elerel/image/upload/v1626507301/desktop-product-detail_zgdflo.png)

- Shopping Bag Page:

![image](https://res.cloudinary.com/elerel/image/upload/v1626548287/desktop-shoppingbag_qxjfez.png)

- Checkout Page:

![image](https://res.cloudinary.com/elerel/image/upload/v1626548341/desktop-checkout_otmkk9.png)

Full desktop wireframes can be access [here](static/readme/wireframes/siopafia_desktop_view.pdf)

#### Tablet and Mobile View:

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


## Surface
   
### Design
-   #### Colour Scheme
    
What colours did you use primarily through the site, headers, text
    - I used [Sessions.edu](https://www.sessions.edu/color-calculator/) to work out the correct complimentary colours, and 
    [Coolors](https://coolors.co/042d52-1b466c-f9fafa) to create the palette below.
    <p><img src="readme_materials/colors.jpg"></p>

-   #### Typography
    -   The Cutive Mono font is the logo font used throughout the whole website with Sans Serif as the fallback font in case for 
    any reason the font isn't being imported into the site correctly. I chose this as I believe it has a modern feel and 
    reflects the style of the remainder of the site.

    ![image](https://res.cloudinary.com/elerel/image/upload/v1628189312/cutivemono_taxx12.png)

-   #### Imagery
    - For most of the product images, I compiled a list from [Kaggle](https://www.kaggle.com/paramaggarwal/fashion-product-images-small) and then sourced the rest of the images from [Pixabay](https://pixabay.com/), [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/)

    - All photos were put through [Tiny PNG](https://tinypng.com/) to reduce the file size and improve loading time.

-   #### Icons
    -   The icons used throughout the site are taken from [Font Awesome](https://fontawesome.com/).


---

## Technologies used

### Languages Used:

-   [HTML5](https://en.wikipedia.org/wiki/HTML5): used for creating the structure of the project
-   [CSS3](https://en.wikipedia.org/wiki/CSS): used to style and position all pages
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript): used to create interactive elements on the relevant pages
-   [Python](https://www.python.org/): used as the primary backend framework

### Frameworks, Libraries and Other Sources Used:

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
- [JQuery](https://jquery.com/) was used extensively throughout the site, in order to provide functionality for Bootstrap elements, and for Stripe. 
- [GitPod](https://gitpod.io/) was used as an IDE for this project. 
- [GitHub](https://github.com/) is where siopaFIA's repository is stored. Regular commits were made throughout, and code was pushed to GitHub from GitPod.

## Testing
