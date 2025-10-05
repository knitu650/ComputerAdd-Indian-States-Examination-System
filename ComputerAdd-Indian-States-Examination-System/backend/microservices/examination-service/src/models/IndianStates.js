const mongoose = require('mongoose');

const indianStateSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    unique: true
  },
  
  code: {
    type: String,
    required: true,
    unique: true
  },
  
  type: {
    type: String,
    enum: ['state', 'union_territory'],
    required: true
  },
  
  capital: {
    type: String,
    required: true
  },
  
  largestCity: String,
  
  formation: {
    date: Date,
    description: String
  },
  
  geography: {
    area: Number, // in km²
    borders: [String],
    coastline: Number,
    highestPoint: String,
    majorRivers: [String],
    climate: String,
    coordinates: {
      latitude: Number,
      longitude: Number
    }
  },
  
  demographics: {
    population: Number,
    density: Number,
    sexRatio: Number,
    literacyRate: Number,
    urbanPopulation: Number,
    ruralPopulation: Number
  },
  
  language: {
    official: [String],
    spoken: [String]
  },
  
  government: {
    governor: String,
    chiefMinister: String,
    legislature: String,
    parliamentarySeats: Number,
    assemblySeats: Number
  },
  
  economy: {
    gdp: Number,
    gdpPerCapita: Number,
    majorIndustries: [String],
    agriculture: [String],
    exports: [String]
  },
  
  culture: {
    festivals: [String],
    dances: [String],
    cuisine: [String],
    crafts: [String],
    monuments: [String]
  },
  
  history: {
    ancientHistory: String,
    medievalHistory: String,
    modernHistory: String,
    importantEvents: [{
      event: String,
      year: Number,
      description: String
    }]
  },
  
  tourism: {
    popularDestinations: [String],
    unesco WorldHeritageSites: [String],
    touristArrivals: Number
  },
  
  education: {
    universities: Number,
    literacyRate: Number,
    majorInstitutions: [String]
  },
  
  images: {
    flag: String,
    map: String,
    emblem: String,
    photos: [String]
  },
  
  metadata: {
    lastUpdated: {
      type: Date,
      default: Date.now
    },
    dataSource: String
  }
  
}, { timestamps: true });

// Indexes
indianStateSchema.index({ name: 1 });
indianStateSchema.index({ code: 1 });
indianStateSchema.index({ type: 1 });

module.exports = mongoose.model('IndianState', indianStateSchema);
