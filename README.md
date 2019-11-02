[![Build Status](https://travis-ci.org/elenasacristan/treebooks.svg?branch=master)](https://travis-ci.org/elenasacristan/treebooks)

# TreeBooks! – Fourth milestone project

TreeBooks is a charity that aims to raise money to plant trees by renting second hand books.

In order to be able to rent books the users need to register. Only registered users will be able to rent books, read reviews, join waiting list for a book, keep track of the books read and save the books that they like in a favourites list.

The users who are not registered will see in the landing page the main reasons why they should register. Users not register can't rent books but can see the listing with all the books and the details page. In the register page they won't be able to see the reviews but they will be able to see the average ratings for each book and the main details about the books.

Also registered and not registered users can donate books to the charity. If they want to donate they can see in the donate.html page the map with the collection points where they can drop their books to help the charity to grow the collection of books to offer.

All users can also read how the website works by reading the about.html page  
All users will also have access to the projects page where they can see how much money has been raised by the charity until now and what projects is the charity going to donate the money raised.

The users can search for a specific book or author by typing on the search box.

The users can contact the charity using the contact form in case they have any questions or projects in mind.

The user will be able to follow TreeBooks on social media by clicking on the icons on the footer of the page.

See below the link to the website:

UPDATE!!  
http://treebooks.herokuapp.com

## UX

This website is targeting people who likes reading books but at the same time is concerned about how many trees are cut to create new books. They will want to use the website because reading second hand books they are stopping more trees being cut and because the money paid to rent the books will be used in reforestation projects.

TreeBooks is a charity so the aim of the website is to attract users who then will rent books from them. They also want to grow the collection of books by getting people to donate second hand books.

### mock-ups:

Below you can see the mock-ups that I drew using [Pencil](https://pencil.evolus.vn/'https://pencil.evolus.vn/) and [Adobe Fireworks](https://www.adobe.com/products/fireworks.html).

##### Design used for login.html, registration.html, Password reset password page ... write a review form , contact

![many](/static/mockups/small_common_style.png)

##### home.html

![home](/static/mockups/home.png)

##### about

![about](/static/mockups/about.png)

##### projects

![projects](/static/mockups/projects.png)

##### donate

![donate](/static/mockups/donate.png)

##### books

![books](/static/mockups/books.png)

##### detail

![detail](/static/mockups/detail.png)

##### profile

![profile](/static/mockups/profile.png)

##### edit profile

![edit profile](/static/mockups/edit_profile.png)

##### cart

![cart](/static/mockups/cart.png)

##### checkout

![checkout](/static/mockups/checkout.png)

- The final design of the website included some additional functionalities (buttons, carousel, modals and messages) that I thought would be useful as I was working on it. I also changed slighly the styles (colours, transparency, shadows, borders) for others that I found more appropiate.

### User stories

As a charity owner I want to get users to register to the website so I can rent them books and I can raise money to plant new trees.

As a user (member or not) I want to be able to see what is the aim of the website.

As a user (member or not) I want to be able to see what projects is the charity planning to contribute to and how much money the charity has raised so far.

As a user (member or not) I want to be able to contact TreeBooks to send my comments and suggestions for new projects .

As a user (member or not) I want to donate books and I want to know where are the collection points.

As a member I want to register to be able to rent books and contribute to reforestation projects

As a member I want to register to be able to save money reading second hand books instead of buying brand new books.

As a member I want to feel that I'm helping to save the planet by not buying new books and by renting second hand books.

As a member I want to be able to add my name to a waiting list if the book that I want to read is not available

As a member I want to be able to see my place in the waiting lists.

As a member I want to be able to save books as favourites.

As a member I want to be able to see all the books that I have read since I started the membership.

As a member I want to be able to review the books that I have read.

As a member I want to be able to add books to the shopping cart and then pay all of them at once.

As a user (member or not) I want to be able to see all the books in TreeBooks and their details.

As a user(member or not) I want to be able to search for a book or author by typing on the search box.

As a member I want to be able to see the reviews given by other members.

As a user I'd like to know where should I bring the second hand books that I want to donate.

As a member I want to be able to register to the monthly newsletter.

As a member I want to be able to edit my profile details and add a profile image.

## Features

### authentication and authorisation

Registration form allow users to become members

The login form allows register member to login and access all the features of authenticated users. The user will be able to login using the username and also using the email instead of the username. (place holder update username / email)!!!!!!!!!!

The users can reset the password if they forgot the original password using the reset password link on the login.html

### books app

View-all-books. Hyml

Display all the books present on the website. The books are displayed by category and they are sorted by availability first and then by the review score.

In this view the user only will see the name of the book, the rating score and the availability. If they want to know more about the book or rent it they need to click on the more button.

Detail. Html

In this page the user can see all the details about the book. title, author (by clicking on the author name they will get redirected to the Wikipedia url for that author), sinopsys, date it was published, number of pages, book type (hardcover or paperback), number of pages, store where the book has to be collected from, ISBN number.

Then in this page if the book is available and the user is authenticated then the user can select the number of days that wants to rent the book for (the minimum number of days will be 10 and it has been set as the default value) and add it to the shopping cart.

If the book is not available and the user is authenticated then the user can join the waiting list.

If the user is not authenticated he/she will see a button to register in case they would like to rent the book.

### view profile

The user case see his/hers personal and membership details by clicking on the profile tab in the navigation bar.

The profile will display the following information about the user:

- profile image
- membership details (date that the user registered and if they are subscribed to the newsletter)
- currently reading: a list with the books that the user is renting at the moment including the date that they need to be returned.
- personal details (name, email, telephone and date of birth)
- contact preferences  
  At the bottom the user can access the list of books read, the list of books he/she is in the waiting list for and the list of favourites.

In the list of read books the user will have the option to leave a review for the books that have rented. Only will be able to add a review once per book.

In the list of books in waiting list the user will have the option to se the waiting lists for each book so he/she can see what is the order.

Treebooks will contact the next user in the contact list as soon as the book is returned by the previous user. The the next user in the waiting list can proceed to rent the book online. Only the next user in the waiting list will have the option to rent the books for the rest of the users the book will not be available.

ADD message after joint waiting list saying.. You have joined the waiting list we will contact you when you reach your turn

....

### edit profile

The users can edit their profile details by clicking on edit profile on the the View profile page.

### home app pages

### index. Htnl

This is the home page and the user will get redirected to this page when they click on the logo or on the home tab on the nav bar.

This page has a corusel highlighting the main areas of the charity.

At the bottom the users can see the main benefits of being a member. The users that are not authenticated will also see the button register so they can became members.

If the user is already registered the they won't see the register button and instead they will see the header saying 'hello username...

### about. Html

This page will explain the aim of the website and how it works. It will have redirects to other areas of the website (projects. HTML and donate. HTML)

### projects. Hntl

In this page the user can see the total monye raised by the charity since they starting raising money and they also can see the number of times books have been rented.

Also they user will see what are the projects that the charity is trying to raised money for and what is the target.

### donate.

In this page any user (registered or not) who wants to collaborate with the charity can see the collection points available where they can bring their second hand books that they wish to donate.

### Cart

This page will display the book ls that they user have added to the shopping cart and will giv ethe user the option to update the number of days selected or to remove the book.

THEN it will display the total to pay. A £5 deposit by book will be added to the total price and that deposit will be refunded once the book is returned.

Once the user is iin the checkout page he/she can decide if they want to proceed to the payment or keep looking got more books.

### Checkout

In the checkout page the user will see the details of the books that he/she is going to rent an dthe total to pay.

Then they will need to fill out the payment form in order to rent the book.

Once the payment has gone through a success message will be display and then the user can go to specified store where the book belongs and collected.

If there is any error with the payment the user will see an error message //CHANGE COLOR TO DANGER !!

### Other features available from all pages

### search

### contact us

### nav bar

### social links

- \***\*Navigation bar:\*\*** I have created the navigation bar using bootstrap 4 nav bar.

- \***\*Mobile Collapse Button:\*\*** The \***\*Mobile Collapse Button\*\*** will appear in smaller screens (tablets and mobiles) and by clicking on it, it will show the navigation bar as a sidebar.

- \***\*Logo:\*\*** The logo will appear in the navigation bar for every section of the website and when clicked it will redirect the user to the home page (index.html).

- \***\*Social media links:\*\*** They appear on the page footer in every page on the website and by clicking on them the user will get re-directed to the media websites to follow TreeBooks. (since the website is fictitious they will be redirected to the login page for facebook or twitter).

.

- \***\*Contact Us:\*\*** Provides the user with the contact form to get in touch with the charity.

* **Search input box**: On the top left corner of the page the users can enter text to search for a specific book or author. .

### In the index page

- \***\*Carousel:\*\***

- \***\*Modal:\*\*** When the user clicks on "delete button" the confirmation message will be displayed on a modal window and the recipe will only be removed if "YES" is selected. This modal has been taken from [Materialize](<[https://materializecss.com/](https://materializecss.com/)>).

.

## Features Left to Implement

## Technologies Used

#### Database:

- \***\*[Postgress]\*\***

See below the satabase schema:

ADD SCHEMA

![database](/static/img/schema.jpg)

#### Mock-up tool:

- \***\*[XXXX:]()\*\*** I have used XXXX to create the mock-ups for the website.

#### Graphic Design software:

- **\*\*\*\***[Adobe Fireworks:](https://www.adobe.com/products/fireworks.html)**\*\*\*\*** I have used Adobe Fireworks to edit the background images, to create the logo and to do some edits on the mock-ups.

#### Languages:

- \***\*HTML5:\*\*** Is the main language used to create the structure of the website.

- \***\*CSS3:\*\*** Is the language used to add styles to the HTML.

- **\*\*\*\***[JavaScript:](https://developer.mozilla.org/en-US/docs/Web/JavaScript)**\*\*\*\*** This is the language used to add interactivity to the website. It has been used to add the spinner while the pages load and in order TO AUTOSCROLL THE BOOKS WHEB HOVERING OVER

- **\*\*\*\***[Python:](<[https://www.python.org/](https://www.python.org/)****>)\*\*\*\* The main logic of the website has been created using Python.

- \***\*[Django:]()>)\*\*** I have used the django framework.

#### Dependencies:

#### Libraries

- **\*\*\*\***[jQuery](https://jquery.com/)**\*\*\*\*** It is needed for the [Materialize](<[https://materializecss.com/](https://materializecss.com/)>) JavaScript components to function.

* **\*\*\*\***[FontAwesome:](https://fontawesome.com/ "https://fontawesome.com/")**\*\*\*\*** In some cases if FontAwesome icon was more appropriate I have also used FontAwesome.

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

Click [here](https://github.com/elenasacristan/HolidaysYa/tree/master/assets/Documents/checkList.pdf) to see the checklist that I have used to test all the features in all the screen sizes.

### Additional testing

#### Travis

#### django tests

Explain the coverage testing

#### Dev Tools

I have also used development tools in Google Chrome to check how the website would look in different devices (portrait and landscape mode). In addition to that testing I have also asked friends and family to have a look at the website to let me know if everything looks fine on their browsers and devices.

### Problems and bugs:

- \***\*many to many duplication issue in templates\*\***  
  Fixed by using if for loop.first

# GitHub repository

1.  I've created a repository in GitHub called: “elenasacristan/xxxxx” [https://github.com/elenasacristan/CookBook.git](https://github.com/elenasacristan/xxxx.git)

2.  I've initialised git from the terminal using Git Bash:

`git init`

3.  I have created a .gitignore file and I have added the files and folder that don't need to be commited (i.e. '.venv' folder)

4.  I've added the files that I was working on to the Staging area by using:

`git add .`

5.  I've run the commit command with the first commit

`git commit -m “initial commit"`

6.  I copied from GitHub the following path and I ran it in the Git Bash terminal in order to indicate where my remote repository is:

`git remote add origin git@github.com:elenasacristan/xxzxx.git`

`git push -u origin master`

7.  After this has been done I've run regular commits after every important update to the code, and I pushed the changes to GitHub.

## Deployment

### Running my code locally

1.  First in vs code I've created a virtual environment:

`python -m venv .venv`

2. I've Installed django

`CODE HERE

4. Then I've created my app by running the following code (where appname will be replaced by the name of each of my apps)

CODE HERE

5.  I have added each app in the project to the list of INSTALLED APPs

6.  I have added 127.0.0.1?? To the list of allowed hosts.

EXPLAIN ALL APPS  
Send emails  
Templates  
Login using email

CART  
session

7.  Then I have created for each app the files models.py, forms.py,views.py and urls.py.

SEE MODELS SHEMA HERE.. LINK

After creating or updating any of model.py files I have always makemigrations and migrate using the following code.

ADD CODE HERE

8.  I have also created the admin.py in order to add the model to the admin site.

9.  In order to manage image files I have installed pillow

10. I have created a env.py file and I have saved on it all my keys and password.. INDICATE ALL THTA IS SAVED HERE

11. Then this file has been added to the .gitignore to avoid uploading it into Github

12. Then in the settings file I have used the following code so depending on if I'm working on development mode or production the DEBUG will be set to True or False respectively.

### Static files hosting AWS

### Deployment

I have used Heroku to deploy the website. In order to do that I have followed the steps below:

1.  I've changed the settings to Debug=False ("FLASK_DEBUG": "0")

2) I've added the env.py file to the gitignore file.

3) I've created an app in Heroku

5.  In the settings (Config Vars) I've added my environmental variables for the SECRET_KEY, POSTGRESS LINKS.. ETC

6) From the command line in vs code I have created a requirements.txt file with the following command:

`python -m pip freeze > requirements.txt`

7.  From the command line in vs code I have created the Procfile with the following command:

A BIT DIFFERENT?

`echo web: python app.py > Procfile`

8. Then I have pushed all the code to my GitHub repository

9)  After this \***\*I have linked my Heroku app with my GitHub repository\*\*** in order to be able to do "Continous delivery". I've learned how to link Heroku and GitHub with the following tutorial ([https://www.youtube.com/watch?v=\_tiecDrW6yY](https://www.youtube.com/watch?v=_tiecDrW6yY)).

10. Then I have created another app with the same Config Vars and I have created a pipeline where the first app will be the staging app and the second app will be the production app. When I push changes to GitHub I'll be able to see the changes on the Staging App but not in the Production app.

11) Once the website has been fully tested and is working correctly the changes done to the staging app have been promoted to the Production app:

[https://time2eat-cookbook.herokuapp.com/](https://time2eat-cookbook.herokuapp.com/)

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

<!--stackedit_data:

eyJoaXN0b3J5IjpbOTAyMjA3MDAsLTg5MzA0MzMxMiwxNTgzMD

kzMTE0LDE4NDE3Mzc4NTMsMzQ1NDQ3MTkzLC0xODczMDc3MzM3

XX0=

-->
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyNDI1MTYwNzYsMjA3MjA0MTU4MiwtMT
M1OTcwNDE1MywtOTk2NjMzOTQ1LC05OTg2MjIwNTMsODIwMzYw
MjgzLC0xOTQyMTY3ODAsODg5MDU5MDYzLDg2NTQ4OTM0NiwxOT
A2MTUyNjgyLC03ODYwMDU5MTksOTAyMjA3MDAsLTg5MzA0MzMx
MiwxNTgzMDkzMTE0LDE4NDE3Mzc4NTMsMzQ1NDQ3MTkzLC0xOD
czMDc3MzM3XX0=
-->
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTA3MTQzNzkyLC0xMjE0Mzk1MjgsLTE2MD
Q3NTQ0MTBdfQ==
-->
