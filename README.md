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
2. [User Experience (UX)](#user-experience-(ux))
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits) 
---
## Aim
The aim of this django app is to create an interactive interface where users can find out
information about Elwood Castle and book tickets to events held there.  
This app is to be a one stop shop where users can create accounts,
learn more about events and visiting the castle, contact the castle if required and
purchase tickets to upcoming events.

---
## User Experience (UX)
### User Stories
#### Users:
| As a... | I would like... | So I can ... |
| :------ | :-------------- | :----------- |
| User    | Simple navigation to the whole site | Find exactly what I want without searching through links |
| User    | To easily see my basket | Checkout quickly |
| User    | Consistant styling across the site | Navigate across the site without having to think too hard about what elements do |
| User    | A profile page |	Quickly see my orders and checkout details |
| Returning User | To be able to save my default settings | Easily use them to book new events |
| New User | To be able to create an account | Save my details and view my orders |
| Returning User | To be able to reset my password | Update my password if I forget it |
| User    | A contact page where I can find email and phone details of the castle | Get in contact if I have a question about an event |
| User    | Details on the location of the Castle | Find the castle and attend events |
| User    | Booking events to be simple | Avoid filling out too many inputs |
| User    | Confirmation of my bookings | Know that my purchase has worked |
| User    | A date picker for event bookings | Easily visulise what date I'm picking and avoid filling in an input |
| User with a profile | A list of my upcoming and past events | Know what events I have booked |

#### Owners:
| As a... | I would like... | So I can ... |
| :------ | :---------------| :----------- |
| Owner	| Simple navigation to the event pages | Encourage users to buy tickets to events |
| Owner	| Lots of links back to event pages | To get users to buy more tickets |
| Owner	| Links between an event's details page and booking page | Make it easy for users to book events and reduce time spent thinking about this decision |
| Owner	| Professional and clean styling | Keep the site attractive to users without diminishing the castle brand |
| Owner	| Login validation | To prevent users from creating multiple accounts with the same email |
| Owner	| Email verification on accounts | To prevent malicious users from easily creating multiple accounts |
| Owner	| A FAQ page | Prevent too many incoming calls and emails |
| Owner	| Details on visitings the castle | Make sure users know how to get to the castle |	
| Owner	| Bookings to be kept in a basket  | Make sure users only have to pay once, encouraging them to purchase more |
| Owner	| Order Confirmation work even if a user navigates away from the checkout page | Know users haven't purchased tickets without the models updating |
| Owner	| Dates where events are booked up to be unpickable | Know that users haven't purchased tickets to events which won't be able to cater for them |
| Owner	| Validation on the date picking input | Make sure users don't create bookings using dates which aren't correct |
| Owner	| Validation on the ticket input | Stop users booking too many tickets for events which are nearly full |
| Owner/User | Responsive design | Easily use the site across multiple devices |
| Owner/User | Message stlying to be intuitive (red for alerts, green for success) | Quickly understand want the message is trying to convey |	

### Information Architecture
#### Overview
For Elwood Castle a relational database using SQL was the best choice to store the information.
The reasoning behind this choice is because users can't directly add items to the database which
would have wildly unknown values. All orders would follow a similar structure which is where the
users have most control over what is inputted. Unlinke a movie database where each field may store
very different values, here all entries would have a very similar structure with values which don't vary
in data type (i.e. strings or integers) so a relational database made sense. The models built in the Django
framework provide great validation ot prevent incorrect values being added so its extremely unlikely
that Elwood Castle would need a databse structure like MongoDB where unknown values are expected to
be inputted frequently.

The information in each model would also be related to another model in almost all cases. All *orders* have
*bookings* which have *events* etc, having such interlinked models required a relational database to easily
handle the data and prevent creating a large database with lot's of repeated values.

#### Models 
##### User
This inbuilt model is used by Django. Here there was no changes made as it would suit the rest of the models nicely

##### UserAccount
This model builds on the user model provided by Django so that a user could save which orders and
bookings they have made. In the future, if a Subcription service was created it would also tack on
nicely to this model.
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| user | OneToOneField | (related field) User, on_delete=models.CASCADE, related_name='useraccount' |
| first_name | CharField | max_length=100, null=True, blank=True |
| last_name | CharField | max_length=200, null=True, blank=True |
| email | EmailField | max_length=200, null=True, blank=True |
| phone_number | CharField | max_length=20, null=True, blank=True |

##### Event 
This model stores the key information used by our date picker to validate
ticket numbers and dates which are full when a user tries to book and event.
Other than having these key details this model also stores information the user may
want to know about an event before they book it.
In future if events start taking place on selective days of the week, this would
slot in nicely to this model.
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| category | ForeignKey | (related field) Category, null=True, blank=True, on_delete=models.SET_NULL |
| name | CharField | max_length=254 |
| description | TextField |  |
| price | DecimalField | max_digits=8, decimal_places=2, blank=False |
| start_time | TimeField |  |
| rating | DecimalField | max_digits=2, decimal_places=1, null=True, blank=True |
| day_ticket_limit | PositiveIntegerField | blank=False, validators=[MaxValueValidator(200)] |
| supervision | BooleanField | default=True, null=True, blank=True |
| age_restricted | BooleanField | default=True, null=True, blank=False |
| image | ImageField | null=True, blank=True |

##### Category
This model is a simple one used to store the different type of categories each event can fall into.
New categories can be easily added in the castle decides to start hosting new types of events, along
with allowing current event to easily change their category.
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| name | CharField | max_length=50, null=False, blank=False |
| friendly_name | CharField | max_length=100, null=True, blank=True |

##### Order
This is a simple model used to store orders which contain EventBookings.  
It's relation to EventBookings and UserAccounts allows users to see their upcoming
and past bookings on their profile page. It also has a stripe_id so site owners
can check to see for multiple bookings and validation preventing orders from being created
twice by mistake.
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| user_account | ForeignKey | UserAccount, null=True, blank=True, on_delete=models.SET_NULL, related_name='orders' |
| order_number | CharField | max_length=32, null=False, editable=False |
| first_name | CharField | max_length=100, null=False, blank=False |
| last_name | CharField | max_length=200, null=False, blank=False |
| email | EmailField | max_length=200, null=False, blank=False |
| phone_number | CharField | max_length=20, null=True, blank=True |
| date | DateTimeField | auto_now_add=True |
| stripe_id | CharField | max_length=27, null=False, blank=False |
| total | DecimalField | max_digits=7, decimal_places=2, null=True, blank=False, default=0 |

##### EventBooking
This model is used to store each event booked by a user, along with the date and amount of tickets.  
The EventBookings relation to order is used to show upcoming and past events on the users
profile page. The ticket and date fields are also used by the ticket and date validators
when a user tries to book a new event.
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| confirmation_number | CharField | max_length=32, null=False, editable=False |
| order | ForeignKey | (related model) Order, null=False, blank=False, on_delete=models.CASCADE, related_name='bookings' |
| event | ForeignKey | (related model) Event, null=False, blank=False, on_delete=models.CASCADE, |
| date | DateField | auto_now=False, auto_now_add=False, null=False, blank=False |
| ticket_quantity | IntegerField |  |
| booking_total | DecimalField | max_digits=7, decimal_places=2, null=False, blank=False, editable=False, default=0 |

### Wireframes
All wireframes can be found in [Here]()
For induvidual files, click the relevant name:
  * [Navbar]()
  * [Footer]()
  * [Index page]()
  * [Events page]()
  * [Event Details page]()
  * [Book Event page]()
  * [View Basket page]()
  * [Checkout page]()
  * [Checkout Success page]()
  * [User Home page]()
  * [Order Summary page]()
  * [Visit page]()
  * [FAQ page]()
  * [Contact page]()

### Design Choices
#### Target Demographic

## Features
### Existing Features
* #### : 

### Features Left to Implement
* #### :
---
## Technologies Used
### Languages
* [HTML5](https://html.spec.whatwg.org/multipage/) - Used to create the structure of the website.
* [CSS3](https://www.w3.org/Style/CSS/Overview.en.html) - Used to style the website.
* [JavaScript](https://www.javascript.com/) - Used for stripe functionality, as well as Bootstrap & google maps api functionality and the date-picker element.
* [Python (v3.8.6)](https://www.python.org/) - Used to handle backend programming within the Django framework.
### Libraries
* [Google Fonts](https://fonts.google.com/) - Used for website fonts [Lora](https://fonts.google.com/specimen/Lora) for headings, [Raleway](https://fonts.google.com/specimen/Raleway) for content text and [IM Fell French Canon SC](https://fonts.google.com/specimen/IM+Fell+French+Canon+SC) for logo text.
* [Font Awesome](https://fontawesome.com/) - This library provided the Icons used across the site.
* [jQuery](https://jquery.com/) - Included with Bootstrap, also used to code various elements such as the date-picker, stripe functionality and google maps api.
* [Stripe API Library](https://stripe.com/gb) - Used to handle the payments send from the Elwood Website.
### Frameworks
* [Django v3.1.4](https://docs.djangoproject.com/en/3.1/) - Framework used to create the app along with inbuilt templating language.
* [Bootstrap v4.5](https://getbootstrap.com/docs/4.5/getting-started/introduction/) - Framework to add structure & styling to the site, along with resposive breakpoints and pre-built elements.
### Tools 
* [Git](https://git-scm.com/) - Used for version control and tracking changes to the code whilst in development.
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Key for finding bugs and testing responsive design.
* [Autoprefixer](https://autoprefixer.github.io/) - Used to prefix the css, allowing it to work across different browsers.
* [AWS S3](https://aws.amazon.com/s3/) - Used for storing static and media files used across the site.
* [Heroku]() - Used to deploy and host the finished site.
* [Heroku Postgres](https://www.heroku.com/postgres) - Used to serve the database Elwood Castle manages event and user data with.
---
## Testing
See the [testing write up](https://github.com/SDGreen/elwood-castle/blob/master/TESTING.md) for full details on testing.

---
## Deployment

### How to run Elwood Castle's website code locally:
#### Setting up the code:

#### Creating a database:


#### Adding enviroment varibales:

#### Running the app


---
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

Logos created using [Canva](https://www.canva.com/):
* [Color Logo](https://github.com/SDGreen/elwood-castle/blob/master/static/logos/logo_color.jpg) (file name: logo_color.jpg)
* [Dark Logo](https://github.com/SDGreen/elwood-castle/blob/master/static/logos/logo_dark.png) (file name: logo_dark.png)
* [Large Dark Logo](https://github.com/SDGreen/elwood-castle/blob/master/static/logos/logo_dark_large.png) (file name: logo_dark_large.png)
* [Light Logo](https://github.com/SDGreen/elwood-castle/blob/master/static/logos/logo_light.png) (file name: logo_light.png)
* [Navbar Logo](https://github.com/SDGreen/elwood-castle/blob/master/static/logos/navbar_logo.png) (file name: navbar_logo.png)


Favicon created using [Favicon.io](https://favicon.io/favicon-converter/) from edited logo:
* [Favicon](https://github.com/SDGreen/elwood-castle/blob/master/static/logos/favicon.png) (file name: favicon.png)

### Code
* Google map created using [Google Maps JS API](https://developers.google.com/maps/documentation/javascript/tutorial)
* Date picker created using [bootstrap-datepicker](https://bootstrap-datepicker.readthedocs.io/en/latest/)
* CSS prefixer used: [https://autoprefixer.github.io/](https://autoprefixer.github.io/)
---