[![Build Status](https://travis-ci.org/elenasacristan/treebooks.svg?branch=master)](https://travis-ci.org/elenasacristan/treebooks)

# TreeBooks! – Fourth milestone project


This is last milestone project for the Fullstack Web Developer course with Code Institute. 
For this website I'm creating a fictitious charity called TreeBooks which aim is to raise money to plant trees by renting second-hand books.

https://treebooksproject.herokuapp.com/

To be able to rent books the users need to register. Only registered users will be able to rent books, read reviews, join the waiting list for a book, keep track of the books read and save the books that they like in a favourites list.

The users who are not registered will see in the landing page the main reasons why they should register. 
Users not registered can't rent books but they can see the listing with all the books and the details page. In the details page, they won't be able to see the reviews but they will be able to see the average ratings for each book and the main details about the books.

Also registered and not registered users can donate books to the charity. If they want to donate they can see in the donate.html page the map with the collection points where they can drop their books to help the charity to grow the collection of books to offer.

All users can also read how the website works by reading the about.html page and have access to the projects page where they can see how much money has been raised by the charity until now, how many books have been rented and to what projects is the charity going to donate the money raised.

The users can search for a specific book or author by typing on the search box.

The users can contact the charity using the contact form in case they have any questions or projects in mind.

The users will be able to follow TreeBooks on social media by clicking on the icons on the footer of the page.


## UX

This website is targeting people who like reading books but at the same time have concerns about how many trees are cut to create new books. They will want to use the website because reading second-hand books they are stopping more trees being cut and because the money paid to rent the books will be used in reforestation projects.

TreeBooks is a charity so the website aims to attract users who then will rent books from them. They also want to grow the collection of books by getting people to donate their second-hand books.

### mock-ups:

Below you can see the mock-ups that I drew using [Adobe Fireworks](https://www.adobe.com/products/fireworks.html).

##### Common design used for the following pages:

login.html, registration.html, contact.html, review_form.html, password_reset_complete.html, password_reset_confirm.html, password_reset_done.html, password_reset_email.html, password_reset_form.html

![many](/documents/mockups/small_common_style1.png)

##### index.html

![home](/documents/mockups/home1.png)

##### about.html

![about](/documents/mockups/about1.png)

##### projects.html

![projects](/documents/mockups/projects1.png)

##### donate.html

![donate](/documents/mockups/donate1.png)

##### all_books.html

![books](/documents/mockups/books1.png)

##### detail.html

![detail](/documents/mockups/detail1.png)

##### view_profile.html

![profile](/documents/mockups/profile1.png)

##### edit_user_profile.html

![edit profile](/documents/mockups/edit_profile1.png)

##### cart.html

![cart](/documents/mockups/cart1.png)

##### checkout.html

![checkout](/documents/mockups/checkout1.png)

- The final design of the website included some additional functionalities (buttons, carousel, modals and messages) that I thought would be useful as I was working on it. I also changed slightly the styles (colours, transparency, shadows, borders) for others that I found nicer.

### User stories

- As a charity owner, I want to get users to register to the website so I can rent books to them and I can raise money to plant new trees.

- As a user (member or not) I want to be able to see what is the aim of the website.

- As a user (member or not) I want to be able to see what projects is the charity planning to contribute to and how much money the charity has raised so far.

- As a user (member or not) I want to be able to contact TreeBooks to send my comments and suggestions for new projects.

- As a user (member or not) I want to donate books and I want to know where are the collection points.

- As a user I want to register to be able to rent books and contribute to reforestation projects

- As a user I want to register to be able to save money reading second-hand books instead of buying brand new books.

- As a member I want to feel that I'm helping to save the planet by not buying new books and by renting second-hand books.

- As a member I want to be able to add my name to a waiting list if the book that I want to read is not available

- As a member I want to be able to see my position in the waiting lists.

- As a member I want to see a notification when my turn to read the book has been reached.

- As a user I'd like to know what books are available and which ones have waiting lists.

- As a member I want to be able to save books as favourites.

- As a member I want to be able to see all the books that I have read since I started the membership.

- As a member I want to be able to review the books that I have read.

- As a member I want to be able to add books to the shopping cart and then pay all of them at once.

- As a member I want to be able to update the number of days to rent the book from the cart page.

- As a member I want to be able to remove books from the cart if I change my mind about the books.

- As a member I want to see in my profile when is the return date for the books that I'm currently reading.

- As a user (member or not) I want to be able to see all the books in TreeBooks and their details.

- As a user(member or not) I want to be able to search for a book or author by typing on the search box.

- As a member I want to be able to see the reviews given by other members.

- As a member I want to be able to register to the monthly newsletter.

- As a member I want to be able to edit my profile details and add a profile image.

- As a member I want to be able to follow TreeBooks in Social Media.

- As charity owner want to notify the users in case they don't return the books on time.

## Features

### Accounts app

The accounts app will allow users to register to become members of TreeBooks. The registered users will be able to access all the member features.

The users will register using the registration form. Registered users will be able to log in by using the login form with their username and password or with the email and password.

The users can also reset the password if they forgot the original password using the reset password link on the login.html page.

### books app

##### view-all-books.html

Display all the books present on the website. The books are displayed by category and they are sorted in descending order by the review score.

In this page the user only will see the name of the book, the star rating and the rating score. If they want to know more about the book or rent it they need to click on the 'more' button.
If the user is authenticated then he/she will also be able to see a message about the status of the book ('available', 'check waiting list', 'It's your turn!' or 'you are reading this book'.
By clicking on the book title, the 'AVAILABLE' text or the 'It's your turn' badge the user will also be redirected to the detail page.
If the user clicks on 'check waiting list' then it will be re-directed to the waiting list for that book.

##### detail.html

In this page the user can see all the details about the book. These details are the title, the author (by clicking on the author name they will get redirected to the Wikipedia URL for that author), the summary, the category, the date it was published, the ISBN number for the book, the store where the book has to be collected from, the number of pages and the type of book (hardcover or paperback).

In this page if the book is available and the user is authenticated then the user can select the number of days that wants to rent the book for (the minimum number of days will be 10 and it has been set as the default value) and add it to the shopping cart.

If the book is not available and the user is authenticated then the user can join the waiting list.
if the user is already in the waiting list then he/she will see the message 'You are already in the waiting list' and a link to the waiting list so they can see in what position they are.

If the user is not authenticated he/she will see a button to register because only authenticated users can rent books or join the waiting lists.

##### view_profile.html

The users can see their personal and membership details by clicking on the profile tab in the navigation bar.

The profile will display the following information about the user:

- profile image (if the user doesn't upload an image there will be a default profile image displayed)
- membership details (date that the user registered and if they are subscribed to the newsletter)
- currently reading: a list with the books that the user is reading at the moment including the date that they need to be returned.
If the user doesn't return the book on time a warning message will be displayed on this section telling the user to return the book as soon as possible.
- Also if the user wants to return the book before the due date then he/she can click the button 'I have returned the book' once the book has been returned and that way the book will become available for everyone or if there is waiting list it will become available for the next user in the waiting list.

- personal details (first name, last name, date of birth, email, telephone and preferred contact method)
- contact preferences
At the bottom, the user can access the list of books read since he/she became a member, the list of books he/she is in the waiting lists for and the list of favourites books.

These three lists will be displayed in modal windows. The code used to create the modal comes from Bootstrap 4.

In the list of books read the user will have the option to leave a review for the books that have rented. 

By clicking 'Your waiting lists' the modal window will appear and the user will be able to see a list of books that he/she is waiting for with a link in each book to see the waiting list.

Treebooks will contact the next user in the contact list as soon as the book is returned by the previous user. Also, the user will see a notification saying 'it's your turn' on the books listing. Then the next user in the waiting list can proceed to rent the book online. Only the next user in the waiting list will have the option to rent the book, for the rest of the users the book will not be available.

##### edit_user_profile.html

The users can edit their profile details by clicking on edit profile on the profile page.

They will be able to add and edit the profile picture, the date of birth, and the telephone.

Then they can choose to opt-in for the monthly newsletter and they can also select what is the preferred way to be contacted (phone, email or both)

### Home app

##### index.html

This is the home page and the users will get redirected to this page when they click on the logo or the home tab on the navbar.

This page has a carousel highlighting the main areas of the charity.

At the bottom the users can see the main benefits of being a member.
The users that are not authenticated will see the message 'Become a member and you will...' and also they will see the button register so they can become members.

If the user is authenticated then he/she won't see the register button and the header will have the message saying 'Hi USERNAME, with TreeBooks you can...'

##### about.html

This page explains the aim of the website and how it works. It has re-directs to other areas of the website (projects.html and donate.html)

##### projects.html

In this page the user can see how much money has been raised by the charity since the charity started and the user also can see how many times books have been rented since the beginning.

Also, the user will see what are the projects that the charity is trying to raise money for and what is the target for each.

By clicking on the project name the user will be redirected to the projects.
* Note that the projects that I'm showing are two projects that I found randomly on the internet in order to have them as an example in the website but I'm not familiar with them.

##### donate.html

If the users (registered or not) would like to collaborate with the charity by donating books, on this page they can see a map with the collections points where they can drop their books.

##### contact.html

In the footer there is a link to the contact us page. In this page the user can fill out the form to send a message to the charity.

### Cart app

##### cart.html

This page will display the books that the user have added to the shopping cart and will give the user the option to update the number of days selected or remove the books completely.

Then it will display the total to pay. A £5 deposit per book will be added to the total price and that deposit will be refunded once the book is returned.

The user will have the option to proceed to the payment by clicking the 'checkout' button or continue searching for other books by clicking the button 'keep looking'.

### Checkout

##### checkout.html

In the checkout page the user will see the details of the books that he/she is going to rent and the total to pay.

Then they will need to fill out the payment form in order to rent the book(s).

Once the payment has gone through a success message will be displayed and then the user can go to the specified store where the book belongs and collect it.

If there is an error with the payment the user will be notified with an error message.

If the payment has been successful the following will happen:
- The book(s) will be added to the list of read books and the list of current_books
- The return_date will be calculated buy adding the number of days that the user is renting the book for to the present date.
- The book will become NOT available
- The money paid for the book (not including the deposit) will be added to the total money raised for the charity
- The number of books rented will be added to the number of books rented since the charity started.
- If the user was in a waiting list for the books that he/she is renting then his/her name will be removed from the waiting list.

### Waiting_list app

##### waiting_list.html

Only authenticated users will be able to see or join waiting lists for books.

This page will display the list of users waiting for a book in order.
Number 1 will be the next user to read the book, number 2 the second and so on.

If the waiting list is empty the header will say: "You could be next!" and also there will be an alert message saying "There is no one waiting!"

At the bottom of the waiting list there will be two buttons. The "Keep looking" button will redirect the user to the all_books.html page and the "Go to Book" will redirect the user to the detail.html page for that book.

### Reviews app

##### review_form.html

Once the user has rented a book he/she can leave a review.
The users can see the books that they have read on their profile page by clicking on "The books you read". For each book in this list the user will have the option to leave a review. Once they have reviewed the book then they will see the message 'Already reviewed' under the book title.

The review_form.html page will display a form where the user can enter the title of the review, the comment and the score from 0 to 5.

Then the review will be added to the detail.html page for that book.
Each review will display the individual star rating and then all the reviews will be taken into account to calculate the mean score for that book (and that average start rating and score will be displayed on the top left side of the details page)

### Favourites app

The user can add/remove the book that he/she wants to the list of favourites by clicking the heart icon on the pages all_books.html and detail.html.

Then the user can see all the favourites books if he clicks on "Your favourites" on the user profile page.

### Search app

This app will allow the user to search for a book based on the book's title or author name.

The search box is displayed at the top of the navbar and it is visible from all pages.

The books that contain the word entered in the search box either in the title or in the name of the author will be displayed and will be sorted descending by score.

### Other features available from all pages




##### navbar
The navbar will be available from all the pages on the website.
In order to create the navbar I have used Bootstrap 4 and I have used the following link to help me align the elements inside.
https://www.codeply.com/go/qhaBrcWp3v

##### Hamburger button
The hamburger button from bootstrap 4 will appear on small screens and when is clicked it will display the navbar vertically and it will also include the login and cart options.

##### social links
They appear on the page footer in every page on the website and by clicking on them the user will get redirected to the media websites to follow TreeBooks. (since the website is fictitious they will be redirected to the login page for Facebook or Twitter).

##### Logo
The logo will appear in the navigation bar for every section of the website and when clicked it will redirect the user to the home page (index.html).

## Features Left to Implement

I would have like to include in the detail.html page the name of the user reading the book and how many days are left until the book will be available again (for the next user in the waiting list of for all users). The reason why I didn't implement this feature is because I was running out of time and I needed to deliver the project soon.

## Technologies Used

#### Database:

When working locally I have used the [SQLite](https://www.sqlite.org/index.html) database that comes with Django but in production I'm using a [Postgres](https://www.postgresql.org/) database. 

In order to get the Postgress database I created the Heroku app, then in the Resources tab I searched on the Add-ons search bar for Postgress and I selected the 'Hobby Dev' option. After this the DATABASE_URL was ready on the Config Vars in Heroku. 

See database schema for the project below:


![database](/documents/db_schema/data_schema.png)


#### Graphic Design software:

- **[Adobe Fireworks:](https://www.adobe.com/products/fireworks.html)**
I have used Adobe Fireworks to create the logo and the mock-ups.

#### Languages:

- **HTML5:** Is the main language used to create the structure of the website.

- **CSS3:** Is the language used to add styles to the HTML.

- **[JavaScript:](https://developer.mozilla.org/en-US/docs/Web/JavaScript)** This is the language used to add interactivity to the website. I have also used it for the following:
    - To add the auto-scroll effect when hovering over the list of books. 
    - To display the spinner icon while the pages load.
    - To show the collection points map. 
    - Used for the integration with Stripe


- **[Python:](https://www.python.org/)** The main logic of the website has been created using Python.

- **[Django:](https://www.djangoproject.com/)** I have used Django framework to build the backend of the website.

#### Dependencies:

Below is the list of the main packages that I had to install to create the project. These packages are listed in the requirements.txt file together with some other packages that have been installed automatically when installing the main packages.

**Django** is the framework user to create this project.

```Django==1.11.17```

**django-forms-bootstrap** is needed to apply bootstrap styles to the Django forms.

```django-forms-bootstrap==3.1.0```

The **Pillow** package is needed to allow the upload of images.
```Pillow==6.1.0```

The **stripe** package is needed to be able to take payments.

```stripe==2.37.1```

The **dj-database-url** package is the package needed in order to connect to a database URL.
```dj-database-url==0.5.0```

The **psycopg2** package is needed to connect to the Postgress URL.

```psycopg2==2.8.4```

**boto3** and **django-storages** packages are needed to connect Django to S3 (AWS) that is where the media and static files are hosted.
```boto3==1.10.2```
```django-storages==1.7.2```

The **coverage** package is not needed for the project to run but it is needed to create the coverage report when testing the app.
```coverage==4.5.4```

**django-extensions** and **pydot** packages are needed to create the database schema.

```django-extensions==2.2.5```
```pydot==1.4.1```

This **django-template-check** package makes it possible to easily check for basic syntax errors in all loaded Django templates.

```django-template-check==0.3.1```

The **gunicorn** package is needed to connect to Heroku.
```gunicorn==20.0.0```


#### Libraries

* **[jQuery](https://jquery.com/)**: This library is needed for all the interactive elements in the website to work.

* **[FontAwesome:](https://fontawesome.com/ "https://fontawesome.com/")**: The font awesome icons have been used in different areas of the website (search, cart, login, log out, social media and favourites icons)

* **[Google Fonts:](https://fonts.google.com/ "https://fonts.google.com/")** I’ve used the fonts from Google Fonts to style the fonts in the website.

#### Development environment:
**[VisualStudio:](https://visualstudio.microsoft.com/)** I have used Visual Studio to develop the app.

#### Version control system:

**[Git:](https://git-scm.com/ "https://git-scm.com/")** I have used the version control system Git from the "Git Bash" terminal to track changes in the website and push them to GitHub.

#### Hosting service:
- **[Heroku:](https://www.heroku.com/)** I have used Heroku to deploy the website.

## Testing

### Validation

- **HTML:** I have used https://validator.w3.org/ in order to validate the HTML code.

- **CSS:** I have used https://jigsaw.w3.org/css-validator/ in order to validate the CSS code.

- **JavaScript:** I have used https://jshint.com/ in order to check the JavaScript code.

### django tests

I have run tests for the models, forms and views in all apps where applicable.
I have tried to automate the test for as much code as possible but I didn't reach the 100% coverage because in some cases the tests were quite complicated and in these cases I have chosen to test manually.
I have manage to get a coverage of 86.6% on average.
See the coverage reports for each app below.

##### accounts coverage report

![home](/documents/coverage/accounts.png)

##### books coverage report

![home](/documents/coverage/books.png)

##### cart coverage report

![home](/documents/coverage/cart.png)

##### checkout coverage report

![home](/documents/coverage/checkout.png)

##### favourites coverage report

![home](/documents/coverage/favourites.png)

##### home coverage report

![home](/documents/coverage/home.png)

##### reviews coverage report

![home](/documents/coverage/reviews.png)

##### search coverage report

![home](/documents/coverage/search.png)

##### userprofile coverage report

![home](/documents/coverage/userprofile.png)

##### waiting_list coverage report

![home](/documents/coverage/waiting_list.png)

Click [here](/documents/checkList.xlsx) to see the checklist that I have used to test all the features in all the screen sizes.

### Additional testing

#### Travis
At the top of this Readme file you can see that the website passes the Travis test.

The code that I was meant to use in the Travis.yml file was not working and I found out that there were some issues when using python 3.7 and Django 1.11.17. Finally, I found out in Slack the code that was working well for my python and Django versions.

#### Dev Tools

I have also used development tools in Google Chrome to check how the website would look on different devices (portrait and landscape mode). In addition to that testing, I have also asked friends and family to have a look at the website to let me know if everything looks fine on their browsers and devices.

## Problems and bugs:

##### iterating on fields with ManyToMany relationships
I have issues when iterating on fields with ManyToMany relationships. In the end, I could fix these problems by using "if forloop.first" in the templates and in other cases by using values_list in the views.

##### IntergrityError - waiting list
When I changed from the local database to the Postgress database suddenly if I added more than one user to the same waiting list I was getting the following error:

```IntergrityError at/waiting_list/join/2/ duplicate key value violates unique constraint "waiting_list_waitinglist_wl_book_id_key"```

This was strange because locally I could add more than one user to the same waiting list without any error but changing to Postgress I was getting the error.
The tutors suggested me to create a new link to a new Postgres database to see if this could solve the problem but it didn't.
Finally, I noticed that every time I was adding a user to the waiting list I was also adding a book and that is why the book Id was duplicated since the book already existed in the waiting list.
This issue was fixed by using get or create. So a book will only be added if it didn't exist already

##### Currently reading
I also had an issue in the currently reading section. The original UserProfile model didn't have the field current_books when I first created it so instead I was displaying in this section the books included in the read_books field, but only the books where the return date was in the future. When the return date was in the past then the book would disappear from this section.

Then I noticed that if another user bought the same book after, the return date for the book was updated and then the book was appearing again in the currently reading section for each user who had read that book in the past.

The solution was to create a new field in the UserProfile model for the current_books that way the book will be added to current_books when the payment is done and will be removed from current_books when the book is returned so that way it won't be displayed again.

# GitHub repository

1. I've created a repository in GitHub called: “elenasacristan/treebooks” [https://github.com/elenasacristan/treebooks.git](https://github.com/elenasacristan/treebooks.git)

2. I've initialised git from the terminal using Git Bash:

`git init`

3. I have created a .gitignore file and I have added the files and folders that won't need to push to GitHub (i.e. '*.sqlite3','env.py','.vscode/','.venv/', __pycache__, *.pyc)

4. I've added the files that I was working on to the Staging area by using:

`git add .`

5. I've run the commit command with the first commit

`git commit -m “initial commit"`

6. I copied from GitHub the following path and I ran it in the Git Bash terminal in order to indicate where my remote repository is:

`git remote add origin git@github.com:elenasacristan/treebooks.git`

`git push -u origin master`

7. After this has been done I've run regular commits after every important update to the code, and I pushed the changes to GitHub.

## Deployment

### Running my code locally

1. First in vs code I've created a virtual environment:

`python -m venv .venv`

2. I've Installed Django

`pip install django==1.11.17`

3. I've added "127.0.0.1" to the list of ALLOWED HOSTS in the settings.py

4. I have created a env.py that will keep the variables that I need to keep secret and they shouldn't be pushed to Github.
- SECRET_KEY
- ENVIRONMENT
- EMAIL_ADDRESS
- EMAIL_PASSWORD
- STRIPE_PUBLISHABLE
- STRIPE_SECRET
- DATABASE_URL
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

5. In the settings.py I have added the following syntax in order to run different code depending on if the project is in development or production mode.

```
try:
import env
except ImportError:
pass
ENVIRONMENT = os.environ.get('ENVIRONMENT')

if ENVIRONMENT=='DEV':
development = True
else:
development = False
```

```
# will be True in development and False in production
DEBUG = development
```

6. Then I have created the apps in the project by running the following command where APP would be the name of each app:

python manage.py startapp APP

7. Every time an app has been added to the project I have also added the app name to the list of INSTALLED APPS in the settings.py file.

8. I have created a superuser in order to be able to log into the Django Admin site:

```python manage.py createsuperuser```

9. I have started the server by runing:

```python manage.py runserver```

10. If the app has models then I have created the migration files:
```python manage.py makemigrations```

and after I have migrated in order to create the tables in the database:

```python manage.py migrate```

11. Since my apps have forms that I want to style with bootstrap I have installed django-forms-bootstrap

```pip install django-forms-bootstrap```

12. I have also installed Pillow to alow the upload of images

```pip install Pillow```

13. Since we have several templates folders we need to specify in the settings that all the directories called 'templates' contain templates. We do this in the TEMPLATES section

```
'DIRS': [os.path.join(BASE_DIR,'templates')]
```

14. Also in the templates section we need to add the media context processor because we will have media in the project and we need a media ROOT:

```
'django.template.context_processors.media'
```

15. The books that are in the cart won't be saved in the database instead they will be stored in the session while the user is logged in. To ensure that the cart contents are available from every page on the website we need to create a context.
We will create the context.py in the cart app and then that context will be included in the list of contexts inside the TEMPLATES section in the settings.py

```
'cart.context.cart_content'
```

16. Since we are going to take payments using Stripe we will need to install Stripe

```pip install stripe```


17. Then I have added the Postgress database (link saved in the env.py) and in order to be able to connect to the database URL I have installed dj-database-url

```pip install dj-database-url```

* I will also need to import dj-database-url in the settings.py file
18. Since the database is Postgres I also had to install the psycopg2 package.

```pip install psycopg2```

20. In order to test using the production database we will comment out the code referring to the SQLite local database and we will add the following code:

```
DATABASES = {
'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```

21. Then we will need to migrate to create the tables in the new database (we don't need to makemigrations if we haven't made changes to the models)

```python manage.py migrate```

22. And since it is a new database we will also need to create a superuser

```python manage.py createsuperuser```

23. Then we can can update the database section code in order to use a different database depending if we are in production or development:

```
# in development
if development==True:
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}
}
# in production
else:
if "DATABASE_URL" in os.environ:
# production database (Postgress)
DATABASES = {
'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
else:
print('Database URL not found. Using SQLite instead')
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}
}
```

24. Then in [AWS](https://aws.amazon.com/) S3 we will configure our buckets to host the static and media files there.

25. To use S3 we will need to install django-storages and boto3 and we will also have to add storages to INSTALLED_APPS

```pip install django-storages```
```pip install boto3```

```
INSTALLED_APPS = [
.....
'storages',
.....
]
```

26. We will need to create a custom_storages.py file in order to specify the locations for Media and Static.

```
class StaticStorage(S3Boto3Storage):
location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
location = settings.MEDIAFILES_LOCATION
```

26. After this we will have to update the settings.py as follows:

```
# variables and keys needed in order to set up the connection with AWS S3
AWS_S3_OBJECT_PARAMETERS = {
'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
'CacheControl': 'max-age=94608000'
}

AWS_STORAGE_BUCKET_NAME = 'tree-books'
AWS_S3_REGION_NAME = 'eu-west-3'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_SECRET_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

27. Then we will run the following command to send the files to S3:

```
python manage.py collectstatic
```

26. Finally, we can add additional syntax to the settings.py to use different code for the static and media storage depending on if we are in development or production

```
# in development we keep the files locally
if development==True:

# we need a static root. All static files will be in the static directory
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# we need a media root. All media will be in the media directory
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# in production we use AWS S3 to host the media and static files
else:
# variables and keys needed in order to set up the connection with AWS S3
AWS_S3_OBJECT_PARAMETERS = {
'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
'CacheControl': 'max-age=94608000'
}

AWS_STORAGE_BUCKET_NAME = 'tree-books'
AWS_S3_REGION_NAME = 'eu-west-3'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_SECRET_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

### Deployment

Once the website is working correctly I have deployed to Heroku following these steps:

1. I have created an app (I already created an app before in order to get the Postgress URL link)

2. In the settings (Config Vars) I have added all the environmental variables that were included in the env.py apart from 'ENVIRONMENT'

3. Then I went back to vscode and I installed gunicorn. This is required to connect to Heroku
```pip install gunicorn```

4. I also updated the requirements.txt
```pip freeze > requirements.txt```

5. I created the Procfile (to tell Heroku what type of app is getting)

```web: gunicorn treebooks.wsgi:application```

6. Then I added to the Config Vars DISABLE_COLLECTSTATIC = 1 to tell Heroku not to try to collect Static files.

7. After this we need to add the Heroku app address to the ALLOWED_HOST section in settings.py

8. Then we will push the changes to GitHub

9. In Heroku in the deploy section, we will connect to our Github repository and deploy the branch.

10. After checking that everything is working correctly we can 'Enable Automatic Deploys and that way when we push code to GitHub it will automatically deploy the project in Heroku

### My repository

https://github.com/elenasacristan/treebooks

### My deployed app

https://treebooksproject.herokuapp.com/

## Credits

#### Content

The books details and images have been taken from Wikipedia.

#### Media

All the images used in the websites have been obtained from Google images using the Advance Search and selecting “free to use, share or modify, even commercially”. See the links below:

##### carousel images

[https://www.maxpixel.net/Frying-Pan-Cooking-Food-Cook-Figure-Fried-3125716](https://www.maxpixel.net/Frying-Pan-Cooking-Food-Cook-Figure-Fried-3125716)

##### user profile images for the test users

[https://www.seriouseats.com/2015/05/pancakes-around-the-world.html](https://www.seriouseats.com/2015/05/pancakes-around-the-world.html)

##### other images

Project 1

Project 2

Emoticon for favourites

Book icon in index. Html and detail. Html

Tree icon in index. Html

Timer icon used in index. Htnk and detail. Htnl


## Acknowledgements

**Templates**

#####navbar

In order to create the navbar I have used the following link to help me with the alignment.

LINK

##### ecommerce Xxxx template

I have used the template Xxxx in order to start building the basic design for the all_book. HTML, the detail. HTML and the cart and the. I have customise it.

**Tutorials**

Userprofile

Redirect to the same page

List values

Client

Test

Data schema

Leaflet

Hover ove4

Spiner

- **Login / Register**:
I watch the following tutorial to understand how to create the login/register functions.
[https://www.youtube.com/watch?v=vVx1737auSE](https://www.youtube.com/watch?v=vVx1737auSE)

* \***\*Upload image\*\***
I found information about how to upload images into mongodb using flask on the following video tutorial:
[https://www.youtube.com/watch?v=DsgAuceHha4](https://www.youtube.com/watch?v=DsgAuceHha4)

- \***\*Display image as soon as it is selected\*\***
The following post help me to create the code in order to display the image as soon as it is selected using the input file.
[https://gist.github.com/zulhfreelancer/1a1b68062da349d6268f0aaa43991b99](https://gist.github.com/zulhfreelancer/1a1b68062da349d6268f0aaa43991b99)

* \***\*Create interactive visualization using DC/JS Crossfilter\*\***
I learn how to set up the connection between mongodb and DC/JS Crossfilter by following the tutorial in the link below:
http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/

- \***\*Log out / clear cookies\*\***
In the link below I learnt about how to remove the cookies when the user logs out. https://www.tutorialspoint.com/flask/flask_sessions.htm

* As always the slack community has been very helpful when I had any question.

- I'm also really thankful to the Tutors who help me understanding how to set up environmental variables in vscode.