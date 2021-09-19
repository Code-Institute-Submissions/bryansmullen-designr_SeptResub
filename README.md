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
| 1.1 | https://bryansmullen-designr.herokuapp.com/                                                                               | &check; | [Test 1.1](./docs/testing/html-validation/1.1.html) |
| 1.2 | https://bryansmullen-designr.herokuapp.com/about                                                                          | &check; | [Test 1.2](./docs/testing/html-validation/1.2.html) |
| 1.3 | https://bryansmullen-designr.herokuapp.com/portfolio/                                                                     | &check; | [Test 1.3](./docs/testing/html-validation/1.3.html) |
| 2.1 | https://bryansmullen-designr.herokuapp.com/accounts/signup/                                                               | &check; | [Test 2.1](./docs/testing/html-validation/2.1.html) |
| 2.2 | https://bryansmullen-designr.herokuapp.com/accounts/login/                                                                | &check; | [Test 2.2](./docs/testing/html-validation/2.2.html) |
| 2.3 | https://bryansmullen-designr.herokuapp.com/accounts/password/reset/                                                       | &check; | [Test 2.3](./docs/testing/html-validation/2.3.html) |
| 2.4 | https://bryansmullen-designr.herokuapp.com/accounts/password/reset/done/                                                  | &check; | [Test 2.4](./docs/testing/html-validation/2.4.html) |
| 2.5 | https://bryansmullen-designr.herokuapp.com/accounts/confirm-email/                                                        | &check; | [Test 2.5](./docs/testing/html-validation/2.5.html) |
| 2.6 | https://bryansmullen-designr.herokuapp.com/accounts/confirm-email/MTE:1mRwWt:4TTj7Ta4nidKFInclh8AFKP6MO21xBlksifxr9LfCY4/ | &check; | [Test 2.6](./docs/testing/html-validation/2.6.html) |
| 3.1 | https://bryansmullen-designr.herokuapp.com/blog/                                                                          | &check; | [Test 3.1](./docs/testing/html-validation/3.1.html) |
| 3.2 | https://bryansmullen-designr.herokuapp.com/blog/new/                                                                      | &check; | [Test 3.2](./docs/testing/html-validation/3.2.html) |
| 3.3 | https://bryansmullen-designr.herokuapp.com/blog/edit/1/                                                                   | &check; | [Test 3.3](./docs/testing/html-validation/3.3.html) |
| 3.4 | https://bryansmullen-designr.herokuapp.com/blog/delete/1/                                                                 | &check; | [Test 3.4](./docs/testing/html-validation/3.4.html) |
| 4.1 | https://bryansmullen-designr.herokuapp.com/cart/                                                                          | &check; | [Test 4.1](./docs/testing/html-validation/4.1.html) |
| 4.2 | https://bryansmullen-designr.herokuapp.com/checkout/                                                                      | &check; | [Test 4.2](./docs/testing/html-validation/4.2.html) |
| 4.3 | https://bryansmullen-designr.herokuapp.com/checkout/checkout_success/645599EC2D994B9490B49013EDBDACD9                     | &check; | [Test 4.3](./docs/testing/html-validation/4.3.html) |
| 5.1 | https://bryansmullen-designr.herokuapp.com/services/                                                                      | &check; | [Test 5.1](./docs/testing/html-validation/5.1.html) |
| 5.2 | https://bryansmullen-designr.herokuapp.com/profiles/                                                                      | &cross; | [Test 5.2](./docs/testing/html-validation/5.2.html) |

## CSS Validation

CSS Validation Was Completed Using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/) as per Code Institute Recommendations

| Test Case # | Page | Pass | Proof |
| --- | --- | --- | --- |
| 1.1 | [checkout.css](./checkout/static/checkout/css/checkout.css) | &check; | [Test 1.1](./docs/testing/css-validation/1.1.html) |
| 1.2 | [admin.css](./static/css/admin.css)                         | &check; | [Test 1.2](./docs/testing/css-validation/1.2.html) |
| 1.3 | [reset.css](./static/css/reset.css)                         | &check; | [Test 1.3](./docs/testing/css-validation/1.3.html) |
| 1.4 | [style.css](./static/css/style.css)                         | &check; | [Test 2.1](./docs/testing/css-validation/1.4.html) |

## JS Validation

JS Validation Was Completed Using [https://jshint.com/](https://jshint.com/) as per Code Institute Recommendations

| Test Case # | Page | Pass | Proof |
| --- | --- | --- | --- |
| 1.1 | [login.html](./templates/allauth/account/login.html) | &check; | [Test 1.1](./docs/testing/js-validation/1.1.PNG) |
| 1.2 | [admin.css](./static/js/displayCountry.js)           | &check; | [Test 1.2](./docs/testing/js-validation/1.2.PNG) |
| 1.3 | [reset.css](./static/js/initSidenav.js)              | &cross; | [Test 1.3](./docs/testing/js-validation/1.3.PNG) |
| 1.4 | [style.css](./static/js/stripeElements.js)           | &cross; | [Test 2.1](./docs/testing/js-validation/1.4.PNG) |
| 1.4 | [style.css](./static/js/yearInject.js)               | &check; | [Test 2.1](./docs/testing/js-validation/1.4.PNG) |

## Python Validation

Python Validation Was Completed Using [http://pep8online.com/](http://pep8online.com/) as per Code Institute Recommendations

| Test Case # | Page | Pass | Proof |
| --- | --- | --- | --- |
| 1.1 | [blog/admin.py](./blog/admin.py)                                | &check; | [Test 1.1](./docs/testing/python-validation/1.1.PNG) |
| 1.2 | [blog/apps.py](./blog/apps.py)                                  | &check; | [Test 1.2](./docs/testing/python-validation/1.2.PNG) |
| 1.3 | [blog/forms.py](./blog/forms.py)                                | &check; | [Test 1.3](./docs/testing/python-validation/1.3.PNG) |
| 1.4 | [blog/models.py](./blog/models.py)                              | &check; | [Test 1.4](./docs/testing/python-validation/1.4.PNG) |
| 1.5 | [blog/tests.py](./blog/tests.py)                                | &check; | [Test 1.5](./docs/testing/python-validation/1.5.PNG) |
| 1.6 | [blog/urls.py](./blog/urls.py)                                  | &check; | [Test 1.6](./docs/testing/python-validation/1.6.PNG) |
| 1.7 | [blog/views.py](./blog/views.py)                                | &check; | [Test 1.7](./docs/testing/python-validation/1.7.PNG) |
| 2.1 | [cart/admin.py](./cart/admin.py)                                | &check; | [Test 2.1](./docs/testing/python-validation/2.1.PNG) |
| 2.2 | [cart/apps.py](./cart/apps.py)                                  | &check; | [Test 2.2](./docs/testing/python-validation/2.2.PNG) |
| 2.3 | [cart/contexts.py](./cart/contexts.py)                          | &check; | [Test 2.3](./docs/testing/python-validation/2.3.PNG) |
| 2.4 | [cart/models.py](./cart/models.py)                              | &check; | [Test 2.4](./docs/testing/python-validation/2.4.PNG) |
| 2.5 | [cart/tests.py](./cart/tests.py)                                | &check; | [Test 2.5](./docs/testing/python-validation/2.5.PNG) |
| 2.6 | [cart/urls.py](./cart/urls.py)                                  | &check; | [Test 2.6](./docs/testing/python-validation/2.6.PNG) |
| 2.7 | [cart/views.py](./cart/views.py)                                | &check; | [Test 2.7](./docs/testing/python-validation/2.7.PNG) |
| 3.1 | [checkout/admin.py](./checkout/admin.py)                        | &check; | [Test 3.1 ](./docs/testing/python-validation/3.1.PNG) |
| 3.2 | [checkout/apps.py](./checkout/apps.py)                          | &check; | [Test 3.2 ](./docs/testing/python-validation/3.2.PNG) |
| 3.3 | [checkout/forms.py](./checkout/forms.py)                        | &check; | [Test 3.3 ](./docs/testing/python-validation/3.3.PNG) |
| 3.4 | [checkout/models.py](./checkout/models.py)                      | &check; | [Test 3.4 ](./docs/testing/python-validation/3.4.PNG) |
| 3.5 | [checkout/signals.py](./checkout/signals.py)                    | &check; | [Test 3.5 ](./docs/testing/python-validation/3.5.PNG) |
| 3.6 | [checkout/tests.py](./checkout/tests.py)                        | &check; | [Test 3.6 ](./docs/testing/python-validation/3.6.PNG) |
| 3.7 | [checkout/urls.py](./checkout/urls.py)                          | &check; | [Test 3.7 ](./docs/testing/python-validation/3.7.PNG) |
| 3.8 | [checkout/views.py](./checkout/views.py)                        | &check; | [Test 3.8 ](./docs/testing/python-validation/3.8.PNG) |
| 3.9 | [checkout/webhook_handler.py](./checkout/webhook_handler.py)    | &check; | [Test 3.9 ](./docs/testing/python-validation/3.9.PNG) |
| 3.10| [checkout/webhooks.py](./checkout/webhooks.py)                  | &check; | [Test 3.10](./docs/testing/python-validation/3.10.PNG) |
| 4.1 | [home/admin.py](./home/admin.py)                                | &check; | [Test 4.1](./docs/testing/python-validation/4.1.PNG) |
| 4.2 | [home/apps.py](./home/apps.py)                                  | &check; | [Test 4.2](./docs/testing/python-validation/4.2.PNG) |
| 4.3 | [home/models.py](./home/models.py)                              | &check; | [Test 4.3](./docs/testing/python-validation/4.3.PNG) |
| 4.4 | [home/tests.py](./home/tests.py)                                | &check; | [Test 4.4](./docs/testing/python-validation/4.4.PNG) |
| 4.5 | [home/urls.py](./home/urls.py)                                  | &check; | [Test 4.5](./docs/testing/python-validation/4.5.PNG) |
| 4.6 | [home/views.py](./home/views.py)                                | &check; | [Test 4.6](./docs/testing/python-validation/4.6.PNG) |
| 5.1 | [main/asgi.py](./main/asgi.py)                                  | &check; | [Test 5.1](./docs/testing/python-validation/5.1.PNG) |
| 5.2 | [main/settings.py](./main/settings.py)                          | &check; | [Test 5.2](./docs/testing/python-validation/5.2.PNG) |
| 5.3 | [main/urls.py](./main/urls.py)                                  | &check; | [Test 5.3](./docs/testing/python-validation/5.3.PNG) |
| 5.4 | [main/wsgi.py](./main/wsgi.py)                                  | &check; | [Test 5.4](./docs/testing/python-validation/5.4.PNG) |
| 6.1 | [portfolio/admin.py](./portfolio/admin.py)                      | &check; | [Test 6.1](./docs/testing/python-validation/6.1.PNG) |
| 6.2 | [portfolio/apps.py](./portfolio/apps.py)                        | &check; | [Test 6.2](./docs/testing/python-validation/6.2.PNG) |
| 6.3 | [portfolio/models.py](./portfolio/models.py)                    | &check; | [Test 6.3](./docs/testing/python-validation/6.3.PNG) |
| 6.4 | [portfolio/tests.py](./portfolio/tests.py)                      | &check; | [Test 6.4](./docs/testing/python-validation/6.4.PNG) |
| 6.5 | [portfolio/urls.py](./portfolio/urls.py)                        | &check; | [Test 6.5](./docs/testing/python-validation/6.5.PNG) |
| 6.6 | [portfolio/views.py](./portfolio/views.py)                      | &check; | [Test 6.6](./docs/testing/python-validation/6.6.PNG) |
| 7.1 | [profiles/admin.py](./profiles/admin.py)                        | &check; | [Test 7.1](./docs/testing/python-validation/7.1.PNG) |
| 7.2 | [profiles/apps.py](./profiles/apps.py)                          | &check; | [Test 7.2](./docs/testing/python-validation/7.2.PNG) |
| 7.3 | [profiles/forms.py](./profiles/forms.py)                        | &check; | [Test 7.3](./docs/testing/python-validation/7.3.PNG) |
| 7.4 | [profiles/models.py](./profiles/models.py)                      | &check; | [Test 7.4](./docs/testing/python-validation/7.4.PNG) |
| 7.5 | [profiles/tests.py](./profiles/tests.py)                        | &check; | [Test 7.5](./docs/testing/python-validation/7.5.PNG) |
| 7.6 | [profiles/urls.py](./profiles/urls.py)                          | &check; | [Test 7.6](./docs/testing/python-validation/7.6.PNG) |
| 7.7 | [profiles/views.py](./profiles/views.py)                        | &check; | [Test 7.7](./docs/testing/python-validation/7.7.PNG) |
| 8.1 | [services/admin.py](./services/admin.py)                        | &check; | [Test 8.1](./docs/testing/python-validation/8.1.PNG) |
| 8.2 | [services/apps.py](./services/apps.py)                          | &check; | [Test 8.2](./docs/testing/python-validation/8.2.PNG) |
| 8.3 | [services/models.py](./services/models.py)                      | &check; | [Test 8.3](./docs/testing/python-validation/8.3.PNG) |
| 8.4 | [services/tests.py](./services/tests.py)                        | &check; | [Test 8.4](./docs/testing/python-validation/8.4.PNG) |
| 8.5 | [services/urls.py](./services/urls.py)                          | &check; | [Test 8.5](./docs/testing/python-validation/8.5.PNG) |
| 8.6 | [services/views.py](./services/views.py)                        | &check; | [Test 8.6](./docs/testing/python-validation/8.6.PNG) |
| 9.1 | [custom_storages.py](./custom_storages.py)                      | &check; | [Test 9.1](./docs/testing/python-validation/9.1.PNG) |
| 9.2 | [manage.py](./manage.py)                                        | &check; | [Test 9.2](./docs/testing/python-validation/9.2.PNG) |

### Modelled Device Testing

To test the layout on multiple devices, Google Chrome DevTools is used to simulate the size of multiple devices and screen ratios. Screen responsiveness has been noted to ensure the correct screen ratio was delivered, links are tested by clicking through, images are checked to ensure they displayed correctly on all devices, and the website as a whole is checked to ensure everything renders as expected.

The following device dimensions are tested:

- iPhone 5/SE
- iPad
- Desktop

| Test Case # | Page | Device | Pass | Proof |
| --- | --- | --- | --- | --- |
| 1.1  | https://bryansmullen-designr.herokuapp.com/                                                                               | iPhone 5/SE | &check; | [Test 1.1 ](./docs/testing/modelled-device-testing/1.1.PNG) |
| 1.2  | https://bryansmullen-designr.herokuapp.com/about                                                                          | iPhone 5/SE | &check; | [Test 1.2 ](./docs/testing/modelled-device-testing/1.2.PNG) |
| 1.3  | https://bryansmullen-designr.herokuapp.com/portfolio/                                                                     | iPhone 5/SE | &check; | [Test 1.3 ](./docs/testing/modelled-device-testing/1.3.PNG) |
| 1.4  | https://bryansmullen-designr.herokuapp.com/accounts/signup/                                                               | iPhone 5/SE | &check; | [Test 1.4 ](./docs/testing/modelled-device-testing/1.4.PNG) |
| 1.5  | https://bryansmullen-designr.herokuapp.com/accounts/login/                                                                | iPhone 5/SE | &check; | [Test 1.5 ](./docs/testing/modelled-device-testing/1.5.PNG) |
| 1.6  | https://bryansmullen-designr.herokuapp.com/accounts/password/reset/                                                       | iPhone 5/SE | &check; | [Test 1.6 ](./docs/testing/modelled-device-testing/1.6.PNG) |
| 1.7  | https://bryansmullen-designr.herokuapp.com/accounts/password/reset/done/                                                  | iPhone 5/SE | &check; | [Test 1.7 ](./docs/testing/modelled-device-testing/1.7.PNG) |
| 1.8  | https://bryansmullen-designr.herokuapp.com/accounts/confirm-email/                                                        | iPhone 5/SE | &check; | [Test 1.8 ](./docs/testing/modelled-device-testing/1.8.PNG) |
| 1.9  | https://bryansmullen-designr.herokuapp.com/accounts/confirm-email/MTE:1mRwWt:4TTj7Ta4nidKFInclh8AFKP6MO21xBlksifxr9LfCY4/ | iPhone 5/SE | &check; | [Test 1.9 ](./docs/testing/modelled-device-testing/1.9.PNG) |
| 1.10 | https://bryansmullen-designr.herokuapp.com/blog/                                                                          | iPhone 5/SE | &check; | [Test 1.10](./docs/testing/modelled-device-testing/1.10.PNG) |
| 1.11 | https://bryansmullen-designr.herokuapp.com/blog/new/                                                                      | iPhone 5/SE | &check; | [Test 1.11](./docs/testing/modelled-device-testing/1.11.PNG) |
| 1.12 | https://bryansmullen-designr.herokuapp.com/blog/edit/1/                                                                   | iPhone 5/SE | &check; | [Test 1.12](./docs/testing/modelled-device-testing/1.12.PNG) |
| 1.13 | https://bryansmullen-designr.herokuapp.com/blog/delete/1/                                                                 | iPhone 5/SE | &check; | [Test 1.13](./docs/testing/modelled-device-testing/1.13.PNG) |
| 1.14 | https://bryansmullen-designr.herokuapp.com/cart/                                                                          | iPhone 5/SE | &check; | [Test 1.14](./docs/testing/modelled-device-testing/1.14.PNG) |
| 1.15 | https://bryansmullen-designr.herokuapp.com/checkout/                                                                      | iPhone 5/SE | &check; | [Test 1.15](./docs/testing/modelled-device-testing/1.15.PNG) |
| 1.16 | https://bryansmullen-designr.herokuapp.com/checkout/checkout_success/645599EC2D994B9490B49013EDBDACD9                     | iPhone 5/SE | &check; | [Test 1.16](./docs/testing/modelled-device-testing/1.16.PNG) |
| 1.17 | https://bryansmullen-designr.herokuapp.com/services/                                                                      | iPhone 5/SE | &check; | [Test 1.17](./docs/testing/modelled-device-testing/1.17.PNG) |
| 1.18 | https://bryansmullen-designr.herokuapp.com/profiles/                                                                      | iPhone 5/SE | &check; | [Test 1.18](./docs/testing/modelled-device-testing/1.18.PNG) |
| 2.1  | https://bryansmullen-designr.herokuapp.com/                                                                               | iPad        | &check; | [Test 2.1 ](./docs/testing/modelled-device-testing/2.1.PNG) |
| 2.2  | https://bryansmullen-designr.herokuapp.com/about                                                                          | iPad        | &check; | [Test 2.2 ](./docs/testing/modelled-device-testing/2.2.PNG) |
| 2.3  | https://bryansmullen-designr.herokuapp.com/portfolio/                                                                     | iPad        | &check; | [Test 2.3 ](./docs/testing/modelled-device-testing/2.3.PNG) |
| 2.4  | https://bryansmullen-designr.herokuapp.com/accounts/signup/                                                               | iPad        | &check; | [Test 2.4 ](./docs/testing/modelled-device-testing/2.4.PNG) |
| 2.5  | https://bryansmullen-designr.herokuapp.com/accounts/login/                                                                | iPad        | &check; | [Test 2.5 ](./docs/testing/modelled-device-testing/2.5.PNG) |
| 2.6  | https://bryansmullen-designr.herokuapp.com/accounts/password/reset/                                                       | iPad        | &check; | [Test 2.6 ](./docs/testing/modelled-device-testing/2.6.PNG) |
| 2.7  | https://bryansmullen-designr.herokuapp.com/accounts/password/reset/done/                                                  | iPad        | &check; | [Test 2.7 ](./docs/testing/modelled-device-testing/2.7.PNG) |
| 2.8  | https://bryansmullen-designr.herokuapp.com/accounts/confirm-email/                                                        | iPad        | &check; | [Test 2.8 ](./docs/testing/modelled-device-testing/2.8.PNG) |
| 2.9  | https://bryansmullen-designr.herokuapp.com/accounts/confirm-email/MTE:1mRwWt:4TTj7Ta4nidKFInclh8AFKP6MO21xBlksifxr9LfCY4/ | iPad        | &check; | [Test 2.9 ](./docs/testing/modelled-device-testing/2.9.PNG) |
| 2.10 | https://bryansmullen-designr.herokuapp.com/blog/                                                                          | iPad        | &check; | [Test 2.10](./docs/testing/modelled-device-testing/2.10.PNG) |
| 2.11 | https://bryansmullen-designr.herokuapp.com/blog/new/                                                                      | iPad        | &check; | [Test 2.11](./docs/testing/modelled-device-testing/2.11.PNG) |
| 2.12 | https://bryansmullen-designr.herokuapp.com/blog/edit/1/                                                                   | iPad        | &check; | [Test 2.12](./docs/testing/modelled-device-testing/2.12.PNG) |
| 2.13 | https://bryansmullen-designr.herokuapp.com/blog/delete/1/                                                                 | iPad        | &check; | [Test 2.13](./docs/testing/modelled-device-testing/2.13.PNG) |
| 2.14 | https://bryansmullen-designr.herokuapp.com/cart/                                                                          | iPad        | &check; | [Test 2.14](./docs/testing/modelled-device-testing/2.14.PNG) |
| 2.15 | https://bryansmullen-designr.herokuapp.com/checkout/                                                                      | iPad        | &check; | [Test 2.15](./docs/testing/modelled-device-testing/2.15.PNG) |
| 2.16 | https://bryansmullen-designr.herokuapp.com/checkout/checkout_success/645599EC2D994B9490B49013EDBDACD9                     | iPad        | &check; | [Test 2.16](./docs/testing/modelled-device-testing/2.16.PNG) |
| 2.17 | https://bryansmullen-designr.herokuapp.com/services/                                                                      | iPad        | &check; | [Test 2.17](./docs/testing/modelled-device-testing/2.17.PNG) |
| 2.18 | https://bryansmullen-designr.herokuapp.com/profiles/                                                                      | iPad        | &check; | [Test 2.18](./docs/testing/modelled-device-testing/2.18.PNG) |
| 3.1  | https://bryansmullen-designr.herokuapp.com/                                                                               | Desktop     | &check; | [Test 3.1 ](./docs/testing/modelled-device-testing/3.1.PNG) |
| 3.2  | https://bryansmullen-designr.herokuapp.com/about                                                                          | Desktop     | &check; | [Test 3.2 ](./docs/testing/modelled-device-testing/3.2.PNG) |
| 3.3  | https://bryansmullen-designr.herokuapp.com/portfolio/                                                                     | Desktop     | &check; | [Test 3.3 ](./docs/testing/modelled-device-testing/3.3.PNG) |
| 3.4  | https://bryansmullen-designr.herokuapp.com/accounts/signup/                                                               | Desktop     | &check; | [Test 3.4 ](./docs/testing/modelled-device-testing/3.4.PNG) |
| 3.5  | https://bryansmullen-designr.herokuapp.com/accounts/login/                                                                | Desktop     | &check; | [Test 3.5 ](./docs/testing/modelled-device-testing/3.5.PNG) |
| 3.6  | https://bryansmullen-designr.herokuapp.com/accounts/password/reset/                                                       | Desktop     | &check; | [Test 3.6 ](./docs/testing/modelled-device-testing/3.6.PNG) |
| 3.7  | https://bryansmullen-designr.herokuapp.com/accounts/password/reset/done/                                                  | Desktop     | &check; | [Test 3.7 ](./docs/testing/modelled-device-testing/3.7.PNG) |
| 3.8  | https://bryansmullen-designr.herokuapp.com/accounts/confirm-email/                                                        | Desktop     | &check; | [Test 3.8 ](./docs/testing/modelled-device-testing/3.8.PNG) |
| 3.9  | https://bryansmullen-designr.herokuapp.com/accounts/confirm-email/MTE:1mRwWt:4TTj7Ta4nidKFInclh8AFKP6MO21xBlksifxr9LfCY4/ | Desktop     | &check; | [Test 3.9 ](./docs/testing/modelled-device-testing/3.9.PNG) |
| 3.10 | https://bryansmullen-designr.herokuapp.com/blog/                                                                          | Desktop     | &check; | [Test 3.10](./docs/testing/modelled-device-testing/3.10.PNG) |
| 3.11 | https://bryansmullen-designr.herokuapp.com/blog/new/                                                                      | Desktop     | &check; | [Test 3.11](./docs/testing/modelled-device-testing/3.11.PNG) |
| 3.12 | https://bryansmullen-designr.herokuapp.com/blog/edit/1/                                                                   | Desktop     | &check; | [Test 3.12](./docs/testing/modelled-device-testing/3.12.PNG) |
| 3.13 | https://bryansmullen-designr.herokuapp.com/blog/delete/1/                                                                 | Desktop     | &check; | [Test 3.13](./docs/testing/modelled-device-testing/3.13.PNG) |
| 3.14 | https://bryansmullen-designr.herokuapp.com/cart/                                                                          | Desktop     | &check; | [Test 3.14](./docs/testing/modelled-device-testing/3.14.PNG) |
| 3.15 | https://bryansmullen-designr.herokuapp.com/checkout/                                                                      | Desktop     | &check; | [Test 3.15](./docs/testing/modelled-device-testing/3.15.PNG) |
| 3.16 | https://bryansmullen-designr.herokuapp.com/checkout/checkout_success/645599EC2D994B9490B49013EDBDACD9                     | Desktop     | &check; | [Test 3.16](./docs/testing/modelled-device-testing/3.16.PNG) |
| 3.17 | https://bryansmullen-designr.herokuapp.com/services/                                                                      | Desktop     | &check; | [Test 3.17](./docs/testing/modelled-device-testing/3.17.PNG) |
| 3.18 | https://bryansmullen-designr.herokuapp.com/profiles/                                                                      | Desktop     | &cross; | [Test 3.18](./docs/testing/modelled-device-testing/3.18.PNG) |

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


| Use Case # | As A Persona | I Want to  | So That |
| --- | --- | --- | ---| 

| 1.4 | As an unauthenticated user | I want to browse the blog  | I can see what value the designer can provide for me  |
| 2.1 | As an authenticated user | I want to order services from the designer | I can have custom designs made for me |
| 2.2 | As an authenticated user | I want to pay for my order through the app | I can purchase the service there and then |
| 3.1 | As a business owner | I want to display my portfolio | I can showcase my work |
| 3.2 | As a business owner | I want to update a blog | To generate traffic to my website and to add value to my services |
| 3.3 | As a business owner | I want to sell my services | To generate income |
| 3.4 | As a business owner | I want to see past orders | I can contact the payee to discuss their design needs |


## User Story Testing

| Maps To User Story # | Steps To Recreate                                                                                  | Expected Results                                        | Pass/Fail |
| ---                  | ---                                                                                                | ---                                                     | ---       | 
| 1.1                  | Navigate to [Home Page](https://bryansmullen-designr.herokuapp.com/*)                              | Home page should render                                 | &check;   |
|                      | Click on register Nav Link                                                                         | Registration page should render                         | &check;   |
|                      | Enter a valid email address, username, password, and repeat the same password, and click 'sign up' | A message is rendered instructing user to check email   | &check;   |
|                      | User checks email, finds relevant email and clicks on confirmation link                            | Confirm email page is rendered                          | &check;   |
|                      | User clicks 'confirm' button to confirm email address                                              | Message is displayed saying email is confirmed, user redirected to sign in page                   | &check;   |
|                      | User enters email and password on sign in page and clicks sign in                                  | User successfully granted access and redirected to home page | &check;   |
| 1.2                  | Navigate to [Home Page](https://bryansmullen-designr.herokuapp.com/*)                              | Home page should render                                 | &check;   |
|                      | Click on Login Nav Link                                                                         | Registration page should render                         | &check;   |
|                      | User enters email and password on sign in page and clicks sign in                                  | User successfully granted access and redirected to home page | &check;   |
| 1.3                  | Navigate to [Home Page](https://bryansmullen-designr.herokuapp.com/*)                              | Home page should render                                 | &check;   |
|                      | Click on Portfolio Nav Link                                                                        | Portfolio page should render                         | &check;   |
| 1.4                  | Navigate to [Home Page](https://bryansmullen-designr.herokuapp.com/*)                              | Home page should render                                 | &check;   |
|                      | Click on Blog Nav Link                                                                             | Blog page should render                         | &check;   |
                                                                    




---

## Issues

Profiles Page Fails HTML Validation due to stray tags generated automatically by django's forms
initSidenav.js fails JS Validation - this file is provided by Materialize as is, and therefore works as designed
stripeElements.js fails JS Validation - this file is created in line with Code Institute tutorials, and due to the complexity of the stripe flow, and the fact that this file currently functions as designed, it has not been edited.
populate with issues fixed
checkout/forms.py fails pep8 validation over a line that is 80 characters long. This has been tolerated for legibility reasons

## Deployment

### Gitpod

### Heroku

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
