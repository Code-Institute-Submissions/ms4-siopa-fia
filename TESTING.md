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

- W3 HTML Validator Results:
![image](https://res.cloudinary.com/elerel/image/upload/v1627549562/w3HTMLchecker_px7ncd.png)

The error showing was in regards to the type attribute under the postblockjs section (toasts) in the base.html page- I later removed this and it made no difference to the code.


### Performance

Lighthouse Testing:

- Added the suggested attribute 'rel="noreferrer"' to each of the anchor tags to improve the best practices score:
![image](https://res.cloudinary.com/elerel/image/upload/v1627475064/lighthouse1_ykmloo.png)

- To improve optimization, I included the word "unsubscribe" in the anchor tag  so the user knows where the link directs:
![image](https://res.cloudinary.com/elerel/image/upload/v1627475157/seo_dhrrq1.png)

The other notes included in the lighthouse testing included how the site failed the PWA (progressive Web Apps) instability requirements, which I ignored for now.
