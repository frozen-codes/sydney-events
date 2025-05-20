# Sydney Events

A web application that automatically scrapes and displays events happening in Sydney, Australia.

## Features

- **Event Scraping**: Automatically scrapes events from popular Sydney event sites:
  - Eventbrite Sydney
  - TimeOut Sydney
  - Meetup Sydney
  
- **Minimalist Frontend**: Clean, responsive interface to browse events
  - Search and filter functionality
  - Event cards with key information
  
- **Email Capture**: Collects user emails before redirecting to ticket pages
  
- **Automated Updates**: Scheduled scraping to keep event data fresh

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: React
- **Database**: SQLite
- **Scraping**: BeautifulSoup, Requests
- **Scheduling**: APScheduler

## Setup and Installation

### Prerequisites
- Python 3.8+
- Node.js and npm

### Backend Setup
1. Navigate to the backend directory:
   ```
   cd sydney_events/backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Initialize the database:
   ```
   python database/schema.py
   ```

6. Run the Flask app:
   ```
   python app.py
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```
   cd sydney_events/frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm start
   ```

4. For production build:
   ```
   npm run build
   ```

## Deployment

The application can be deployed on platforms like:
- Render
- Vercel
- Heroku

## License

This project is open source and available under the MIT License.

## Acknowledgements

- Data is sourced from public event websites
- This application is for educational purposes only 