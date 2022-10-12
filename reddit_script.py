#!/usr/bin/env python
# coding: utf-8

# In[30]:


from logging import exception
import praw

import config

user_agent = "Scraper 1.0 by mrX"

reddit = praw.Reddit(client_id = config.client_id, client_secret = config.client_secret, user_agent = user_agent)


# In[31]:


def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num

def list_average(List):
    avg = sum(List)/len(List)
    
    return avg

print("Welcome to the 'Reddit Script'! Type your subreddit of choice and see some interesting statistics about it! \n Important Note: Type 'quit_the_program' to terminate.\n")


# In[40]:


headlines_set = set()
headlines_all = []

users_set = set()
users_all = []

scores_all = []


user_input = input("Enter name of the subreddit: ")

while(user_input != "quit_the_program"):

    try:

        headlines_set = set()
        headlines_all = []

        users_set = set()
        users_all = []

        scores_all = []
        
        for submission in reddit.subreddit(user_input).hot(limit=None):

            headlines_set.add(submission.title) # adding the titles to our set.
            headlines_all.append(submission.title)

            #selftext_all.append(submission.selftext)

            users_set.add(submission.author)
            users_all.append(submission.author)

            scores_all.append(submission.score)

        print(f"The number of all headlines: {len(headlines_all)}"   )
        print(f"The number of all DISTINCT headlines: {len(headlines_set)}"  )


        print(f"The number of DISTINCT users posted: {len(users_set)}")
        print(f"The average upvote score for all posts: {round(list_average(scores_all))}")


        print(f"The user who has posted the most: {most_frequent(users_all)} - Number of total posts: {users_all.count(most_frequent(users_all))}")

    except Exception as e: 

        print("You have entered a subreddit which does not exist. Please try again :)")
        print(e)
    user_input = input("\nEnter name of the subreddit: ")
    
    #if(user_input == "quit_the_program"):
        #print("Thanks for using the Reddit Script! Goodbye!")
print("Thanks for using the Reddit Script! Goodbye!")

