import sys
from googleapiclient.discovery import build

def youtubeClient():
    """
        Function to set up and return a YouTube client instance
    """
    try:
        api_key = "AIzaSyDsdJ3EuHqO7VcvwLxVsGlgVePVTe3FRi4"
        youtube_client = build('youtube', 'v3', developerKey=api_key)
        
    except KeyError:
        sys.stderr.write("API key is invalid.\n")
        sys.exit(1)

    return youtube_client
