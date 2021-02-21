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
- As a user, I want to be able to see my finished designs in a private user area
- As a user, I want to be able to request changes to the artwork, so long as I have sufficient edits allowed
- As a user, I want to be able to pay for my order on the website using a secure method
- As a designer, I want to be able to showcase my public work to the world to generate new business
- As a designer, I want to be able to accept new commissions from users
- As a designer, I want to be able to accept payment for commissions up front
- As a designer, I want to be able to limit the number of edits a user can make before the artwork is considered
  finished
- As a designer, I want to be able to charge a premium rate if the user does not want the artwork displayed in the
  public portfolio

- Account
open orders
closed orders

## Data Types

The following data types will be used in the project, and an SQL table will be generated for each:

- User - Individual users
    - Id [str] (unique, PK)
    - Name [str]
    - Email [str] (unique, used for authentication)
    - Password [str] (hashed)
- Services - Services offered by the designer for purchase
    - Id [str] (unique, PK)
    - Category [str]
    - Name [str] (unique)
    - Description [str]
    - Price [int]
    - Public [bool]
- Designs - Completed tangible pieces of artwork
    - Id [str] (unique, PK)
    - Category [str]
    - Date [date]
    - Complete [bool]
    - Brief [text]
    - Image [str] (unique, url to jpg/png)
    - Owner [str] (FK)
    - EditsRemaining [int] (default 1)
- Messages - Edit requests relating to a particular piece of artwork
    - Id [str] (unique, PK)
    - Owner [str] (FK)
    - Artwork [str] (FK)
    - Message [text]
    
## Permissions

- User
    - Create - All
    - Read - Admin/self
    - Update - self * implement password recovery
    - Delete - self
- Services
    - Create - Admin
    - Read - Admin
    - Update - Admin
    - Delete - Admin
- Designs
    - Create - Admin
    - Read - Admin/Owner
    - Update - Admin/Owner (limited to edit requests)
    - Delete - Admin
- Messages
    - Create - Admin/Authenticated User
    - Read - Admin/Authenticated User
    - Update - Owner
    - Delete - Owner
  
## Testing
- Urls
- View
- Models
- Helper Files

[comment]: <> (## Features)

[comment]: <> (In this section, you should go over the different parts of your project, and describe each in a sentence or so.)

[comment]: <> (### Existing Features)

[comment]: <> (- Feature 1 - allows users X to achieve Y, by having them fill out Z)

[comment]: <> (- ...)

[comment]: <> (For some/all of your features, you may choose to reference the specific project files that implement them, although this)

[comment]: <> (is entirely optional.)

[comment]: <> (In addition, you may also use this section to discuss plans for additional features to be implemented in the future:)

[comment]: <> (### Features Left to Implement)

[comment]: <> (- Another feature idea)

[comment]: <> (## Technologies Used)

[comment]: <> (In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used)

[comment]: <> (to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was)

[comment]: <> (used.)

[comment]: <> (- [JQuery]&#40;https://jquery.com&#41;)

[comment]: <> (    - The project uses **JQuery** to simplify DOM manipulation.)

[comment]: <> (## Testing)

[comment]: <> (In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that)

[comment]: <> (the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and)

[comment]: <> (ensure that they all work as intended, with the project providing an easy and straightforward way for the users to)

[comment]: <> (achieve their goals.)

[comment]: <> (Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your)

[comment]: <> (approach, link to the test file&#40;s&#41; and explain how to run them.)

[comment]: <> (For any scenarios that have not been automated, test the user stories manually and provide as much detail as is)

[comment]: <> (relevant. A particularly useful form for describing your testing process is via scenarios, such as:)

[comment]: <> (1. Contact form:)

[comment]: <> (    1. Go to the "Contact Us" page)

[comment]: <> (    2. Try to submit the empty form and verify that an error message about the required fields appears)

[comment]: <> (    3. Try to submit the form with an invalid email address and verify that a relevant error message appears)

[comment]: <> (    4. Try to submit the form with all inputs valid and verify that a success message appears.)

[comment]: <> (In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.)

[comment]: <> (You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you)

[comment]: <> (haven't addressed them yet.)

[comment]: <> (If this section grows too long, you may want to split it off into a separate file and link to it from here.)

[comment]: <> (## Deployment)

[comment]: <> (This section should describe the process you went through to deploy the project to a hosting platform &#40;e.g. GitHub Pages)

[comment]: <> (or Heroku&#41;.)

[comment]: <> (In particular, you should provide all details of the differences between the deployed version and the development)

[comment]: <> (version, if any, including:)

[comment]: <> (- Different values for environment variables &#40;Heroku Config Vars&#41;?)

[comment]: <> (- Different configuration files?)

[comment]: <> (- Separate git branch?)

[comment]: <> (In addition, if it is not obvious, you should also describe how to run your code locally.)

[comment]: <> (## Credits)

[comment]: <> (### Content)

[comment]: <> (- The text for section Y was copied from the [Wikipedia article Z]&#40;https://en.wikipedia.org/wiki/Z&#41;)

[comment]: <> (### Media)

[comment]: <> (- The photos used in this site were obtained from ...)

### Acknowledgements

Home BG Photo by Max Vakhtbovych from Pexels

Design examples: 
- Photo by Magda Ehlers from Pexels
- Photo by Sy Donny from Pexels
- Photo by Kaboompics .com from Pexels
- Photo by Ann H from Pexels
- Photo by eric anada from Pexels

[comment]: <> (- I received inspiration for this project from X)