import React, { useState } from 'react';
import './EventModal.css';

const EventModal = ({ event, onClose, onSubmit }) => {
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');
  
  const validateEmail = (email) => {
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(email.toLowerCase());
  };
  
  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!email) {
      setError('Please enter your email address');
      return;
    }
    
    if (!validateEmail(email)) {
      setError('Please enter a valid email address');
      return;
    }
    
    setError('');
    onSubmit(email);
  };
  
  return (
    <div className="modal-overlay">
      <div className="modal">
        <button className="close-btn" onClick={onClose}>&times;</button>
        
        <h2>Almost there!</h2>
        <p>Enter your email to continue to the event page:</p>
        
        <h3>{event.title}</h3>
        
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <input
              type="email"
              placeholder="Your email address"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className={error ? 'error' : ''}
            />
            {error && <div className="error-message">{error}</div>}
          </div>
          
          <div className="form-actions">
            <button type="button" className="cancel-btn" onClick={onClose}>
              Cancel
            </button>
            <button type="submit" className="submit-btn">
              Continue to Event
            </button>
          </div>
          
          <p className="privacy-note">
            We'll only use your email to share updates about similar events.
          </p>
        </form>
      </div>
    </div>
  );
};

export default EventModal; 