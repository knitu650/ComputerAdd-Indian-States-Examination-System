import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Header from './components/common/Header/Header';
import Home from './pages/Home/Home';
import Login from './pages/Auth/Login/Login';
import ExamInterface from './components/examination/ExamInterface/ExamInterface';
import './App.css';

function App() {
  return (
    <div className="App">
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/exam/:examId" element={<ExamInterface />} />
      </Routes>
    </div>
  );
}

export default App;
