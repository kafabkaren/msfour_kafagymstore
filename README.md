# KAFAGYM STORE

Welcome to [Kafagym Store Platform](https://msfour-kafagymstore.herokuapp.com/)

## Project rationale

The Kafagym Store platform was built, designed and deployed by Fabrice Karenzi as his final milestone project at the [Code Institute](https://codeinstitute.net/se/) Full Stack Web Development diploma. The website is
designed to provide customers at the Kafagym Store with the online options to puchase, rate and review the products made available to them from the store. It should be reminded that though it will turn into a viable e-commerce website for business at a later stage; it is serving for the purpose of education for the moment. It is a mobile responsive website.<br>

![MS4 Responsiveness.JPG]()

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

### The Kafagym website features:<br>

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
    <li>MY PROFILE</li>
    - My profile page renders a dashboard with the information related to specific user.
    <br> It also includes the dashboard shows the user information and the number of orders they so far placed.<br>
    - Superuser (admin) has privileges to add a new product to the store.<br><br>
    <li>PAYMENT</li>
    - There are two steps involved in this process:<br>
        - Cart which is getting all the user orders.<br>
        - Checkout which allows user to add their shipping details and make a secure payment via stripe.<br><br>
    <li>FEATURES REMAINING TO IMPLEMENT</li>
    - Connecting to additional payment systems such as PayPal<br>
    - Adding a 24/7 service via chat<br>
    - Displaying number of product images per product<br>
    - Enlarging product image upon hovering<br>
    - Creating account with social media<br>
    - Product comparison options<br>
    - Payment in various currencies<br>
</ul>

## Surface Plane

__ Colours__
This is an e-commerce website that has a lot of products with images containing different colours, White (#FFFFFF) is used as the main background colour to keep the entire image of the website settled. The shop colour is Hunter Green (#09572A) and this is used for some icons and fonts. Jet (#333333) is used as the main font colour, Golden Yellow (#FFDF00) is used for buttons and alerts to stand them out. Flame (#E84610) is used for other things that need user's attention. These are the base colours and similar colours are used on the different parts and sections on the website.

# TECHNOLOGIES USED

### Languages Used

* HTML5
* CSS3
* JavaScript
* Python
    - Django
    
<ul>
    <li>Languages Used:</li>
    <ul>
    <li>[HT](https://getbootstrap.com/docs/4.5/getting-started/introduction/)</li><br><br>
    <li>Frameworks, Libraries & Programs Used:
    1. [Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/):
    - Bootstrap was used to ensure the responsiveness and styling of the website.

    1. [Google Fonts](https://fonts.google.com/)
    - Google fonts were used to import the 'Roboto and Sans-Serif' fonts used for typography.

    1. [Git](https://git-scm.com/)
    - For version control, Git was used mainly to commit with help of Gitpod terminal and Push to GitHub.
    1. [GitHub](https://github.com/)
    - GitHub is used for storing the code pushed from Git.

    1. [Balsamiq](https://balsamiq.com/)
    - Balsamiq was used to create the website home page [wireframe](https://github.com/kafamem/msone-kafagym/blob/master/assets/images/Landing%20page.png) during the design process.
    1. [Befunky](https://www.befunky.com/create/resize-image/)
    - Befunky was such a handy website for picture editor used to resize images used in this project.
    1. [ColorZilla](https://www.colorzilla.com/)
    - ColorZilla was such a handy extension used to pick the appropriate hexadecimal during the design process.
    </li>
</ul>
    <li>Typography</li><br>


    - The 'Press Start 2P' is the main font that was used while 'Sans Serif' was kept as backup font in case 'Press Start 2P' fails to respond effectively. The two typographies were fetched from google fonts. I found 'Press Start 2P' friendly for games design.<br><br>
    <li>Emoji Icons</li><br>
    - Five emoji icons were used in JavaScript code in order to accompany the user anticipated feelings upon guessing right or wrong in relation to the secret number and from the html 'Attempt' and 'Score' elements.<br>   

</ul>

### Design<br>
The web design main target is to provide the user with the ability to interact with the game. The layout consists of features and elements that allows the user to navigate and use the interact with the game. 
<ul>
    <li>Colour Scheme</li><br>
    - The dominating color throughout the entire layout is dark grey which is combined with light grey color used for header and the instruction card area. In order to make the text content stand out, I used the orange color for typography which created a harmonious combination for both text and buttons background color.<br><br>
    <li>Typography</li><br>
    - The 'Press Start 2P' is the main font that was used while 'Sans Serif' was kept as backup font in case 'Press Start 2P' fails to respond effectively. The two typographies were fetched from google fonts. I found 'Press Start 2P' friendly for games design.<br><br>
    <li>Emoji Icons</li><br>
    - Five emoji icons were used in JavaScript code in order to accompany the user anticipated feelings upon guessing right or wrong in relation to the secret number and from the html 'Attempt' and 'Score' elements.<br>   

</ul>

### Wireframes

The wireframes for the site were created with help of Balsamiq. They feature the site look from different angles i.e computer, mobile phone and tablet views.

* Guess The Number Computer View Wireframe - [wireframe](https://github.com/kafamem/mstwo-guess-the-number/blob/master/docs/wireframes/MS2%20Computer%20View.jpg)
* Guess The Number Mobile Phone View Wireframe - [wireframe](https://github.com/kafamem/mstwo-guess-the-number/blob/master/docs/wireframes/MS2%20Mobile%20Phone%20View.jpg)
* Guess The Number Tablet View Wireframe - [wireframe](https://github.com/kafamem/mstwo-guess-the-number/blob/master/docs/wireframes/MS2%20Tablet%20View.jpg)


## Features

### Existing Features
<ul>
The site layout consists of three main areas:<br><br>
    <li>The header that shows the name and the purpose of the site.</li><br>
    <li>The game area which consits of secret number area where the hidden number is represented by the question mark. It is in this area where the guessed number shows up after a correct match. This styling in this regards also changes from 15rem for the initial and deafult settings to 30rem width after guessing right.<br>
    <li>The input area serves for typing the number. The user can type in or scroll up and down to choose the number. Under this area, is the check button to submit the input for comparison and get the feedback. 
    </li><br>
    <li>The site also includes the 'Attempt' and 'Topscore' features. The Attempt feature which is a counting down from twenty down to zero, shows the user how many times they have tried to reach the perfect match. In case of failure i.e the last attempt equals to zero; then the 'You lost the game' message pops up. On the other hand, the Topscore feature keeps the highest score so far reached.</li><br>
    <li>The 'Again' which is under the attempt and topscore features servers for starting the game session without losing track of the topscore. The game is to reset to the initial settings but keeping the topscore. However, upon refreshing the page the game will start from scratch.</li>
    <li>The last area is the instruction which guide the user on how to play the game.</li>
</ul>

### Features Left to implement
<ul>
    <li>To better improve the game I plan to add on levels of difficulty where the user will be challenged to choose between easy and hard levels. To this level, the user may be provided with only a limited number of attempts to guess right with high score.</li><br>

</ul>

## Technologies used

### Languages Used

* HTML5
* CSS3
* JavaScript


### Framework, Libraries, Websites & Tools Used

1. [Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/):
    - Bootstrap was used to ensure the responsiveness and styling of the website.

1. [Google Fonts](https://fonts.google.com/)
    - Google fonts were used to import the 'Roboto and Sans-Serif' fonts used for typography.

1. [Git](https://git-scm.com/)
    - For version control, Git was used mainly to commit with help of Gitpod terminal and Push to GitHub.
1. [GitHub](https://github.com/)
    - GitHub is used for storing the code pushed from Git.

1. [Balsamiq](https://balsamiq.com/)
    - Balsamiq was used to create the website home page [wireframe](https://github.com/kafamem/msone-kafagym/blob/master/assets/images/Landing%20page.png) during the design process.
1. [Befunky](https://www.befunky.com/create/resize-image/)
    - Befunky was such a handy website for picture editor used to resize images used in this project.
1. [ColorZilla](https://www.colorzilla.com/)
    - ColorZilla was such a handy extension used to pick the appropriate hexadecimal during the design process.

## Validation

In order to check the validity of the website code, the W3C Markup Validator and W3C CSS Validator were used on each page of the website to check the syntax errors.
* [HTML Validator](https://validator.w3.org/) returned zero errors in the markup.
* [CSS Validator](https://jigsaw.w3.org/css-validator/) returned zero errors in the styling.
* [JavaScript Validator](https://jshint.com/) returned five warnings but no errors were identified. 

## Compatibility Testing

The site is compatible with different devices including mobile and tablet as well as computer. The responsiveness aspect was regularly checked using Google Chrome inspect features without forgetting Safari and Mozilla Firefox.

### Testing User Stories from User Experience (UX)

As a user and the plater at same time of the game on the website, I want to:
<ul>
    <li>Navigate the page easily.</li><br>
    The page layout makes it easier to navigate around. The features on the web page are straightforward to find and get along with with ease.<br><br>
    <li>Type in my guessing number.</li><br>
    The user is provided with the field to enter their prefered number as guess. The user can either type or scroll up or down to select the prefered number.<br><br>
    <li>To be able to check the correctness of the number I entered.</li><br>
    The user check whether their prefered guess number matched or did not match with the hidden secret number. This is done upon clicking the 'Check' button which prompts a feedback. The correct match appears both in the secret number box and the typing box.<br><br>
    <li>Get feedback after checking my number.</li><br>
    Upon clicking the Check button, the user gets a feedback with the phrase 'Wow! Exact number' in case the match was correct, the phrase 'The number is low' in case the number entered  is lower than the secret number and the phrase 'The number is high' in case the number entered is higher than the secret number. The user can also get a failure notification 'You lost the game' after exhausting the counting down attempts with no correct guess.<br><br>
    <li>Know how many attempts still available to score for each guess and see my top score.</li><br>
    The user is provided with the information about how many attempts were tried in a form of counting down as well as the top score reahced so far. Here the topscore is actually equal to the highest value number from the attempts. With this information, the user can strategically plan for the next score.<br><br>
    <li>To start the game without losing my current top score.</li><br>
    For the purpose of competition, the user may need to show off the topscore they reached but without losing the ability to keep playing. In this case, the 'Again' button was set to start the game again without losing track of the topscore.<br><br>
    <li>Restart over the game.</li><br>
    The user can choose to start over the entire game session by refreshing the page. This will reset all game features back to the starting point; topscore included. 
</ul>

### Further Testing
* The website was tested through different browsers; Google Chrome, Mozilla Firefox, Microsoft Edge and Safari browsers.
* The website was viewed through various devices including iPhone7 and iPad, large screen and laptop to check it responsiveness.

## Deployment

### GitHub pages
The following steps were followed to deploy the project to GitHub Pages:

1. After logging in to GitHub, locate the GitHub Repository
1. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
1. Scroll down the Settings page until you reach the "GitHub Pages" Section.
1. Under "Source", click the dropdown called "None" and select "Master Branch".
1. The page will automatically refresh.
1. Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.

### Workspace
In order to write wode, I use Gitpod IDE. 
1. After logging in to Gitpod, I choose the 'kafamem/mstwo-guess-the-number' workspace.
1. Then, I select open from adjacent three dots. Then the workspace name opens the project design interface. This has terminals, coding area as well as the preview mode.

## Credits

### code
* [Bootstrap4](https://getbootstrap.com/docs/4.1/getting-started/introduction/): Bootstrap Library was used to ensure the responsiveness of the website.

### content
* All the text content was written by the developer.

### Acknowledgements
* My mentor for his technical guidance.  
* Tutor support at Code Institute their technical support.
