[![Build Status](https://travis-ci.org/elenasacristan/treebooks.svg?branch=master)](https://travis-ci.org/elenasacristan/treebooks)

# TreeBooks! – Fourth milestone project

TreeBooks is a charity that aims to raise money to plant trees by renting second-hand books.

To be able to rent books the users need to register. Only registered users will be able to rent books, read reviews, join the waiting list for a book, keep track of the books read and save the books that they like in a favourites list.

The users who are not registered will see in the landing page the main reasons why they should register. Users not registered can't rent books but they can see the listing with all the books and the details page. In the details page, they won't be able to see the reviews but they will be able to see the average ratings for each book and the main details about the books.

Also registered and not registered users can donate books to the charity. If they want to donate they can see in the donate.html page the map with the collection points where they can drop their books to help the charity to grow the collection of books to offer.

All users can also read how the website works by reading the about.html page.
All users will also have access to the projects page where they can see how much money has been raised by the charity until now, how many books have been rented and to what projects is the charity going to donate the money raised.

The users can search for a specific book or author by typing on the search box.

The users can contact the charity using the contact form in case they have any questions or projects in mind.

The user will be able to follow TreeBooks on social media by clicking on the icons on the footer of the page.

See below the link to the website:

https://treebooksproject.herokuapp.com/

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

- The final design of the website included some additional functionalities (buttons, carousel, modals and messages) that I thought would be useful as I was working on it. I also changed slightly the styles (colours, transparency, shadows, borders) for others that I found more appropriate.

### User stories

As a charity owner, I want to get users to register to the website so I can rent books to them and I can raise money to plant new trees.

As a user (member or not) I want to be able to see what is the aim of the website.

As a user (member or not) I want to be able to see what projects is the charity planning to contribute to and how much money the charity has raised so far.

As a user (member or not) I want to be able to contact TreeBooks to send my comments and suggestions for new projects.

As a user (member or not) I want to donate books and I want to know where are the collection points.

As a user I want to register to be able to rent books and contribute to reforestation projects

As a user I want to register to be able to save money reading second-hand books instead of buying brand new books.

As a member I want to feel that I'm helping to save the planet by not buying new books and by renting second-hand books.

As a member I want to be able to add my name to a waiting list if the book that I want to read is not available

As a member I want to be able to see my position in the waiting lists.

As a member I want to see a notification when my turn to read the book has been reached.

As a user I'd like to know what books are available and which ones have waiting lists.

As a member I want to be able to save books as favourites.

As a member I want to be able to see all the books that I have read since I started the membership.

As a member I want to be able to review the books that I have read.

As a member I want to be able to add books to the shopping cart and then pay all of them at once.

As a member I want to be able to update the number of days to rent the book from the cart page.

As a member I want to be able to remove books from the cart if I change my mind about the books.

As a member I want to see in my profile when is the return date for the books that I'm currently reading.

As a user (member or not) I want to be able to see all the books in TreeBooks and their details.

As a user(member or not) I want to be able to search for a book or author by typing on the search box.

As a member I want to be able to see the reviews given by other members.

As a member I want to be able to register to the monthly newsletter.

As a member I want to be able to edit my profile details and add a profile image.

As a member I want to be able to follow TreeBooks in Social Media.

## Features

### Accounts app

The accounts app will allow users to register to become members of TreeBooks. The registered users will be able to access all the member features.

The users will register using the registration form and then they will be able to log in by using the login form with their username and password or with the email and password.

The users can also reset the password if they forgot the original password using the reset password link on the login.html page.

### books app

#####view-all-books.html

Display all the books present on the website. The books are displayed by category and they are sorted in descending order by the review score.

In this page the user only will see the name of the book, the star rating and the rating score. If they want to know more about the book or rent it they need to click on the 'more' button.
If the user is authenticated then he/she will also be able to see a message about the status of the book ('available', 'check waiting list', 'It's your turn!' or 'you are reading this book'.
By clicking on the book title, the 'AVAILABLE' text or the 'It's your turn' badge the user will also be redirected to the detail page.
If the user clicks on 'check waiting list' then it will be re-directed to the waiting list for that book.

#####detail.html

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

In the list of books read the user will have the option to leave a review for the books that have rented. Only will be able to add one review per book.

By clicking 'books in waiting list' the modal window will appear and the user will be able to see a list of books that he is waiting for with a link in each book to see the waiting list.

Treebooks will contact the next user in the contact list as soon as the book is returned by the previous user. Also, the user will see a notification saying 'it's your turn' on the books listing. Then the next user in the waiting list can proceed to rent the book online. Only the next user in the waiting list will have the option to rent the book for the rest of the users the book will not be available.


##### edit_user_profile.html

The users can edit their profile details by clicking on edit profile on the profile page.

They will be able to add and edit the profile picture, the date of birth, and the telephone.

Then they can choose to opt-in for the monthly newsletter and they can also select what is the preferred way to be contacted (phone, email or both)


### Home app

##### index.html

This is the home page and the user will get redirected to this page when they click on the logo or the home tab on the navbar.

This page has a carousel highlighting the main areas of the charity.

At the bottom the users can see the main benefits of being a member. 
The users that are not authenticated will see the message 'Become a member and you will...' and also they will see the button register so they can become members.

If the user is authenticated then he/she won't see the register button and the header will have the message saying 'Hi USERNAME, with TreeBooks you can...'

##### about.html

This page explains the aim of the website and how it works. It has re-directs to other areas of the website (projects.html and donate.html)

##### projects.html

In this page the user can see how much money has been raised by the charity since the charity started and the user also can see rental since the beginning.

Also, the user will see what are the projects that the charity is trying to raise money for and what is the target for each.

By clicking on the project name the user will be redirected to the projects.
* Note that the projects that I'm showing are two projects that I found randomly on the internet in order to have them as an example in the website but I'm not familiar with them.

##### donate.html

If the users (registered or not) would like to collaborate with the charity by donating books, on this page they can see a map with the collections points where they can drop their books.

##### contact.html

In the footer there is a link to the contact us page. In this page the user can fill out the form to send a message to the charity.

### Cart app

#####cart.html

This page will display the books that the user have added to the shopping cart and will give the user the option to update the number of days selected or remove the books completely.

Then it will display the total to pay. A £5 deposit by book will be added to the total price and that deposit will be refunded once the book is returned.

The user will have the option to proceed to the payment by clicking the 'checkout' button or continue searching for other books by clicking the button 'keep looking' .

### Checkout

#####chaeckout.html

In the checkout page the user will see the details of the books that he/she is going to rent and the total to pay.

Then they will need to fill out the payment form in order to rent the book(s).

Once the payment has gone through a success message will be displayed and then the user can go to the specified store where the book belongs and collect it.

If there is an error with the payment the user will see an error message.

If the payment has been successful the following will happen:
 - The book(s) will be added to the list of read books and the list of current_books
 - The book will become NOT available
 - The money paid for the book (not including the deposit) will be added to the total money raised for the charity
 - The number of books rented will be added to the number of books rented since the charity started.
 - If the user was in a waiting list for the books that he/she is renting then his/her name will be removed from the waiting list.

### Waiting_list app

##### waiting_list.html

Only authenticated users will be able to see or join waiting lists for books.

This page will display the list of users waiting for a book in order.
Number 1 will be the next user to read the book, number 2 the second and so on.

If the waiting list is empty the header will say: "You could be next!" and then there will be an alert message saying "There is no one waiting!"

At the bottom of the waiting list there will be two buttons. The "Keep looking" button will redirect the user to the all_books.html page and the "Go to Book" will redirect the user to the detail.html page for that book.


### Reviews app

##### review_form.html

Once the user has rented a book he/she can leave a review. 
The users can see the books that they have read on their profile page and in the "See the books you read" section they can see all the books they have read and for each one they will have the option to leave a review. Once they have reviewed the book then they will see the message 'Already reviewed' under the book title.

The review_form.html page will display a form where the user can enter the title of the review, the comment and the score from 0 to 5.

Then the review will be added to the detail.html page for that book.
Each review will display the individual star rating and then all the reviews will be taken into account to calculate the mean score for that book (and that average start rating and score will be displayed on the top left side of the details page)


### Favourites app

The user can add/remove the book that he/she wants to the list of favourites by clicking the heart icon on the pages all_books and detail.

Then the user can see all the favourites books if he clicks on "See your favourites" on the user profile page.


### Search app

This app will allow the user to search for a book based on the title name or author name.

The search box is displayed at the top of the navbar and it is visible from all pages.

The books that contain the word entered in the title or in the name of the author will be displayed and will be sorted by score descending.

### Other features available from all pages






### nav bar
The navbar will be available from all the pages in the website.
In order to create the navbar I have used Bootstrap 4 and I have used the following link to help me align the elements inside.

### Hamburger button
The hamburger button from bootstrap 4 will appear on small screens and when is clicked with display the navbar vertically and it will also include the login and cart options.

### social links

. They appear on the page footer in every page on the website and by clicking on them the user will get redirected to the media websites to follow TreeBooks. (since the website is fictitious they will be redirected to the login page for facebook or twitter).

### Logo
The logo will appear in the navigation bar for every section of the website and when clicked it will redirect the user to the home page (index.html).





.

## Features Left to Implement

If the book is not available then display the current reader on the details.html page.

## Technologies Used

#### Database:

- \***\*[Postgress]\*\***

See below the database schema:

ADD SCHEMA

![database](/documents/db_schema/data_schema.png)

#### Graphic Design software:

- **\*\*\*\***[Adobe Fireworks:](https://www.adobe.com/products/fireworks.html)**\*\*\*\*** I have used Adobe Fireworks to create the logo and the mock-ups.

#### Languages:

- \***\*HTML5:\*\*** Is the main language used to create the structure of the website.

- \***\*CSS3:\*\*** Is the language used to add styles to the HTML.

- **\*\*\*\***[JavaScript:](https://developer.mozilla.org/en-US/docs/Web/JavaScript)**\*\*\*\*** This is the language used to add interactivity to the website. It has been used to add the spinner while the pages load and in order TO AUTOSCROLL THE BOOKS WHEB HOVERING OVER

- **\*\*\*\***[Python:](<[https://www.python.org/](https://www.python.org/)****>)\*\*\*\* The main logic of the website has been created using Python.

- \***\*[Django:]()>)\*\*** I have used the django framework.

#### Dependencies:

#### Libraries

- **\*\*\*\***[jQuery](https://jquery.com/)**\*\*\*\***

* **\*\*\*\***[FontAwesome:](https://fontawesome.com/ "https://fontawesome.com/")**\*\*\*\*** .

* **\*\*\*\***[Google Fonts:](https://fonts.google.com/ "https://fonts.google.com/")**\*\*\*\*** I’ve used the fonts from Google Fonts to style the fonts in the website.

#### Development environment:

- **\*\*\*\***[VisualStudio:](https://visualstudio.microsoft.com/)**\*\*\*\***

I have used Visual Studio to develop the app.

#### Version control system:

- **\*\*\*\***[Git:](https://git-scm.com/ "https://git-scm.com/")**\*\*\*\***

I have used the version control system Git from the "Git Bash" terminal in order to track changes in the website and push them to GitHub.

#### Hosting service:

- **\*\*\*\***[Heroku:](<[https://www.heroku.com/](https://www.heroku.com/)****>)\*\*\*\*

I have used Heroku in order to deploy the website.

## Testing

### Validation

- \***\*HTML:\*\*** I have used https://validator.w3.org/ in order to validate the HTML code.

- \***\*CSS:\*\*** I have used https://jigsaw.w3.org/css-validator/ in order to validate the CSS code.

- \***\*JavaScript:\*\*** I have used https://jshint.com/ in order to check the JavaScript code.

### Features and responsiveness testing

#### django tests

I have run tests for the models, forms and views in all apps where applicable. See the coverage reports for each app below:

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

The code that I was meant to use in the Travis.yml file was not working and I found out that there were some issues when using python 3.7 and django 1.11.17. Finally, I found out in Slack the code that was working well for my python and django versions.

#### Dev Tools

I have also used development tools in Google Chrome to check how the website would look on different devices (portrait and landscape mode). In addition to that testing, I have also asked friends and family to have a look at the website to let me know if everything looks fine on their browsers and devices.

### Problems and bugs:

I have issues when iterating on fields with many to many relationships and in the end, I could fix these problems by using (loop.first) and in other cases by using of list_values.

When I changed from the local database to the Postgress database suddenly I started having errors when adding more than one user to the waiting list. This issue was very strange because in the local database was working fine. I ask the Tutors and they suggest to create a new link to a new postgrees database to see if this could solve the problem but it didn't.
Finally I noticed that every time I was adding a user to the waiting list I was also adding a book and that is why the book Id was duplicated.

Current books if the book became available again it will appear on the profile fro the other users that have already finished the book

This issue was fixed by using get or create. So a book will only be added if it didn't exist already.

# GitHub repository

1. I've created a repository in GitHub called: “elenasacristan/xxxxx” [https://github.com/elenasacristan/Xxxxx.git](https://github.com/elenasacristan/xxxx.git)

2. I've initialised git from the terminal using Git Bash:

`git init`

3. I have created a .gitignore file and I have added the files and folder that don't need to be commited (i.e. '.venv' folder)

4. I've added the files that I was working on to the Staging area by using:

`git add .`

5. I've run the commit command with the first commit

`git commit -m “initial commit"`

6. I copied from GitHub the following path and I ran it in the Git Bash terminal in order to indicate where my remote repository is:

`git remote add origin git@github.com:elenasacristan/xxzxx.git`

`git push -u origin master`

7. After this has been done I've run regular commits after every important update to the code, and I pushed the changes to GitHub.

## Deployment

### Running my code locally

1. First in vs code I've created a virtual environment:

`python -m venv .venv`

2. I've Installed django

`CODE HERE

4. Then I've created my app by running the following code (where appname will be replaced by the name of each of my apps)

CODE HERE

5. I have added each app in the project to the list of INSTALLED APPs

6. I have added 127.0.0.1?? To the list of allowed hosts.

EXPLAIN ALL APPS 
Send emails 
Templates 
Login using email

CART 
session

7. Then I have created for each app the files models.py, forms.py,views.py and urls.py.

SEE MODELS SHEMA HERE.. LINK

After creating or updating any of model.py files I have always makemigrations and migrate using the following code.

ADD CODE HERE

8. I have also created the admin.py in order to add the model to the admin site.

9. In order to manage image files I have installed pillow

10. I have created a env.py file and I have saved on it all my keys and password.. INDICATE ALL THTA IS SAVED HERE

11. Then this file has been added to the .gitignore to avoid uploading it into Github

12. Then in the settings file I have used the following code so depending on if I'm working on development mode or production the DEBUG will be set to True or False respectively.

### Static files hosting AWS

### Deployment

I have used Heroku to deploy the website. In order to do that I have followed the steps below:

1. I've changed the settings to Debug=False ("FLASK_DEBUG": "0")

2) I've added the env.py file to the gitignore file.

3) I've created an app in Heroku

5. In the settings (Config Vars) I've added my environmental variables for the SECRET_KEY, POSTGRESS LINKS.. ETC

6) From the command line in vs code I have created a requirements.txt file with the following command:

`python -m pip freeze > requirements.txt`

7. From the command line in vs code I have created the Procfile with the following command:

A BIT DIFFERENT?

`echo web: python app.py > Procfile`

8. Then I have pushed all the code to my GitHub repository

9) After this \***\*I have linked my Heroku app with my GitHub repository\*\*** in order to be able to do "Continous delivery". I've learned how to link Heroku and GitHub with the following tutorial ([https://www.youtube.com/watch?v=\_tiecDrW6yY](https://www.youtube.com/watch?v=_tiecDrW6yY)).

10. Then I have created another app with the same Config Vars and I have created a pipeline where the first app will be the staging app and the second app will be the production app. When I push changes to GitHub I'll be able to see the changes on the Staging App but not in the Production app.

11) Once the website has been fully tested and is working correctly the changes done to the staging app have been promoted to the Production app:

[https://xxxxxxx.herokuapp.com/](https://xxxxxx.herokuapp.com/)

### My repository

https://github.comelenasacristan/XXXX/

### My deployed app

http://XXXX.herokuapp.com

## Credits

#### Content

- \***\*Data:\*\*** The data for the recipes has been collected from https://en.wikibooks.org/wiki/Category:Recipes

#### Media

##### background image login / register page

- The image used for the background image in the intro page was obtained from Google images using the Advance Search and selecting “free to use, share or modify, even commercially”. See link below:

[https://www.maxpixel.net/Frying-Pan-Cooking-Food-Cook-Figure-Fried-3125716](https://www.maxpixel.net/Frying-Pan-Cooking-Food-Cook-Figure-Fried-3125716)

##### recipes images

- The recipes images have been obtained from Google images using the Advance Search and selecting “free to use, share or modify, even commercially”. See links below:

[https://www.seriouseats.com/2015/05/pancakes-around-the-world.html](https://www.seriouseats.com/2015/05/pancakes-around-the-world.html)

[https://pixabay.com/photos/food-fish-chips-fish-and-chips-3687804/](https://pixabay.com/photos/food-fish-chips-fish-and-chips-3687804/)

[https://pixabay.com/images/search/burger/](https://pixabay.com/images/search/burger/)

[https://commons.wikimedia.org/wiki/File:Bolo_de_Mel.JPG](https://commons.wikimedia.org/wiki/File:Bolo_de_Mel.JPG)

[https://www.flickr.com/photos/30478819@N08/35961379924](https://www.flickr.com/photos/30478819@N08/35961379924)

[https://www.flickr.com/photos/146966953@N02/28879437404](https://www.flickr.com/photos/146966953@N02/28879437404)

[https://www.flickr.com/photos/39908901@N06/8406293769](https://www.flickr.com/photos/39908901@N06/8406293769)

[https://www.flickr.com/photos/jeffreyww/5063817774](https://www.flickr.com/photos/jeffreyww/5063817774)

[https://www.flickr.com/photos/ellaolsson/30863436677](https://www.flickr.com/photos/ellaolsson/30863436677)

[https://pxhere.com/en/photo/619505](https://pxhere.com/en/photo/619505)

[https://pixabay.com/photos/iced-coffee-coffee-drink-2710815/](https://pixabay.com/photos/iced-coffee-coffee-drink-2710815/)

[https://www.flickr.com/photos/30478819@N08/43801037610](https://www.flickr.com/photos/30478819@N08/43801037610)

[https://pixabay.com/photos/salad-tuna-salad-article-nafut-1088411/](https://pixabay.com/photos/salad-tuna-salad-article-nafut-1088411/)

## Acknowledgements

\***\*Templates\*\***

- I have used the following bootstrap login design to help me creating the login/register pages and then I have modified the colours and image.

[https://startbootstrap.com/snippets/sign-in-split/](https://startbootstrap.com/snippets/sign-in-split/)

\***\*Tutorials\*\***

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
