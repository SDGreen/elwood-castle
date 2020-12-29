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

* On every event details page there is a direct link to book the event, along with one on the event's card before the user 
even clicks on the event to get more details.

> As a Owner, I would like professional and clean styling, so I can keep the site attractive to users without diminishing the castle brand.

* Throughout the site attention has been page not to overcrowd pages and keep styling consistant. All buttons have the same styling,
along with text-links following the same styling. Clear fonts which have some character have been used which don't 
take away from the seriousness of Elwood Castle.

> As a Owner, I would like login validation, so I can prevent users from creating multiple accounts with the same email.

* By using the AllAuth package, all accounts must have a distinct email.

> As a Owner, I would like email verification on accounts, so I can prevent malicious users from easily creating multiple accounts.

* All users have to verify their account via the email they used to create it, otherwise it cannot be accessed.

> As a Owner, I would like a FAQ page, so I can prevent too many incoming calls and emails.

* A FAQ page has been set up which provides answers to most common questions. An accordion has been picked 
to display the information in a clean manner. Users can quickly identify their issues and open up the relevant 
answer without crowding the page.

> As a Owner, I would like details on visitings the castle, so I can make sure users know how to get to the castle.

* The Visit page offers users a google map of the location of the castle, aswell as the full address and contact details.

> As a Owner, I would like bookings to be kept in a basket, so I can make sure users only have to pay once, encouraging them to purchase more.

* As users navigate through the site, unpaid bookings are held in a basket which relys on session data to stay up-to-date.
Users can use this basket to add more bookings, update bookings and remove bookings before they have to checkout.

> As a Owner, I would like order confirmation work even if a user navigates away from the checkout page, so I can Know users haven't purchased tickets without the models updating.

* If the user navigates away from the checkout page before the order is submitted to the model it is handled by the webhooks instead.
This way users can still recieve the confirmation they'd need and the Order and EventBooking models aren't missing
entries which they should have. The webhook checks the database for a order with a matching stripe_id to the 
payment intent. If this isn't found after 10 searches then the webhook handler creates the order and send the confirmation
emails.

> As a Owner, I would like dates where events are booked up to be unpickable, so I can know that users haven't purchased tickets to events which won't be able to cater for them.

* When users navigate to the book and event page, the date picker is given an array of dates which are unbookable due to the ticket 
limit being reached. The date picker then disables these dates to prevent users from booking them. 

> As a Owner, I would like validation on the date picking input, so I can make sure users don't create bookings using dates which aren't correct.

* To prevent users inputting dates, the date input only accepts inputs from the date picker.

> As a Owner, I would like validation on the ticket input, so I can stop users booking too many tickets for events which are nearly full.

* The ticket datepicker input has an event listener. This checks booked events in the database and the user's basket tickets to make sure 
they can't accidently book more ticket then are avaliable. Booked up dates in the database are disabled on the date picker. If the user
has all the tickets for a particular day in their basket then the input for that date is disabled to prevent them getting
more. If for some reason the ticket amount in the user's basket exceeds the amount avaliable at checkout, this item is rejected and 
removed from the basket before the payment can be processed as an added layer of security against over booking.

> As a Owner/User, I would like responsive design, so I can easily use the site across multiple devices.

* The site has responsive elements on almost everypage. The homepage hides the contact button on smaller devices. The navbar
collapses to a mobile dropdown on medium and small devices. The event cards hide extra detail that can be found on 
their induvidual pages on smaller screens along with reducing how many cards appear on each row. Information on the event details page,
checkout and visit page all shifts to make it easier to view on smaller devices. Images are cut from the smallest screens 
for basket, order and booking summaries to make the infomation easier to understand. Overall the site has very responsive design 
with an aim to make information more digestable (rather than just to make it move).

> As a Owner/User, I would like message stlying to be intuitive (red for alerts, green for success), so I can quickly understand want the message is trying to convey.

* Toast messages are consistantly styled so error messages produce red toast headings, success messages produce green toast headings
and info messages produce blue toast headings.

---
#### Responsive Design Testing
The responsive design was tested using these physical devices:
* Galaxy S8 (Chrome)
* Google Pixel 4a (Chrome)
* iPad Air 2 (Safari)
* Leveno IdeaPad S340 (Chrome)
* MacBook Pro(Chrome & Safari)
* iPhone X (Safari)

No major issues were uncovered

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
    * Some pages on the iPad Pro portait mode have a large amount of space before reaching the footer 


### Browser testing
The app was physically tested on the following browsers:
* Microsoft Edge version 87.0.664.66
* Chrome version 87.0.4280.88 
* Firefox version 82.0.2
    * The ticket input on this browser automatically gets a red border 
    after picking a date but this wasn't deemed a massive problem
* Safari version 14.0 (15610.1.28.1.9, 15610)

### Code Validation
* HTML5 code validated using [https://validator.w3.org/](https://validator.w3.org/)
* CSS3 code validated using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)
    * No issues found
* JS code validated using [https://jshint.com/](https://jshint.com/)
    * 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). - Not deemed an issue
    * 'template literal syntax' is only available in ES6 (use 'esversion: 6'). - Not deemed an issue
* Python code validated using [Extend Class Python Validator](https://extendsclass.com/python-tester.html)
    * Some issues with f-strings as the checker didn't deem them valid python. These were not considered a problem.



### Bugs
During the development proccess many bugs (predictably) arose. Here are some of the more interesting 
examples and how they were overcome:

#### Adding tickets to a booking in the basket would create new items basket rather than update the current values:
This occured because the basket was storing the event_ids as strings and the event_ids 
coming from the database were integers. For the tickets values to be updated
the event_id from the database had to be convereted to a string before it be used to find 
a match in the basket.

#### Basket data could not be stored in the payment intent meta data, this kept failing.
This issue kept occuring and I was convinced it was to do with trying to store the event (as an object not id)
in the payment intent after it had been JSON serialised. After numberous attempts it was discovered the actual 
variable causing the issue was total. Total was a Decimal and json.dumps() couldn't handle that type of input.
Instead the total was changed to a float and the basket and user data could be stored in the payment intent.

#### Toast messages failed to load the toast templates.
After setting up messages and toast templates unfortunatly they wouldn't load on the page.
It turned out the template logic `{% if tag == 'SUCCESS' %}` was using the wrong case.
The correct code was `{% if tag == 'success' %}` after which the toasts loaded correctly.

#### Bookings would not save their totals.
This issues occured due to a simple slip of the mind. I was using:  
`self.total = self.bookings.aggregate(Sum(booking_total))`
Which is the correct way to aggregate a value but not to access it.
To access the total I shoul have used:  
`self.total = self.bookings.aggregate(Sum(booking_total))[booking_total__sum]`

#### The main logo in the navbar would appear off center on smaller screens.
This issue had an obvious cause. On smaller screens the logo jumps to the center of 
the navbar and aligns itself so it has an equal margin between elements either side.
As there are two elements on the right hand side and only one on the left this meant the 
logo would naturally align itself off the center of the page.  
Despite trying absolute positioning and mutliple other css tricks the answer was really simple.
I added extra margin to the element on the left of the logo so it was forced to align itself
towards the center of the page.

#### Migrating the database to Heroku Postgres failed.
This issue stumped me as I couldn't work out why the models wouldn't migrate over 
to the new database. The original error was:  
`psycopg2.errors.StringDataRightTruncation: value too long for type character varying(27)`  
In the end I followed the advice found [Here](https://stackoverflow.com/questions/9036102/databaseerror-value-too-long-for-type-character-varying100)
(the fourth answer) and deleted all my migration files other than __init__.py which fixed the issue.
I'm still not 100% sure why this worked but imagine it is to with separate migration files
conflicting with each other during the migration process. 
    