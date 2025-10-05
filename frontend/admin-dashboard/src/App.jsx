import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/common/Layout/Layout';
import DashboardPage from './pages/Dashboard/DashboardPage';
import UserListPage from './pages/Users/UserListPage';
import ExamListPage from './pages/Exams/ExamListPage';
import './App.css';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<DashboardPage />} />
          <Route path="/users" element={<UserListPage />} />
          <Route path="/exams" element={<ExamListPage />} />
          {/* Add other admin routes here */}
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;