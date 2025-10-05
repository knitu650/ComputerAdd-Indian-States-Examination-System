const mongoose = require('mongoose');
const IndianState = require('../../../microservices/examination-service/src/models/IndianStates');

const indianStatesData = [
  {
    name: 'Andhra Pradesh',
    code: 'AP',
    type: 'state',
    capital: 'Amaravati',
    largestCity: 'Visakhapatnam',
    formation: {
      date: new Date('1956-11-01'),
      description: 'Formed on linguistic basis'
    },
    geography: {
      area: 160205,
      borders: ['Telangana', 'Karnataka', 'Tamil Nadu', 'Odisha'],
      coastline: 974,
      highestPoint: 'Arma Konda',
      majorRivers: ['Godavari', 'Krishna'],
      climate: 'Tropical'
    },
    demographics: {
      population: 49386799,
      density: 308,
      literacyRate: 67.7
    },
    language: {
      official: ['Telugu'],
      spoken: ['Telugu', 'Urdu', 'Hindi']
    }
  },
  {
    name: 'Karnataka',
    code: 'KA',
    type: 'state',
    capital: 'Bengaluru',
    largestCity: 'Bengaluru',
    formation: {
      date: new Date('1956-11-01'),
      description: 'Formed as Mysore State, renamed in 1973'
    },
    geography: {
      area: 191791,
      borders: ['Goa', 'Maharashtra', 'Telangana', 'Andhra Pradesh', 'Tamil Nadu', 'Kerala'],
      majorRivers: ['Krishna', 'Cauvery'],
      climate: 'Varied'
    },
    demographics: {
      population: 61095297,
      density: 319,
      literacyRate: 75.6
    },
    language: {
      official: ['Kannada'],
      spoken: ['Kannada', 'Urdu', 'Telugu', 'Tamil']
    }
  }
];

async function seedStates() {
  try {
    await mongoose.connect(process.env.MONGODB_URI);
    
    await IndianState.deleteMany({});
    await IndianState.insertMany(indianStatesData);
    
    console.log('Indian states seeded successfully');
    process.exit(0);
  } catch (error) {
    console.error('Seeding error:', error);
    process.exit(1);
  }
}

if (require.main === module) {
  seedStates();
}

module.exports = seedStates;
