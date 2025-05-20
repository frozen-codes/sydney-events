import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import EventList from './components/EventList';
import EventModal from './components/EventModal';
import Header from './components/Header';
import Footer from './components/Footer';

function App() {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedEvent, setSelectedEvent] = useState(null);
  const [showModal, setShowModal] = useState(false);
  
  useEffect(() => {
    // Fetch events from API
    const fetchEvents = async () => {
      try {
        setLoading(true);
        const response = await axios.get('/api/events');
        setEvents(response.data);
        setLoading(false);
      } catch (err) {
        setError('Failed to fetch events. Please try again later.');
        setLoading(false);
        console.error('Error fetching events:', err);
      }
    };
    
    fetchEvents();
  }, []);
  
  const handleGetTickets = (event) => {
    setSelectedEvent(event);
    setShowModal(true);
  };
  
  const handleCloseModal = () => {
    setShowModal(false);
    setSelectedEvent(null);
  };
  
  const handleSubmitEmail = async (email) => {
    if (!selectedEvent || !email) return;
    
    try {
      await axios.post('/api/track-email', {
        email: email,
        event_id: selectedEvent.id
      });
      
      // Redirect to ticket link
      window.open(selectedEvent.ticket_link, '_blank');
      handleCloseModal();
    } catch (err) {
      console.error('Error tracking email:', err);
      // Still redirect to ticket link even if tracking fails
      window.open(selectedEvent.ticket_link, '_blank');
      handleCloseModal();
    }
  };
  
  return (
    <div className="app">
      <Header />
      
      <main className="container">
        {loading ? (
          <div className="loading">Loading events...</div>
        ) : error ? (
          <div className="error">{error}</div>
        ) : (
          <EventList events={events} onGetTickets={handleGetTickets} />
        )}
      </main>
      
      {showModal && selectedEvent && (
        <EventModal 
          event={selectedEvent}
          onClose={handleCloseModal}
          onSubmit={handleSubmitEmail}
        />
      )}
      
      <Footer />
    </div>
  );
}

export default App; 