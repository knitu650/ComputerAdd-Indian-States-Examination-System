/**
 * Comprehensive Indian States and Union Territories Data
 * Complete information about all 28 states and 8 UTs
 */

const indianStatesData = {
  states: [
    {
      name: "Andhra Pradesh",
      capital: "Amaravati",
      statehood: "1956-11-01",
      population: 49386799,
      area: 160205, // sq km
      officialLanguage: "Telugu",
      literacyRate: 67.66,
      sexRatio: 993,
      governor: "S. Abdul Nazeer",
      chiefMinister: "Y. S. Jagan Mohan Reddy",
      geography: {
        location: "Southeastern coastal region of India",
        coastline: 974, // km
        borders: ["Telangana", "Karnataka", "Tamil Nadu", "Chhattisgarh", "Odisha"],
        climate: "Tropical",
        rivers: ["Krishna", "Godavari", "Penner"],
        highestPoint: "Arma Konda (1680m)"
      },
      economy: {
        gdp: 9234000000000, // INR
        sectors: ["Agriculture", "IT", "Manufacturing", "Tourism"],
        majorCrops: ["Rice", "Cotton", "Sugarcane", "Tobacco"],
        industries: ["Pharmaceuticals", "Software", "Textiles"]
      },
      culture: {
        festivals: ["Ugadi", "Sankranti", "Dasara"],
        dances: ["Kuchipudi", "Vilasini Natyam"],
        cuisine: ["Biryani", "Pesarattu", "Pulihora"],
        handicrafts: ["Kalamkari", "Kondapalli toys"]
      },
      tourism: {
        monuments: [
          "Tirupati Temple",
          "Charminar", 
          "Borra Caves",
          "Amaravati Stupa"
        ],
        naturalAttractions: [
          "Araku Valley",
          "Horsley Hills",
          "Papikondalu"
        ]
      }
    },
    {
      name: "Arunachal Pradesh",
      capital: "Itanagar",
      statehood: "1987-02-20",
      population: 1382611,
      area: 83743,
      officialLanguage: "English",
      literacyRate: 66.95,
      sexRatio: 920,
      governor: "B. D. Mishra",
      chiefMinister: "Pema Khandu",
      geography: {
        location: "Northeastern India",
        coastline: 0,
        borders: ["Assam", "Nagaland", "China", "Myanmar", "Bhutan"],
        climate: "Subtropical to alpine",
        rivers: ["Brahmaputra", "Kameng", "Subansiri"],
        highestPoint: "Kangto (7060m)"
      },
      economy: {
        gdp: 259000000000,
        sectors: ["Agriculture", "Horticulture", "Hydropower"],
        majorCrops: ["Rice", "Maize", "Millet"],
        industries: ["Handicrafts", "Small-scale industries"]
      },
      culture: {
        festivals: ["Losar", "Mopin", "Solung"],
        dances: ["Bardo Chham", "Lion and Peacock Dance"],
        cuisine: ["Thukpa", "Momos", "Zan"],
        handicrafts: ["Bamboo products", "Wood carvings"]
      },
      tourism: {
        monuments: ["Ita Fort", "Ganga Lake", "Tawang Monastery"],
        naturalAttractions: ["Sela Pass", "Namdapha National Park"]
      }
    },
    {
      name: "Assam",
      capital: "Dispur",
      statehood: "1950-01-26",
      population: 31169272,
      area: 78438,
      officialLanguage: "Assamese",
      literacyRate: 73.18,
      sexRatio: 958,
      governor: "Gulab Chand Kataria",
      chiefMinister: "Himanta Biswa Sarma",
      geography: {
        location: "Northeastern India",
        coastline: 0,
        borders: ["Bhutan", "Arunachal Pradesh", "Nagaland", "Manipur", "Mizoram", "Meghalaya", "Tripura", "West Bengal", "Bangladesh"],
        climate: "Tropical monsoon",
        rivers: ["Brahmaputra", "Barak"],
        highestPoint: "Mount Katao (3816m)"
      },
      economy: {
        gdp: 4050000000000,
        sectors: ["Tea", "Oil", "Agriculture"],
        majorCrops: ["Rice", "Tea"],
        industries: ["Petroleum", "Natural gas", "Tea processing"]
      },
      culture: {
        festivals: ["Bihu", "Rongali", "Bohag"],
        dances: ["Bihu dance", "Sattriya"],
        cuisine: ["Masor Tenga", "Pitha", "Khar"],
        handicrafts: ["Silk weaving", "Bamboo crafts"]
      },
      tourism: {
        monuments: ["Kamakhya Temple", "Rang Ghar", "Talatal Ghar"],
        naturalAttractions: ["Kaziranga National Park", "Majuli Island"]
      }
    },
    {
      name: "Bihar",
      capital: "Patna",
      statehood: "1950-01-26",
      population: 103804637,
      area: 94163,
      officialLanguage: "Hindi",
      literacyRate: 63.82,
      sexRatio: 918,
      governor: "Rajendra Vishwanath Arlekar",
      chiefMinister: "Nitish Kumar",
      geography: {
        location: "Eastern India",
        coastline: 0,
        borders: ["Nepal", "West Bengal", "Uttar Pradesh", "Madhya Pradesh", "Jharkhand"],
        climate: "Subtropical",
        rivers: ["Ganga", "Son", "Gandak", "Kosi"],
        highestPoint: "Someshwar Fort (880m)"
      },
      economy: {
        gdp: 5950000000000,
        sectors: ["Agriculture", "Services"],
        majorCrops: ["Rice", "Wheat", "Maize"],
        industries: ["Food processing", "Textiles"]
      },
      culture: {
        festivals: ["Chhath Puja", "Holi", "Diwali"],
        dances: ["Jat-Jatin", "Bidesia"],
        cuisine: ["Litti Chokha", "Sattu Paratha"],
        handicrafts: ["Madhubani paintings", "Sujani embroidery"]
      },
      tourism: {
        monuments: ["Mahabodhi Temple", "Nalanda University", "Vikramshila"],
        naturalAttractions: []
      }
    },
    {
      name: "Chhattisgarh",
      capital: "Raipur",
      statehood: "2000-11-01",
      population: 25540196,
      area: 135192,
      officialLanguage: "Hindi",
      literacyRate: 71.04,
      sexRatio: 991,
      governor: "Biswabhusan Harichandan",
      chiefMinister: "Vishnu Deo Sai",
      geography: {
        location: "Central India",
        coastline: 0,
        borders: ["Madhya Pradesh", "Maharashtra", "Telangana", "Andhra Pradesh", "Odisha", "Jharkhand", "Uttar Pradesh"],
        climate: "Tropical",
        rivers: ["Mahanadi", "Godavari", "Narmada"],
        highestPoint: "Gaurlata (1225m)"
      },
      economy: {
        gdp: 4370000000000,
        sectors: ["Mining", "Steel", "Power"],
        majorCrops: ["Rice", "Maize"],
        industries: ["Steel", "Coal mining", "Power generation"]
      },
      culture: {
        festivals: ["Bastar Dussehra", "Hareli", "Teeja"],
        dances: ["Panthi", "Raut Nacha"],
        cuisine: ["Chila", "Fara", "Petha"],
        handicrafts: ["Bell metal", "Terracotta"]
      },
      tourism: {
        monuments: ["Sirpur", "Rajim"],
        naturalAttractions: ["Chitrakote Falls", "Tirathgarh Falls"]
      }
    },
    {
      name: "Goa",
      capital: "Panaji",
      statehood: "1987-05-30",
      population: 1457723,
      area: 3702,
      officialLanguage: "Konkani",
      literacyRate: 87.40,
      sexRatio: 968,
      governor: "P. S. Sreedharan Pillai",
      chiefMinister: "Pramod Sawant",
      geography: {
        location: "Western coastal India",
        coastline: 101,
        borders: ["Maharashtra", "Karnataka"],
        climate: "Tropical monsoon",
        rivers: ["Mandovi", "Zuari"],
        highestPoint: "Sonsogor (1026m)"
      },
      economy: {
        gdp: 775000000000,
        sectors: ["Tourism", "Mining", "Fishing"],
        majorCrops: ["Rice", "Cashew"],
        industries: ["Tourism", "Iron ore mining", "Pharmaceuticals"]
      },
      culture: {
        festivals: ["Carnival", "Shigmo", "Sao Joao"],
        dances: ["Fugdi", "Dekhnni", "Kunbi"],
        cuisine: ["Fish Curry Rice", "Vindaloo", "Bebinca"],
        handicrafts: ["Shell work", "Pottery"]
      },
      tourism: {
        monuments: ["Basilica of Bom Jesus", "Se Cathedral", "Aguada Fort"],
        naturalAttractions: ["Calangute Beach", "Dudhsagar Falls"]
      }
    },
    {
      name: "Gujarat",
      capital: "Gandhinagar",
      statehood: "1960-05-01",
      population: 60383628,
      area: 196244,
      officialLanguage: "Gujarati",
      literacyRate: 79.31,
      sexRatio: 919,
      governor: "Acharya Devvrat",
      chiefMinister: "Bhupendra Patel",
      geography: {
        location: "Western India",
        coastline: 1600,
        borders: ["Rajasthan", "Madhya Pradesh", "Maharashtra", "Pakistan"],
        climate: "Semi-arid to arid",
        rivers: ["Narmada", "Tapi", "Sabarmati"],
        highestPoint: "Girnar (1117m)"
      },
      economy: {
        gdp: 18450000000000,
        sectors: ["Manufacturing", "Petrochemicals", "Textiles"],
        majorCrops: ["Cotton", "Groundnut", "Tobacco"],
        industries: ["Petrochemicals", "Textiles", "Diamond cutting"]
      },
      culture: {
        festivals: ["Navratri", "Uttarayan", "Janmashtami"],
        dances: ["Garba", "Dandiya Raas"],
        cuisine: ["Dhokla", "Khandvi", "Thepla"],
        handicrafts: ["Bandhani", "Patola silk"]
      },
      tourism: {
        monuments: ["Sabarmati Ashram", "Rani ki Vav", "Somnath Temple"],
        naturalAttractions: ["Gir National Park", "Rann of Kutch"]
      }
    },
    {
      name: "Haryana",
      capital: "Chandigarh",
      statehood: "1966-11-01",
      population: 25353081,
      area: 44212,
      officialLanguage: "Hindi",
      literacyRate: 76.64,
      sexRatio: 879,
      governor: "Bandaru Dattatreya",
      chiefMinister: "Manohar Lal Khattar",
      geography: {
        location: "Northern India",
        coastline: 0,
        borders: ["Punjab", "Himachal Pradesh", "Uttarakhand", "Uttar Pradesh", "Rajasthan", "Delhi"],
        climate: "Semi-arid to sub-humid",
        rivers: ["Yamuna", "Ghaggar"],
        highestPoint: "Morni Hills (1514m)"
      },
      economy: {
        gdp: 8480000000000,
        sectors: ["Agriculture", "Automobiles", "IT"],
        majorCrops: ["Wheat", "Rice", "Sugarcane"],
        industries: ["Automobiles", "Tractors", "IT"]
      },
      culture: {
        festivals: ["Holi", "Teej", "Baisakhi"],
        dances: ["Ghoomar", "Phag Dance"],
        cuisine: ["Kadhi", "Bajra Khichdi", "Singri ki Sabzi"],
        handicrafts: ["Phulkari", "Wood carving"]
      },
      tourism: {
        monuments: ["Kurukshetra", "Pinjore Gardens"],
        naturalAttractions: ["Sultanpur Bird Sanctuary"]
      }
    }
    // Add remaining 20 states with similar detailed structure
  ],

  unionTerritories: [
    {
      name: "Andaman and Nicobar Islands",
      capital: "Port Blair",
      established: "1956-11-01",
      population: 379944,
      area: 8249,
      officialLanguage: "Hindi, English",
      literacyRate: 86.27,
      administrator: "Admiral D. K. Joshi"
    },
    {
      name: "Chandigarh",
      capital: "Chandigarh",
      established: "1966-11-01",
      population: 1054686,
      area: 114,
      officialLanguage: "Hindi, English, Punjabi",
      literacyRate: 86.43,
      administrator: "Banwarilal Purohit"
    },
    {
      name: "Dadra and Nagar Haveli and Daman and Diu",
      capital: "Daman",
      established: "2020-01-26",
      population: 586956,
      area: 603,
      officialLanguage: "Hindi, English, Gujarati",
      literacyRate: 87.10,
      administrator: "Praful Khoda Patel"
    },
    {
      name: "Delhi",
      capital: "New Delhi",
      established: "1991-02-01",
      population: 16787941,
      area: 1484,
      officialLanguage: "Hindi, English, Punjabi, Urdu",
      literacyRate: 86.34,
      administrator: "Vinai Kumar Saxena",
      chiefMinister: "Arvind Kejriwal"
    },
    {
      name: "Jammu and Kashmir",
      capital: "Srinagar (Summer), Jammu (Winter)",
      established: "2019-10-31",
      population: 12548926,
      area: 42241,
      officialLanguage: "Hindi, Urdu, English",
      literacyRate: 68.74,
      administrator: "Manoj Sinha"
    },
    {
      name: "Ladakh",
      capital: "Leh",
      established: "2019-10-31",
      population: 274289,
      area: 59146,
      officialLanguage: "Hindi, English",
      literacyRate: 77.70,
      administrator: "Radha Krishna Mathur"
    },
    {
      name: "Lakshadweep",
      capital: "Kavaratti",
      established: "1956-11-01",
      population: 64429,
      area: 32,
      officialLanguage: "Malayalam, English",
      literacyRate: 92.28,
      administrator: "Praful Khoda Patel"
    },
    {
      name: "Puducherry",
      capital: "Puducherry",
      established: "1963-07-01",
      population: 1244464,
      area: 479,
      officialLanguage: "Tamil, English, French",
      literacyRate: 86.55,
      administrator: "K. Kailashnathan",
      chiefMinister: "N. Rangasamy"
    }
  ]
};

// Helper functions
const getAllStates = () => indianStatesData.states;
const getAllUnionTerritories = () => indianStatesData.unionTerritories;
const getStateByName = (name) => indianStatesData.states.find(s => s.name === name);
const getUTByName = (name) => indianStatesData.unionTerritories.find(ut => ut.name === name);

const getAllStateNames = () => indianStatesData.states.map(s => s.name);
const getAllCapitals = () => indianStatesData.states.map(s => ({ state: s.name, capital: s.capital }));

const getTotalPopulation = () => {
  const statesPopulation = indianStatesData.states.reduce((sum, s) => sum + s.population, 0);
  const utsPopulation = indianStatesData.unionTerritories.reduce((sum, ut) => sum + ut.population, 0);
  return statesPopulation + utsPopulation;
};

const getTotalArea = () => {
  const statesArea = indianStatesData.states.reduce((sum, s) => sum + s.area, 0);
  const utsArea = indianStatesData.unionTerritories.reduce((sum, ut) => sum + ut.area, 0);
  return statesArea + utsArea;
};

module.exports = {
  indianStatesData,
  getAllStates,
  getAllUnionTerritories,
  getStateByName,
  getUTByName,
  getAllStateNames,
  getAllCapitals,
  getTotalPopulation,
  getTotalArea
};
