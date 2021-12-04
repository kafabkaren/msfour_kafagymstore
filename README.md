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
        - Checkout which allows user to add their shipping details and make a secure payment via stripe.<br><br>
    <li>ADMIN</li>
    - The admin panel, which can be created with Django project, where Admin can take control of products and other data.<br><br>
    <li>FEATURES REMAINING TO IMPLEMENT</li>
    - Connecting to additional payment systems such as PayPal<br>
    - Adding a 24/7 service via chat<br>
    - Displaying number of product images per product<br>
    - Enlarging product image upon hovering<br>
    - Creating account with social media<br>
    - Product comparison options<br>
    - Payment in various currencies<br>
</ul>

### Back-End<br>

Users have options to purchase products as guest users or account holder users. Guest users cannot save personal details for their next shopping as personal details such as name, email address, shipping address etc belong to their order in the database. Account holder users who create an account with their email address and username, user name (user profile) is linked with their order so that personal details can be retrieved. Each product belongs to a category, a brand and these are identified by id. Each order has a unique order number which is generated when the order is processed and orders have shopper's and product details.
SQLite, which is Django built-in database is used for development mode and Heroku Postgre is used for production mode. AWS (Amazon Web Services) is used to hold all static files and folders for the website for production mode.

Below is the chart of the database to show the data relationships.<br><br>

### Database Structure<br>



## Surface Plane

__ Colour Scheme __

The overall colour scheme consists of a number of colours. Dark colour (#4B4D4F) was used in the navigation area and for text font. Orange (#F7941E) was mainly used for button styling and navigation links styling. It was also used for the footer. The general background colour was light grey (#EAEDED). White colour (#FFF) was used for links primarily before hovering effects. The boostrap text-success, text-warning, text-danger, and text-info were used for toasts messages. In some cases text-dark and text-muted styles were used for links.<br><br> 

__ Typography __

The googel font 'Roboto' was used as the main text font throught the website while 'Sans Serif' was kept as backup font in case 'Roboto' fails to respond effectively. The two typographies were fetched from google fonts. I found 'Roboto' friendly for e-commerce design purpose.<br><br>

__ Icons __

Fontawesome icons were used for UX purposes to help the user's guidance to navigate the website.<br>

## Skeleton Plane

The design of this website layout relied mostly on the bootstrap library to ensure the convenience of both desktop  and mobile designs. The site is fully responsive with appropriate layout that match the images sizes to fit into the webpage layout. Thus, shoppers using a mobile phone have no difficulties looking for products and purchase them and be able navigate around the site. Below are the wireframes of the core pages of the website.

### Wireframes

The wireframes for the site were created with help of Balsamiq. They feature the site look from different angles i.e computer, mobile phone and tablet views.

* Guess The Number Computer View Wireframe - [wireframe](https://github.com/kafamem/mstwo-guess-the-number/blob/master/docs/wireframes/MS2%20Computer%20View.jpg)
* Guess The Number Mobile Phone View Wireframe - [wireframe](https://github.com/kafamem/mstwo-guess-the-number/blob/master/docs/wireframes/MS2%20Mobile%20Phone%20View.jpg)
* Guess The Number Tablet View Wireframe - [wireframe](https://github.com/kafamem/mstwo-guess-the-number/blob/master/docs/wireframes/MS2%20Tablet%20View.jpg)

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
* [Balsamiq](https://balsamiq.com/):
    - Balsamiq was used to create the website home page
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
    <li>To view product details, know the price, see the image, size if any, description etc.</li>
        - The website has a clear purchase navigation with pop-up messages, which allow user to pass the purchase to checkout.
    <li>To know about new offers(e.g. free delivery cost upon purchasing products of not less that 500 SEK etc).</li>
    <li>To view product details in my cart and confirm everything before purchase.</li>
        - 
    <li>Add, update and delete products in my cart so I can take control of my purchase.</li>
        - As a user I can add/edit/delete products in my shopping cart
    <li>To feel comfortable providing my personal information(card details) through a secured payment system.</li>
        - The safety of payment process is ensured by Stripe which deals with payments infrastructure for the internet. Webhooks are set to avoid accidental money transactions.
    <li>To ensure the products and cost as final check on checkout page.</li>
        - The shopping cart functionality ensures the manipulation of the products and makes it (edit/delete). When user update products in the cart, they can see the new total price simulitaniously.
    <li>To ensure my purchase has gone through, receive a confirmation notice and email</li>
    <li>To sign up and purchase products easier and see the order history.</li>
    <li>Add and update personal details.</li>
        - Every registered user will have a personal profile on their dashboard.
    <li>Account password reset function in case I forget it.</li>
    <li>To give to a user with or without account an option to checkout.</li>
</ul>

As a Store owner at The Kafagym Store website I expect/want/need:
<ul>
    <li>To provide a simple design e-commerce website without difficulties to look at the products and purchase them.</li>
        - 
    <li>To add new products to sell.</li>
        - Only superuser or admin will have access to product management options and can govern the content of the website. He will be able to edit/delete buttons, which regular users can't see.
    <li>To edit and update product.</li>
        - Only superuser or admin will have access to product management options and can govern the content of the website. He will be able to edit/delete buttons, which regular users can't see.
    <li>To delete product.</li>
        - Only superuser or admin will have access to product management options and can govern the content of the website. He will be able to edit/delete buttons, which regular users can't see.
    <li>To secure the website.</li>
        - Superuser will ensure the security of the website.
</ul>

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



## Compatibility Testing

The site is compatible with different devices including mobile and tablet as well as computer. The responsiveness aspect was regularly checked using Google Chrome inspect features without forgetting Safari and Mozilla Firefox.

### Testing User Stories from User Experience (UX)

As a user and the plater at same time of the game on the website, I want to:
<ul>
    <li></li><br> 
</ul>

### Further Testing
* 

## Deployment



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
