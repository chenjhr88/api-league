#!/usr/bin/env python
# coding: utf-8

# # Social Media, Bots and APIs
# 
# ## Part \#1: Create Your First Twitter Bot
# 
# In this notebook, you will create your first Twitter Bot. Here are some guidelines you will have to follow throughout this chapter: 
# 
# ### Classroom Expectations and Ethical Bot Usage
# 
# * Any tweets you send will be visible to your teacher, your classmates, the Fremd community, and the broader Internet
#   * You are representing Fremd High School with any tweets you send
#   * Profanity, harassment, spamming, or any other misbehavior will result in a discipline referral and being reassigned a new project
#   
#   
# * Do not spam Twitter users (even by accident)
#     * Do not send _numerous_ unsolicited tweets to the same account
#     * Do not try to send the same tweet out over and over again
#     * Do not tweet more than once per minute 
#     * To avoid accidental spamming, use [_import time_](https://pythonspot.com/sleep/) and _time.sleep(60)_ in any loops that send tweets   
#     
#     
# * Bot creators must follow these ethical principles:
#   * Inform users that your account is a bot (do not impersonate a real person) 
#   * Inform users who controls your bot 
#   * Inform users who can access the data your bot collects
#   * A bot should never be created for the purpose of harming its users (theft, fraud, harassment, spam, etc) 
# 
# Now that this is done, let's create a Twitter account:

# ### Step 1: Sign Up For a Twitter Account
# 
# Follow the instructions below step-by-step without working ahead of the screenshots. First go to https://twitter.com/signup and fill in the information below using your D211 email address:

# In[38]:


from IPython.display import Image
Image(filename="Screenshots/1_Login.png")


# ### Step 2: Enter Your Phone Number
# 
# You should use your own phone number if you are comfortable using this, you have your phone with you, and you get signal in the computer lab. If not, you can use or create a free Google Voice account at https://voice.google.com or you can check with your teacher for other options.

# In[31]:


from IPython.display import Image
Image(filename="Screenshots/2_Phone.png")


# ### Step 3: Confirm Phone Number, Email Address, and Pick a Profile Picture
# 
# Complete the following steps:
# * Confirm your phone number by typing in the code
# * Confirm your email address
# * Upload a school-appropriate profile picture
#   * The picture does NOT have to be of you
#   * This will help prevent you getting flagged as a spammer:
#   * https://www.buzzfeed.com/blakemontgomery/twitter-will-start-using-algorithms-to-crack-down-on-abusive?utm_term=.mrM4B91ZWr#.fj6wlJ6oEO

# In[32]:


from IPython.display import Image
Image(filename="Screenshots/3_Confirm.png")


# ### Step 4: Don't like you username?  You can change it!
# 
# Follow the directions below to change your username.  It must be something unique to the twitter world!

# In[33]:


from IPython.display import Image
Image(filename="Screenshots/4_Username.png")


# ### Step 5: Go to the Twitter App Site
# 
# Go to https://apps.twitter.com/ so you can create your first app.

# In[34]:


from IPython.display import Image
Image(filename="Screenshots/5_App.png")


# ### Step 7: Name Your App
# 
# Use the details listed below, but make sure to add a string of random numbers at the end of the Name category. Your app can't have the same name as another student's, so add a few numbers to the end of your app name to make it unique.

# In[35]:


from IPython.display import Image
Image(filename="Screenshots/6_Create.png")


# ### Step 8: Save your API Key and API Secret
# 
# An API key is what allows you to access your account securely through the API interface. Do not share it with anyone else: you must keep it as secure as your username and password.

# In[36]:


from IPython.display import Image
Image(filename="Screenshots/7_Keys.png")


# ### Step 9: Generate an Access Token
# 
# You also need to generate an Access Token and Access Secret. If you are interested in the difference between an API Key/Secret and an Access Token/Secret, [click here for a nice summary that goes into more detail than you need for this course.](http://stackoverflow.com/questions/28057430/what-is-the-access-token-vs-access-token-secret-and-consumer-key-vs-consumer-s)

# In[37]:


from IPython.display import Image
Image(filename="Screenshots/8_Tokens.png")


# **Task \#1:** Enter Your API (Consumer) Key/Secret and Access Token/Secret Below:
# 
# This initializes the API object which allows us to send Tweets and perform other actions from our newly-created account:
# 
# **CAUTION: When you copy/paste your keys and tokens into your notebook there may be additional characters inserted to the beginning of the string! Delete any strange characters that appear.**

# In[1]:


# tweepy is a Python module for interacting with the Twitter API
import tweepy, time, sys
 
# enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'DGskShkG0JmR1Oj0VdtiOX01K'# keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '2qH7Vivi61gjtAcmgomZ2eTsKyJ6z690F8Z6Ah7jd1u6pwcxi3'# keep the quotes, replace this with your consumer secret key
ACCESS_TOKEN = '973206621693333504-EZz5fS0kkodFQdlvA2rsylrnWlXn8UP'# keep the quotes, replace this with your access token
ACCESS_SECRET = 'TksFzMzhdg91DcNJwb8lRn64Xlf7VtNVB9x0pqINZc32p'# keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth) # this creates the API object


# ### Send Your First Tweet
# 
# **Task \#2:** Initialize the variable *my_message* to the string "Hello World! This tweet was generated by a bot I created in #APCSP. #FHSspirit #CSforall @AP_Trevor" 
# 
# Then call the following method to send your first tweet: *api.update_status(my_message)*
# 
# Do not run this cell multiple times. You do not want your account to get locked out for suspected spamming or harassment.

# In[2]:


# your code here
my_message = "Hello World! This tweet was generated by a bot I created in #APCSP. #FHSspirit #CSforall @AP_Trevor"
api.update_status(my_message)


# Take a look at all of the output above and scan for anything interesting. Then check Twitter and see if your first tweet went out to the world successfully!

# ### Tweeting Your First Picture
# 
# **Task \#3:** Send a tweet with a picture attached. Find any JPEG picture and name it _picture1.jpg_, and save it to the folder containing this notebook. This picture should be 100% school appropriate.
# 
# Now initialize a variable, *my_picture*, to the string 'picture1.jpg'.
# 
# Also intialize a variable, *my_status*, to a school-appropriate string of your choice. Remember that Twitter status updates cannot exceed 280 characters.
# 
# Finally, send the tweet using the following method call: *api.update_with_media(my_picture, my_status)*

# In[3]:


# your code here
my_picture = "picture1.jpg"
my_status = "Yellow"
api.update_with_media(my_picture, my_status)


# ### Searching Twitter
# 
# **Task \#4:** Run the cell below to search for the most recent tweets that mention the Fremd High School account, *@fremdvikings*. Then write code to find out how many tweets were in your search results.
# 
# Your Answer: 15

# In[4]:


#your search query is for @fremdvikings:
tweet_list = api.search(q="@fremdvikings")

#print out the text of the search results:
for tweet in tweet_list:
    print(tweet.text)
    
# write code below to see how many tweets were in your search results:


# **Task \#5:** Try a few more searches using the following terms:
# 
# * @FremdBot
# * #APCSP
# * #CSforall
# * at least two more (school-appropriate) searches
# 
# Include each set of results in its own cell. Comment on anything interesting you found in a markdown cell after your code cells, or even reply to any tweets you think were meant for you.

# In[5]:


# your code here (@Fremdbot)
tweet_list = api.search(q="@Fremdbot")
for tweet in tweet_list:
    print(tweet.text)


# In[6]:


# your code here (#APCSP)
tweet_list = api.search(q="#APCSP")
for tweet in tweet_list:
    print(tweet.text)


# In[7]:


# your code here (#CSforall)
tweet_list = api.search(q="#CSforall")
for tweet in tweet_list:
    print(tweet.text)


# In[9]:


# your code here (your choice #1)
tweet_list = api.search(q="#Madara")
for tweet in tweet_list:
    print(tweet.text)


# In[11]:


# your code here (your choice #2)
tweet_list = api.search(q="#Taiwan")
for tweet in tweet_list:
    print(tweet.text)


# ### Brainstorm Project Ideas
# 
# **Task \#6:** Build upon old ideas or come up with some new ideas you have for creating your own Twitter bot. Can you think of ways to incorporate image filters, web scraping, the Google Maps API, or Open Data? Try to categorize your brainstorms as "big project (months of work)" and "feasible project (2 week project)."
# 
# *big project ideas (months of work):* Creating a webpage that updates itself and prints the status of certain accounts by scraping them.
# 
# *feasible project ideas (2 week project):* Using photos from Twitter and pinpointing them onto a map of the world to see where each one was taken.
# 

# ### Explore the documentation
# 
# **Task \#7:** Browse the following documentation: 
# 
# https://media.readthedocs.org/pdf/tweepy/v3.5.0/tweepy.pdf
# 
# http://docs.tweepy.org/en/v3.5.0/
# 
# *Note: You do not need to write a written response or any code for this particular task.*
