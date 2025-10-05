const mongoose = require('mongoose');

const IndianStateSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        unique: true,
    },
    capital: {
        type: String,
        required: true,
    },
    region: {
        type: String,
        enum: ['North', 'South', 'East', 'West', 'Central', 'North-East'],
    },
    population: {
        type: Number,
    },
    officialLanguages: [String],
    majorFestivals: [String],
    geography: {
        area: String, // in sq km
        climate: String,
    },
    history: {
        formationDate: String,
        keyEvents: [String],
    },
    culture: {
        cuisine: [String],
        danceForms: [String],
        artForms: [String],
    },
    mapImageUrl: String,
    createdAt: {
        type: Date,
        default: Date.now,
    },
});

module.exports = mongoose.model('IndianState', IndianStateSchema);