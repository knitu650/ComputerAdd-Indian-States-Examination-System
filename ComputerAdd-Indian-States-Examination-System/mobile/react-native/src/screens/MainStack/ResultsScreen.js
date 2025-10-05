import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

const ResultsScreen = ({ route, navigation }) => {
  const { answers } = route.params;
  const score = Object.values(answers).filter(answer => answer === 'A').length; // Dummy scoring

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Exam Results</Text>
      <Text style={styles.scoreText}>Your Score: {score} / 3</Text>
      <Button title="Try Again" onPress={() => navigation.navigate('Exam')} />
      <Button title="Logout" onPress={() => navigation.navigate('Login')} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  scoreText: {
    fontSize: 20,
    marginBottom: 20,
  },
});

export default ResultsScreen;