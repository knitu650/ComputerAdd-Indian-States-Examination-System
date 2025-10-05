import React from 'react';
import styles from './UserList.module.css';

const UserList = ({ users }) => {
  return (
    <div className={styles.userListContainer}>
      <table className={styles.userTable}>
        <thead>
          <tr>
            <th>Username</th>
            <th>Email</th>
            <th>Role</th>
            <th>Joined Date</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td>{user.username}</td>
              <td>{user.email}</td>
              <td><span className={`${styles.role} ${styles[user.role]}`}>{user.role}</span></td>
              <td>{user.joined}</td>
              <td>
                <button className={styles.actionButton}>Edit</button>
                <button className={`${styles.actionButton} ${styles.deleteButton}`}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default UserList;