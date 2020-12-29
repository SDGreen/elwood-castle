# Elwood Castle
![Elwood Castle](https://github.com/SDGreen/elwood-castle/blob/master/flat_pages/static/flat_pages/images/background.jpg?raw=true)
### Deployed site: [https://elwood-castle.herokuapp.com/](https://elwood-castle.herokuapp.com/)

#### For testing the following credentials can be used:
* User Credentials:  
  - Username: TestUser  
  - Password: testingelwood  
  - Email: test@test.com 

* Card payments:
  - Card number: 4242 4242 4242 4242
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
The aim of this Django app is to create an interactive interface where users can find out
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
| User    | Consistent styling across the site | Navigate across the site without having to think too hard about what elements do |
| User    | A profile page |	Quickly see my orders and checkout details |
| Returning User | To be able to save my default settings | Easily use them to book new events |
| New User | To be able to create an account | Save my details and view my orders |
| Returning User | To be able to reset my password | Update my password if I forget it |
| User    | A contact page where I can find email and phone details of the castle | Get in contact if I have a question about an event |
| User    | Details on the location of the Castle | Find the castle and attend events |
| User    | Booking events to be simple | Avoid filling out too many inputs |
| User    | Confirmation of my bookings | Know that my purchase has worked |
| User    | A date picker for event bookings | Easily visualize what date I'm picking and avoid filling in an input |
| User with a profile | A list of my upcoming and past events | Know what events I have booked |

#### Owners:
| As a... | I would like... | So I can ... |
| :------ | :---------------| :----------- |
| Owner	| Simple navigation to the event pages | Encourage users to buy tickets to events |
| Owner	| Lots of links back to event pages | To get users to buy more tickets |
| Owner	| Links between an event's details page and booking page | Make it easy for users to book events and reduce time spent thinking about this decision |
| Owner	| Professional and clean styling | Keep the site attractive to users without diminishing the castle's brand |
| Owner	| Login validation | To prevent users from creating multiple accounts with the same email |
| Owner	| Email verification on accounts | To prevent malicious users from easily creating multiple accounts |
| Owner	| An FAQ page | Prevent too many incoming calls and emails |
| Owner	| Details on visiting the castle | Make sure users know how to get to the castle |	
| Owner	| Bookings to be kept in a basket  | Make sure users only have to pay once, encouraging them to purchase more |
| Owner	| Order Confirmation to work even if a user navigates away from the checkout page | Know users haven't purchased tickets without the models updating |
| Owner	| Dates where events are fully booked to be unpickable | Know that users haven't purchased tickets to events which won't be able to cater for them |
| Owner	| Validation on the date picking input | Make sure users don't create bookings using dates which aren't correct |
| Owner	| Validation on the ticket input | Stop users booking too many tickets for events which are nearly full |
| Owner/User | Responsive design | Easily use the site across multiple devices |
| Owner/User | Message styling to be intuitive (red for alerts, green for success) | Quickly understand what the message is trying to convey |	

### Information Architecture
#### Overview
For Elwood Castle a relational database using SQL was the best choice to store the information.
The reasoning behind this choice is because users can't directly add items to the database which
would have wildly unknown values. All orders would follow a similar structure which is where the
users have most control over what is inputted. Unlink a movie database, where each field may store
very different values, here all entries would have a very similar structure with values which don't vary
in data type (i.e. strings or integers) so a relational database made sense. The models built in the Django
framework provide great validation to prevent incorrect values being added, so it's extremely unlikely
that Elwood Castle would need a database structure like MongoDB where unknown values are expected to
be inputted frequently.

The information in each model would also be related to another model in almost all cases. All *orders* have
*bookings* which have *events* etc. Having such interlinked models required a relational database to easily
handle the data and prevent creating a large database with many repeated values.

#### Models 
##### User
This inbuilt model is used by Django. Here there was no changes made as it would suit the rest of the models nicely.

##### UserAccount
This model builds on the user model provided by Django so that a user could save which orders and
bookings they have made. In the future, if a subscription service was created it would also tack on
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
ticket numbers and dates which are full when a user tries to book an event.
Other than having these key details, this model also stores information the user may
want to know about an event before they book it.
In future, if events start taking place on selective days of the week, this would
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
This is a simple model used to store the different types of categories each event can fall into.
New categories can be easily added if the castle decides to start hosting new types of events, along
with allowing current events to easily change their category.
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| name | CharField | max_length=50, null=False, blank=False |
| friendly_name | CharField | max_length=100, null=True, blank=True |

##### Order
This is a simple model used to store orders which contain EventBookings.  
It's relation to EventBookings and UserAccounts allows users to see their upcoming
and past bookings on their profile page. It also has a stripe_id field for validation, preventing orders from being created
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
The EventBooking's relation to the Order model is used to show upcoming and past events on the user's
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
All wireframes can be found [Here](https://github.com/SDGreen/elwood-castle/tree/master/wireframes)  
I reccomend viewing the [Navbar](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/navbars.pdf)
and [Footer](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/footers.pdf) files first to give context to the rest of the wireframes.  
For individual files, please click the relevant name:
  * [Navbar](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/navbars.pdf)
  * [Footer](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/footers.pdf)
  * [Index page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/index.pdf)
  * [Events page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/events.pdf)
  * [Event Details page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/event-detail.pdf)
  * [Book Event page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/book-event.pdf)
  * [View Basket page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/view-basket.pdf)
  * [Checkout page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/checkout.pdf)
  * [Checkout Success page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/checkout-success.pdf)
  * [User Home page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/user-home.pdf)
  * [Order Summary page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/order-summary.pdf)
  * [Visit page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/visit.pdf)
  * [FAQ page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/faq.pdf)
  * [Contact page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/contact.pdf)

  Please note that these wireframes may not match the finished product. Some elements
  may be moved or changed based on feedback or styling issues discovered during development.

### Design Choices
#### Overview
For the Elwood Castle website, the design is informed by other castle websites. Looking
at [Leeds Castle](https://www.leeds-castle.com/), [Hever Castle](https://www.hevercastle.co.uk/), [Alnwick Castle](https://www.alnwickcastle.com/),
[Sandringham Castle](https://sandringhamestate.co.uk/) & the [English Heritage](https://www.english-heritage.org.uk/) websites
identified aspects to include (heritage fonts, large vista images) but also helped inform what Elwood Castle's
site would like to do differently.

##### Layout
Of the sites mentioned above, one issue they all suffered from was cluttered and blockly
layout (particularly the navbars). For this site, to keep UX high, the site will 
have a much cleaner layout with a slim navbar. As a site with a large target demographic 
with varying levels of computer literacy, it's important to keep the available space 
easy to read and thus use.

##### Images
One thing borrowed from other castle sites was the use of large vista images on the landing page.
This accomplishes two goals: firstly, the images protect Elwood Castle's brand as the opening impression
of Elwood Castle is it's grand views and impressive grounds. Secondly,
it acts as an advertisement to visit the castle which furthers the bussiness goal
of attracting new visitors.  
For event images, I've taken the stylistic choice to use tight focused images
rather than large, wide images. The idea behind this choice is to keep the page
feeling uncluttered when mutliple images are shown. Using these more intimate shots
preserves a feeling of outside space whereas lots of large, wide images would be
confusing when placed together. The smaller shots will also look better when shrunk
onto cards, whereas large shots would be hard to see when reduced in size (without cropping).

##### Fonts
To keep brand consistency, [IM Fell French Canon SC](https://fonts.google.com/specimen/IM+Fell+French+Canon+SC)
is used as the Logo font. This font projects a heritage feel whilst remaining readable.  
For headings and buttons [Lora](https://fonts.google.com/specimen/Lora) has been used. This is because
the font still retains a feel for the Logo font (it contains serifs) whilst being very
readable. Other sites mentioned above used their logo font (typically all capitals like Elwood Castle's)
which gave their sites an erractic, angry feel. To maintain a good UX whilst keeping this feeling of
tradition, Lora is similar to our Logo text but lacks the readablity and impression
issues an all caps font would have. 
Lastly, [Raleway](https://fonts.google.com/specimen/Raleway) has been used for body text. This is to maintain
readablity as it's often used in blocks of text where serif fonts can start to feel cluttered.  
Overall, I feel these fonts maintain the castle's brand whilst aiding the business goal 
of attracting visitors and new bookings as they keep the website easy to read and use.

##### Colour Palette
![Elwood Colour Palette](https://github.com/SDGreen/elwood-castle/blob/master/images_for_readme/elwood-castle-colour-palette.jpg?raw=true)  
The colour palette used for the Elwood Castle site is actually just colours
picked from the main image of [Elwood Castle](https://github.com/SDGreen/elwood-castle/blob/master/flat_pages/static/flat_pages/images/background.jpg?raw=true).  
The choice to use colours picked from Elwood's main brand image is to maintain
brand consistency and to keep the palette looking natural.  
The sites used for researching castles (mentioned above) all either relied on 
red or dark tones which I feel diminishes UX. Darker colours force the user 
to search for content due to the lack of contrast, deep reds are 
often used as warning colours which doesn't lend to a positive UX.
By keeping the colours natural and light the site helps distingush itself 
from competitors and provides a positive UX.

For messages, three very standard colours were used. Red for errors, green 
for success and blue for infomation. By keeping these colours consistent with 
user expectations, the site can quickly and clearly communicate what type of 
message the user is receiving without them even having to read it. One slight 
difference is the red, green and blue used are all pastels to prevent a jarring
contrast with the sites main palette.

---
## Features
### Existing Features
* #### Dynamic Event Search Bar 
    * Events can be searched by description, name and category using the search 
    bar.
    * Dropdown menus allow the user to search by category, price & rating (highest to lowest and vice versa).
    * The search bar dropdowns for price and rating change to icons on smaller screens, where as the category 
    dropdown turns to an icon on only the smallest screens as it's meaning is hardest to 
    translate into an icon.
    * Number of results for searches and categories is dynamically displayed on the page underneath 
    the search bar (search terms are not shown to prevent profanities being displayed on the page).
* #### Dynamic Event Cards
    * Each event card features an image of the event or the stock missing image
    if no image has been uploaded for the event.
    * On larger screens, the price and rating are displayed on each card; on smaller
    pages these are hidden to keep the page looking tidy.
    * Each card has links to the event details page and a direct link to the booking page.
    * The number of cards per row changes dynamically depeninding on screen size, 
    this keeps the page looking uncluttered and prevents the images from becoming too 
    small to understand or comically large.
* #### Dynamic Event Details Page 
    * Each event has an event details page which renders the information stored in the database. 
    * The layout shifts depending on screen size to keep the information easy to read.
    * The information within the "Key Details" and "Notes" sections changes depending on 
    the event's category, if it requires adult supervision, or is age restricted.
* #### Smart Date Picker
    * The date picker automatically disables fully booked dates (days where the amount of 
    tickets booked matches the event's 'day_ticket_limit' value), along with dates over a year in 
    the future, one day in the future, past days of the current month, Christmas dates and New Years day when the 
    castle is closed. 
    * The date picker searches the user's basket to prevent them from booking too many tickets 
    even if the values aren't present in the database.
    * The ticket input alerts users to available tickets for their chosen date and warns them 
    if this value is 5 or less. If the available tickect value is 0, but the date isn't disabled 
    due to the user having these tickets in their basket (which isn't checked when disabled 
    dates are generated) then the input is disabled and the user is asked to pick a new date.
* #### Smart Ticket Update input
    * Users can update their ticket quantities in their basket. The update script checks 
    the database for bookings to make sure the day_ticket_limit of that event isn't exceeded.
* #### Stripe Payments 
    * Users can checkout and purchase event tickets using the Stripe API.
* #### Smart Checkout Validator
    * User details and basket are validated twice before the stripe API is called to make 
    the payment. Once to check the user details are valid, along with checking that no
    tickets in the basket somehow exceed the day_ticket_limit of the event they are purchasing.
    If ticket quantities in the basket do exceed the day_ticket_limit, then they are removed 
    from the basket. This feature also prevents users from purchasing tickets that may have been 
    in their basket, whilst other users have already purchased the maximum tickets for that day, thus 
    preventing overbooking.
    If there are any issues with the details or basket items the payment can't take place 
    and the page is reloaded showing the user an error message and assuring them the purchase hasn't 
    gone through.
* #### Checkout Redundancy
    * If somehow the user navigate away from the checkout page before the order is submitted 
    to the database then it is created in the webhooks.
* #### Order and Booking Confirmation/Emails
    * Once a payment is successful the user gets an email confirming their order, along 
    with individual emails for bookings which they can use to pick up their tickets. 
    * Once an order is created the user is redirected to a checkout summary page displaying 
    information about that order.
* #### Account Creation 
    * Users can create an account with Elwood Castle, this automatically creates 
    a UserAccount entry for the User in the database. They can use the account to 
    view previous orders, upcoming and past events.
* #### User Account
    * Users can store their details and use them next time 
    a user reaches checkout.
    * User details can be updated from their account page. This will not affect their 
    user details (username, email, password) and this is outlined under the update details form.
* #### Password Reset 
    * Users can update their password using their email if they have forgotton their current 
    one.
* #### Contact Form
    * Users can send emails to Elwood's Gmail account using the contact form. 
    If the user is logged in, it will preload their saved email into the email 
    field of the form.
* #### Toast Alerts 
    * Throughout the site Toast alerts are used to give the user feedback, such as 
    when a user logs in, logs out, adds items to a basket, removes/updates 
    basket items, checks out out successfully etc.
    * Alerts change colour depending on the type of message used to create them, 
    red for error, green for success and blue for information (i.e. email verification emails being sent).
* #### Responsive Basket
    * The basket won't allow users to checkout if their basket is empty.
    * If the basket is empty it offers a link back to events page.
* #### Responsive Fixed Navbar
  * Includes dropdown links to account pages which change depending on if the 
  user is logged in, a superuser or an anonymous user.
  * Logo text disappears on smaller screens, key elements (basket and account dropdown) 
  remain as icons, whilst less essential links are stored in a mobile dropdown.
  * Logo image changes size depening on screen size.
  * Due to it's small size it remains fixed to the top of the page to eliminate the need
  for a "back to top" button.
* #### Simple Footer
    * Footer remains consistent across the site and includes three social links and a link
    to the creator's github page. All external links create a new tab rather than change the 
    current windows location. 
    The social links aren't live and so currently redirect back to the index page with a
    message explaining why.
* #### Dismissable Alert Banner
    * On the events page, a banner appears linking users to the FAQ page if they want 
    information about Elwood Castle's Covid-19 policy.
    * The banner is dismissable but reappears each time a user goes to the events page 
    where it's message is most important.
* #### Dynamic Landing Page 
    * Has a scrolling background of Elwood Castle's grand vista images.
    * Elwood's logo appears above the key links highlighted on the page.
    * On very small devices the less used contact link is removed to maintain 
    the balance of the page.

### Features Left to Implement
* #### Subscription Service
    * In future it would be great to create a subscription service where uses pay 
    either per year or month, which entitles them to a certain amount of free 
    tickets.
* #### Real-time Ratings 
    * A future feature would be to allow users to rate events which automatically 
    updates an event's rating in real-time.
* #### Ticket Reservation
    * With sites like Ticketmaster, tickets are held for a period of time and cannot 
    be booked whilst another user has them in their basket. Currently this feature 
    is not deemed necessary as Elwood Castle doesn't deal with the types of volumes 
    that a major arena deals with but it would be good to add in future.
* #### Styled Superuser Dashboard 
    * With more time, a nicely styled dashboard would be created for super users.
    Currently it is just the standard Django admin dashboard which is usable but 
    one fitting with the rest of the site would be better for UX.
* #### Custom 404 Page 
    * Fairly self explanatory, but this feature wasn't deemed necessary for the site 
    to be deployed.

---
## Technologies Used
### Languages
* [HTML5](https://html.spec.whatwg.org/multipage/) - Used to create the structure of the website.
* [CSS3](https://www.w3.org/Style/CSS/Overview.en.html) - Used to style the website.
* [JavaScript](https://www.javascript.com/) - Used for stripe functionality, as well as Bootstrap & Google maps API functionality and the date-picker element.
* [Python (v3.8.6)](https://www.python.org/) - Used to handle backend programming within the Django framework.
### Libraries
* [Google Fonts](https://fonts.google.com/) - Used for website fonts [Lora](https://fonts.google.com/specimen/Lora) for headings, [Raleway](https://fonts.google.com/specimen/Raleway) for content text and [IM Fell French Canon SC](https://fonts.google.com/specimen/IM+Fell+French+Canon+SC) for logo text.
* [Font Awesome](https://fontawesome.com/) - This library provided the Icons used across the site.
* [jQuery](https://jquery.com/) - Included with Bootstrap, also used to code various elements such as the date picker, stripe functionality and Google maps API.
* [Stripe API Library](https://stripe.com/gb) - Used to handle the payments send from the Elwood Website.
### Frameworks
* [Django v3.1.4](https://docs.djangoproject.com/en/3.1/) - Framework used to create the app along with inbuilt templating language.
* [Bootstrap v4.5](https://getbootstrap.com/docs/4.5/getting-started/introduction/) - Framework to add structure & styling to the site, along with
responsive breakpoints and pre-built elements.
### Tools 
* [Git](https://git-scm.com/) - Used for version control and tracking changes to the code whilst in development.
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Key for finding bugs and testing responsive design.
* [Autoprefixer](https://autoprefixer.github.io/) - Used to prefix the CSS, allowing it to work across different browsers.
* [AWS S3](https://aws.amazon.com/s3/) - Used for storing static and media files used across the site.
* [Heroku](https://www.heroku.com/home) - Used to deploy and host the finished site.
* [Heroku Postgres](https://www.heroku.com/postgres) - Used to serve the database Elwood Castle manages event and user data with.
---
## Testing
See the [testing write up](https://github.com/SDGreen/elwood-castle/blob/master/TESTING.md) for full details on testing.

---
## Deployment

### How to run Elwood Castle's code locally:
The Elwood Castle app was coded using the GitPod IDE. The git repository is stored locally before being pushed 
to the remote repository online at GitHub.

To run Elwood Castle's app locally you will need the following:
    * Python installed on your environment
    * An AWS account
    * A Stripe account
    * A Google maps API key

#### Setting up the code:

1. Go to: [https://github.com/SDGreen/elwood-castle](https://github.com/SDGreen/elwood-castle)
2. Click the "Code" button next to the "Gitpod" button which will have a dropdown including "Clone with HTTPS",
"Open with GitHub Desktop" & "Download ZIP"
3. To clone the repository using HTTPS, under "Clone with HTTPS", click the copy to clipboard icon. To clone the
repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the copy to clipboard icon.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to appear.
7. Type git `clone`, and then paste the URL you copied in Step 3 (https://github.com/SDGreen/elwood-castle.git).
8. Install the requirements by typing `pip3 install -r requirements.txt` in your CLI
9. Finally create a superuser using `python3 manage.py create superuser`

#### Creating a database:
1. To use the local version of the database first type `python3 manage.py makemigrations`
2. Then migrate (`python3 manage.py migrate`) the migrations so that your local db.sqlite3
database included with Django is setup.
3. To use the same data as this Elwood Castle site, type `python3 manage.py loaddata`
4. You now have a local version of the database.

#### Adding environment varibales:
In either your `env.py` file or your environment settings (like GitPod offers) you'll need to
add the following  environment variables:

    * SECRET_KEY = <Your secret key>
    * STRIPE_PUBLIC_KEY = <Stripe public key>
    * STRIPE_SECRET_KEY = <Stripe secret key>
    * STRIPE_WH_SECRET  = <Wehhook key>
    * AWS_ACCESS_KEY_ID = <Your AWS access key id>
    * AWS_S3_REGION_NAME  = <Your AWS region name>
    * AWS_SECRET_ACCESS_KEY = <Your AWS secret key>
    * AWS_STORAGE_BUCKET_NAME = <Your AWS bucket name>

While technically not an environment variable, you'll also need to add your Google API key to this file:  
`flat_pages/templates/flat_pages/visit.html`  
Add your key to this script tag in the file:   
`<script async defer
    src="https://maps.googleapis.com/maps/api/js?key<YOUR_KEY_HERE>&callback=initMap"
    type="text/javascript"></script>`  
Make sure you restrict your Google API to just your local environment (and deployed site if created)

#### Running the app
1. If you are using your AWS bucket to serve the static and media files, go to the bucket and create 
a file named `media/`
2. Export all the files in your local environment directory `media`, to the `media/` file in your AWS bucket.
3. You are ready to run the code locally!

### Deploying to Heroku
1. If you have added any new packages which the code requires to run, type `pip3 freeze > requirements.txt`
to creat a requirements file.
2. If you have deleted the Procfile, create a new one containing: `web: gunicorn elwood_castle.wsgi:application` in your root directory.
3. Create a new app in Heroku, if you want to use Heroku Postgres to serve your database you can do so 
by going to the dashboard *resources*>*add-ons* and attaching the Heroku Postgres database.
    * Please note, you will need to make your migrations and load the data to the new Postgres database as detailed above in 
  the **Creating a database** steps. Ensure the DATABASE_URL variable matches that in your Heroku App's 
  **Config Vars**
4. Add your environment variables as detailed in the steps for **Adding environment variables** above
to your apps **Config Vars** including this new variable:  
USE_AWS = True
5. Download the Heroku CLI if you haven't already (found under the *Deploy* tab on the dashboard).
6. Login to Heroku using `heroku login`
7. Set up a remote repository connected to you Heroku app: `git remote add heroku <your heroku git URL>`
    * If you're unsure of your Heroku git URL it can be found under *settings* on the dashboard.
8. Finally push your code to the Heroku remote repo after making any change.  
`git add .`   
`git commit -m "some change"`  
`git push heroku master`

The site is now deployed remotely.

---
## Credits

### Content
* All copy was written by myself.
* Fake phone number provided by [Fake Number](https://fakenumber.org/uk/london).

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
* [Missing Image Placeholder](https://pxhere.com/en/photo/1334124) (file name: no-image.jpg)
* [Old Kitchen](https://pxhere.com/en/photo/1069371) (file name: kitchen.jpg)
* [Puppet](https://pxhere.com/en/photo/896895) (file name: puppet.jpg)
* [Sparkler](https://pxhere.com/en/photo/1169641) (file name: sparkler.jpg)
* [Spice Market](https://pxhere.com/en/photo/959535) (file name: spices.jpg)
* [Tapestry](https://pxhere.com/en/photo/575238) (file name: tapestry.jpg)
* [Teacup](https://pxhere.com/en/photo/649039) (file name: tea.jpg)
* [Castle Vista](https://pxhere.com/en/photo/843450) (file name: vista.jpg)
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
* Card, Navbar, Accordian and Form setups adjusted from [Bootstrap 4 examples](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
* Google map created using [Google Maps JS API](https://developers.google.com/maps/documentation/javascript/tutorial)
* Date picker created using [bootstrap-datepicker](https://bootstrap-datepicker.readthedocs.io/en/latest/)
* CSS prefixer used: [https://autoprefixer.github.io/](https://autoprefixer.github.io/)
* Every effort has been taken to avoid this apps code from becoming too similar to the
[Boutique Ado](https://github.com/ckz8780/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546) 
Code Institute mini project but it was a very helpful tool in setting up the site.
* READme stucture borrows heavily from the [Code institute readme example](https://github.com/Code-Institute-Solutions/SampleREADME#)

### Acknowledgements
A massive thank you to my mentor Antonio Rodriguez for his continuous and helpful feedback (even in the face of tropical storms).   
Thanks also to the kind people at tutor support who went above and beyond to help me fix issues.  
Finally a thank you to Sharon Luff for helping me start my journey into coding and providing great moral support along the way.  




---