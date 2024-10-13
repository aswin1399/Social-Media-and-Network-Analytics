import sys
import praw


def redditClient():
    """
        Function to set up and return a Reddit client instance
    """
    try:
        clientId = "pKVCr2fIOsrT00cE7i4E5A"
        clientSecret = "2y7Ly9ECss1rVnZLppCg2EwJbk8gQw"
        userAgents = 'client for SNAM2024'

        redditClient = praw.Reddit(client_id = clientId,
                                   client_secret = clientSecret,
                                   user_agent = userAgents) 
        
    except KeyError:
        sys.stderr.write("Key or secret token are invalid.\n")
        sys.exit(1)


    return redditClient