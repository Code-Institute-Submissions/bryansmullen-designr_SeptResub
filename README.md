# Designr

Designr is an exciting new web application for a graphic designer to reach their clients. This application functions as
both a personal portfolio for a graphic designer, as well as a way for users to peruse their public work and commission
new work.

## UX

This website is for `users` seeking to hire a graphic designer for new custom artwork, as well as for
a `graphic designer` to showcase their work, accept new commissions, and deliver completed artwork to their clients.

In particular, the following user stories will be achieved:

- As a user, I want to see the designers previous work, based on the type of work I am looking for. For example: poster,
  logo, business card, etc.
- As a user, I want to be able to purchase individual graphic design services from the designer
- As a user, I want to be able to pay for my order on the website using a secure method
- As a designer, I want to be able to showcase my public work to the world to generate new business
- As a designer, I want to be able to accept new commissions from users
- As a designer, I want to be able to accept payment for commissions up front

## Features

- Portfolio - An publicly accessible area where the designer can post their work for the world to see
- Registration - An area for users to register so they can make private orders from the designer
- Services - An area where services the designer is advertising can be added to a cart for purchase
- Cart/Checkout - A secure shopping cart & checkout for the user to pay for services
- Admin - An admin area for the designer to receive and keep track of orders and payments

### Existing Features

- The portfolio area allows users to see the designers previous work
- The services area allows users to purchase design services from the designer by choosing the items and adding to cart
- The cart/checkout area allows the user to purchase items using the secure checkout by filling out their card details
- The portfolio allows the designer to showcase their work by uploading items in the admin area
- The admin area allows the designer to receive the new commissions by logging in and checking for new items. They can
  then communicate with the users via email
- The cart/checkout feature allows the designer to accept payment up front

### Features left to implement

- A messaging area to allow users and designers to communicate without the need for external email
- A My Designs area for users to view their previously commissioned works

[comment]: <> (## Technologies Used)

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - Markup Language
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - Stylesheets
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/javascript) - Front End Scripting
- [Materialize](https://materializecss.com/) - Front End Library
- [Python](https://docs.python.org/3/) - Back End Scripting
- [Django](https://docs.djangoproject.com/en/3.1/) - Back End Framework
- [Stripe](https://stripe.com/docs) - Secure Payments API
- [AWS](https://docs.aws.amazon.com/index.html) - Static File Hosting
- [Heroku](https://devcenter.heroku.com/categories/reference) - Application Hosting

- In the absence of a specific, detailed and comprehensive module on automated testing provided by the course, manual testing has been opted for. It is assumed that this will not be penalised.
- The deployed, live version of the site was utilised for the tests.

### Tests Conducted

#### Finished Project Tests

The function of these tests is to ensure that the finished project renders acceptably on all intended devices. Four sets of tests were completed:

- Validation
- Modelled Device Testing
- Automated Cross Browser Testing
- Manual Browser Testing

#### Validation

Validation took place on HTML, CSS, JS, and Python files in the project.

#### Modelled Device Testing

To test the layout on multiple devices, Google Chrome DevTools is used to simulate the size of multiple devices and screen ratios. Screen responsiveness has been noted to ensure the correct screen ratio was delivered, links are tested by clicking through, images are checked to ensure they displayed correctly on all devices, and the website as a whole is checked to ensure everything renders as expected.

The following device dimensions are tested:

- Moto G4
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 5/SE
- iPhone 6,7,8
- iPhone 6,7,8 Plus
- iPhone X
- iPad
- iPad Pro
- Surface Duo
- Galaxy Fold
- Desktop

#### Automated Cross Browser Testing

To test the layout on multiple browsers, [browserstack](https://www.browserstack.com) is used to emulate different browsers running on virtual machines. The following browsers are tested:

- Catalina 13.1
- Firefox 82
- Chrome 64
- Opera 48
- Yandex 14.12

#### Manual Cross Browser Testing

To complement the above results the website is also tested manually on up-to-date browsers available on the developer's machine.

The following browsers are tested:

- Edge
- Brave
- Chrome

---

## Deployment

This project is deployed on Heroku, which can be accessed at [Designr](https://github.com/bryansmullen/designr) or [Designr Deployed Version](https://bryansmullen-designr.herokuapp.com/). The deployment is linked to the Master Branch of the repo, and will automatically update the deployment when any changes are committed to this branch of the remote repository. The deployment procedure is documented below.

- Project was initialized as a git repository
- A remote repository was linked to the project using github
- Code was commited to git and pushed to github taking care to ignore sensitive files, for example .env, as well as venv folders and notes files
- It was ensured that both an up-to-date requirements.txt file was maintained, and a Procfile to configure heroku also existed
- A remote repository was created for the project using heroku
- Environment variables from the local environment were added to heroku's config variables
- Heroku was configured to automatically deploy from the github master branch

[BACK TO CONTENTS](#Contents)

## Cloning a Local Version

The procedure for cloning a local version on a windows machine is detailed below. Instructions for Mac/Linux will be considered at a later date.

- Ensure Git, Python, Pip, and PyCharm are installed on your machine
- Clone the [github repository](https://github.com/bryansmullen/designr) using `git clone https://github.com/bryansmullen/designr.git`
- Within the created folder, create and activate a virtual environment
- Install the project requirements within the virtual environment the requirements.txt file
- Inside the main directory, rename sampleenvfile to .env and add values for each env variable
- In your terminal, navigated to the project directory, run `python manage.py runserver`

# Acknowledgements

Home BG Photo by Max Vakhtbovych from Pexels

Design examples:

- Photo by Magda Ehlers from Pexels
- Photo by Sy Donny from Pexels
- Photo by Kaboompics .com from Pexels
- Photo by Ann H from Pexels
- Photo by eric anada from Pexels
- Photo by alleksana from Pexels
