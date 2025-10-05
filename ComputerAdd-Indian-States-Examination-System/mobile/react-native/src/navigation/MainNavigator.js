import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Icon from 'react-native-vector-icons/Ionicons';
import DashboardScreen from '../screens/MainStack/DashboardScreen';
import ExamScreen from '../screens/MainStack/ExamScreen';
import StatesScreen from '../screens/MainStack/StatesScreen';
import ProfileScreen from '../screens/MainStack/ProfileScreen';

const Tab = createBottomTabNavigator();

const MainNavigator = () => {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ focused, color, size }) => {
          let iconName;

          if (route.name === 'Dashboard') {
            iconName = focused ? 'home' : 'home-outline';
          } else if (route.name === 'Exams') {
            iconName = focused ? 'document-text' : 'document-text-outline';
          } else if (route.name === 'States') {
            iconName = focused ? 'map' : 'map-outline';
          } else if (route.name === 'Profile') {
            iconName = focused ? 'person' : 'person-outline';
          }

          return <Icon name={iconName} size={size} color={color} />;
        },
        tabBarActiveTintColor: '#667eea',
        tabBarInactiveTintColor: 'gray',
      })}>
      
      <Tab.Screen name="Dashboard" component={DashboardScreen} />
      <Tab.Screen name="Exams" component={ExamScreen} />
      <Tab.Screen name="States" component={StatesScreen} />
      <Tab.Screen name="Profile" component={ProfileScreen} />
    </Tab.Navigator>
  );
};

export default MainNavigator;
