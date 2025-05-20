import React, { useState } from 'react';
import EventCard from './EventCard';
import './EventList.css';

const EventList = ({ events, onGetTickets }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [filter, setFilter] = useState('all');
  
  // Filter events based on search term and source filter
  const filteredEvents = events.filter(event => {
    const matchesSearch = event.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         event.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         event.location.toLowerCase().includes(searchTerm.toLowerCase());
                         
    const matchesFilter = filter === 'all' || event.source.toLowerCase().includes(filter.toLowerCase());
    
    return matchesSearch && matchesFilter;
  });
  
  return (
    <div className="event-list-container">
      <div className="filters">
        <input
          type="text"
          placeholder="Search events..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="search-input"
        />
        
        <div className="filter-buttons">
          <button 
            className={filter === 'all' ? 'active' : ''} 
            onClick={() => setFilter('all')}
          >
            All
          </button>
          <button 
            className={filter === 'eventbrite' ? 'active' : ''} 
            onClick={() => setFilter('eventbrite')}
          >
            Eventbrite
          </button>
          <button 
            className={filter === 'timeout' ? 'active' : ''} 
            onClick={() => setFilter('timeout')}
          >
            TimeOut
          </button>
          <button 
            className={filter === 'meetup' ? 'active' : ''} 
            onClick={() => setFilter('meetup')}
          >
            Meetup
          </button>
        </div>
      </div>
      
      <div className="event-grid">
        {filteredEvents.length > 0 ? (
          filteredEvents.map(event => (
            <EventCard 
              key={event.id} 
              event={event} 
              onGetTickets={onGetTickets} 
            />
          ))
        ) : (
          <div className="no-events">No events found matching your criteria.</div>
        )}
      </div>
    </div>
  );
};

export default EventList; 