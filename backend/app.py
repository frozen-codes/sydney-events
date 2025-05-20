import os
import json
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
import re

from database.schema import init_db
from database.db_manager import DatabaseManager
from scrapers.scraper_manager import ScraperManager

app = Flask(__name__, static_folder='../frontend/build')
CORS(app)  # Enable CORS for all routes

# Initialize database
init_db()
db_manager = DatabaseManager()

# Email validation regex
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

@app.route('/api/events', methods=['GET'])
def get_events():
    """Get all events from the database"""
    events = db_manager.get_all_events()
    return jsonify(events)

@app.route('/api/track-email', methods=['POST'])
def track_email():
    """Track user email when they click on an event"""
    data = request.json
    
    if not data or 'email' not in data or 'event_id' not in data:
        return jsonify({'error': 'Missing email or event_id'}), 400
        
    email = data['email']
    event_id = data['event_id']
    
    # Validate email
    if not EMAIL_REGEX.match(email):
        return jsonify({'error': 'Invalid email format'}), 400
        
    try:
        db_manager.save_email(email, event_id)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    """Serve the frontend React app"""
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

def run_scrapers():
    """Run all scrapers on schedule"""
    scraper_manager = ScraperManager()
    scraper_manager.run_all_scrapers()

# Set up scheduler to run scrapers every 6 hours
scheduler = BackgroundScheduler()
scheduler.add_job(func=run_scrapers, trigger="interval", hours=6)

if __name__ == "__main__":
    # Start the scheduler
    scheduler.start()
    
    # Run initial scrape
    run_scrapers()
    
    # Start the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True) 