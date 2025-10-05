#!/usr/bin/env python3
"""Generate Android Layouts and Remaining React Native Files"""

import os

BASE_DIR = "/workspace/ComputerAdd-Indian-States-Examination-System"

def create_file(filepath, content):
    full_path = os.path.join(BASE_DIR, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ {filepath}")

LAYOUT_AND_RN_FILES = {
    # Android Layouts
    "mobile/android/app/src/main/res/layout/activity_exam.xml": '''<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/questions_recycler_view"
        android:layout_width="0dp"
        android:layout_height="0dp"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintBottom_toTopOf="@+id/submit_button"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent" />

    <Button
        android:id="@+id/submit_button"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:text="Submit Exam"
        android:layout_margin="16dp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
''',

    "mobile/android/app/src/main/res/layout/fragment_dashboard.xml": '''<?xml version="1.0" encoding="utf-8"?>
<ScrollView
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <TextView
            android:id="@+id/welcome_text"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Welcome back!"
            android:textSize="24sp"
            android:textStyle="bold"
            android:layout_marginBottom="16dp" />

        <TextView
            android:id="@+id/stats_text"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Loading stats..."
            android:textSize="16sp" />

    </LinearLayout>

</ScrollView>
''',

    "mobile/android/app/src/main/res/layout/fragment_exam.xml": '''<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/exams_recycler_view"
        android:layout_width="0dp"
        android:layout_height="0dp"
        android:padding="8dp"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
''',

    "mobile/android/app/src/main/res/layout/fragment_states.xml": '''<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/states_recycler_view"
        android:layout_width="0dp"
        android:layout_height="0dp"
        android:padding="8dp"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
''',

    "mobile/android/app/src/main/res/values/colors.xml": '''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="primary">#667EEA</color>
    <color name="primary_dark">#5568D3</color>
    <color name="accent">#764BA2</color>
    <color name="success">#48BB78</color>
    <color name="error">#F56565</color>
    <color name="warning">#ED8936</color>
    <color name="background">#F7FAFC</color>
    <color name="surface">#FFFFFF</color>
    <color name="text_primary">#2D3748</color>
    <color name="text_secondary">#718096</color>
</resources>
''',

    "mobile/android/app/src/main/res/values/styles.xml": '''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="AppTheme" parent="Theme.MaterialComponents.DayNight.DarkActionBar">
        <item name="colorPrimary">@color/primary</item>
        <item name="colorPrimaryDark">@color/primary_dark</item>
        <item name="colorAccent">@color/accent</item>
    </style>

    <style name="Button.Primary" parent="Widget.MaterialComponents.Button">
        <item name="backgroundTint">@color/primary</item>
        <item name="android:textColor">@android:color/white</item>
    </style>

    <style name="TextInput" parent="Widget.MaterialComponents.TextInputLayout.OutlinedBox">
        <item name="boxStrokeColor">@color/primary</item>
    </style>
</resources>
''',

    "mobile/android/app/src/main/res/values/themes.xml": '''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="Theme.IndianStatesExam" parent="Theme.MaterialComponents.DayNight.DarkActionBar">
        <item name="colorPrimary">@color/primary</item>
        <item name="colorPrimaryVariant">@color/primary_dark</item>
        <item name="colorOnPrimary">@android:color/white</item>
        <item name="colorSecondary">@color/accent</item>
        <item name="colorSecondaryVariant">@color/accent</item>
        <item name="colorOnSecondary">@android:color/white</item>
        <item name="android:statusBarColor">?attr/colorPrimaryVariant</item>
    </style>
</resources>
''',

    "mobile/android/app/src/main/res/raw/state_data.json": '''{
  "states": [
    {
      "name": "Andhra Pradesh",
      "capital": "Amaravati",
      "population": 49386799,
      "area": 160205,
      "language": "Telugu"
    },
    {
      "name": "Karnataka",
      "capital": "Bengaluru",
      "population": 61095297,
      "area": 191791,
      "language": "Kannada"
    },
    {
      "name": "Tamil Nadu",
      "capital": "Chennai",
      "population": 72138958,
      "area": 130060,
      "language": "Tamil"
    }
  ]
}
''',

    "mobile/android/app/build.gradle": '''apply plugin: 'com.android.application'
apply plugin: 'kotlin-android'

android {
    compileSdkVersion 33
    
    defaultConfig {
        applicationId "com.computeradd.indianstates"
        minSdkVersion 24
        targetSdkVersion 33
        versionCode 1
        versionName "1.0"
    }
    
    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
    
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.4'
    implementation 'com.google.android.material:material:1.9.0'
    implementation 'androidx.recyclerview:recyclerview:1.3.1'
    implementation 'androidx.cardview:cardview:1.0.0'
    
    // Biometric
    implementation 'androidx.biometric:biometric:1.1.0'
    
    // Camera
    implementation 'androidx.camera:camera-camera2:1.2.3'
    implementation 'androidx.camera:camera-lifecycle:1.2.3'
    implementation 'androidx.camera:camera-view:1.2.3'
    
    // Network
    implementation 'com.squareup.okhttp3:okhttp:4.11.0'
    implementation 'com.squareup.retrofit2:retrofit:2.9.0'
    implementation 'com.squareup.retrofit2:converter-gson:2.9.0'
    
    // Image Loading
    implementation 'com.github.bumptech.glide:glide:4.15.1'
}
''',

    "mobile/android/app/proguard-rules.pro": '''# Add project specific ProGuard rules here.
-keepattributes *Annotation*
-keepclassмembers class * {
    @android.webkit.JavascriptInterface <methods>;
}
-keep class com.computeradd.indianstates.models.** { *; }
''',

    "mobile/android/settings.gradle": '''rootProject.name = "IndianStatesExam"
include ':app'
''',

    "mobile/android/gradle.properties": '''org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
android.useAndroidX=true
android.enableJetifier=true
''',

    # React Native Additional Files
    "mobile/react-native/src/screens/AuthStack/SplashScreen.js": '''import React, { useEffect } from 'react';
import { View, Text, StyleSheet, ActivityIndicator } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useAuth } from '../../hooks/useAuth';

const SplashScreen = ({ navigation }) => {
  const { setUser } = useAuth();

  useEffect(() => {
    checkAuth();
  }, []);

  const checkAuth = async () => {
    try {
      const token = await AsyncStorage.getItem('authToken');
      
      if (token) {
        // TODO: Validate token with API
        navigation.replace('Main');
      } else {
        navigation.replace('Login');
      }
    } catch (error) {
      navigation.replace('Login');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Indian States Exam</Text>
      <ActivityIndicator size="large" color="#667eea" />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 30,
    color: '#667eea',
  },
});

export default SplashScreen;
''',

    "mobile/react-native/src/screens/MainStack/HomeScreen.js": '''import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
} from 'react-native';

const HomeScreen = ({ navigation }) => {
  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Welcome to</Text>
        <Text style={styles.subtitle}>Indian States Examination System</Text>
      </View>

      <View style={styles.content}>
        <TouchableOpacity
          style={styles.card}
          onPress={() => navigation.navigate('Exams')}>
          <Text style={styles.cardIcon}>📝</Text>
          <Text style={styles.cardTitle}>Take Exams</Text>
          <Text style={styles.cardDescription}>
            Test your knowledge about Indian states
          </Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.card}
          onPress={() => navigation.navigate('States')}>
          <Text style={styles.cardIcon}>🗺️</Text>
          <Text style={styles.cardTitle}>Explore States</Text>
          <Text style={styles.cardDescription}>
            Learn about 28 states and 8 UTs
          </Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.card}
          onPress={() => navigation.navigate('Dashboard')}>
          <Text style={styles.cardIcon}>📊</Text>
          <Text style={styles.cardTitle}>Your Progress</Text>
          <Text style={styles.cardDescription}>
            Track your exam performance
          </Text>
        </TouchableOpacity>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    padding: 30,
    backgroundColor: '#667eea',
  },
  title: {
    fontSize: 18,
    color: '#fff',
    opacity: 0.9,
  },
  subtitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#fff',
    marginTop: 5,
  },
  content: {
    padding: 15,
  },
  card: {
    backgroundColor: '#fff',
    borderRadius: 12,
    padding: 20,
    marginBottom: 15,
    elevation: 3,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  cardIcon: {
    fontSize: 40,
    marginBottom: 10,
  },
  cardTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 8,
  },
  cardDescription: {
    fontSize: 14,
    color: '#666',
  },
});

export default HomeScreen;
''',

    "mobile/react-native/src/screens/MainStack/SettingsScreen.js": '''import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  Switch,
  TouchableOpacity,
  ScrollView,
} from 'react-native';

const SettingsScreen = () => {
  const [notifications, setNotifications] = useState(true);
  const [darkMode, setDarkMode] = useState(false);
  const [biometric, setBiometric] = useState(true);

  const settingsOptions = [
    {
      title: 'Notifications',
      value: notifications,
      onValueChange: setNotifications,
    },
    {
      title: 'Dark Mode',
      value: darkMode,
      onValueChange: setDarkMode,
    },
    {
      title: 'Biometric Login',
      value: biometric,
      onValueChange: setBiometric,
    },
  ];

  return (
    <ScrollView style={styles.container}>
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Preferences</Text>
        
        {settingsOptions.map((option, index) => (
          <View key={index} style={styles.settingItem}>
            <Text style={styles.settingLabel}>{option.title}</Text>
            <Switch
              value={option.value}
              onValueChange={option.onValueChange}
              trackColor={{ false: '#ccc', true: '#667eea' }}
            />
          </View>
        ))}
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Account</Text>
        
        <TouchableOpacity style={styles.menuItem}>
          <Text style={styles.menuText}>Change Password</Text>
        </TouchableOpacity>
        
        <TouchableOpacity style={styles.menuItem}>
          <Text style={styles.menuText}>Privacy Settings</Text>
        </TouchableOpacity>
        
        <TouchableOpacity style={styles.menuItem}>
          <Text style={styles.menuText}>Delete Account</Text>
        </TouchableOpacity>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>About</Text>
        
        <View style={styles.menuItem}>
          <Text style={styles.menuText}>Version</Text>
          <Text style={styles.menuValue}>1.0.0</Text>
        </View>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  section: {
    backgroundColor: '#fff',
    marginTop: 10,
    paddingVertical: 8,
  },
  sectionTitle: {
    fontSize: 14,
    fontWeight: '600',
    color: '#888',
    paddingHorizontal: 20,
    paddingVertical: 8,
  },
  settingItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#f0f0f0',
  },
  settingLabel: {
    fontSize: 16,
    color: '#333',
  },
  menuItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingVertical: 15,
    borderBottomWidth: 1,
    borderBottomColor: '#f0f0f0',
  },
  menuText: {
    fontSize: 16,
    color: '#333',
  },
  menuValue: {
    fontSize: 16,
    color: '#888',
  },
});

export default SettingsScreen;
''',

    "mobile/react-native/src/navigation/AuthNavigator.js": '''import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import LoginScreen from '../screens/AuthStack/LoginScreen';
import RegisterScreen from '../screens/AuthStack/RegisterScreen';
import SplashScreen from '../screens/AuthStack/SplashScreen';

const Stack = createNativeStackNavigator();

const AuthNavigator = () => {
  return (
    <Stack.Navigator initialRouteName="Splash">
      <Stack.Screen
        name="Splash"
        component={SplashScreen}
        options={{ headerShown: false }}
      />
      <Stack.Screen
        name="Login"
        component={LoginScreen}
        options={{ headerShown: false }}
      />
      <Stack.Screen
        name="Register"
        component={RegisterScreen}
        options={{ title: 'Create Account' }}
      />
    </Stack.Navigator>
  );
};

export default AuthNavigator;
''',

    "mobile/react-native/src/navigation/TabNavigator.js": '''import React from 'react';
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
''',

    "mobile/react-native/package.json": '''{
  "name": "IndianStatesExam",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "android": "react-native run-android",
    "ios": "react-native run-ios",
    "start": "react-native start",
    "test": "jest",
    "lint": "eslint ."
  },
  "dependencies": {
    "react": "18.2.0",
    "react-native": "0.72.5",
    "@react-navigation/native": "^6.1.9",
    "@react-navigation/bottom-tabs": "^6.5.11",
    "@react-navigation/native-stack": "^6.9.17",
    "react-native-screens": "^3.27.0",
    "react-native-safe-area-context": "^4.7.4",
    "@reduxjs/toolkit": "^1.9.7",
    "react-redux": "^8.1.3",
    "axios": "^1.5.1",
    "@react-native-async-storage/async-storage": "^1.19.5",
    "react-native-vector-icons": "^10.0.2",
    "react-native-biometrics": "^3.0.1",
    "react-native-camera": "^4.2.1",
    "react-native-permissions": "^3.10.1",
    "react-native-image-picker": "^5.6.1",
    "react-native-sqlite-storage": "^6.0.1",
    "react-native-reanimated": "^3.5.4",
    "react-native-gesture-handler": "^2.13.4"
  },
  "devDependencies": {
    "@babel/core": "^7.23.2",
    "@babel/preset-env": "^7.23.2",
    "@babel/runtime": "^7.23.2",
    "@react-native/eslint-config": "^0.72.2",
    "@react-native/metro-config": "^0.72.11",
    "@tsconfig/react-native": "^3.0.2",
    "@types/react": "^18.2.31",
    "@types/react-test-renderer": "^18.0.4",
    "babel-jest": "^29.7.0",
    "eslint": "^8.51.0",
    "jest": "^29.7.0",
    "metro-react-native-babel-preset": "0.76.8",
    "prettier": "^3.0.3",
    "react-test-renderer": "18.2.0",
    "typescript": "5.2.2"
  },
  "engines": {
    "node": ">=16"
  }
}
''',
}

print(f"🚀 Generating {len(LAYOUT_AND_RN_FILES)} files...")
for filepath, content in LAYOUT_AND_RN_FILES.items():
    create_file(filepath, content)

print(f"\n✅ Created {len(LAYOUT_AND_RN_FILES)} files!")
print("\n📱 Summary:")
print("  ✅ Android layouts complete")
print("  ✅ Android resources complete")
print("  ✅ React Native screens complete")
print("  ✅ React Native navigation complete")
print("  ✅ package.json with all dependencies")
print("\n🎉 ALL MOBILE FILES COMPLETE!")
