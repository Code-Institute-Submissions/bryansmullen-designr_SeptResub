# Designr

Designr is an exciting new web application for a graphic designer to reach their clients. This application functions as
both a personal portfolio and blog for a graphic designer, as well as a way for users to peruse their public work and commission
new work.

## UX

This website is for `users` seeking to hire a graphic designer for new custom artwork, as well as for
a `business owner` to showcase their work, accept new commissions, and deliver completed artwork to their clients. The blog portion of the website is designed for the `business owner` to generate interest and traffic to the website and could potentially be managed by a `blog administrator`.


## User Stories

| Use Case # | As A Persona | I Want to  | So That |
| --- | --- | --- | ---| 
| 1.1 | As an unauthenticated user | I want to Create An Account  | I can log in and create orders  |
| 1.2 | As an unauthenticated user | I want to log in  | I can create an order  |
| 1.3 | As an unauthenticated user | I want to browse the portfolio  | I can see what previous work the designer has done  |
| 1.4 | As an unauthenticated user | I want to browse the blog  | I can see what value the designer can provide for me  |
| 2.1 | As an authenticated user | I want to order services from the designer | I can have custom designs made for me |
| 2.2 | As an authenticated user | I want to pay for my order through the app | I can purchase the service there and then |
| 3.1 | As a business owner | I want to display my portfolio | I can showcase my work |
| 3.2 | As a business owner | I want to update a blog | To generate traffic to my website and to add value to my services |
| 3.3 | As a business owner | I want to sell my services | To generate income |
| 3.4 | As a business owner | I want to see past orders | I can contact the payee to discuss their design needs |


## Features

- Portfolio - An publicly accessible area where the designer can post their work for the world to see
- Registration - An area for users to register so they can make private orders from the designer
- Services - An area where services the designer is advertising can be added to a cart for purchase
- Cart/Checkout - A secure shopping cart & checkout for the user to pay for services
- Admin - An admin area for the designer to receive and keep track of orders and payments
- Blog - An updateable blog which allows the designer to generate interest and traffic to the website, and adds value to their services

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

## Typography & Color Scheme

TODO

## Data Structure

The database schema of the relational database is described visually in an ERD chart found [here](./docs/data/erd.png)

## Wireframes

Wireframes are available [here](./docs/wireframes/wireframes.pdf)]

## Technologies Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - Markup Language
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - Stylesheets
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/javascript) - Front End Scripting
- [Materialize](https://materializecss.com/) - Front End Library
- [Python](https://docs.python.org/3/) - Back End Scripting
- [Django](https://docs.djangoproject.com/en/3.1/) - Back End Framework
- [Stripe](https://stripe.com/docs) - Secure Payments API
- [AWS](https://docs.aws.amazon.com/index.html) - Static File Hosting
- [Heroku](https://devcenter.heroku.com/categories/reference) - Application Hosting
- [AllAuth](https://django-allauth.readthedocs.io/en/latest/) - Authentication Plugin for Django
- [Django Extensions](https://django-extensions.readthedocs.io/en/latest/index.html) - Used to generate ERD Document
- [Pygraphviz](https://pygraphviz.github.io/) - Used to generate ERD Document


- In the absence of a specific, detailed and comprehensive module on automated testing provided by the course, manual testing has been opted for. It is assumed that this will not be penalised.
- The deployed, live version of the site was utilised for the tests.



## Tests

The function of these tests is to ensure that the finished project renders acceptably on all intended devices. Four sets of tests were completed:

- Validation
- Modelled Device Testing
- Automated Cross Browser Testing
- Manual Browser Testing

### Validation

Validation took place on HTML, CSS, JS, and Python files in the project.

#### HTML Validation

HTML Validation Was Completed Using [https://validator.w3.org/](https://validator.w3.org/) as per Code Institute Recommendations

| Test Case # | Page | Pass | Proof |
| --- | --- | --- | --- |
| 1.1 | https://bryansmullen-designr.herokuapp.com/ | &check; | [Test 1.1](./docs/testing/html-validation/1.1.html) |
| 1.2 | https://bryansmullen-designr.herokuapp.com/about  | &check; | [Test 1.2](./docs/testing/html-validation/1.2.html) |
| 1.3 | https://bryansmullen-designr.herokuapp.com/portfolio/ | &check; | [Test 1.3](./docs/testing/html-validation/1.3.html) |
| 2.1 | https://bryansmullen-designr.herokuapp.com/accounts/signup/ | &check; | [Test 2.1](./docs/testing/html-validation/2.1.html) |
| 2.2 | https://bryansmullen-designr.herokuapp.com/accounts/login/  | &check; | [Test 2.2](./docs/testing/html-validation/2.2.html) |
| 2.3 | https://bryansmullen-designr.herokuapp.com/accounts/password/reset/ | &check; | [Test 2.3](./docs/testing/html-validation/2.3.html) |
| 2.4 | https://bryansmullen-designr.herokuapp.com/accounts/password/reset/done/  | &check; | [Test 2.4](./docs/testing/html-validation/2.4.html) |
| 2.5 | https://bryansmullen-designr.herokuapp.com/accounts/confirm-email/  | &check; | [Test 2.5](./docs/testing/html-validation/2.5.html) |
| 2.6 | https://bryansmullen-designr.herokuapp.com/accounts/confirm-email/MTE:1mRwWt:4TTj7Ta4nidKFInclh8AFKP6MO21xBlksifxr9LfCY4/ | &check; | [Test 2.6](./docs/testing/html-validation/2.6.html) |
| 3.1 | https://bryansmullen-designr.herokuapp.com/blog/  | &check; | [Test 3.1](./docs/testing/html-validation/3.1.html) |
| 3.2 | https://bryansmullen-designr.herokuapp.com/blog/new/  | &check; | [Test 3.2](./docs/testing/html-validation/3.2.html) |
| 3.3 | https://bryansmullen-designr.herokuapp.com/blog/edit/1/ | &check; | [Test 3.3](./docs/testing/html-validation/3.3.html) |
| 3.4 | https://bryansmullen-designr.herokuapp.com/blog/delete/1/ | &check; | [Test 3.4](./docs/testing/html-validation/3.4.html) |
| 4.1 | https://bryansmullen-designr.herokuapp.com/cart/  | &check; | [Test 4.1](./docs/testing/html-validation/4.1.html) |
| 4.2 | https://bryansmullen-designr.herokuapp.com/checkout/  | &check; | [Test 4.2](./docs/testing/html-validation/4.2.html) |
| 4.3 | https://bryansmullen-designr.herokuapp.com/checkout/checkout_success/645599EC2D994B9490B49013EDBDACD9 | &check; | [Test 4.3](./docs/testing/html-validation/4.3.html) |
| 5.1 | https://bryansmullen-designr.herokuapp.com/services/  | &check; | [Test 5.1](./docs/testing/html-validation/5.1.html) |
| 5.2 | https://bryansmullen-designr.herokuapp.com/profiles/  | &cross; | [Test 5.2](./docs/testing/html-validation/5.2.html) |

## CSS Validation

CSS Validation Was Completed Using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/) as per Code Institute Recommendations

| Test Case # | Page | Pass | Proof |
| --- | --- | --- | --- |
| 1.1 | [checkout.css](./checkout/static/checkout/css/checkout.css) | &check; | [Test 1.1](./docs/testing/css-validation/1.1.html) |
| 1.2 | [admin.css](./static/css/admin.css) | &check; | [Test 1.2](./docs/testing/css-validation/1.2.html) |
| 1.3 | [reset.css](./static/css/reset.css) | &check; | [Test 1.3](./docs/testing/css-validation/1.3.html) |
| 1.4 | [style.css](./static/css/style.css) | &check; | [Test 2.1](./docs/testing/css-validation/1.4.html) |

## JS Validation

JS Validation Was Completed Using [https://jshint.com/](https://jshint.com/) as per Code Institute Recommendations

| Test Case # | Page | Pass | Proof |
| --- | --- | --- | --- |
| 1.1 | [login.html](./templates/allauth/account/login.html) | &check; | [Test 1.1](./docs/testing/js-validation/1.1.PNG) |
| 1.2 | [displayCountry.js](./static/js/displayCountry.js) | &check; | [Test 1.2](./docs/testing/js-validation/1.2.PNG) |
| 1.3 | [initSidenav.js](./static/js/initSidenav.js)  | &check; | [Test 1.3](./docs/testing/js-validation/1.3.PNG) |
| 1.4 | [stripeElements.js](./static/js/stripeElements.js) | &check; | [Test 2.1](./docs/testing/js-validation/1.4.PNG) |
| 1.4 | [yearInject.js](./static/js/yearInject.js) | &check; | [Test 2.1](./docs/testing/js-validation/1.4.PNG) |

## Python Validation

Python Validation Was Completed Using [http://pep8online.com/](http://pep8online.com/) as per Code Institute Recommendations

| Test Case # | Page | Pass | Proof |
| --- | --- | --- | --- |
| 1.1 | [blog/admin.py](./blog/admin.py)  | &check; | [Test 1.1](./docs/testing/python-validation/1.1.PNG) |
| 1.2 | [blog/apps.py](./blog/apps.py)  | &check; | [Test 1.2](./docs/testing/python-validation/1.2.PNG) |
| 1.3 | [blog/forms.py](./blog/forms.py)  | &check; | [Test 1.3](./docs/testing/python-validation/1.3.PNG) |
| 1.4 | [blog/models.py](./blog/models.py)  | &check; | [Test 1.4](./docs/testing/python-validation/1.4.PNG) |
| 1.5 | [blog/tests.py](./blog/tests.py)  | &check; | [Test 1.5](./docs/testing/python-validation/1.5.PNG) |
| 1.6 | [blog/urls.py](./blog/urls.py)  | &check; | [Test 1.6](./docs/testing/python-validation/1.6.PNG) |
| 1.7 | [blog/views.py](./blog/views.py)  | &check; | [Test 1.7](./docs/testing/python-validation/1.7.PNG) |
| 2.1 | [cart/admin.py](./cart/admin.py)  | &check; | [Test 2.1](./docs/testing/python-validation/2.1.PNG) |
| 2.2 | [cart/apps.py](./cart/apps.py)  | &check; | [Test 2.2](./docs/testing/python-validation/2.2.PNG) |
| 2.3 | [cart/contexts.py](./cart/contexts.py)  | &check; | [Test 2.3](./docs/testing/python-validation/2.3.PNG) |
| 2.4 | [cart/models.py](./cart/models.py)  | &check; | [Test 2.4](./docs/testing/python-validation/2.4.PNG) |
| 2.5 | [cart/tests.py](./cart/tests.py)  | &check; | [Test 2.5](./docs/testing/python-validation/2.5.PNG) |
| 2.6 | [cart/urls.py](./cart/urls.py)  | &check; | [Test 2.6](./docs/testing/python-validation/2.6.PNG) |
| 2.7 | [cart/views.py](./cart/views.py)  | &check; | [Test 2.7](./docs/testing/python-validation/2.7.PNG) |
| 3.1 | [checkout/admin.py](./checkout/admin.py)  | &check; | [Test 3.1 ](./docs/testing/python-validation/3.1.PNG) |
| 3.2 | [checkout/apps.py](./checkout/apps.py)  | &check; | [Test 3.2 ](./docs/testing/python-validation/3.2.PNG) |
| 3.3 | [checkout/forms.py](./checkout/forms.py)  | &check; | [Test 3.3 ](./docs/testing/python-validation/3.3.PNG) |
| 3.4 | [checkout/models.py](./checkout/models.py)  | &check; | [Test 3.4 ](./docs/testing/python-validation/3.4.PNG) |
| 3.5 | [checkout/signals.py](./checkout/signals.py)  | &check; | [Test 3.5 ](./docs/testing/python-validation/3.5.PNG) |
| 3.6 | [checkout/tests.py](./checkout/tests.py)  | &check; | [Test 3.6 ](./docs/testing/python-validation/3.6.PNG) |
| 3.7 | [checkout/urls.py](./checkout/urls.py)  | &check; | [Test 3.7 ](./docs/testing/python-validation/3.7.PNG) |
| 3.8 | [checkout/views.py](./checkout/views.py)  | &check; | [Test 3.8 ](./docs/testing/python-validation/3.8.PNG) |
| 3.9 | [checkout/webhook_handler.py](./checkout/webhook_handler.py)  | &check; | [Test 3.9 ](./docs/testing/python-validation/3.9.PNG) |
| 3.10| [checkout/webhooks.py](./checkout/webhooks.py)  | &check; | [Test 3.10](./docs/testing/python-validation/3.10.PNG) |
| 4.1 | [home/admin.py](./home/admin.py)  | &check; | [Test 4.1](./docs/testing/python-validation/4.1.PNG) |
| 4.2 | [home/apps.py](./home/apps.py)  | &check; | [Test 4.2](./docs/testing/python-validation/4.2.PNG) |
| 4.3 | [home/models.py](./home/models.py)  | &check; | [Test 4.3](./docs/testing/python-validation/4.3.PNG) |
| 4.4 | [home/tests.py](./home/tests.py)  | &check; | [Test 4.4](./docs/testing/python-validation/4.4.PNG) |
| 4.5 | [home/urls.py](./home/urls.py)  | &check; | [Test 4.5](./docs/testing/python-validation/4.5.PNG) |
| 4.6 | [home/views.py](./home/views.py)  | &check; | [Test 4.6](./docs/testing/python-validation/4.6.PNG) |
| 5.1 | [main/asgi.py](./main/asgi.py)  | &check; | [Test 5.1](./docs/testing/python-validation/5.1.PNG) |
| 5.2 | [main/settings.py](./main/settings.py)  | &check; | [Test 5.2](./docs/testing/python-validation/5.2.PNG) |
| 5.3 | [main/urls.py](./main/urls.py)  | &check; | [Test 5.3](./docs/testing/python-validation/5.3.PNG) |
| 5.4 | [main/wsgi.py](./main/wsgi.py)  | &check; | [Test 5.4](./docs/testing/python-validation/5.4.PNG) |
| 6.1 | [portfolio/admin.py](./portfolio/admin.py)  | &check; | [Test 6.1](./docs/testing/python-validation/6.1.PNG) |
| 6.2 | [portfolio/apps.py](./portfolio/apps.py)  | &check; | [Test 6.2](./docs/testing/python-validation/6.2.PNG) |
| 6.3 | [portfolio/models.py](./portfolio/models.py)  | &check; | [Test 6.3](./docs/testing/python-validation/6.3.PNG) |
| 6.4 | [portfolio/tests.py](./portfolio/tests.py)  | &check; | [Test 6.4](./docs/testing/python-validation/6.4.PNG) |
| 6.5 | [portfolio/urls.py](./portfolio/urls.py)  | &check; | [Test 6.5](./docs/testing/python-validation/6.5.PNG) |
| 6.6 | [portfolio/views.py](./portfolio/views.py)  | &check; | [Test 6.6](./docs/testing/python-validation/6.6.PNG) |
| 7.1 | [profiles/admin.py](./profiles/admin.py)  | &check; | [Test 7.1](./docs/testing/python-validation/7.1.PNG) |
| 7.2 | [profiles/apps.py](./profiles/apps.py)  | &check; | [Test 7.2](./docs/testing/python-validation/7.2.PNG) |
| 7.3 | [profiles/forms.py](./profiles/forms.py)  | &check; | [Test 7.3](./docs/testing/python-validation/7.3.PNG) |
| 7.4 | [profiles/models.py](./profiles/models.py)  | &check; | [Test 7.4](./docs/testing/python-validation/7.4.PNG) |
| 7.5 | [profiles/tests.py](./profiles/tests.py)  | &check; | [Test 7.5](./docs/testing/python-validation/7.5.PNG) |
| 7.6 | [profiles/urls.py](./profiles/urls.py)  | &check; | [Test 7.6](./docs/testing/python-validation/7.6.PNG) |
| 7.7 | [profiles/views.py](./profiles/views.py)  | &check; | [Test 7.7](./docs/testing/python-validation/7.7.PNG) |
| 8.1 | [services/admin.py](./services/admin.py)  | &check; | [Test 8.1](./docs/testing/python-validation/8.1.PNG) |
| 8.2 | [services/apps.py](./services/apps.py)  | &check; | [Test 8.2](./docs/testing/python-validation/8.2.PNG) |
| 8.3 | [services/models.py](./services/models.py)  | &check; | [Test 8.3](./docs/testing/python-validation/8.3.PNG) |
| 8.4 | [services/tests.py](./services/tests.py)  | &check; | [Test 8.4](./docs/testing/python-validation/8.4.PNG) |
| 8.5 | [services/urls.py](./services/urls.py)  | &check; | [Test 8.5](./docs/testing/python-validation/8.5.PNG) |
| 8.6 | [services/views.py](./services/views.py)  | &check; | [Test 8.6](./docs/testing/python-validation/8.6.PNG) |
| 9.1 | [custom_storages.py](./custom_storages.py)  | &check; | [Test 9.1](./docs/testing/python-validation/9.1.PNG) |
| 9.2 | [manage.py](./manage.py)  | &check; | [Test 9.2](./docs/testing/python-validation/9.2.PNG) |

### Modelled Device Testing

To test the layout on multiple devices, Google Chrome DevTools is used to simulate the size of multiple devices and screen ratios. Screen responsiveness has been noted to ensure the correct screen ratio was delivered, links are tested by clicking through, images are checked to ensure they displayed correctly on all devices, and the website as a whole is checked to ensure everything renders as expected.

The following device dimensions are tested:

- iPhone 5/SE
- iPad
- Desktop

| Test Case # | Page | Device | Pass | Proof |
| --- | --- | --- | --- | --- |
| 1.1  | https://bryansmullen-designr.herokuapp.com/ | iPhone 5/SE | &check; | [Test 1.1 ](./docs/testing/modelled-device-testing/1.1.PNG) |
| 1.2  | https://bryansmullen-designr.herokuapp.com/about  | iPhone 5/SE | &check; | [Test 1.2 ](./docs/testing/modelled-device-testing/1.2.PNG) |
| 1.3  | https://bryansmullen-designr.herokuapp.com/portfolio/ | iPhone 5/SE | &check; | [Test 1.3 ](./docs/testing/modelled-device-testing/1.3.PNG) |
| 1.4  | https://bryansmullen-designr.herokuapp.com/accounts/signup/ | iPhone 5/SE | &check; | [Test 1.4 ](./docs/testing/modelled-device-testing/1.4.PNG) |
| 1.5  | https://bryansmullen-designr.herokuapp.com/accounts/login/  | iPhone 5/SE | &check; | [Test 1.5 ](./docs/testing/modelled-device-testing/1.5.PNG) |
| 1.6  | https://bryansmullen-designr.herokuapp.com/accounts/password/reset/ | iPhone 5/SE | &check; | [Test 1.6 ](./docs/testing/modelled-device-testing/1.6.PNG) |
| 1.7  | https://bryansmullen-designr.herokuapp.com/accounts/password/reset/done/  | iPhone 5/SE | &check; | [Test 1.7 ](./docs/testing/modelled-device-testing/1.7.PNG) |
| 1.8  | https://bryansmullen-designr.herokuapp.com/accounts/confirm-email/  | iPhone 5/SE | &check; | [Test 1.8 ](./docs/testing/modelled-device-testing/1.8.PNG) |
| 1.9  | https://bryansmullen-designr.herokuapp.com/accounts/confirm-email/MTE:1mRwWt:4TTj7Ta4nidKFInclh8AFKP6MO21xBlksifxr9LfCY4/ | iPhone 5/SE | &check; | [Test 1.9 ](./docs/testing/modelled-device-testing/1.9.PNG) |
| 1.10 | https://bryansmullen-designr.herokuapp.com/blog/  | iPhone 5/SE | &check; | [Test 1.10](./docs/testing/modelled-device-testing/1.10.PNG) |
| 1.11 | https://bryansmullen-designr.herokuapp.com/blog/new/  | iPhone 5/SE | &check; | [Test 1.11](./docs/testing/modelled-device-testing/1.11.PNG) |
| 1.12 | https://bryansmullen-designr.herokuapp.com/blog/edit/1/ | iPhone 5/SE | &check; | [Test 1.12](./docs/testing/modelled-device-testing/1.12.PNG) |
| 1.13 | https://bryansmullen-designr.herokuapp.com/blog/delete/1/ | iPhone 5/SE | &check; | [Test 1.13](./docs/testing/modelled-device-testing/1.13.PNG) |
| 1.14 | https://bryansmullen-designr.herokuapp.com/cart/  | iPhone 5/SE | &check; | [Test 1.14](./docs/testing/modelled-device-testing/1.14.PNG) |
| 1.15 | https://bryansmullen-designr.herokuapp.com/checkout/  | iPhone 5/SE | &check; | [Test 1.15](./docs/testing/modelled-device-testing/1.15.PNG) |
| 1.16 | https://bryansmullen-designr.herokuapp.com/checkout/checkout_success/645599EC2D994B9490B49013EDBDACD9 | iPhone 5/SE | &check; | [Test 1.16](./docs/testing/modelled-device-testing/1.16.PNG) |
| 1.17 | https://bryansmullen-designr.herokuapp.com/services/  | iPhone 5/SE | &check; | [Test 1.17](./docs/testing/modelled-device-testing/1.17.PNG) |
| 1.18 | https://bryansmullen-designr.herokuapp.com/profiles/  | iPhone 5/SE | &check; | [Test 1.18](./docs/testing/modelled-device-testing/1.18.PNG) |
| 2.1  | https://bryansmullen-designr.herokuapp.com/ | iPad  | &check; | [Test 2.1 ](./docs/testing/modelled-device-testing/2.1.PNG) |
| 2.2  | https://bryansmullen-designr.herokuapp.com/about  | iPad  | &check; | [Test 2.2 ](./docs/testing/modelled-device-testing/2.2.PNG) |
| 2.3  | https://bryansmullen-designr.herokuapp.com/portfolio/ | iPad  | &check; | [Test 2.3 ](./docs/testing/modelled-device-testing/2.3.PNG) |
| 2.4  | https://bryansmullen-designr.herokuapp.com/accounts/signup/ | iPad  | &check; | [Test 2.4 ](./docs/testing/modelled-device-testing/2.4.PNG) |
| 2.5  | https://bryansmullen-designr.herokuapp.com/accounts/login/  | iPad  | &check; | [Test 2.5 ](./docs/testing/modelled-device-testing/2.5.PNG) |
| 2.6  | https://bryansmullen-designr.herokuapp.com/accounts/password/reset/ | iPad  | &check; | [Test 2.6 ](./docs/testing/modelled-device-testing/2.6.PNG) |
| 2.7  | https://bryansmullen-designr.herokuapp.com/accounts/password/reset/done/  | iPad  | &check; | [Test 2.7 ](./docs/testing/modelled-device-testing/2.7.PNG) |
| 2.8  | https://bryansmullen-designr.herokuapp.com/accounts/confirm-email/  | iPad  | &check; | [Test 2.8 ](./docs/testing/modelled-device-testing/2.8.PNG) |
| 2.9  | https://bryansmullen-designr.herokuapp.com/accounts/confirm-email/MTE:1mRwWt:4TTj7Ta4nidKFInclh8AFKP6MO21xBlksifxr9LfCY4/ | iPad  | &check; | [Test 2.9 ](./docs/testing/modelled-device-testing/2.9.PNG) |
| 2.10 | https://bryansmullen-designr.herokuapp.com/blog/  | iPad  | &check; | [Test 2.10](./docs/testing/modelled-device-testing/2.10.PNG) |
| 2.11 | https://bryansmullen-designr.herokuapp.com/blog/new/  | iPad  | &check; | [Test 2.11](./docs/testing/modelled-device-testing/2.11.PNG) |
| 2.12 | https://bryansmullen-designr.herokuapp.com/blog/edit/1/ | iPad  | &check; | [Test 2.12](./docs/testing/modelled-device-testing/2.12.PNG) |
| 2.13 | https://bryansmullen-designr.herokuapp.com/blog/delete/1/ | iPad  | &check; | [Test 2.13](./docs/testing/modelled-device-testing/2.13.PNG) |
| 2.14 | https://bryansmullen-designr.herokuapp.com/cart/  | iPad  | &check; | [Test 2.14](./docs/testing/modelled-device-testing/2.14.PNG) |
| 2.15 | https://bryansmullen-designr.herokuapp.com/checkout/  | iPad  | &check; | [Test 2.15](./docs/testing/modelled-device-testing/2.15.PNG) |
| 2.16 | https://bryansmullen-designr.herokuapp.com/checkout/checkout_success/645599EC2D994B9490B49013EDBDACD9 | iPad  | &check; | [Test 2.16](./docs/testing/modelled-device-testing/2.16.PNG) |
| 2.17 | https://bryansmullen-designr.herokuapp.com/services/  | iPad  | &check; | [Test 2.17](./docs/testing/modelled-device-testing/2.17.PNG) |
| 2.18 | https://bryansmullen-designr.herokuapp.com/profiles/  | iPad  | &check; | [Test 2.18](./docs/testing/modelled-device-testing/2.18.PNG) |
| 3.1  | https://bryansmullen-designr.herokuapp.com/ | Desktop | &check; | [Test 3.1 ](./docs/testing/modelled-device-testing/3.1.PNG) |
| 3.2  | https://bryansmullen-designr.herokuapp.com/about  | Desktop | &check; | [Test 3.2 ](./docs/testing/modelled-device-testing/3.2.PNG) |
| 3.3  | https://bryansmullen-designr.herokuapp.com/portfolio/ | Desktop | &check; | [Test 3.3 ](./docs/testing/modelled-device-testing/3.3.PNG) |
| 3.4  | https://bryansmullen-designr.herokuapp.com/accounts/signup/ | Desktop | &check; | [Test 3.4 ](./docs/testing/modelled-device-testing/3.4.PNG) |
| 3.5  | https://bryansmullen-designr.herokuapp.com/accounts/login/  | Desktop | &check; | [Test 3.5 ](./docs/testing/modelled-device-testing/3.5.PNG) |
| 3.6  | https://bryansmullen-designr.herokuapp.com/accounts/password/reset/ | Desktop | &check; | [Test 3.6 ](./docs/testing/modelled-device-testing/3.6.PNG) |
| 3.7  | https://bryansmullen-designr.herokuapp.com/accounts/password/reset/done/  | Desktop | &check; | [Test 3.7 ](./docs/testing/modelled-device-testing/3.7.PNG) |
| 3.8  | https://bryansmullen-designr.herokuapp.com/accounts/confirm-email/  | Desktop | &check; | [Test 3.8 ](./docs/testing/modelled-device-testing/3.8.PNG) |
| 3.9  | https://bryansmullen-designr.herokuapp.com/accounts/confirm-email/MTE:1mRwWt:4TTj7Ta4nidKFInclh8AFKP6MO21xBlksifxr9LfCY4/ | Desktop | &check; | [Test 3.9 ](./docs/testing/modelled-device-testing/3.9.PNG) |
| 3.10 | https://bryansmullen-designr.herokuapp.com/blog/  | Desktop | &check; | [Test 3.10](./docs/testing/modelled-device-testing/3.10.PNG) |
| 3.11 | https://bryansmullen-designr.herokuapp.com/blog/new/  | Desktop | &check; | [Test 3.11](./docs/testing/modelled-device-testing/3.11.PNG) |
| 3.12 | https://bryansmullen-designr.herokuapp.com/blog/edit/1/ | Desktop | &check; | [Test 3.12](./docs/testing/modelled-device-testing/3.12.PNG) |
| 3.13 | https://bryansmullen-designr.herokuapp.com/blog/delete/1/ | Desktop | &check; | [Test 3.13](./docs/testing/modelled-device-testing/3.13.PNG) |
| 3.14 | https://bryansmullen-designr.herokuapp.com/cart/  | Desktop | &check; | [Test 3.14](./docs/testing/modelled-device-testing/3.14.PNG) |
| 3.15 | https://bryansmullen-designr.herokuapp.com/checkout/  | Desktop | &check; | [Test 3.15](./docs/testing/modelled-device-testing/3.15.PNG) |
| 3.16 | https://bryansmullen-designr.herokuapp.com/checkout/checkout_success/645599EC2D994B9490B49013EDBDACD9 | Desktop | &check; | [Test 3.16](./docs/testing/modelled-device-testing/3.16.PNG) |
| 3.17 | https://bryansmullen-designr.herokuapp.com/services/  | Desktop | &check; | [Test 3.17](./docs/testing/modelled-device-testing/3.17.PNG) |
| 3.18 | https://bryansmullen-designr.herokuapp.com/profiles/  | Desktop | &cross; | [Test 3.18](./docs/testing/modelled-device-testing/3.18.PNG) |

### Automated Cross Browser Testing

To test the layout on multiple browsers, [browserstack](https://www.browserstack.com) is used to emulate different browsers running on virtual machines. The following browsers are tested:

- Catalina 13.1
- Firefox 82
- Chrome 64
- Opera 48
- Yandex 14.12

### Manual Cross Browser Testing

To complement the above results the website is also tested manually on up-to-date browsers available on the developer's machine.

The following browsers are tested:

- Edge
- Brave
- Chrome

## User Story Testing

| Maps To User Story # | Steps To Recreate  | Expected Results  | Pass/Fail |
| ---  | ---  | --- | --- | 
| 1.1  | Navigate to [Home Page](https://bryansmullen-designr.herokuapp.com/)  | Home page should render | &check; |
|  | Click on register Nav Link | Registration page should render | &check; |
|  | Enter a valid email address, username, password, and repeat the same password, and click 'sign up' | A message is rendered instructing user to check email | &check; |
|  | User checks email, finds relevant email and clicks on confirmation link  | Confirm email page is rendered  | &check; |
|  | User clicks 'confirm' button to confirm email address  | Message is displayed saying email is confirmed, user redirected to sign in page | &check; |
|  | User enters existing account email and password on sign in page and clicks sign in | User successfully granted access and redirected to home page | &check; |
| 1.2  | Navigate to [Home Page](https://bryansmullen-designr.herokuapp.com/)  | Home page should render | &check; |
|  | Click on Login Nav Link  | Registration page should render | &check; |
|  | User enters existing account email and password on sign in page and clicks sign in | User successfully granted access and redirected to home page | &check; |
| 1.3  | Navigate to [Home Page](https://bryansmullen-designr.herokuapp.com/)  | Home page should render | &check; |
|  | Click on Portfolio Nav Link  | Portfolio page should render | &check; |
| 1.4  | Navigate to [Home Page](https://bryansmullen-designr.herokuapp.com/)  | Home page should render | &check; |
|  | Click on Blog Nav Link | Blog page should render | &check; |
|  | Click on Any Blog Instance Heading | Blog detail page should render | &check; |
| 2.1  | Navigate to [Home Page](https://bryansmullen-designr.herokuapp.com/)  | Home page should render | &check; |
|  | Click on Login Nav Link  | Registration page should render | &check; |
|  | User enters existing account email and password on sign in page and clicks sign in | User successfully granted access and redirected to home page | &check;  |
|  | Click on services link | User redirected to services page | &check; |
|  | Click on any service's 'add to cart' button | Item added to cart and user redirected to cart page | &check; |
|  | Click on 'go to checkout button | User redirected to checkout page | &check; |
|  | Enter Any Missing Personal or address information and enter a valid card number (use 4242 4242 4242 4242 / 4242 / 42424 for testing) and click 'complete order' | User redirected to checkout success page | &check; |
| 2.2 | Navigate to [Home Page](https://bryansmullen-designr.herokuapp.com/)  | Home page should render | &check; |
|  | Click on Login Nav Link  | Registration page should render | &check; |
|  | User enters existing account email and password on sign in page and clicks sign in | User successfully granted access and redirected to home page | &check;  |
|  | Click on services link | User redirected to services page | &check; |
|  | Click on any service's 'add to cart' button | Item added to cart and user redirected to cart page | &check; |
|  | Click on 'go to checkout button | User redirected to checkout page | &check; |
|  | Enter Any Missing Personal or address information and enter a valid card number (use 4242 4242 4242 4242 / 4242 / 42424 for testing) and click 'complete order' | User redirected to checkout success page | &check; |
| 3.1 | Navigate to [Admin Page](https://bryansmullen-designr.herokuapp.com/admin)  | Admin Login page should render | &check; |
| | Enter superuser credentials and click log in | User should be redirected to site backend | &check; |
| | Click on the add button next to Portfolio Entrys | Add portfolio entry page should be displayed | &check; |
| | Add a title, content, and image of the portfolio artwork desired  and click save | User should be redirected to list of portfolio entries and success message should display  | &check; |
| | Navigate to [Portfolio Page](https://bryansmullen-designr.herokuapp.com/portfolio/) | Portfolio page should display with new content | &check; |
| 3.2 | Navigate to [Home Page](https://bryansmullen-designr.herokuapp.com/)  | Home page should render | &check; |
|  | Click on Login Nav Link  | Registration page should render | &check; |
|  | User enters existing superuser account email and password on sign in page and clicks sign in | User successfully granted access and redirected to home page | &check;  |
|  | Navigate to [Blog Page](https://bryansmullen-designr.herokuapp.com/blog/)  | Blog page should render | &check; |
|  | Click New Blog Entry Button | User should be redirected to add new blog entry page | &check; |
|  | Enter blog title and content and click add blog entry | User should be redirected to blog list page and new content should display correctly | &check; |
| 3.3 | Navigate to [Admin Page](https://bryansmullen-designr.herokuapp.com/admin)  | Admin Login page should render | &check; |
| | Enter superuser credentials and click log in | User should be redirected to site backend | &check; |
| | Click on the add button next to Services | Add service page should be displayed | &check; |
| | Add a title, content, price, and image of the portfolio artwork desired and click save | User should be redirected to list of services and success message should display  | &check; |
| | Navigate to [Services Page](https://bryansmullen-designr.herokuapp.com/services/) | Services page should display with new content | &check; |
| 3.3 | Navigate to [Admin Page](https://bryansmullen-designr.herokuapp.com/admin)  | Admin Login page should render | &check; |
| | Enter superuser credentials and click log in | User should be redirected to site backend | &check; |
| | Click on Orders under the Checkout Heading | List of previous orders should display | &check; |
| | Click on any order | Details of order including contact details for the customer should display | &check; |

---
Navigate to [Home Page](https://bryansmullen-designr.herokuapp.com/*)  | Home page should render | &check; |
## Issues

Profiles Page Fails HTML Validation due to stray tags generated automatically by django's forms
initSidenav.js fails JS Validation - this file is provided by Materialize as is, and therefore works as designed
stripeElements.js fails JS Validation - this file is created in line with Code Institute tutorials, and due to the complexity of the stripe flow, and the fact that this file currently functions as designed, it has not been edited.
populate with issues fixed
checkout/forms.py fails pep8 validation over a line that is 80 characters long. This has been tolerated for legibility reasons

## Deployment

### Heroku

This project is deployed on Heroku, which can be accessed at [Designr](https://github.com/bryansmullen/designr) or [Designr Deployed Version](https://bryansmullen-designr.herokuapp.com/). The deployment is linked to the Master Branch of the repo, and will automatically update the deployment when any changes are committed to this branch of the remote repository. The deployment procedure is documented below.

# Prerequisites
You must have gitpod account to clone a development version of this repository. Please refer to the [Gitpod Docs](https://www.gitpod.io/docs). You will also require the [Gitpod Browser Extension](https://www.gitpod.io/docs/browser-extension/). Finally you will require a stripe account and an aws account. You will require a [heroku account](https://dashboard.heroku.com/apps) and an [aws account](https://aws.amazon.com/) also.

1. Navigate to Gitpod, and create a new workspace using the python-django template. If the terminal starts a process automatically, quit out of it with `ctrl + c`
2. Remove the files and folders that are pre populated using `rm -rf *` in the gitpod workspace's terminal.
3. Clone the repository using the command `git clone https://github.com/bryansmullen/designr.git`
4. Move the contents of the cloned folder out to the root directory using `mv designr/* .` and then delete the remaining directory `designr`
5. Add all project files to the git repo by running `git add .`. Commit the changes by running `git commit -m 'initial commit'`
6. Add the heroku cli to your gitpod workspace by running `curl https://cli-assets.heroku.com/install.sh | sh`
7. Log into your heroku account via the heroku cli by running `heroku login -i` and entering your credentials
8. Create a new heroku application by running `heroku create` in the terminal. This will create a new application and generate a random name for it.
9. Navigate to your heroku account in your browser and click on the newly created application. Navigate to the resources tab, and in the search box for `add-ons` search for `Heroku Postgres`. Select `Hobby Dev -Free
10. Return to your heroku dashboard and navigate to the settings tab of your application. Under `Config Vars` click `Reveal Config Vars`.
11. In Config Vars set a new variable key SECRET_KEY with a value of a random string. You can find an auto generated secret key by searching google for secret key generator. Example: `https://randomkeygen.com/`
10. Navigate to your stripe dashboard, and locate the options for 'developers' and navigate to this page. Ensure 'TEST MODE' is enabled.
11. Navigate to API Keys and copy the publishable key, and paste it into herokus Config Vars with a key of STRIPE_PUBLIC_KEY. Reveal the secret key and paste this with a key of STRIPE_SECRET_KEY.
12. On your heroku dashboard click on `Open App`. This should display a temporary Welcome Screen. Copy the URL from your address bar. Example: `https://###################.herokuapp.com`
13. In stripe navigate to 'webhooks' and create a new endpoint. Paste the url you just copied and append `checkout/wh/` to the end of it. Example `https://###################.herokuapp.com/checkout/wh/`. Click on `select events`, and from the dropdown select all payment_intent and charge events. Click Add events. Finally click `Add webhook`
14. On the created webhook, click to reveal the `signing secret`, copy this, and paste it into Heroku's Config Vars with a Key of STRIPE_WH_SECRET
15. Navigate to your aws account. Locate the s3 service and create a new bucket. Allow public access. Click on Create Bucket.
16. Click on the new bucket and navigate to `permissions`. Under `Bucket Policy` click edit. Copy the bucket ARN. Find the button for `Generate Bucket Policy`. From this new window select the type of policy as `s3 bucket policy`. Under principal enter `*`. Under Actions select `GetObject`. Under Amazon Resource Name paste the value copied from your bucket name. Confirm these options and copy out the generated bucket policy. Return to the bucket policy creation and paste this in. Finally under `Resource` append `/*` to the end of your ARN to ensure you can access all resources in this bucket. Click save changes to save this bucket policy.
17. In the AWS Console, on the top right of the screen, click your user name. The dropdown has an option to view security credentials. Under `Your Security Credentials` click the drop down for `Access Keys (access key ID and secret key access)`. Click the option to create new access key, and then show the access key. Copy the access key id and return to heroku config vars, and paste this value in with the key AWS_ACCESS_KEY_ID. Then return to aws and copy the secret access key and paste this into herokus config vars with the key AWS_SECRET_ACCESS_KEY
18. Add an additional key USE_AWS and set the value to TRUE
19. Add the domain of your heroku app to the `allowed hosts` section of the `main/settings.py` file. Example: `###################.herokuapp.com`
20. Build the application by running `git push heroku main`
21. In the terminal, quit any running process with ctrl + c. Migrate the database using `heroku run python manage.py migrate`
22. Create a superuser by running `heroku run python manage.py createsuperuser` and following the prompts in the terminal
23. Navigate to `https://##############.heroku.com/admin` (ie - your instance appended with `/admin`) to log into the admin panel with your new superuser
24. Navigate to Accounts => Email Addresses. Select your superuser. Click to enable both `Verified` and `Primary`. Click Save.
25. To seed your data, navigate to Portfolio => Portfolio entrys and click on `Add`. Add some seed information by adding a title, content and image file for data you wish to display as part of the portfolio. Similarly Services must be seeded from the backend by navigating to Services => Services and clicking Add. Add as many services as you wish to be available.


[BACK TO CONTENTS](#Contents)

## Cloning a Development Version

# Prerequisites
You must have gitpod account to clone a development version of this repository. Please refer to the [Gitpod Docs](https://www.gitpod.io/docs). You will also require the [Gitpod Browser Extension](https://www.gitpod.io/docs/browser-extension/). Finally you will require a stripe account and an aws account.

1. Navigate to Gitpod, and create a new workspace using the python-django template. If the terminal starts a process automatically, quit out of it with `ctrl + c`
2. Remove the files and folders that are pre populated using `rm -rf *` in the gitpod workspace's terminal. You will also need to delete the .gitignore
3. Clone the repository using the command `git clone https://github.com/bryansmullen/designr.git`
4. Move the contents of the cloned folder out to the root directory using `mv designr/* .` and then delete the remaining directory `designr`
5. Install project dependancies using `pip3 install -r requirements.txt`
6. Rename main/sampleenvfile to main/.env using the command `mv ./main/sampleenvfile ./main/.env`
7. In ./main/.env for development version delete DATABASE_URL and USE_AWS environment variables, as well as AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
8. In ./main/.env set DEVELOPMENT=TRUE
9. In ./main/.env set SECRET_KEY= to a random string. You can find an auto generated secret key by searching google for secret key generator. Example: `https://randomkeygen.com/`
10. Navigate to your stripe dashboard, and locate the options for 'developers' and navigate to this page. Ensure 'TEST MODE' is enabled.
11. Navigate to API Keys and copy the publishable key, and paste it into ./main/.env as the value for STRIPE_PUBLIC_KEY. Reveal the secret key and paste this as the value for STRIPE_SECRET_KEY
12. In your terminal find your development domain by running `python3 manage.py runserver`, and then ctrl + click on the url that is displayed (http://127.0.0.1:8000). This will open a new browser window with the public facing url of the development application. Example: `https://8000-###################.gitpod.io`. Copy this url.
13. In stripe navigate to 'webhooks' and create a new endpoint. Paste the url you just copied and append `checkout/wh/` to the end of it. Example `https://8000-###################.gitpod.io/checkout/wh/`. Click on `select events`, and from the dropdown select all payment_intent and charge events. Click Add events. Finally click `Add webhook`
14. On the created webhook, click to reveal the `signing secret`, copy this, and paste it into ./main/.env as the value for STRIPE_WH_SECRET
15. In the terminal, quit the running process with ctrl + c. Migrate the database using `python3 manage.py migrate`
16. Create a superuser by running `python3 manage.py createsuperuser` and following the prompts in the terminal
17. Run the server using `python3 manage.py runserver`. Ctrl + click on the url that is displayed to launch the development application
18. Navigate to `https://8000-##############.gitpod.io/admin` (ie - your instance appended with `/admin`) to log into the admin panel with your new superuser
19. Navigate to Accounts => Email Addresses. Select your superuser. Click to enable both `Verified` and `Primary`. Click Save.
20. To seed your data, navigate to Portfolio => Portfolio entrys and click on `Add`. Add some seed information by adding a title, content and image file for data you wish to display as part of the portfolio. Similarly Services must be seeded from the backend by navigating to Services => Services and clicking Add. Add as many services as you wish to be available.

# Acknowledgements

Home BG Photo by Max Vakhtbovych from Pexels

Design examples:

- Photo by Magda Ehlers from Pexels
- Photo by Sy Donny from Pexels
- Photo by Kaboompics .com from Pexels
- Photo by Ann H from Pexels
- Photo by eric anada from Pexels
- Photo by alleksana from Pexels
