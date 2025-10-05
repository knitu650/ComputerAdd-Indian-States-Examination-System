import React, { useState, useEffect } from 'react';
import { View, Text, Button, StyleSheet, FlatList } from 'react-native';

const questions = [
  { id: '1', text: 'What is the capital of Maharashtra?' },
  { id: '2', text: 'Which state is known as the "Land of Five Rivers"?' },
  { id: '3', text: 'What is the largest state in India by area?' },
];

const ExamScreen = ({ navigation }) => {
  const [answers, setAnswers] = useState({});

  const handleSelectAnswer = (questionId, option) => {
    setAnswers({ ...answers, [questionId]: option });
  };

  const handleSubmit = () => {
    // Navigate to the Results screen, passing the answers
    navigation.navigate('Results', { answers });
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Indian States Examination</Text>
      <FlatList
        data={questions}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={styles.questionContainer}>
            <Text style={styles.questionText}>{item.text}</Text>
            {/* Placeholder for answer options */}
            <Button title="Option A" onPress={() => handleSelectAnswer(item.id, 'A')} />
            <Button title="Option B" onPress={() => handleSelectAnswer(item.id, 'B')} />
          </View>
        )}
      />
      <Button title="Submit Exam" onPress={handleSubmit} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  questionContainer: {
    marginBottom: 20,
  },
  questionText: {
    fontSize: 18,
    marginBottom: 10,
  },
});

export default ExamScreen;