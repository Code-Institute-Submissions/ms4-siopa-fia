<div align="center">
<h1 align="center">MS4: Testing Section</h1>
</div>

## Contents

- [Validation](#validation)
- [Performance](#performance)
- [Device Testing](#device-testing)
- [Fixed Bugs](#fixed-bugs)
- [Known Bugs](#known-bugs)
- [Links and Navigation](#links-and-navigation)
- [Testing User Stories](#testing-user-stories)

---

### Validation

- [W3 HTML Validator](https://validator.w3.org/) Results:

![image](https://res.cloudinary.com/elerel/image/upload/v1627549562/w3HTMLchecker_px7ncd.png)

The error showing was in regards to the type attribute under the postblockjs section (toasts) in the base.html page- I later removed this and it made no difference to the code.

- [W3 Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) Results:

![image](https://res.cloudinary.com/elerel/image/upload/v1627550328/cssvalidation_hfhkp5.png)

Two errors were displayed upon results showing- I wasn't overly concerned about this since they are originating from the Bootstrap CDN and would be out of my control.

- [JSHint](https://jshint.com/): 

![image]https://res.cloudinary.com/elerel/image/upload/v1627551061/jshint_cpa9z3.png)

Just the one error here regarding the missing semi-colon (line 119 in stripe-elements.js) which I subsequently added and no further errors followed.

- [PEP8](http://pep8online.com/):

![image](https://res.cloudinary.com/elerel/image/upload/v1627554718/pep8_q7qj4z.png)

The screenshot above shows the main issues that popped up across several views.py pages- I made sure to address these and no further errors were displayed.

![image](https://res.cloudinary.com/elerel/image/upload/v1627554869/pep8blog_whsula.png)




### Performance

Lighthouse Testing:

- Added the suggested attribute 'rel="noreferrer"' to each of the anchor tags to improve the best practices score:
![image](https://res.cloudinary.com/elerel/image/upload/v1627475064/lighthouse1_ykmloo.png)

- To improve optimization, I included the word "unsubscribe" in the anchor tag  so the user knows where the link directs:
![image](https://res.cloudinary.com/elerel/image/upload/v1627475157/seo_dhrrq1.png)

The other notes included in the lighthouse testing included how the site failed the PWA (progressive Web Apps) instability requirements, which I ignored for now.

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
Fix? 

- Unsubscribe link not displaying (its in a text file, may need to change this to a html file instead?)


