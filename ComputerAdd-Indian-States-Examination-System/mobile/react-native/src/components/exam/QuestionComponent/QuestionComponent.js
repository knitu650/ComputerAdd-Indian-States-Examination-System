import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Image } from 'react-native';

const QuestionComponent = ({ question, selectedAnswer, onAnswerSelect }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.questionNumber}>
        Question {question.number} of {question.total}
      </Text>
      
      <Text style={styles.questionText}>{question.questionText}</Text>

      {question.imageUrl && (
        <Image source={{ uri: question.imageUrl }} style={styles.image} />
      )}

      <View style={styles.options}>
        {question.options.map((option, index) => (
          <TouchableOpacity
            key={index}
            style={[
              styles.option,
              selectedAnswer === option.text && styles.selectedOption
            ]}
            onPress={() => onAnswerSelect(option.text)}>
            <View style={styles.optionCircle}>
              {selectedAnswer === option.text && (
                <View style={styles.selectedCircle} />
              )}
            </View>
            <Text style={styles.optionText}>{option.text}</Text>
          </TouchableOpacity>
        ))}
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 20,
  },
  questionNumber: {
    fontSize: 14,
    color: '#888',
    marginBottom: 10,
  },
  questionText: {
    fontSize: 18,
    fontWeight: '500',
    color: '#333',
    marginBottom: 20,
  },
  image: {
    width: '100%',
    height: 200,
    borderRadius: 10,
    marginBottom: 20,
  },
  options: {
    marginTop: 10,
  },
  option: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 15,
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 8,
    marginBottom: 10,
  },
  selectedOption: {
    borderColor: '#667eea',
    backgroundColor: '#f0f4ff',
  },
  optionCircle: {
    width: 24,
    height: 24,
    borderRadius: 12,
    borderWidth: 2,
    borderColor: '#ddd',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 12,
  },
  selectedCircle: {
    width: 12,
    height: 12,
    borderRadius: 6,
    backgroundColor: '#667eea',
  },
  optionText: {
    flex: 1,
    fontSize: 16,
    color: '#333',
  },
});

export default QuestionComponent;
