const express = require('express');
const certificateRoutes = require('./routes/certificate.routes');
const { Web3 } = require('web3');

const app = express();
app.use(express.json());

// Connect to an Ethereum node
// In a real app, this would be a provider like Infura or Alchemy
const web3 = new Web3(process.env.ETHEREUM_NODE_URL || 'http://localhost:8545');
app.set('web3', web3);

app.use('/api', certificateRoutes);

const PORT = process.env.PORT || 8087;

app.listen(PORT, () => {
    console.log(`Blockchain service running on port ${PORT}`);
});