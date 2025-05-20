import os
import sys
import sqlite3
from datetime import datetime, timedelta

# Add the parent directory to the path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.db_manager import DatabaseManager
from database.schema import init_db

def add_sample_events():
    """Add sample events to the database for testing"""
    print("Adding sample events to the database...")
    
    # Initialize database if it doesn't exist
    init_db()
    
    # Create a database manager
    db_manager = DatabaseManager()
    
    # Create sample events
    sample_events = [
        {
            'title': 'Sydney Opera House Tour',
            'date_time': (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d %H:%M:%S'),
            'location': 'Sydney Opera House, Bennelong Point, Sydney NSW 2000',
            'description': 'Experience the beauty of the Sydney Opera House with a guided tour. Learn about its history and architecture.',
            'ticket_link': 'https://www.sydneyoperahouse.com/visit-us/tours-and-experiences.html',
            'source': 'Eventbrite'
        },
        {
            'title': 'Bondi Beach Festival',
            'date_time': (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S'),
            'location': 'Bondi Beach, Sydney NSW 2026',
            'description': 'Join us for a day of music, food, and fun at the annual Bondi Beach Festival. Activities for all ages.',
            'ticket_link': 'https://www.bondifestival.com.au',
            'source': 'Eventbrite'
        },
        {
            'title': 'Sydney Harbour Bridge Climb',
            'date_time': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S'),
            'location': 'Sydney Harbour Bridge, Sydney NSW 2000',
            'description': 'Climb to the summit of the Sydney Harbour Bridge for panoramic views of the city and harbor.',
            'ticket_link': 'https://www.bridgeclimb.com',
            'source': 'TimeOut Sydney'
        },
        {
            'title': 'Tech Meetup: AI and Machine Learning',
            'date_time': (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S'),
            'location': 'Sydney Startup Hub, 11 York St, Sydney NSW 2000',
            'description': 'Join tech enthusiasts for an evening of discussions about the latest in AI and machine learning technologies.',
            'ticket_link': 'https://www.meetup.com/sydney-tech',
            'source': 'Meetup'
        },
        {
            'title': 'Sydney Food and Wine Festival',
            'date_time': (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d %H:%M:%S'),
            'location': 'The Rocks, Sydney NSW 2000',
            'description': 'Experience the best of Sydney\'s culinary scene with food stalls, wine tastings, and cooking demonstrations.',
            'ticket_link': 'https://www.sydneyfoodandwine.com.au',
            'source': 'TimeOut Sydney'
        },
        {
            'title': 'Startup Networking Event',
            'date_time': (datetime.now() + timedelta(days=4)).strftime('%Y-%m-%d %H:%M:%S'),
            'location': 'Fishburners, 11 York St, Sydney NSW 2000',
            'description': 'Network with fellow entrepreneurs and investors in Sydney\'s startup ecosystem.',
            'ticket_link': 'https://www.meetup.com/sydney-startups',
            'source': 'Meetup'
        }
    ]
    
    # Save events to database
    saved_count = 0
    for event in sample_events:
        try:
            db_manager.save_event(event)
            saved_count += 1
        except Exception as e:
            print(f"Error saving event: {e}")
            continue
            
    print(f"Successfully added {saved_count} sample events to the database")
    
    return saved_count

if __name__ == "__main__":
    add_sample_events() 