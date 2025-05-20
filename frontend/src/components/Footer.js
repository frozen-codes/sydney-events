import React from 'react';
import './Footer.css';

const Footer = () => {
  const currentYear = new Date().getFullYear();
  
  return (
    <footer className="footer">
      <div className="container">
        <p>&copy; {currentYear} Sydney Events</p>
        <p className="disclaimer">
          Event information is scraped from public sources. We are not affiliated with event organizers.
        </p>
        <div className="sources">
          <p>Data sources:</p>
          <ul>
            <li><a href="https://www.eventbrite.com.au/d/australia--sydney/events/" target="_blank" rel="noopener noreferrer">Eventbrite</a></li>
            <li><a href="https://www.timeout.com/sydney/things-to-do" target="_blank" rel="noopener noreferrer">TimeOut Sydney</a></li>
            <li><a href="https://www.meetup.com/find/?location=au--sydney" target="_blank" rel="noopener noreferrer">Meetup</a></li>
          </ul>
        </div>
      </div>
    </footer>
  );
};

export default Footer; 