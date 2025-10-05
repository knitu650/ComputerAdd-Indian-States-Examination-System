import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const ProgressCard = ({ stats }) => {
  return (
    <View style={styles.card}>
      <Text style={styles.title}>Your Progress</Text>
      
      <View style={styles.statsRow}>
        <View style={styles.stat}>
          <Text style={styles.statValue}>{stats?.totalExams || 0}</Text>
          <Text style={styles.statLabel}>Exams Taken</Text>
        </View>
        
        <View style={styles.stat}>
          <Text style={styles.statValue}>{stats?.averageScore || 0}%</Text>
          <Text style={styles.statLabel}>Average Score</Text>
        </View>
        
        <View style={styles.stat}>
          <Text style={styles.statValue}>{stats?.rank || '-'}</Text>
          <Text style={styles.statLabel}>Rank</Text>
        </View>
      </View>

      <View style={styles.progressBar}>
        <View style={[styles.progressFill, { width: `${stats?.averageScore || 0}%` }]} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#fff',
    margin: 15,
    padding: 20,
    borderRadius: 10,
    elevation: 3,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 15,
  },
  statsRow: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginBottom: 20,
  },
  stat: {
    alignItems: 'center',
  },
  statValue: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#667eea',
  },
  statLabel: {
    fontSize: 12,
    color: '#888',
    marginTop: 5,
  },
  progressBar: {
    height: 8,
    backgroundColor: '#f0f0f0',
    borderRadius: 4,
    overflow: 'hidden',
  },
  progressFill: {
    height: '100%',
    backgroundColor: '#667eea',
  },
});

export default ProgressCard;
