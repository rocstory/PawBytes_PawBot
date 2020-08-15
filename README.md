# Paw Bytes Twitter Bot
Paw Bytes is a three part personal project which models a fictional restaurant.

The three components of this project are
 - [React Web Application](https://github.com/rocstory/PawBytes_WebApp)
 - Twitter Bot
 - [MongoDB Database](https://github.com/rocstory/PawBytes_PawBot)

The Twitter Bot (Paw Bot) was designed to be an extension of the Paw Bytes Restaurant which allows customers to leave compliments (treats) to their favorite Paw Pals.

Paw Bytes Paw Bot interacts with it's customers on the social media platform, Twitter. Customers are able to leave compliments (e-treats) to any of our Paw Pals. The Paw bot collects tweets which mentions one or more Paw Pals and stores it within the Paw Bytes database.

<img src="./screenshots/pawbytes_smap.jpg" width="500" height="500">

## Please note
- The file 'pawbytes_psql_db.py' is no longer being used with the bot.
- Files containing sensitive information were removed from the project.

## Paw Bot
- Paw Bot account name: [@PawBytes](https://twitter.com/PawBytes)
- The Paw bot is developed using Python.

### How it works
- To interact with Paw Bot, mention @PawBytes in a tweet with the hashtag of the Paw Pal that you would like to tweet at. See table below for some of the Paw Pals and their associated hashtag.
- Once the tweet has been made the Paw Bot will then store the tweet into the database and reply back with a thank you message.

| Paw Pal       | Hashtag       |
| ------------- |:-------------:|
| Misty         | #misty        |
| Carson        | #carson       |
| Blue          | #blue         |
| Rocky         | #rocky        |
| Buddy         | #buddy        |

#### 1 Tweet at Paw Bot
- Tweet at Paw Bot with any of the hashtags associated with a Paw Pal

<img src="./screenshots/step1.PNG" width="310.5" height="552">

#### 2 Paw Bot replies
- Paw Bot parses the tweet, checks if a Paw Pal has been mentioned and stores it into the database.
-  Paw Bot then replies back to the user with a thank you message and a prompt to check the Paw Bytes webpage to view their etreat.

<img src="./screenshots/step2.PNG" width="310.5" height="552">

## Project Status
- This project is complete.

## Future implementation
- Adding a function to reject tweets that contain any malicious or negative materials in it.
- Improving the response given by Paw Bot.
- Creating unit tests.

## Current Bugs
- There are currently no bugs as of 8/5/2020


## Reflection
Developing the Paw Bytes Twitter Bot with Python was a fun experience! Taking on this project has helped me gain a better understanding of Python.

## Challenges
- There were no challenges faced when developing Paw Bot.

## Collaborators
There are currently no collaborators on this project as of 8/5/2020


