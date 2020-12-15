# Vacation Planner Web App

This web application is created for company purposes.
App goal is to have a central place where employees can add their planned vacation or any other type of leave.
Visitor should be able to:
- Register
- Login
- Check current status of vacation days left
- Add\Update personal information
- Add Vacation or any other type of leave
- Check all current entries
- Check the calendar
- Manage entries (update\delete)
- Delete user profile
- Logout

# <p align="center">[Vacation Planner Web App Link](https://vacation-planner-web-app.herokuapp.com/ "Vacation Planner Web App")</p>

## User Experience

### Plan

Every company needs to have a fully functional vacation planner, to track the current vacation days status of all employees.
Also, it should be very handy for a manager to quickly check who has vacation at a specific time.
Other employees should also be aware who has vacation and when, so they can quickly plan for themselves

### User Stories

Reason why creating this web application:

- be a place where visitor can create their profile by registering 
- be a place where visitor can login, plan vacation and create vacation entries
- be a place where visitor can check how many days they have left
- be a place where visitor can update their personal information
- be a place where visitor can glance at a calendar and have an overview of their booked vacation days
- be a place where visitor can modify its vacation entries
- be a place where visitor can delete its profile

## Wireframes

I used [AdobeXD](https://www.adobe.com/ie/products/xd.html) to create
[wireframes](https://github.com/vladimir-cmd/vacation-planner-web-app/tree/master/wireframes-mockups) in: 
[Front Page Before Login](https://github.com/vladimir-cmd/vacation-planner-web-app/blob/master/wireframes-mockups/Front_Page_Before_Login.png), 
[Front Page After Login](https://github.com/vladimir-cmd/vacation-planner-web-app/blob/master/wireframes-mockups/Front_Page_After_Login.png), 
[User Profile Page](https://github.com/vladimir-cmd/vacation-planner-web-app/blob/master/wireframes-mockups/Users_profile.png), 
[Add New Entry](https://github.com/vladimir-cmd/vacation-planner-web-app/blob/master/wireframes-mockups/Add_New_Entry.png), 
[Edit Entry](https://github.com/vladimir-cmd/vacation-planner-web-app/blob/master/wireframes-mockups/Edit_Entry.png), 
[Manage Entry](https://github.com/vladimir-cmd/vacation-planner-web-app/blob/master/wireframes-mockups/Manage_Entries.png)

## Features

### Page Features:

- [Home](http://vacation-planner-web-app.herokuapp.com/calendar_home)

  - This page starts with a header.
  - Home page contains calendar where user can see its days booked.
  - Calendar can be switched to month, week, or day view. 
  - User can click on a specific date to update the entry.
  - User can move between months.

- [Profile](http://vacation-planner-web-app.herokuapp.com/profile/<username>)
  - Profile page contains information about user
  - User can click on 'Update Profile Info' button to enter following:
    - First Name
    - Last Name
    - Email Address
  - User can see how many days there are left
  - User can also delete its own profile by clicking on 'Delete Profile' button
    - Sanity check will be executed -> there will be a popup asking user if its sure
  
- [New Entry](http://vacation-planner-web-app.herokuapp.com/add_entry)
  - On this page user can add new Vacation entry
  - User can choose from the following:
    - Select Department (Choose Department)
    - Select Entry Type (Choose Entry Type)
    - Entry Description
    - Start Date
    - End Date
    

### All Page Features:

- **Semantic HTML**: All pages have been written with semantic HTML in mind.
- **Fixed Header**: Each page has a fixed header, for ease of navigation.
- **Responsive Design**: Site pages are designed to work on all sizes of device.

### Specific Features:

- **Subscribe to Newsletter**: Every page includes subscribe to newsletter section where visitor can subscribe for the latest recepies.

## Technologies Used

In this project the following technologies have been used.

- [HTML](https://en.wikipedia.org/wiki/HTML)

  - Semantic markup language as the shell of the site.

- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

  - Cascading Style Sheets as the design of the site.

- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

  - Programming language for the workability of the site.

- [Google Fonts](https://fonts.google.com/)

  - Google's font catalog places typography front and center, inviting users to explore, sort, and test fonts for use in more than 135 languages.

- [FontAwesome](https://fontawesome.com/)

  - **FontAwesome** provided the icons used on the page.

- [Bootstrap 4](https://getbootstrap.com/)

  - To be easily responsive, navbar, the list groups, card decks and forms were used to give a clean, simple and ordered look. I wanted to re-inforce what I had learnt from the UCFD module.

- [Gitpod](https://gitpod.io/)

  - IDE (Integrated Development Environment).

- [GitHub](github.com/)

  - The remote hosting platform.

- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)

  - To see visually the elements of what each code produced, what happens if code is changed, and responsiveness of different device sizes.

- [Jigsaw](https://jigsaw.w3.org/css-validator)

  - To check for any errors in the CSS code.

- [W3C Markup Validator](https://validator.w3.org/)
  - To check for any errors in HTML code.

## Testing

Testing information is found on a separate file [TESTING.MD](https://vladimir-cmd.github.io/pub_restaurant_search.github.io/TESTING.md)

## Deployment

Creation of website

This website is deployed using GitHub pages.

**GitHub pages** was used to deploy this site. 
   1. Go to repository master branch ([Source](https://vladimir-cmd.github.io/pub_restaurant_search.github.io))
   2. Press Settings button on right. 
   3. Scroll down to Github Pages section. 
   4. There will be link to website
   Note: there is only a master branch. No other branches were created.

To run the copy of website, there are two options:

1. Sign to your GitHub account
2. search for the following repository: https://vladimir-cmd.github.io/pub_restaurant_search.github.io
3. In the upper right corner click on "Fork" button
4. You have successfully duplicated my website to your GitHub account

OR

Important: must have git CLI installed on local machine

1. Sign to your GitHub account
2. search for the following repository: https://vladimir-cmd.github.io/pub_restaurant_search.github.io
3. Click on "Clone or download" button and copy the path
4. Open Command Line interface (Windows - Powershell or Linux\MacOS - Terminal)
5. git clone https://github.com/vladimir-cmd/pub_restaurant_search.github.io.git
6. You have successfully clonned repository on your local machine
   Note: You would require a web server to run the site from your local machine.
   As a workaround, you can use repl.it

You can open the site in repl.it

1. Sign to your GitHub account
2. search for the following repository: https://vladimir-cmd.github.io/pub_restaurant_search.github.io
3. Click on "Clone or download" button and copy the path
4. Open repl.it
5. Navigate to myrepls
6. In the upper right corner click on "new repl"
7. In a new window, select "Import From GitHub"
8. Paste the link you copied in step 3

## Credits

### Content
- The Map is Google Maps [Google Maps](https://maps.google.com/)

### Media
- The photos used are taken from [Unsplash](https://unsplash.com/) - Photos for everyone

### Acknowledgements

- I want to give huge thanks to my mentor [Precious Ilege](https://www.linkedin.com/in/precious-ijege-908a00168/) for guiding me thru this milestone project. I would not be able to finish this project on time if not for Precious. His suggestions, advices, and mentoring helped me in great deal to finish this project on time, even though I started late.
