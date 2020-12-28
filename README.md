# Elwood Castle
![Elwood Castle](https://github.com/SDGreen/elwood-castle/blob/master/flat_pages/static/flat_pages/images/background.jpg?raw=true)
### Deployed site: [https://elwood-castle.herokuapp.com/](https://elwood-castle.herokuapp.com/)

#### For testing the following credentials be used:
* User Credentials:  
  - Username: TestUser  
  - Password: testingelwood  
  - Email: test@test.com 

* Card payments:
  - card number: 4242 4242 4242 4242
  - Zip & CCV must be filled out with any integers
---
## Table of Contents
1. [Aim](#aim)
2. [UX](#ux)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits) 

---

## Aim
The aim of this django app is to create an interactive interface where users can find out information about Elwood Castle and book tickets to events held there.  
This app is to be a one stop shop where users can create accounts, learn more about events and visiting the castle, contact the castle if required and purchase tickets to upcoming events.
## UX

### User Stories


### Information Architecture

### Wireframes

### Target Demographic

### Design Choices

## Features
### Existing Features
* #### : 

### Features Left to Implement
* #### :
## Technologies Used
* [HTML5](https://html.spec.whatwg.org/multipage/) - To create the structure of the page.
* [CSS3](https://www.w3.org/Style/CSS/Overview.en.html) - Used to style the website.
* [Materialize v0.100.2/](http://archives.materializecss.com/0.100.2/) - This framework was used to create a responsive mobile-first design, along with some components (listed in [credits](#credits)).
* [JavaScript](https://www.javascript.com/) - Included with Materialize for their framework to function.
* [jQuery](https://jquery.com/) - Included with Materialize, also used to code form_fields.js, password_validator.js and searchbar_fields.js (along with some javaScript)
* [Python (v3.8)](https://www.python.org/) - Used to code the base app.py which runs the website using the Flask framework. Also used to facilitate MongoDB operations.
* [Flask (v1.1.2)](https://flask.palletsprojects.com/en/1.1.x/) - Framework used to create the app which runs the website.
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Templating language used for the website pages.
* [MongoDB](https://docs.mongodb.com/) - Used to host the database along with retrieve data, save edits, deletions and inserts.
* [Git](https://git-scm.com/) - Used for version control and tracking changes to the code whilst in development.
* [Google Fonts](https://fonts.google.com/) - Used for website fonts [Didact Gothic](https://fonts.google.com/specimen/Didact+Gothic) for headings, [Raleway](https://fonts.google.com/specimen/Raleway) for content text and [Special Elite](https://fonts.google.com/specimen/Special+Elite) for logo text.
* [Font Awesome](https://fontawesome.com/) - This library provided the Icons used across the site.
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Key for finding bugs and testing responsive design.
* [Autoprefixer](https://autoprefixer.github.io/) - Used to prefix the css, allowing it to work across different browsers.

## Testing


### Database CRUD Operations:


* #### 

* #### Update Operations:
    * When a user tries to update one of their films, a form is generated with all the existing data already filled in.
    * Once updated, the new data now is in the database instead.
    * If a user adds a movie to their watchlist or favourites, that movie's ID appears in the users relevant list.

* #### Delete Operations:
    * When a user deletes their movie, it is removed from the database and their submitted movies list.

### User Validation:

* #### Login Validation:
    * Users can't login with an incorrect password. The respective error message appears.
    * Users can't login with the incorrect username. The appropriate error message appears.

* #### Sign Up Validation:
    * Users can't create an account with a username currently in the database. The appropriate error message appears.
    * Users can't create an account with an email currently in the database. The correct error message appears.
    * If the password and retype password fields don't match, the login button is disabled.
    * Users can't create passwords under 5 or over 20 characters long.
    * Users can't create usernames under 3 or over 10 characters long.

* #### User is Logged On Validation:
    * If a user is logged in, the navbar "Login" button turns into an account dropdown menu.
    * If the user is logged in, links to the login page on the homepage and footer redirect to the user's homepage.
    * If the user is logged in, the movie cards display "add to watchlist" and "add to favourites" options.
    * If the user is logged in, the movie pages display "add to watchlist" and "add to favourites" options at the bottom of the page.
    * If the user is logged in and on a movie page they created, the update and delete buttons appear.
    * If a user isn't logged in, calls to login appear on the browse, search and movie pages.
    * Movie cards and movie pages will display remove from watchlist/favourites option if that movie is already in the list in question.

### DOM Manipulation:

* If the options arrow is clicked on the search bar, a larger form will appear below with more search fields. If clicked again this form is collapsed.
* If a user clicks on the plus icon on the update/insert movie forms, a new input field will appear.
* If the minus icon is click on the update/insert movie forms, new inputs will be deleted but the original cannot be.

#### Responsive Design Testing
The responsive design was tested using multiple physical devices:
* Galaxy S8 (Chrome)
* iPhone 6 plus (Safari)
* iPad Air 2 (Safari)
* Leveno IdeaPad S340 (Chrome)
* MacBook (Chrome & Safari)
* iPhone X (Safari)

Chrome DevTools was also used to test the design on the following devices:
* Moto G4
* Galaxy S5
* Pixel 2
* Pixel 2 XL
* iPhone 5/SE
* iPhone 6/7/8
* iPhone 6/7/8 Plus
* iPhone X
* iPad 
* iPad Pro

### Browser testing

Spooky Spool was physically tested on the following browsers:
* Microsoft Edge version 86.0.622.63
* Chrome version 86.0.4240.111 
* Firefox version 81.0
* Safari version 14.0.5 (15610.1.28.1.9)

### Code Validation
* HTML5 code validated using [https://validator.w3.org/](https://validator.w3.org/)
* CSS3 code validated using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)
* JS code validated using [https://jshint.com/](https://jshint.com/)
* Python code validated using [Extend Class Python Validator](https://extendsclass.com/python-tester.html)
### User Stories tested
#### As a user, I want to know what I can actually do with this website, so I'll know if I want to create an account.

### Bugs

    
## Deployment

### How to run Spooky Spool's website code locally:
#### Setting up the code:

#### Creating a database:


#### Adding enviroment varibales:

#### Running the app



## Credits
### Media


Copyright free images taken from [Pxhere](https://pxhere.com/)
* [Archer](https://pxhere.com/en/photo/1410420) (file name: archer.jpg)
* [Armour Set](https://pxhere.com/en/photo/615382) (file name: helmet.jpg)
* [Baking](https://pxhere.com/en/photo/757323) (file name: baking.jpg)
* [Banquet Hall](https://pxhere.com/en/photo/830346) (file name: banquet.jpg)
* [Blacksmith's Forge](https://pxhere.com/en/photo/1272972) (file name: blacksmith.jpg)
* [Carousel](https://pxhere.com/en/photo/879353) (file name: carousel.jpg)
* [Dried flowers](https://pxhere.com/en/photo/1231000) (file name: perfume.jpg)
* [Coat of Arms](https://pxhere.com/en/photo/535891) (file name: crest.jpg)
* [Crossed Swords](https://pxhere.com/en/photo/1570543) (file name: swords.jpg)
* [Crayons](https://pxhere.com/en/photo/608898) (file name: caryons.jpg)
* [Elwood Castle](https://pxhere.com/en/photo/1056258) (file name: background.jpg)
* [Elwood Gardens](https://pxhere.com/en/photo/1190433) (file name: background-gardens.jpg)
* [Elwood Grounds](https://pxhere.com/en/photo/1398482) (file name: background-grounds.jpg)
* [Falcon](https://pxhere.com/en/photo/551960) (file name: falcon.jpg)
* [Gallery Hall](https://pxhere.com/en/photo/1059117) (file name: halls.jpg)
* [Haunted Hall](https://pxhere.com/en/photo/870234) (file name: spooky.jpg)
* [Jousting Knight](https://pxhere.com/en/photo/590971) (file name: joust.jpg)
* [Kid's Castle](https://pxhere.com/en/photo/862705) (file name: small-castle.jpg)
* [Knight](https://pxhere.com/en/photo/687171) (file name: knight.jpg)
* [Library](https://pxhere.com/en/photo/707871) (file name: library.jpg)
* [Mead Bottles](https://pxhere.com/en/photo/1032511) (file name: bottles.jpg)
* [Old Kitchen](https://pxhere.com/en/photo/1069371) (file name: kitchen.jpg)
* [Puppet](https://pxhere.com/en/photo/896895) (file name: puppet.jpg)
* [Sparkler](https://pxhere.com/en/photo/1169641) (file name: sparkler.jpg)
* [Spice Market](https://pxhere.com/en/photo/959535) (file name: spices.jpg)
* [Tapestry](https://pxhere.com/en/photo/575238) (file name: tapestry.jpg)
* [Teacup](https://pxhere.com/en/photo/649039) (file name: tea.jpg)
* [Wine Glasses](https://pxhere.com/en/photo/733330) (file name: romantic.jpg)






Logos created using [FreeLogoDesign](https://www.freelogodesign.org/):


Favicon created using [Favicon.io](https://favicon.io/favicon-converter/) from edited logo:
* [Favicon](https://github.com/SDGreen/SpookySpool/tree/master/static/images/favicon.png) (file name: favicon.png)

## Code
