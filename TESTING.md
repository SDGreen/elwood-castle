## Testing
### User Stories tested

> As a User, I would like simple navigation to the whole site, so I can find exactly what I want without searching through links.

* Users are never more two clicks away from parts of the site that they are expected to access quickly. 
On some smaller devices contact, FAQ and visit pages are 3 clicks away but they are always easily accessible 
from the fixed Navabar.  
Seeing old order summaries does take more clicks to access but this is not expected to be a key
feature users need to view in a rush and user will also have their order emails.

> As a User, I would like to easily see my basket, so I can checkout quickly.

* Users can always click on their basket which is in the top right of the screen. As it is a key feature, at smaller 
breakpoints this basket icon remains in place rather then entering the mobile dropdown menu.

> As a User, I would like consistant styling across the site, so I can navigate across the site without having to think too hard about what elements do.

* All buttons and text-links have consistant styling. Disabled buttons (such as checkout and book under certain condition) 
actually colour & no longer react to being hovered over so users can tell something has changed
and the action that would usually occur will not.

> As a User, I would like a profile page, so I can quickly see my orders and checkout details.

* Logged in users can easily access their user home page under the account dropdown in the navbar. 
This single page relays upcoming bookings, past bookings, their default details used at checkout 
and their orders. Orders numbers can be clicked to get a full summary.

> As a Returning User, I would like to be able to save my default settings, so I can easily use them to book new events.

* On the user home page, users can update their details which will be used next time they checkout. If a user 
updates their details, a confirmation toast appears letting them know the action has 
occured. The page is reloaded showing the new details. If there is an error then the page still reloads 
but an error message appears informing them there was an issue updating the details.

> As a New User, I would like to be able to create an account, so I can save my details and view my orders.

* New users can quickly create an account from the account dropdown by clicking 'Register'. Once their details
have been filled out and validated they are sent a confirmation email asking them to verify their account.

> As a Returning User, I would like To be able to reset my password, so I can update my password if I forget it.

* Under the login option on the Login page their is a 'forgot password' option which allows users to update their 
password. A link is sent to their email which they can use to update the users password. Info toasts are sent 
when the email have been sent and a success toast appears once they have completed updating their password.

> As a User, I would like a contact page where I can find email and phone details of the castle, so I can get in contact if I have a question about an event.

* Under the info dropdown you can access the contact page. The first option is a form to send an email to the castle. 
Underneath this form the phone number can be found.

> As a User, I would like details on the location of the Castle, so I can find the castle and attend events.

* On the FAQ page a google map is loaded with the location of the castle along with full address into.

> As a User, I would like booking events to be simple, so I can avoid filling out too many inputs.

* Booking an event on the site is incredibly easy. There are just two inputs, once a date has been picked 
the avaliable tickets for that date appears under the ticket quantity input so users can quickly know if that
date is suitable for them.

> As a User, I would like confirmation of my bookings, so I can know that my purchase has worked.

* Once a order has been saved to the database and this has been verified by the webhook handler then a email confirming 
the order is sent out. Additional emails are also sent per booking. Checkouts which experience no issues redirect the user 
to a checkout success page which verifies an order is completed (along with the emails).
Logged in users can also check an order by looking at their order history.

> As a User, I would like a date picker for event bookings, so I can easily visulise what date I'm picking and avoid filling in an input.

* When users try to book an event and click on the date input, a date picker is displayed on the page.

> As a User with a profile, I would like a list of my upcoming and past events, so I can know what events I have booked.

* A user's account home page displayed upcoming and past bookings in date order so they can see all the events they have booked.

> As a Owner, I would like simple navigation to the event pages, so I can encourage users to buy tickets to events.

* The event page is one of the first links seen on the landing page, along with being the second link after home in the navbar.
On the mobile navbar it is the second link after home.

> As a Owner, I would like lots of links back to event pages, so I can get users to buy more tickets.

* There are multiple links back to the events pages. There is one on the landing page, links appear in empty baskets 
and user profiles who have no bookings. After successful checkouts, users are linked back to events & baskets have 
an option to go back to events or checkout. After a user successfully adds a booking to their basket or logs in they 
are redirected to the events page and not the basket page. These all provide users ample chance to get back to events
and add more bookings.

> As a Owner, I would like links between an event's details page and booking page, so I can make it easy for users to book events and reduce time spent thinking about this decision.

> As a Owner, I would like professional and clean styling, so I can keep the site attractive to users without diminishing the castle brand.

> As a Owner, I would like login validation, so I can prevent users from creating multiple accounts with the same email.

> As a Owner, I would like email verification on accounts, so I can prevent malicious users from easily creating multiple accounts.

> As a Owner, I would like a FAQ page, so I can prevent too many incoming calls and emails.

> As a Owner, I would like details on visitings the castle, so I can make sure users know how to get to the castle.

> As a Owner, I would like bookings to be kept in a basket, so I can make sure users only have to pay once, encouraging them to purchase more.

> As a Owner, I would like order confirmation work even if a user navigates away from the checkout page, so I can Know users haven't purchased tickets without the models updating.

> As a Owner, I would like dates where events are booked up to be unpickable, so I can know that users haven't purchased tickets to events which won't be able to cater for them.

> As a Owner, I would like validation on the date picking input, so I can make sure users don't create bookings using dates which aren't correct.

> As a Owner, I would like validation on the ticket input, so I can stop users booking too many tickets for events which are nearly full.

> As a Owner/User, I would like responsive design, so I can easily use the site across multiple devices.

> As a Owner/User, I would like message stlying to be intuitive (red for alerts, green for success), so I can quickly understand want the message is trying to convey.
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

The app was physically tested on the following browsers:
* Microsoft Edge version 86.0.622.63
* Chrome version 87.0.4280.88 
* Firefox version 81.0
* Safari version 14.0.5 (15610.1.28.1.9)

### Code Validation
* HTML5 code validated using [https://validator.w3.org/](https://validator.w3.org/)
* CSS3 code validated using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)
* JS code validated using [https://jshint.com/](https://jshint.com/)
* Python code validated using [Extend Class Python Validator](https://extendsclass.com/python-tester.html)



### Bugs

    