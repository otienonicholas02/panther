import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1>🐆 Panther Logistics</h1>
          <p>Kenya's Premier Logistics Platform</p>
        </header>
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </div>
    </Router>
  );
}

function Home() {
  return (
    <main>
      <section className="hero">
        <h2>Welcome to Panther Logistics</h2>
        <p>Fast, Reliable, and Secure Logistics Solutions for Kenya</p>
        <button className="cta-button">Get Started</button>
      </section>
    </main>
  );
}

export default App;