<div align="center">
<h1 align="center">MS4: Testing Section</h1>
</div>

## Contents

- [Validation](#validation)
- [Performance](#performance)
- [Fixed Bugs](#fixed-bugs)
- [Known Bugs](#known-bugs)
- [Testing Stripe Payments](#testing-stripe-payments)
- [Manual Testing](#links-and-navigation)
- [Testing User Stories](#testing-user-stories)

---

## Validation

- [W3 HTML Validator](https://validator.w3.org/) Results:

![image](https://res.cloudinary.com/elerel/image/upload/v1627549562/w3HTMLchecker_px7ncd.png)

The error showing was in regards to the type attribute under the postblockjs section (toasts) in the base.html page- I later removed this and it made no difference to the code.

- [W3 Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) Results:

![image](https://res.cloudinary.com/elerel/image/upload/v1627550328/cssvalidation_hfhkp5.png)

Two errors were displayed upon results showing- I wasn't overly concerned about this since they are originating from the Bootstrap CDN and would be out of my control.

- [JSHint:](https://jshint.com/)

![image]https://res.cloudinary.com/elerel/image/upload/v1627551061/jshint_cpa9z3.png)

Just the one error here regarding the missing semi-colon (line 119 in stripe-elements.js) which I subsequently added and no further errors followed.

- [PEP8:](http://pep8online.com/)

![image](https://res.cloudinary.com/elerel/image/upload/v1627554718/pep8_q7qj4z.png)

The screenshot above shows the main issues that popped up across several views.py pages- I made sure to address these and no further errors were displayed.

![image](https://res.cloudinary.com/elerel/image/upload/v1627554869/pep8blog_whsula.png)




## Performance

Lighthouse Testing:

- Added the suggested attribute 'rel="noreferrer"' to each of the anchor tags to improve the best practices score:
![image](https://res.cloudinary.com/elerel/image/upload/v1627475064/lighthouse1_ykmloo.png)

- To improve optimization, I included the word "unsubscribe" in the anchor tag  so the user knows where the link directs:
![image](https://res.cloudinary.com/elerel/image/upload/v1627475157/seo_dhrrq1.png)

The other notes included in the lighthouse testing included how the site failed the PWA (progressive Web Apps) instability requirements, which I ignored for now.

### Chrome Developer Tools
I used Chrome Developer Tools very often to check the responsivity across several devices, to check the console for any errors and preview any changes that could be made.

# Bugs
1. Size not displaying in the shopping bag:

![image](https://res.cloudinary.com/elerel/image/upload/v1628075067/sizebug_ghbdgt.png)
![image](https://res.cloudinary.com/elerel/image/upload/v1628075226/sizebug2_nnoeex.png)

Resolved: <strong>Yes.</strong>
On the product_detail.html page, I soon understood the importance of how the name field had to match exactly the value field as set out in the backend. To resolve, I simply removed the whitespace that was causing the issue and the sizes then displayed as they should:

![image](https://res.cloudinary.com/elerel/image/upload/v1628107829/product_detail_vnem0z.png)

Sizes now correctly displaying:

![image](https://res.cloudinary.com/elerel/image/upload/v1628107982/size_resolved_w6ehyb.png)

Other bugs:

-  Through the Heroku deployed site, the sizes only show "N/A" while from gitpod, it    renders no problem. Once the user arrives at the checkout page, the sizes are then displayed as well as in the checkout success page and confirmation email.
Fix? Yes- changed all items that require has_sizes to yes- some were incorrectly labelled as "no".

- Unsubscribe link not displaying (its in a text file, may need to change this to a html file instead?) Fixed: removed the anchor tag and replaced with just hte simple unsubscribe url


Other changes made before during production:
- Removed the two decimals from rating- looked better with a simple decimal point

- When checkout success page url is copied and pasted into a new browser, the page renders and shows sensitive information. I wanted to avoid this so added an if statement to prevent another user from viewing this sensitive information.

- No placeholder image coming through when no image is uploaded:
![image](https://res.cloudinary.com/elerel/image/upload/v1628550609/noimage_ytr7ml.png)
Fix: **Yes**
In order to get around this, I double checked the media url and path name which was not matching the file name in the media directory and changed it to the correct name.

## Known Bugs

- When the user is signed in, if they click Register or Sign In in the footer, they are redirected to the home page and no message appears to notify they are already logged in 
    - I wasnt immediately sure how to go about fixing this error- I first thought it might be a good idea to remove these from the footer, but left the two links there in case a guest user would like to sign up quickly while browsing the site. 

## Testing Stripe Payments

- In order to make sure the Stripe payments were proving successful, I needed to make sure the test webhooks were functioning and the correct endpoint was added: 
```
https://siopafia.herokuapp.com/checkout/wh/
```
- I tested on two separate cards- one that was proven to succeed and another card used to fail payment.

- Successful payment confirmation:
![image](https://res.cloudinary.com/elerel/image/upload/v1628610602/checkoutsuccessful_wdt2ot.png)

- Webhook Succeeded: 
![image](https://res.cloudinary.com/elerel/image/upload/v1628610785/webhookintentsucceed_t8qlqy.png)

- Email confirmation sent to customer that payment and order was successful:
![image](https://res.cloudinary.com/elerel/image/upload/v1628610631/checkoutemail_kzugjs.png)

- Payment failure message notifying customer of insufficient funds:
![image](https://res.cloudinary.com/elerel/image/upload/v1628610979/insufficfunds_zuvhul.png)

- Payment failure with card declined message: 
![image](https://res.cloudinary.com/elerel/image/upload/v1628611089/carddeclined_ulz5bq.png)

- Webhook results displaying payment failures:
![image](https://res.cloudinary.com/elerel/image/upload/v1628611173/webhookresults_t6wkqt.png)

## Manual Testing

Testing has been primarily and regualrly carried across my own desktop on a Windows 10 Home 20H2 Edition, 64 bit and on my mobile phone, a Samsung Galaxy A50.

Chrome, Firefox, Opera, Microsoft Edge, iOS and Samsung Internet were the browsers used to test all pages. The chart below reflects the results: 

|                  |                                |                                                                                                                                                                                          | Windows 10 Home Edition 20H2 Edition. 64 bit. |         |       |                | Smasung Galaxy A50       |
|------------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|---------|-------|----------------|--------------------|
| Page             | Users                          | Test                                                                                                                                                                                     | Chrome                                        | Firefox | Opera | Microsoft Edge | iOS (Version 14.6) |
| **Home**             | All                            |  Page renders without any errors                                                                                                                                                                  | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Home             | All                            | Background image renders correctly                                                                                                                                                          | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Home             | All                            | Hero-text correctly renders                                                                                                                                                                 | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Home             | All                            | 'Sale Now On' button renders                                                                                                                                                         | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Home             | All                            | Ensure 'Shop Now' button navigates to All Products page                                                                                                                                | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Home             | All                            | Shopping bag amount shows total on home page (navbar)                                                                                                                                                                 | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| **All Pages**        | All                            | Navbar renders correctly                                                                                                                                                                    | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure Delivery Banner with scroll-text animation above navbar renders                                                                                                                                                                     | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure siopaFIA logo appears on the navbar and redirects to home page when clicked                                                                                         | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure search bar above dropdown navlinks is operational                                                                                         | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure 'My Account' and shopping basket nav-links render                                                                                                                        | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure navlink dropdown options, 'All Products, Clothing, Skincare, Footwear, About Us and Blog' options appear when clicked and redirect to correct location                                                                                      | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | Non-registered User             | Ensure 'My Account' displays 'Register' and 'Login' only                                                                               | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | Non-registered User            | Ensure non registered users are able to register on the site                                                                                                                        | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | Non-logged in registered users | Ensure non-logged in registered users are able to login                                                                                                                             | Pass               | Pass                               | Pass    | Pass  | Pass           | Pass               |
| All Pages        | Logged in Registered Users     | Ensure 'My Account' nav-link displays 'My Profile' and 'Logout' user-options that navigate to the user profile page, the logout link is functional                               | Pass        |                   | Pass    | Pass  | Pass           | Pass               |
| All Pages        | Superuser                      | Ensure 'My Account' nav-link dropdown displays 'Product Management', 'Blog Management', 'My Profile' and 'Logout'.                                                                                                   | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Check shopping basket icon when clicked navigates to the shopping bag                                                                                                               | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure the total in the shopping bag reflects the total cost of the items in the bag and is displayed below the bag icon.                          | Pass                                          | Pass    | Pass  | Pass           | Pass               |                                                            | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure search box query returns matching result and quantity from the 'Products' page                                                                                                   | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure 'All Products' dropdown displays 'By Price', 'By Rating' and 'By Category' and 'All Products' options, which all direct to the products page, and display the correct products from the link option chosen              | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure 'Clothing' navlink returns a drop down list consisting of 'Dresses', 'Tops', 'Bottoms', 'Sale', and 'All Clothing' which redirect to their chosen item from All Products page             | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure 'Skincare' dropdown displays 'Handmade Soaps', 'Cleansers', 'Serums', 'Body' and 'All Skincare' options, which all navigate to the selected skincare category product page, whilst displaying the correct products         | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure 'Footwear' dropdown menu item displays 'All Footwear' which navigates to the Footwear category product page                                | Pass                                          | Pass    | Pass  | Pass           | Pass                                                                                                                                            | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure site footer renders, and is displayed at the bottom of the page, no matter size or amount of content                                                                                 | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure that the footer is divided equally in to its separate parts and 'Follow Us' is clearly display to the left of the footer                                                                                                               | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure that Facebook, Twitter and Instagram, Pinterest and Vimeo icons are present, and navigate to the correct pages in a new tab by use of target blank attribute                                                                               | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure all footer links below 'Shop' and 'Company' navigate to the correct locations and is a new tab                                                                                                                     | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure email address form renders under 'Newsletter Subscribe' section in footer and navigates to 'newsletter_signup' when user clicks submit                                                                                                                        | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| All Pages        | All                            | Ensure that the 'newsletter_unsubscribe' page renders once the user clicks 'here' beneath subscribe form to unsubscribe from company newsletter.                                                                                     | Pass                                          | Pass    | Pass  | Pass           | Pass               |             
| **Products**         | All                            | Ensure all product images are displaying correctly                                                                                                                                | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Products         | All                            | Ensure correct product name, category, rating and price are on display on each product card                                                                                                                                   | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Products         | All                            | Ensure the user is navigated to the product_detail page once the image is clicked                                                                                              | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Products         | All                            | Ensure 'Sort By' functionality is in place                                                                                                                                                 | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Products         | All                            | Ensure that a placeholder image is present if no image is uploaded by superuser/admin                                                                                                                | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Products         | Superuser                      | Edit and Delete buttons are present                                                                                                                                     | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Products         | Superuser                      | Ensure 'Edit' functionality is in place and user is successful in editing a product                                                                  | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Products         | Superuser                      | Ensure 'Delete' functionality is in place and defensive programming by use of a modal prompt is in place                                                                                     | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Products         | Superuser                      | Ensure that when 'Cancel' is selected, no further delete action is taken                                                                | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Products         | Superuser                      | Ensure that when 'Delete' is selected, the item is successfully removed and a toast message to confirm this renders                                                       | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| **Add Product**      | Superuser                      | Ensure all add_product fields are present                                                                                                                               | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Add Product     | Superuser                      | Ensure add_product form cannot be submitted without fillinf in required fields                                                                                                        | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Add Product      | Superuser                      | When the 'Add Product' button is selected, the item is then added to the database                                                                                     | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Add Product      | Superuser                      | Ensure 'Cancel' redirects user to the all_products page                                                                                                                      | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| **Edit Product**     | Superuser                      | Ensure that the product form is pre-filled and a toast message alert to inform user of their editing actions is present                                                                                       | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Edit Product     | Superuser                      | Ensure image 'remove' and 'upload' functionality is in place                                  | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Edit Product     | All                            | Ensure that the edit product page cannot be viewed by a non superuser copying and pasting the url into their browser                                                                                     | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| **Product Detail**  | All                            | Ensure product image is displaying correctly                                                                                                                                                   | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Product detail   | All                            | Ensure that product details are correctly displayed                                                                                                                                                | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Product detail   | All                            | Ensure quantity input selector is present and operating as it should                                                                                                                           | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Product detail   | All                            | Ensure the 'Keep Shopping' button navigates back to the products page                                                                                                                | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Product detail   | All                            | Verify that the Add to Bag button adds the selected product to the bag and displays the bag total underneath the bag icon                             | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| **Bag**  | All                            | Ensure that all selected product details are displayed                                                                                                                                            | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Bag  | All                            | Ensure that quantity input selector is present and functions                                                                                                                                  | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Bag  | All                            | Ensure the 'Update' button is functioning correctly                                                                                                                                       | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Bag  | All                            | Ensure the 'Remove' button is functioning and updates the total accordingly                                                  | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Bag  | All                            | Ensure that the bag total, delivery cost and grand total are displayed, and if applicable how much the user needs to spend to avail of the free delivery offer                    | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Bag  | All                            | Ensure the 'Keep Shopping' button navigates back to the product page                                                                                                                | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Bag  | All                            | Ensure the secure checkout button navigates to checkout page                                                                                                       | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Bag  | All                            | Ensure if the product has sizes, the correct size is added to the bag                                                                                                            | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| **Checkout**         | All                            | Ensure all order information is displayed as expected                                                                                                                               | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Checkout         | All                            | Ensure user full name and email address form fields are displayed                                                                                                                        | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Checkout         | All                            | Ensure user billing address fields are displayed                                                                                                                                         | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Checkout         | All                            | Ensure 'save details' checkbox is displayed                                                                                                                                           | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Checkout         | All                            | Ensure payment field is displayed                                                                                                                                                   | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Checkout         | All                            | Ensure checkout form cannot be submitted without the required fields being completed                                                                                                | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Checkout         | All                            | Ensure that payment succeeds when test credit card number is entered, and the page redirects to 'checkout success', with the order details displayed                                | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Checkout         | All                            | Ensure that the payment was unsuccessful when using a fail test card and the relevant message is displayed to the user                                                           | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Checkout         | All                            | Ensure user is informed that an order confirmation will be sent to the customer once an order is successfully placed                                                                                                 | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Checkout         | All                            | Ensure that the form cannot be submitted without the necessary fields being completed                                                                                                    | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| **Checkout Success** | Registered User                | Ensure that the checkout success page cannot be viewed by another user by copying and pasting the url                                                                                    | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Checkout         | All                            | Ensure that the 'adjust bag' button navigates back to the bag page                                                                                                                 | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Checkout         | All                            | Ensure that Stripe webhooks succeed in the event of a successful card payment                                                                                                            | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Checkout         | All                            | Ensure that Stripe webhooks fail in the event of a unsuccessful card payment, and that feedback is given to the user                                                                     | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Checkout         | All                            | Ensure that an order confirmation email is sent to the customer                                                                                                                          | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| **About**            | All                            | Ensure all content, including 'Our Philosophy' rendering as it should on About page                                                                                                                                             | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| **Blog**             | All                            | Ensure all blog posts added are displayed                                                                                        | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Blog             | All                            | Ensure that Blog title and post submission are displayed                                                                | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Blog             | All                            | Ensure that images are displayed if present for that post in the database                                                                                                                | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Blog             | All                            | Ensure that the 'Add Post' button below blogs is not displayed                                                                                                                 | Pass                                          |         | Pass  | Pass           | Pass               |
| Blog             | Superuser                      | Ensure that 'Edit' and 'Delete' links are displayed beneath each blog post                                                                                                           | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Blog             | Superuser                      | Ensure that 'Edit' navigates to the 'Edit_blog' page                                                                                                                                | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Blog             | Superuser                      | Ensure that 'Delete' opens a confirmation modal                                                                                                                                     | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Blog             | Superuser                      | Ensure that choosing 'cancel' in the modal, nothing further happens and it reverts back to the previous page                                                                    | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Blog             | Superuser                      | Ensure 'confirm' in the delete post modal, the post is deleted                                                                                                           | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Blog             | Superuser                      | Ensure that the 'Add Post' button navigates the user to the 'Add blog' page                                                                                                              | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| **Contact**          | All                            | Ensure contact form renders                                                                                                                                                         | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Contact          | All                            | Ensure form will not submit without required fields being filled in                                                                                                                 | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Contact          | All                            | Verify that contact form submits and sends a confirmation message to user                                                                                                                        | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Contact          | All                            | Ensure that the cancel button navigates to the home page                                                                                                                                 | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| **Faq**              | All                            | Ensure all FAQs are displayed                                                                                             | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Faq              | All                            | ENsure the question and answer are displayed, and that the  Faqs are displayed                                                | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Faq              | Non-superuser                  | Ensure that 'Add Faq' button is not displayed                                                                                                                    | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Faq              | Superuser                      | Ensure that 'Edit' and 'Delete' are displayed beneath each Faq                                                                                                                   | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Faq              | Superuser                      | Ensure that 'Delete' opens a confirmation modal                                                                                                                                      | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Faq              | Superuser                      | Ensure when selecting 'cancel' in the delete Faq modal it closes the modal without any delete action being taken                                                                      | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Faq              | Superuser                      | Ensure that on clicking on 'confirm' in the delete faq modal, the faq is removed                                                                                                            | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Faq              | All                            | Ensure that the 'contact' link navigates to the contact page                                                                                                                          | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| **Profile**          | Logged in Registered Users     | Verify that the Profile page loads                                                                                                                                                       | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Profile          | Logged in Registered Users     | Verify that the session user's billing information and order history is displayed correctly                                                                                              | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Profile          | All                            | Ensure that the profile page prompts login page to render if a different user copying and pasting the url                                                                                            | Pass                                          | Pass    | Pass  | Pass           | Pass               |
| Profile          | Logged in Registered Users     | Ensure the 'Update Information'  button updates the user's billing information                                                                                                      | Pass                                          | Pass    | Pass  | Pass           | Pass               |
---
## Testing User Stories

To ensure the site meets user expectations, I tested each of the user stories categorised below:

### First Time User
- *I want to easily navigate around the site so that I can find what I am looking for quickly*
    - With the implementation of the site sticky navbar and footer across all pages, links are clearly marked allowing the user to navigate easily around the site
    - Each of the buttons on each page is clearly marked and functional
    - The site is consistent in appearance without anything unexpected or hidden from the user, with many options to redirect to the home page if need be.

- *I want to view the site on all screen sizes so that I can view across all devices*
    - The site has been tested across many browsers and screen sizes successfully and with the use of Google Developer Chrome Tools, Responsinator and Browserstack this was an important feature to test out frequently throughout development.

- *I want to view a list of products available to buy*
    - The user is able to view a list of products through either the All Products page or by category. They can refine their search by clicking the category tabs at the top of the page:
    ![image](https://res.cloudinary.com/elerel/image/upload/v1628612069/categorytabs_waj1ci.png
    )

- *I want to be able to view individual product details so I can see exactly what I am buying*
    - The user simply clicks on the item image and are navgated to the product detail page where there is a non-lengthy description, size and quantity selector box and proceed to their shopping bag from there
    - The names, categories and price all match the same item selected from the product page 

- *I want to be able to read about the company so that I gain trust and support local business*
    - Should the user wish to find out more about the company's values and origins they can select 'About Us' that is found on the navbar across all pages
    - In addition, they can contact the company should they have any queries

- *I want to be able to search for categories of products so that I can find the best-rated/priced products in a specific category*
    - The 'Sort By' selector box is useful in assisting the user to select categories and this is present on every product page throughout the site:
    ![image](https://res.cloudinary.com/elerel/image/upload/v1628612699/sortbybox_ifoccm.png)

- *I want to be able to view items selected in the shopping bag so I easily see how much I am spending*
    - The user can at any time view their total spend by viewing the total amount above the shopping bag icon- each time an item is added or removed, the total amount reflects this change
    - If the user clicks on the shopping bag icon/total amount in the navbar, they are navigated to the shopping bag

- *I want to be able to adjust or remove items from the shopping bag in case I change my mind*
    - Their shopping bag can be adjusted by clicking on the bag icon in the navbar and then they are redirected to the shopping bag
    - Once they are in the shopping bag page, they can adjust the bag by choosing the amount using the quantity selector box or remove the item completely by selecting 'Remove' - both options present below the quantity selector box:
    ![image](https://res.cloudinary.com/elerel/image/upload/v1628613418/updatebag_puyd4r.png)

- *I want to access contact details so that I can get in touch with any questions*
    - A Contact Us link is available in the About Us dropdown item in the navbar and in the footer, under Company menu should the user wish to access the contact page
    - Once the user is on the Contact page, they will find more contact details and can also submit the form with any questions they might have

- *I want to easily access social media about the company to discover their social media presence*
    - The user can find the company social links in the left-hand-side footer and each page then opens up in a new tab

- *I want to be able to register for a user profile account by choosing a username or password so that I can store my personal details and purchase history*
    - The user can easily set up their own account by clicking 'Register' in under 'My Account' present on the navbar. This link is also available in the company section in the footer. 

- *I want to be able to make purchases as a guest user so that I dont need to set up an account if I dont want to*
    - The user can still make purchases from the site without signing up creating a better user experience if they wish to purchase something in a hurry. The user just needs to fill out the forms and will be notified the same way a registered user is by email of purchase confirmation. They need to create an account if they wish to have their billing information saved for the next time they come to purchase.

### Registered User 

- *I want to be able to log in and out of my profile to protext my information whilst not active on the site*
    The user can log in and out of the site from 'My Account' link on the navbar. They are informed when they log in and out with a success toast message:

    - Signed in:
    ![image](https://res.cloudinary.com/elerel/image/upload/v1628614767/signedin_qzt545.png)

    - Sign out prompt: 
    ![image](https://res.cloudinary.com/elerel/image/upload/v1628614799/signoutprompt_kr50hw.png)

    - Signed out: 
    ![image](https://res.cloudinary.com/elerel/image/upload/v1628614825/signedout_oedqkb.png)

- *I want to be able to update my details so that I can update address or other details in case they change*
    - Once the user is signed in, they simply click on 'My Profile' from the 'My Account' link in the navbar. Then they are navigated to the profile page where they can update the form and select 'Update Information':
    ![image](https://res.cloudinary.com/elerel/image/upload/v1628615002/updateinfo_wxnoti.png)
    - Information is then updated and user is notified:
    ![image](https://res.cloudinary.com/elerel/image/upload/v1628615099/profileupdated_q4hkmp.png)

- *I want to be able to store my address for later use to avoid retyping it every time I make a purchase*
    - The user's address is automatically saved when they are logged in and make a purchase for the first time- from here it is saved to their profile. A further implementation would be to have a selector box with the option to choose if the billing address is different to the delivery address and if selected, another address form would appear.

- *I want to be able to store my purchase history so that I have access to the previous purchase history*
    - In the user's profile page, the right side of the page contains the user's oder history containing the order number, date of purchase, items bought and total paid. If they click on the order number they are then redirected to that previous purchase confirmation page.
    - The user is notified that is it a past confirmation for that order they are viewing by use of an alert message:
    ![image](https://res.cloudinary.com/elerel/image/upload/v1628615526/alert_zthpo1.png)

- *I want to store my choices in checkout so that I can go back to the site in case I wish to add more products later on*
    - The user's added items to the bag will remain in their bag unless the session cookie id is deleted or they visit the site again from a different browser. A feature I would have liked to implement is set up a favourites section in the user profile so they can save their items to purchase for another time.

- *I want to be able to make secure payments and ensure my payments are handled securely*
    - The user can be assured that through use of Stripe their payments are handled securely. They are notified below the 'Complete Order' button how much their card will be debited.

- *I want to be able to receive an email confirmation of payment*
    - The user will receive an email confirming that their payment and order went through successfully. Another feature to add to the site in this regard would be to send an email to the user should they unexpectedly close their browser before the purchase is made, so that they can return to that exact page from their email.
    - The confirmation email will detail all the purchase information of that particular transaction. Should they need, they can contact the site admin from that email if they have any questions.

## Site Owner User Stories    

The site owner, superuser or admin can access the admin panel from the 

#### [Back to contents](#contents)

#### [Back to README.md](README.md)