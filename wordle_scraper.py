import tweepy
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv


class WordleScraper(tweepy.StreamingClient):
    def __init__(self, bearer_token, puzzle):
        super().__init__(bearer_token)
        self.puzzle = puzzle
        self.data = []
        # TODO: Clear Rules Associated With Client Token
        
    def scrape(self):
        self.add_rules(tweepy.StreamRule(f'Wordle {self.puzzle}'))
        self.filter(threaded=True)
    
    def on_tweet(self, tweet):
        print(tweet.text)

if __name__ == '__main__':
    load_dotenv()
    scraper = WordleScraper(os.getenv('BEARER_TOKEN'), '')
    scraper.scrape()
