import React from 'react';
import UserList from '../../components/user-management/UserList/UserList';
import styles from './UserListPage.module.css';

const UserListPage = () => {
  // Placeholder data for users
  const users = [
    { id: 'u1', username: 'student1', email: 'student1@example.com', role: 'student', joined: '2023-10-01' },
    { id: 'u2', username: 'student2', email: 'student2@example.com', role: 'student', joined: '2023-10-05' },
    { id: 'u3', username: 'admin1', email: 'admin1@example.com', role: 'admin', joined: '2023-09-15' },
  ];

  return (
    <div className={styles.userPage}>
      <h1>User Management</h1>
      <UserList users={users} />
    </div>
  );
};

export default UserListPage;