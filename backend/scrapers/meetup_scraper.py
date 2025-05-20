import requests
from bs4 import BeautifulSoup
from datetime import datetime
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class MeetupScraper:
    def __init__(self):
        self.base_url = "https://www.meetup.com/find/?location=au--sydney&source=EVENTS"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
    def scrape_events(self):
        """Scrape events from Meetup Sydney"""
        all_events = []
        
        try:
            # Use verify=False to bypass SSL verification
            response = requests.get(self.base_url, headers=self.headers, verify=False, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            event_cards = soup.select('div.eventCard')
            
            for card in event_cards:
                try:
                    # Extract event details
                    title_elem = card.select_one('h2.eventCardHead--title')
                    title = title_elem.text.strip() if title_elem else "No Title"
                    
                    date_elem = card.select_one('time')
                    date_time = date_elem.text.strip() if date_elem else "Check website for dates"
                    
                    location_elem = card.select_one('address.venueDisplay')
                    location = location_elem.text.strip() if location_elem else "Sydney, Australia"
                    
                    description_elem = card.select_one('p.eventCardHead--description')
                    description = description_elem.text.strip() if description_elem else ""
                    
                    link_elem = card.select_one('a.eventCard--link')
                    ticket_link = link_elem['href'] if link_elem and 'href' in link_elem.attrs else ""
                    
                    # Create event object
                    event = {
                        'title': title,
                        'date_time': date_time,
                        'location': location,
                        'description': description[:200] + '...' if len(description) > 200 else description,
                        'ticket_link': ticket_link,
                        'source': 'Meetup'
                    }
                    
                    all_events.append(event)
                except Exception as e:
                    print(f"Error parsing Meetup event card: {e}")
                    continue
                    
        except Exception as e:
            print(f"Error scraping Meetup Sydney: {e}")
            print("Continuing with other sources...")
            
        return all_events


if __name__ == "__main__":
    scraper = MeetupScraper()
    events = scraper.scrape_events()
    for event in events:
        print(f"Title: {event['title']}")
        print(f"Date: {event['date_time']}")
        print(f"Location: {event['location']}")
        print(f"Link: {event['ticket_link']}")
        print("-" * 50) 