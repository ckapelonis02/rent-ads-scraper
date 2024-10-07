# House Rent Ads Scraper

## Project Overview

This project is a Python script that scrapes classified ads ("αγγελίες") from the Χανιώτικα Νέα website, specifically from the "Ενοικιάσεις Κατοικιών" category.

The script saves the website's HTML content locally, extracts and filters ads based on a specific search term, and compares new ads with previously saved ones. It stores both the old and new filtered ads using Python's pickle module.

## Requirements

    Python 3.x
    requests (for sending HTTP requests)
    BeautifulSoup from bs4 (for parsing HTML)
    pickle (for saving and loading filtered ads)

## Notes

This was one of my first Python projects, at a time when finding a house was very difficult in Chania (where I am studying), due to tourism and high rents.

I used to wake up really early and run this program, then I would get disappointed when no good results came up, so I would go to sleep again 😴.

I made it public as a reminder that even the simplest scripts can carry great emotional weight.
