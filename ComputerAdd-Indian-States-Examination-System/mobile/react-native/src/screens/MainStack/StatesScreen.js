import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  FlatList,
  TouchableOpacity,
  StyleSheet,
  Image,
} from 'react-native';
import { indianStates } from '../../utils/statesData';

const StatesScreen = ({ navigation }) => {
  const [states, setStates] = useState([]);

  useEffect(() => {
    setStates(indianStates);
  }, []);

  const renderState = ({ item }) => (
    <TouchableOpacity
      style={styles.stateCard}
      onPress={() => navigation.navigate('StateDetail', { state: item })}>
      
      <Image
        source={{ uri: item.imageUrl || 'https://via.placeholder.com/60' }}
        style={styles.stateImage}
      />
      
      <View style={styles.stateInfo}>
        <Text style={styles.stateName}>{item.name}</Text>
        <Text style={styles.stateCapital}>Capital: {item.capital}</Text>
        <Text style={styles.statePopulation}>
          Population: {(item.population / 1000000).toFixed(1)}M
        </Text>
      </View>
      
      <Icon name="chevron-forward" size={20} color="#ccc" />
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Indian States & UTs</Text>
      
      <FlatList
        data={states}
        renderItem={renderState}
        keyExtractor={item => item.name}
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
  header: {
    fontSize: 24,
    fontWeight: 'bold',
    padding: 20,
    backgroundColor: '#fff',
  },
  list: {
    padding: 10,
  },
  stateCard: {
    flexDirection: 'row',
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 15,
    marginBottom: 10,
    alignItems: 'center',
    elevation: 2,
  },
  stateImage: {
    width: 60,
    height: 60,
    borderRadius: 8,
    marginRight: 15,
  },
  stateInfo: {
    flex: 1,
  },
  stateName: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
  },
  stateCapital: {
    fontSize: 12,
    color: '#666',
    marginTop: 4,
  },
  statePopulation: {
    fontSize: 12,
    color: '#888',
    marginTop: 2,
  },
});

export default StatesScreen;
