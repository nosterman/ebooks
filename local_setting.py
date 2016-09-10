'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'osAfRW7kCRHmWHZiJAWwlAH8R'
MY_CONSUMER_SECRET = '6ny6kVsW613PUVadvCxEiJmVcHLbJAmfHmOs6wrjEuLMQP3vHj'
MY_ACCESS_TOKEN_KEY = '774071179334283264-0EO90EmjItyoqGceSMauPUpT1PJJV0Y'
MY_ACCESS_TOKEN_SECRET = 'zIZinHj2rRRHMoRpILNEIsEGIPBdDOKTa71dE9bdub4VN'

SOURCE_ACCOUNTS = ["nateosterman", "LtSuns", "bjmoonshoes", "iamtylermarie"] 
ODDS = 1 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "theboys_ebooks" #The name of the account you're tweeting to.
