import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scrapers.eventbrite_scraper import EventbriteScraper
from scrapers.timeout_scraper import TimeoutScraper
from scrapers.meetup_scraper import MeetupScraper
from database.db_manager import DatabaseManager
from database.schema import init_db

class ScraperManager:
    def __init__(self):
        self.eventbrite_scraper = EventbriteScraper()
        self.timeout_scraper = TimeoutScraper()
        self.meetup_scraper = MeetupScraper()
        self.db_manager = DatabaseManager()
        
    def run_all_scrapers(self):
        """Run all scrapers and save results to database"""
        print("Starting scraping process...")
        
        # Initialize database if it doesn't exist
        init_db()
        
        # Run each scraper
        print("Scraping Eventbrite...")
        eventbrite_events = self.eventbrite_scraper.scrape_events()
        print(f"Found {len(eventbrite_events)} events from Eventbrite")
        
        print("Scraping TimeOut Sydney...")
        timeout_events = self.timeout_scraper.scrape_events()
        print(f"Found {len(timeout_events)} events from TimeOut")
        
        print("Scraping Meetup...")
        meetup_events = self.meetup_scraper.scrape_events()
        print(f"Found {len(meetup_events)} events from Meetup")
        
        # Combine all events
        all_events = eventbrite_events + timeout_events + meetup_events
        
        # Save events to database
        saved_count = 0
        for event in all_events:
            try:
                self.db_manager.save_event(event)
                saved_count += 1
            except Exception as e:
                print(f"Error saving event: {e}")
                continue
                
        print(f"Successfully saved {saved_count} events to database")
        
        # Clean up old events
        self.db_manager.clear_old_events()
        print("Removed old events from database")
        
        return saved_count
        

if __name__ == "__main__":
    manager = ScraperManager()
    manager.run_all_scrapers() 