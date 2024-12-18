# RHS-Bathroom-System

*This is the system designed to monitor and direct students to the bathrooms during classes*

## Functionality:
+ Managed through a web application
+ students sign in, automatically assigned to a bathroom by time of day/current class location
+ Handled the restrictions on class change, time of day, capacity limit of bathrooms, and more.
+ Future implementation: alert administrators when someone forgot to sign out of the bathroom & other monitoring capabilities

## About
+ Hosted via Flask
+ front end is simple HTML/CSS/JS
+ Uses studentvue API to scrape data
+ mariadb for the database (graciously hosted by the University of Mary Washington)
+ Note: Definitely vulnerable to SQL injections, so make sure to take care of that before pushing to prod.

Feel free to make any pull requests or build off of it for your own school system. 

MIT License, Copyright - Colin Wolfe 2023
