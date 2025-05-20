import React from 'react';
import './EventCard.css';

const EventCard = ({ event, onGetTickets }) => {
  // Format date for display if it's not the default message
  const formatDate = (dateString) => {
    if (dateString === "Check website for dates" || 
        dateString === "Check website for dates and times") {
      return dateString;
    }
    
    try {
      // Try to parse and format the date if it's in a standard format
      const date = new Date(dateString);
      if (!isNaN(date.getTime())) {
        return date.toLocaleDateString('en-AU', {
          weekday: 'short',
          day: 'numeric',
          month: 'short',
          year: 'numeric',
          hour: '2-digit',
          minute: '2-digit'
        });
      }
      return dateString;
    } catch (e) {
      return dateString;
    }
  };
  
  // Get source icon
  const getSourceIcon = (source) => {
    const lowerSource = source.toLowerCase();
    if (lowerSource.includes('eventbrite')) {
      return '🎟️';
    } else if (lowerSource.includes('timeout')) {
      return '⏰';
    } else if (lowerSource.includes('meetup')) {
      return '👥';
    }
    return '📅';
  };
  
  return (
    <div className="event-card">
      <div className="event-source">
        <span className="source-icon">{getSourceIcon(event.source)}</span>
        <span className="source-text">{event.source}</span>
      </div>
      
      <h3 className="event-title">{event.title}</h3>
      
      <div className="event-datetime">
        <span className="icon">🗓️</span>
        <span>{formatDate(event.date_time)}</span>
      </div>
      
      <div className="event-location">
        <span className="icon">📍</span>
        <span>{event.location}</span>
      </div>
      
      <p className="event-description">{event.description}</p>
      
      <button 
        className="get-tickets-btn"
        onClick={() => onGetTickets(event)}
      >
        GET TICKETS
      </button>
    </div>
  );
};

export default EventCard; 