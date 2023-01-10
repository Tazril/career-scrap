# Career Assistant
Search for careers in list of scrapped company careers' page

## Introduction

We all know getting a referral or applying directly on career site directly has the most chances of getting a interview call
But we all know how painful it is to remember all the company names and goto their career site and apply
So, in order to solve this problem, I started this project Career Assistant

## Low Level Design
<img width="1057" alt="image" src="https://user-images.githubusercontent.com/42216712/211600776-1ccdf928-6a9a-4b03-9924-ce96d32366c8.png">

## High Level Design
<img width="1334" alt="image" src="https://user-images.githubusercontent.com/42216712/211606027-ead5e35f-4df7-4f7c-9031-9bcd700624bb.png">


## Careers Scraping Flow chart
<img width="847" alt="image" src="https://user-images.githubusercontent.com/42216712/211606133-347539e9-c201-4265-884a-9abed16a7451.png">


## Contribute

Contributions are welcome. You can contribute company scrapper to this project by following the guidlines
0. Choose a company of your choice
1. Clone the repository and create a branch with company name (small case with hyphen)
2. Visit the careers page of the choice of your company
3. Observe how it can be scrap either in two ways a) ajax call or b) beautiful soup
4. Create a python file with the name of your company. Add the logic by inheriting the proper parent class. Check existing examples
5. Add your company class in scrappers.py file
6. Test your code locally by running your code and check if the company postings are showing on UI
7. Raise a pull request with your changes

You are also welcome to modify core logic, UI or any other way.
You are also welcome to create issues (report bug, feature request etc)
