import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Icon from 'react-native-vector-icons/Ionicons';
import HomeScreen from '../screens/MainStack/HomeScreen';
import DashboardScreen from '../screens/MainStack/DashboardScreen';
import ExamScreen from '../screens/MainStack/ExamScreen';
import StatesScreen from '../screens/MainStack/StatesScreen';
import ProfileScreen from '../screens/MainStack/ProfileScreen';

const Tab = createBottomTabNavigator();

const TabNavigator = () => {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ focused, color, size }) => {
          let iconName;

          switch (route.name) {
            case 'Home':
              iconName = focused ? 'home' : 'home-outline';
              break;
            case 'Dashboard':
              iconName = focused ? 'stats-chart' : 'stats-chart-outline';
              break;
            case 'Exams':
              iconName = focused ? 'document-text' : 'document-text-outline';
              break;
            case 'States':
              iconName = focused ? 'map' : 'map-outline';
              break;
            case 'Profile':
              iconName = focused ? 'person' : 'person-outline';
              break;
          }

          return <Icon name={iconName} size={size} color={color} />;
        },
        tabBarActiveTintColor: '#667eea',
        tabBarInactiveTintColor: 'gray',
      })}>
      
      <Tab.Screen name="Home" component={HomeScreen} />
      <Tab.Screen name="Dashboard" component={DashboardScreen} />
      <Tab.Screen name="Exams" component={ExamScreen} />
      <Tab.Screen name="States" component={StatesScreen} />
      <Tab.Screen name="Profile" component={ProfileScreen} />
    </Tab.Navigator>
  );
};

export default TabNavigator;
