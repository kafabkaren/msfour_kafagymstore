# KAFAGYM STORE

Welcome to [Kafagym Store Platform](https://msfour-kafagymstore.herokuapp.com/)

## Project rationale

The Kafagym Store platform was built, designed and deployed by Fabrice Karenzi as his final milestone project at the [Code Institute](https://codeinstitute.net/se/) Full Stack Web Development diploma. The website is
designed to provide customers at the Kafagym Store with the online options to puchase, rate and review the products made available to them from the store. It should be reminded that though it will turn into a viable e-commerce website for business at a later stage; it is serving for the purpose of education for the moment. It is a mobile responsive website.<br>

![MS4 Responsiveness.JPG](https://github.com/kafamem/msfour_kafagymstore/blob/main/media/msfour-resonsiveness.jpg)

# Target Audience of the website:
<ul>
    <li>Sport lovers with interests in sport products</li>
    <li>Customers who want to purchase sport products online</li>
</ul>

# Website Business Goals
<ul>
    <li>Increasing sales through online shopping of sport customers;</li>
    <li>Increading sport market coverage through purchase and delivery;</li>
    <li>Building Kafagym sport community via newsletter subscriptions;</li>
    <li>Building trustworthy sport online shop;</li>
</ul>

## UX<br>
## User stories<br>
As a shopper at The Kafagym Store website I expect/want/need:
<ul>
    <li>To view products to purchase by group of categories(eg. clothes, shoes, weights) and be able to navigate through them.</li>
    <li>Accessible information presented in clear and straight manner, so that I can find the product quickly.</li>
    <li>The ability to search for products based on a number of criteria; rating, price; categories, and name.</li>
    <li>To be able to read reviews and see ratings which can help me make a decision on product to buy.</li>
    <li>To be able to see images and clear relevant content, so that I know what I am about to buy.</li>
    <li>To view product details, know the price, see the image, size if any, description etc.</li>
    <li>To know about new offers(e.g. free delivery cost upon purchasing products of not less that 500 SEK etc).</li>
    <li>To view product details in my cart and confirm everything before purchase.</li>
    <li>Add, update and delete products in my cart so I can take control of my purchase.</li>
    <li>To feel comfortable providing my personal information(card details) through a secured payment system.</li>
    <li>To ensure the products and cost as final check on checkout page.</li>
    <li>To ensure my purchase has gone through, receive a confirmation notice and email</li>
    <li>To sign up and purchase products easier and see the order history.</li>
    <li>Add and update personal details.</li>
    <li>Account password reset function in case I forget it.</li>
</ul>

As a Store owner at The Kafagym Store website I expect/want/need:
<ul>
    <li>To provide a simple design e-commerce website without difficulties to look at the products and purchase them.</li>
    <li>To give to a user with of without account an option to checkout.</li>
    <li>To add new products to sell.</li>
    <li>To edit and update product.</li>
    <li>To delete product.</li>
    <li>To collect user email address for mailing about products, sales if any.</li>
    <li>To secure the website.</li>
</ul>

## UX 5 PLANES

## Strategy Plane

In order to ensure the user's goals and stories, below are the functions and features that were used with their relevant assessment scale ranging from 1 (least) and 5 (most).

| Feature       | Feasibility   | Importance  | 
| ------------- | ------------- | ------------- |
| Displaying products by group of categories  | 5 | 5 |
| Displaying products by category  | 5  | 5  |
| Viewing product details  | 5 | 5  |
| Rating products  | 5 | 4  |
| Reviewing products  | 4 | 4  |
| Search Function  | 5  | 5  |
| Sorting Function | 4  | 5  |
| Modifying products in shopping cart  | 5 | 5  |
| Checkout Function  | 5  | 5  |
| Secure payment  | 5  | 5  |
| Written confirmation after purchase  | 5 | 5  |
| Updating personal details  | 3  | 5  |
| Email subscription  | 5  | 5  |
| Add, Edit, Remove products (Admin only)  | 3 | 5  |
| Add, Edit, Remove Article (Registered Users)  | 3 | 5  |

## Strategy Plane

To satisfy the user's needs the features and functions below were implemented. As for the admin, CRUD (Create, Read, Update and Delete) functions are implemented on the website.
<ul>
    <li>Easy and simple design of the home page that ease the navigation without confusion. Clear grouping of products (Equipment, Outfit and New Offers) on the home page.</li>
    <li>Product pages by the group of categories where users can view all the products belong to the group.</li>
    <li>From the product details page uses can see all the product details. Users can also select options (e.g. Size if any) and add the product in the cart.</li>
    <li>Provision of shopping cart page for users to see all their chosen products before purchase. From there too, users can change the quantity of the product or remove it.</li>
    <li>Checkout page that allows users to provide shipping details and credit card details.</li>
    <li>Checkout success page to let users get confirmation of purchase.</li>
    <li>Register page where users can create an account to keep the shipping address saved and to view order histories.</li>
    <li>Profile page where users can see the personal details and order histories.</li>
    <li>Logout function that users can safely log out and return to home page.</li>
    <li>Product Management pages (admin only) where admin can add, edit, and delete products.</li>
</ul>

## Structure Plane

### Front-End<br>

<ul>
    <li>NAVIGATION AREA</li>
    - The navigation area encompasses five major parts. The first holding the logo (left), the second containing the search product area (in the middle), the third for the login functions (on the right), the fourth for the shopping cart on larger screens (on the right) and last which accomodates the navigation bar under all of the parts. On mobile devices, menu item list is placed at the top left cornder as a burger-button with a fall-back list.<br>
    - The top navigation area is a fixed-top navigation area, for the ease of navigation.<br><br>
    <li>HOME PAGE</li>
    - Under the the navigation area consists of three sections, the Home page consists of Hello image section with a link to products. The second section consists of product categories and third which is area for four fontawesome icons to keep the customers in the loop of what to expect once at Kafagym.<br><br>
    <li>FOOTER</li>
    - The footer consists of Get To Know Us part, Contact Us, Products and Subscribe to Our Newsletters links. There are social media icons with hover effect and active links to the social media pages. For the moment, social media links leads their main pages as we have not yet set social accounts for the business. Also, is the copyright note at the very bottom of the page.<br><br>
    <li>PRODUCTS PAGE</li>
    - Bootstrap was used for the product page and the page is made with Bootstarp grid system to adjust to responsive requirements depending on a screen size. It should also be noted that media queries were used for adequate adjustment with focus on mobile devices. Each product has an image, title, description, price, rating average and reviews, size (if any), quantity selector and add cart button.
    - Superuser (admin) can edit and delete products and content on the page.<br><br>
    <li>PRODUCTS DETAILS</li>
    - The pages where users can see product details, with an option to select criteria (e.g. size) and add it in the shopping cart.<br><br>
    <li>CHECKOUT SUCCESS</li>
    - The confirmation page where users are lead to when the payment process is completed. Users can see the order number, shipping address, product details. This page is accessible for registered users from Profile.<br><br>
    <li>REGISTER</li>
    - The page where users can create an account to save their details for next shopping and keep their purchase histories. A form with a built-in function is created with Django Allauth package.<br><br>
    <li>MY PROFILE</li>
    - My profile page renders a dashboard with the information related to specific user.
    <br> It also includes the dashboard shows the user information and the number of orders they so far placed.<br>
    - Superuser (admin) has privileges to add a new product to the store.<br><br>
    <li>PAYMENT</li>
    - There are two steps involved in this process:<br>
        - Cart which is getting all the user orders.<br>
        - Checkout which allows user to add their shipping details and make a secure payment via stripe .<br><br>
    <li>ADMIN</li>
    - The admin panel, which can be created with Django project, where Admin can take control of products and other data.<br><br>
    <li>FEATURES REMAINING TO IMPLEMENT</li>
    - Adding a 24/7 Online chat service via chat<br>
    - I set the on_sale var in product model but I could not manage to implement its logic due to time constraint.
    - The blog app that is part of my code was replaced by the ejournal app. I did not wish to remove it at the last minute to avoid any unintended drawback at the last minute.<br>
    - Two issues were notice with the ejournal app. The first being the Add Article set as link under Our News menu which makes its page accessible though it requires login credentianls to add an article. The second, once logged in to add article, the link Author displays the names of other registered used. I count to change this and restrict the page to the specific logged in user.<br>
    - A css issue profile page on footer was identified, this stemmed from the application of crisp form and it needs some styling consideration. 
    - Connecting to additional payment systems such as PayPal<br>
    - Displaying number of product images per product<br>
    - Enlarging product image upon hovering<br>
    - Creating account with social media<br>
    - Product comparison options<br>
    - Payment in various currencies<br>
    - I had initiated the blog app but it has failed to run in the deployed version on Heroku while it does on the gitpod. So I decided to disable its relevant link.
</ul>

### Back-End<br>

Users have options to purchase products as guest users or account holder users. Guest users cannot save personal details for their next shopping as personal details such as name, email address, shipping address etc belong to their order in the database. Account holder users who create an account with their email address and username, user name (user profile) is linked with their order so that personal details can be retrieved. Each product belongs to a category, a brand and these are identified by id. Each order has a unique order number which is generated when the order is processed and orders have shopper's and product details.
SQLite, which is Django built-in database is used for development mode and Heroku Postgre is used for production mode. AWS (Amazon Web Services) is used to hold all static files and folders for the website for production mode.

Below is the chart of the database to show the data relationships.<br><br>

* [Homepage](https://github.com/kafamem/msfour_kafagymstore/blob/main/media/Homepage.jpg)
* [Products](https://github.com/kafamem/msfour_kafagymstore/blob/main/media/Products.jpg)


## Surface Plane

__ Colour Scheme __

The overall colour scheme consists of a number of colours. Dark colour (#4B4D4F) was used in the navigation area and for text font. Orange (#F7941E) was mainly used for button styling and navigation links styling. It was also used for the footer. The general background colour was light grey (#EAEDED). White colour (#FFF) was used for links primarily before hovering effects. The boostrap text-success, text-warning, text-danger, and text-info were used for toasts messages. In some cases text-dark and text-muted styles were used for links.<br><br> 

__ Typography __

The googel font 'Roboto' was used as the main text font throught the website while 'Sans Serif' was kept as backup font in case 'Roboto' fails to respond effectively. The two typographies were fetched from google fonts. I found 'Roboto' friendly for e-commerce design purpose.<br><br>

__ Icons __

Fontawesome icons were used for UX purposes to help the user's guidance to navigate the website.<br>

## Skeleton Plane

The design of this website layout relied mostly on the bootstrap library to ensure the convenience of both desktop  and mobile designs. The site is fully responsive with appropriate layout that match the images sizes to fit into the webpage layout. Thus, shoppers using a mobile phone have no difficulties looking for products and purchase them and be able navigate around the site. Below are the wireframes of the core pages of the website.

* [Homepage](https://github.com/kafamem/msfour_kafagymstore/blob/main/media/Homepage.jpg)
* [Products](https://github.com/kafamem/msfour_kafagymstore/blob/main/media/Products.jpg)
* [Product Details](https://github.com/kafamem/msfour_kafagymstore/blob/main/media/Product_detail.jpg)
* [Shopping Cart](https://github.com/kafamem/msfour_kafagymstore/blob/main/media/Shopping%20Cart.jpg)
* [Checkout](https://github.com/kafamem/msfour_kafagymstore/blob/main/media/Checkout.jpg)
* [Tablet view - Product detail](https://github.com/kafamem/msfour_kafagymstore/blob/main/media/Tablet%20View.jpg)
* [Mobile View](https://github.com/kafamem/msfour_kafagymstore/blob/main/media/MobileDevice%20View.jpg)



# TECHNOLOGIES USED

### Languages Used:

* [HTML](https://www.w3schools.com/html/)
* [CSS](https://www.w3schools.com/css/)
* [JavaScript](https://www.w3schools.com/js/)
* [Python](https://www.python.org/)
    - [Django](https://www.djangoproject.com/)

### Framewoks, Libraries & Programs Used:

* [Bootstrap 4](https://getbootstrap.com/docs/4.5/getting-started/introduction/):
    - Bootstrap was used to ensure the responsiveness and styling of the website.
* [Google Fonts](https://getbootstrap.com/docs/4.5/getting-started/introduction/):
    - Google fonts were used to import the 'Roboto and Sans-Serif' fonts used for typography.
* [Git](https://git-scm.com/):
    - For version control, Git was used mainly to commit with help of Gitpod terminal and Push to GitHub.
* [GitHub](https://github.com/):
    - GitHub is used for storing the code pushed from Git.
* [Gitpod](https://gitpod.io/):
    - Gitpod was used as a workspace in production mode of the project
* [Befunky](https://www.befunky.com/create/resize-image/):
    - Befunky was such a handy website for picture editor used to resize images used in this project.
* [ColorZilla](https://www.colorzilla.com/):
    - ColorZilla was such a handy extension used to pick the appropriate hexadecimal during the design process.
* [Heroku](https://www.heroku.com/):
    - Heroku was used a hosting for the project deployment.
* [Stripe](https://stripe.com/en-se):
    - secured payment system used in the project
* [AWS](https://aws.amazon.com/?aws-products-analytics.sort-by=item.additionalFields.productNameLowercase&aws-products-analytics.sort-order=asc&aws-products-business-apps.sort-by=item.additionalFields.productNameLowercase&aws-products-business-apps.sort-order=asc&aws-products-containers.sort-by=item.additionalFields.productNameLowercase&aws-products-containers.sort-order=asc&aws-products-compute.sort-by=item.additionalFields.productNameLowercase&aws-products-compute.sort-order=asc&aws-products-databases.sort-by=item.additionalFields.productNameLowercase&aws-products-databases.sort-order=asc&aws-products-fe-mobile.sort-by=item.additionalFields.productNameLowercase&aws-products-fe-mobile.sort-order=asc&aws-products-game-tech.sort-by=item.additionalFields.productNameLowercase&aws-products-game-tech.sort-order=asc&aws-products-iot.sort-by=item.additionalFields.productNameLowercase&aws-products-iot.sort-order=asc&aws-products-ml.sort-by=item.additionalFields.productNameLowercase&aws-products-ml.sort-order=asc&aws-products-mgmt-govern.sort-by=item.additionalFields.productNameLowercase&aws-products-mgmt-govern.sort-order=asc&aws-products-migration.sort-by=item.additionalFields.productNameLowercase&aws-products-migration.sort-order=asc&aws-products-network.sort-by=item.additionalFields.productNameLowercase&aws-products-network.sort-order=asc&aws-products-security.sort-by=item.additionalFields.productNameLowercase&aws-products-security.sort-order=asc&aws-products-storage.sort-by=item.additionalFields.productNameLowercase&aws-products-storage.sort-order=asc):
    - (Amazon Web Services) for hosting static files and images for the website
* [Fontawesome](https://fontawesome.com/):
    - for icons
* [Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/index.php):
    - for mockup

# FEATURE TESTING

* [Weebhook success](https://github.com/kafamem/msfour_kafagymstore/blob/main/media/stripe_webhook_success.jpg)

# TESTING USER STORIES FROM USER EXPERIENCE (UX)

<ul>
    <li>To view products to purchase by group of categories(eg. clothes, shoes, weights) and be able to navigate through them.</li>
        - The website has a clear and understandable, responsive and fixed navigation bar, which allow to user navigate the pages and sections easily.
    <li>Accessible information presented in clear and straight manner, so that I can find the product quickly.</li>
        - Upon opening the site, the user sees the company logo on the navigation bar and images and content. Through scrolling down the home page, the user can easily understand what the website purpose.
    <li>The ability to search for products based on a number of criteria; rating, price; categories, and name.</li>
        - The user has a number of options to navigate the products:<br>
            - They can access all products on the website through the relevant link on the navigation bar, or the button on the home Page. (on slider)
            - They can also check products by chosing a specific category on the home page.
            - Users they can filter products by category by sorting them as well. 
    <li>To be able to read reviews and see ratings which can help me make a decision on product to buy.</li>
        - Users can rate and review the product. The general rating is calculated as an average of the ratings from different users.
        - Users can alse make reviews of each product.
    <li>To be able to see images and clear relevant content, so that I know what I am about to buy.</li>
        - User can clear see the product image and its related information to be able to decide.
    <li>To view product details, know the price, see the image, size if any, description etc.</li>
        - The website has a clear purchase navigation with pop-up messages, which allow user to pass the purchase to checkout.
    <li>Two product were intentionally put out of stock to account for the non-availbility of the product.</li>
        - User is informed about this via out of stock button.
    <li>To know about new offers(e.g. free delivery cost upon purchasing products of not less that 500 SEK etc).</li>
        - User is informed of new offers at the store through navigation link or delivery banner.
    <li>To view product details in my cart and confirm everything before purchase.</li>
        - User can visualize the purchase preview before confirmation of the order.
    <li>Add, update and delete products in my cart so I can take control of my purchase.</li>
        - As a user I can add/edit/delete products in my shopping cart
    <li>To feel comfortable providing my personal information(card details) through a secured payment system.</li>
        - The safety of payment process is ensured by Stripe which deals with payments infrastructure for the internet. Webhooks are set to avoid accidental money transactions.
    <li>To ensure the products and cost as final check on checkout page.</li>
        - The shopping cart functionality ensures the manipulation of the products and makes it (edit/delete). When user update products in the cart, they can see the new total price simulitaniously.
    <li>To ensure my purchase has gone through, receive a confirmation notice and email</li>
        - Upon submitting order, the user get a toast nofication indicating that the purchase has been successful. In case registered, they also get email notification.
    <li>To sign up and purchase products easier and see the order history.</li>
    <li>Add and update personal details.</li>
        - Every registered user will have a personal profile on their dashboard.
    <li>Account password reset function in case I forget it.</li>
    <li>To give to a user with or without account an option to checkout.</li>
</ul>

As a Store owner at The Kafagym Store website I expect/want/need:
<ul>
    <li>To provide a simple design e-commerce website without difficulties to look at the products and purchase them.</li>
        - The website is easy to navigate. With clear navigation system.
    <li>To add new products to sell.</li>
        - Only superuser or admin will have access to product management options and can govern the content of the website. He will be able to edit/delete buttons, which regular users can't see.
    <li>To edit and update product.</li>
        - Only superuser or admin will have access to product management options and can govern the content of the website. He will be able to edit/delete buttons, which regular users can't see.
    <li>To delete product.</li>
        - Only superuser or admin will have access to product management options and can govern the content of the website. He will be able to edit/delete buttons, which regular users can't see.
    <li>To secure the website.</li>
        - Superuser will ensure the security of the website.
</ul>

# VERSION CONTROL
GitHub as a remote repository was used throught the entire project to keep track of code version control, and below is how they are used as the version control for the project.

__ Setting Up __


* Create a remote repository in GitHub by clicking "New repository" on the main page
* I used Code Institute Template and chose a repository name and click Create Repository making sure that public option was selected.
* Open the repository with Gitpod as Integrated Development Environment (IDE). The Code Institue Template, comes with initial commit that we do not need to do git init command when open IDE. It alse includes gitignore file to keep some confidential information. I had to include files such as pycache, *.sqlite3, env.py etc

__ Setting Up __

* Regular git commits were used after a set of work code was added. It was added, staged and pushed to GitHub to make sure I keep the history of the code modification. The following commands were used in this regards:

```python
* git status | To check the status of new/modified folders, files, and documents

* git add . | To put all new and updated work on the stage in git
  git add <specific file> is used when different types of work are done but do not want to commit everything on the same commitment
* git commit -m "commit message" | To commit the work on the stage in git before pushing it to GitHub
* git push | To update the repository in GitHub for main / master branch

```


# DEPLOYMENT

The cloud based platform Heroku was used to host the website project. It provides backend hosting tech services such as server, application, and database (Heroku Postgres) and programming languages. In addition, the Amazon AWS (a cloud based platform) services were also resorted to host the static files and images since Heroku does not accomodate files for storage.

Below are the processes of deploying the website to Heroku and setting up static files & images in AWS.

__ HEROKU __

* Create an app in Heroku. Click New, put App name and select region
* Add Heroku Postgres for the database
* Install dj_database_url and psycopg2-binary to use Heroku Postgres, and run pip3 freeze > requirements.txt command to add them on requirments.txt
* Update settings.py of the product. Import dj_database_url, comment out sqlite databases and add dj databases variable temporary while the database is transferred to Heroku Postgres
* Run python3 manage.py showmigrations command to see the status of migrations (Currently not migrated). Run python3 manage.py migrate command to migrate
* Import all products data. Run python3 manage.py loaddata command to load the categories first, brands next and products the last. The order of loading is important as all the products are associated with categories and brands
* Create a super user with python3 manage.py createsuperuser command for product admin
* Install gunicorn which acts as the webserver, and freeze it into requirements file with pip3 freeze > requirements.txt command
* Create a Procfile which specifies the commands that are executed by the app on startup
* Temporary disable collectstatic by setting heroku config:set DISABLE_COLLECTSTATIC = 1 and host name of Heroku to allowed hosts in settings.py
* Initialise Heroku in git with heroku: git:remote -a msfour-kafagym and put git into Heroku with git push heroku master
* Set up automatic deployment when git is pushed to GitHub. Go to Deployment on Heroku, search the GitHub repository, connect and click Enable Automatic Deploys
* Generate a new secret key, set it up in Heroku and update settings.py. Change the setting of Debug mode that only True in Development mode
* Check Activity Feed to see Build in Progress to confirm automatic deployment is working


__ AWS __

* Open S3 and create a new bucket, which stores the files, by completing the name and region
* Set up basic settings. Enable static website hosting so that it gives a new endpoint for accessing from the internet. Put index.html and error.html as default values
* Set up CORS configuration which is the access between Heroku and this S3 Bucket
* Set up Bucket Policy. Generate a policy with AWS policy generator. Add /* at the end of Resource to allow access to all resources in the bucket
* Create a user to access the bucket. Go to IAM (Identity and Access Management) and create a group for the user to live in. Then, create a policy by importing pre-built policy
* Attach the policy to the group
* Create a user and add it to the group. When the user is added to the group, it creates csv file containing Access Key ID and Secret access key which are used to authenticate them from Django app. *It is very important to download the file and save it as you cannot download it again

__ CONNECTING TO DJANGO __

* Install two new packages, pip3 install boto3, pip3 install django-storages, and run pip3 freeze > requirements.txt command to add them on requirments.txt
* Update settings.py to tell Django which bucket it should be communicating with *It is very important to keep AWS access keys secrets as these can be used to store or move data in the bucket and you will be charged by Amazon for it
* Add these secret keys on Heroku and set USE_AWS = True
* Create custome_storages.py to tell Django to use S3 to store static files and upload images when it is in production
* Add AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com' to tell Django where the static files come from in production and add some settings for Static and Media files on settings.py
* Add all the updates in git, commit it and push it to GitHub. Heroku runs python3 manage.py to collectstatic during the process which also searches through all the apps and project folders looking for static files. Then, it uses S3 domain settings in conjunction with the custom storage classes that tell the location at the URL where the things should be saved when it is in production. This can be confirmed in S3 bucket
* Add Cache control on settings.py as static files do not change often and to improve the performance for users
* Upload product images via S3. Create a folder, and upload images
* Verify superuser's email address on Heroku Postgres. Login admin and check the VERIFIED and PRIMARY boxes
* Add Stripe keys to Heroku Config Vars and create a new webhook endpoint
* Create Gmail account, add email host pass & user to Heroku Config Vars and add code on settings.py of the product


# RESOURCES
## General Resources
* Code Institute Course Materials
* [Stack Overflow](https://stackoverflow.com/)
* [Youtube](https://www.youtube.com/)
* [W3Schools](https://www.w3schools.com/)
* [Google](https://www.google.se/?hl=sv)

## General Resources & Validation
* [jshint](https://jshint.com/) for testing JavaScript code
* [PEP8 Online](http://pep8online.com/) for checking Python code compliance
* [Chrome DevTools](https://developer.chrome.com/docs/devtools/) for testing, style checking and debugging<br><br>

# Credits

### code
* [Bootstrap4](https://getbootstrap.com/docs/4.1/getting-started/introduction/): Bootstrap Library was used to ensure the responsiveness of the website.

### Media
* 10 images were fetched from [ShutterStock](https://www.shutterstock.com/sv/)

### content
* All the text content was written by the developer.

### Acknowledgements
* My mentor for his technical guidance.  
* Valuable tutoring support at Code Institute.
* Valuable Slack community hints.
