// App.js
import React, { useState } from 'react';
import './App.css';

function App() {
  const [profileName, setProfileName] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null); // Reset any previous error
    setMessage(null); // Reset any previous message

    const payload = {
      profile_name: profileName,
      username,
      password
    };

    try {
      const response = await fetch('http://localhost:5000/linkedin/get_person', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      const result = await response.json();

      if (result.success) {
        setMessage(result.data);
      } else {
        setError('Failed to fetch connection message');
      }
    } catch (err) {
      setError('Error connecting to LinkedIn API. Please try again.');
    }
  };

  return (
    <div className="App">
      <h1>LinkedIn Connection Message Fetcher</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Profile Name:
          <input
            type="text"
            value={profileName}
            onChange={(e) => setProfileName(e.target.value)}
            required
          />
        </label>
        <label>
          Username:
          <input
            type="email"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </label>
        <label>
          Password:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        <button type="submit">Get Connection Message</button>
      </form>
      {message && <div className="success-message">Message: {message}</div>}
      {error && <div className="error-message">Error: {error}</div>}
    </div>
  );
}

export default App;
