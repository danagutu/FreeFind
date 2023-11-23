# FreeFind

## Introduction
This repo contains the code for @danagutu's Program Project for [Out in Tech U](https://outintech.com/mentorship-program/). 


### Motivation
The motivation came from Dana and friends' experience navigating student life in the cost of living crisis.

This means students are particularly keen to find events they can go to that offer free stuff - food, drinks, merch or DIY. 

This project aims to help with discovery of these events. The first milestone of success means Dana and her friends find events to go to that they otherwise wouldn't have noticed!

## Team
- **Dana**: Developer
- **Charles**: Mentor

## Project Scope
The scope for time is 8 weeks, with each week consisting of:
- 2-8 hours of learning and coding
- 2 mentoring sessions

## Technical Overview
- Web scraping with Python, [Requests](https://pypi.org/project/requests/), [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
- Parsing with beautiful soup, [OpenAI chat completion](https://platform.openai.com/docs/guides/text-generation/chat-completions-api)

- Serverless back-end with [Firebase](https://firebase.google.com/)


[will be added as the project develops]


## Weekly Progress Updates

### Week 1 - Ideation
In introduction called we discussed Dana's goals and motivations. 

The trigger for this project was to **build** something as a way to learn real-world coding skills.

Additionally, the project was selected based on:
- Interesting Tech
- Valuable for people Dana knows
- Small enough scope to be feasible, ambitious enough to be expandable

This led to the idea of helping students find events with free food, drinks, activities, or merch.

### Week 2 - Scoping
- Drafted cool screen of this idea (figma)
- Iterations on mockups
- Manually reviewed sample events

### Week 3 - Backend & Development Processes
- Wrote first scraping project using python
- Connected to firebase, and stored some event data
- Completed [Prompt Engineering for developers course](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
- Set up git started good development practise (.gitignore credential files)


### Week 4 - Minimum Viable Backend
- Unblocked access issues with OpenAI
- Used openAI chat completion API to parse descriptions for 'free drinks'
- Improved storage of events in Firebase

### TODO
- Improve scraping to get a good baseline descritpion for 'events', explore and better understand parsing with Beautiful Soup.
- add image URLs
- *in openai_test* - fetch all events from Firebase
- for events missing the 'free_drinks' attributes, run Chat Completion
- Save free_drinks (true/false) in Firebase
- (optional) improve the prompt setup to get free food (true/false)
- populate 5 - 15 events in Firebase

### Week 5 - Front-End and Web Frameworks
- connect to firebase
- host via heroku (?)
- display elements (react?)

### Week 6 - First Release
- Populate back-end
- Explore regular processes (cron?)
- Manage display, any issues on front-end

### Week 7 - Major iterations & Refactors
- Review additional fields to generate
- Review additional data sources for events
- Gather and prioritise feedback from users

### Week 8 - Final Polish & Scope review
- tbd

