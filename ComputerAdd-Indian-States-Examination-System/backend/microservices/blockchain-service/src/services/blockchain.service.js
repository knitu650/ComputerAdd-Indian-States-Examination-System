const Web3 = require('web3');
const fs = require('fs');
const path = require('path');

class BlockchainService {
  
  constructor() {
    this.web3 = new Web3(process.env.BLOCKCHAIN_RPC_URL || 'http://localhost:8545');
    
    // Load contract ABI
    const contractPath = path.join(__dirname, '../contracts/CertificateContract.json');
    // const contractData = JSON.parse(fs.readFileSync(contractPath, 'utf8'));
    
    this.contractAddress = process.env.CONTRACT_ADDRESS;
    // this.contract = new this.web3.eth.Contract(contractData.abi, this.contractAddress);
  }
  
  async issueCertificate(certificateData) {
    try {
      const { certificateId, studentAddress, studentName, examTitle, score, ipfsHash } = certificateData;
      
      const account = await this.web3.eth.accounts.privateKeyToAccount(
        process.env.PRIVATE_KEY
      );
      
      // const tx = await this.contract.methods.issueCertificate(
      //   certificateId,
      //   studentAddress,
      //   studentName,
      //   examTitle,
      //   score,
      //   ipfsHash
      // ).send({ from: account.address });
      
      // return tx;
      
      return { certificateId, txHash: 'dummy_hash' };
      
    } catch (error) {
      console.error('Issue certificate error:', error);
      throw error;
    }
  }
  
  async verifyCertificate(certificateId) {
    try {
      // const isValid = await this.contract.methods.verifyCertificate(certificateId).call();
      // return isValid;
      
      return true;
      
    } catch (error) {
      console.error('Verify certificate error:', error);
      throw error;
    }
  }
  
  async getCertificate(certificateId) {
    try {
      // const certificate = await this.contract.methods.getCertificate(certificateId).call();
      // return certificate;
      
      return {};
      
    } catch (error) {
      console.error('Get certificate error:', error);
      throw error;
    }
  }
}

module.exports = new BlockchainService();
