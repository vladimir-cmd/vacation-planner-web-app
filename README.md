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

- [Home](https://vacation-planner-web-app.herokuapp.com/calendar_home)
  - Home page contains calendar where user can see its days booked.
  - Calendar can be switched to month, week, or day view. 
  - User can click on a specific date to update the entry.
  - User can move between months.
  - User can modify only its own entries.

- [Profile](https://vacation-planner-web-app.herokuapp.com/profile/<username>)
  - Profile page contains information about user
  - User can click on 'Update Profile Info' button to enter following:
    - First Name
    - Last Name
    - Email Address
    - Department
  - User can see how many days there are left
  - User can also delete its own profile by clicking on 'Delete Profile' button
    - Sanity check will be executed -> there will be a popup asking user if its sure
    - By deleting user, all its entries will be deleted as well 
  
- [New Entry](https://vacation-planner-web-app.herokuapp.com/add_entry)
  - On this page user can add new Vacation entry
  - User can choose from the following:
    - Select Department (Choose Department)
      - If you already have Department specified, you can only add entry for that department
    - Select Entry Type (Choose Entry Type)
    - Entry Description
    - Start Date
    - End Date
    

- [Edit Entry](https://vacation-planner-web-app.herokuapp.com/edit_entry/<entry_id>)
  - On this page user can edit its own Vacation entry
  - User can choose from the following:
    - Select Department (Choose Department)
      - If you already have Department specified, you can only add entry for that department
    - Select Entry Type (Choose Entry Type)
    - Entry Description
    - Start Date
    - End Date
    

- [Manage Entry](https://vacation-planner-web-app.herokuapp.com/manage_entries)
  - On this page user can get the overview of its own Vacation entries
  - User can choose from the following:
    - Delete entry
      - Completely deletes entry from the database
    - Edit entry:
        - Select Department (Choose Department)
          - If you already have Department specified, you can only add entry for that department
        - Select Entry Type (Choose Entry Type)
        - Entry Description
        - Start Date
        - End Date


- [Register](https://vacation-planner-web-app.herokuapp.com/register)
  - Future user can register by entering username
  - User must specify password two times
  - Password mus match
  

- [Login](https://vacation-planner-web-app.herokuapp.com/login)
  - User must login in order to add/modify/delete entry
  - User must provide username and password
    

## Technologies Used

In this project the following technologies have been used.

- [HTML](https://en.wikipedia.org/wiki/HTML)

  - Semantic markup language as the shell of the site.

- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

  - Cascading Style Sheets as the design of the site.

- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

  - Programming language for the workability of the site.

- [FontAwesome](https://fontawesome.com/)

  - **FontAwesome** provided the icons used on the page.

- [Materialize](https://materializecss.com/about.html)

  - Created and designed by Google, Material Design is a design language that combines the classic principles of successful design along with innovation and technology. 
  - Google's goal is to develop a system of design that allows for a unified user experience across all their products on any platform.

- [MongoDB](https://www.mongodb.com/1)

  - Database solution for the site
  
- [Python Flask](https://flask.palletsprojects.com/en/1.1.x/)

  - Python Web Framework working closely with Jinja templates and Werkzeug WSGI toolkit.

- [Visual Studio Code](https://code.visualstudio.com/)

  - IDE (Integrated Development Environment).

- [IntelliJ Idea Community Edition](https://www.jetbrains.com/idea/)

  - IDE (Integrated Development Environment).

- [GitHub](github.com/)

  - The remote hosting platform.

- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)

  - To see visually the elements of what each code produced, what happens if code is changed, and responsiveness of different device sizes.

- [Jigsaw](https://jigsaw.w3.org/css-validator)

  - To check for any errors in the CSS code.

## Testing

Testing information is found on a separate file [TESTING.MD](https://github.com/vladimir-cmd/vacation-planner-web-app)

## Deployment

Creation of website

This website is deployed using Heroku.

## Credits

### Content

### Media

### Acknowledgements
