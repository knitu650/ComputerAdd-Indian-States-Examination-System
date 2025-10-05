import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  FlatList,
  TouchableOpacity,
  StyleSheet,
} from 'react-native';
import { examApi } from '../../services/api/examApi';

const ExamScreen = ({ navigation }) => {
  const [exams, setExams] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadExams();
  }, []);

  const loadExams = async () => {
    try {
      const response = await examApi.getAllExams();
      setExams(response.data);
    } catch (error) {
      console.error('Failed to load exams', error);
    } finally {
      setLoading(false);
    }
  };

  const renderExam = ({ item }) => (
    <TouchableOpacity
      style={styles.examCard}
      onPress={() => navigation.navigate('ExamDetails', { examId: item.id })}>
      
      <Text style={styles.examTitle}>{item.title}</Text>
      <Text style={styles.examDescription}>{item.description}</Text>
      
      <View style={styles.examInfo}>
        <Text style={styles.infoText}>⏱️ {item.duration} min</Text>
        <Text style={styles.infoText}>📝 {item.totalQuestions} questions</Text>
        <Text style={styles.infoText}>🏆 {item.totalMarks} marks</Text>
      </View>
      
      <View style={styles.difficultyBadge}>
        <Text style={styles.difficultyText}>{item.difficulty}</Text>
      </View>
    </TouchableOpacity>
  );

  if (loading) {
    return (
      <View style={styles.centerContainer}>
        <Text>Loading exams...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <FlatList
        data={exams}
        renderItem={renderExam}
        keyExtractor={item => item.id}
        contentContainerStyle={styles.list}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  centerContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  list: {
    padding: 15,
  },
  examCard: {
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 20,
    marginBottom: 15,
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  examTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 10,
  },
  examDescription: {
    fontSize: 14,
    color: '#666',
    marginBottom: 15,
  },
  examInfo: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 10,
  },
  infoText: {
    fontSize: 12,
    color: '#888',
  },
  difficultyBadge: {
    alignSelf: 'flex-start',
    backgroundColor: '#667eea',
    paddingHorizontal: 12,
    paddingVertical: 4,
    borderRadius: 12,
  },
  difficultyText: {
    color: '#fff',
    fontSize: 12,
    textTransform: 'capitalize',
  },
});

export default ExamScreen;
