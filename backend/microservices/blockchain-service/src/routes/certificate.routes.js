const express = require('express');
const router = express.Router();

// Placeholder for smart contract interaction
const contractABI = [/* ... Your Contract ABI ... */];
const contractAddress = process.env.CERTIFICATE_CONTRACT_ADDRESS || '0x...';


// @desc    Issue a new certificate
// @route   POST /api/issue-certificate
// @access  Private (Internal)
router.post('/issue-certificate', async (req, res) => {
    const { userId, examId, score } = req.body;
    const web3 = req.app.get('web3');

    if (!userId || !examId || !score) {
        return res.status(400).json({ message: 'Missing required data for certificate' });
    }

    try {
        // In a real implementation:
        // const accounts = await web3.eth.getAccounts();
        // const contract = new web3.eth.Contract(contractABI, contractAddress);
        // const result = await contract.methods.issueCertificate(userId, examId, score).send({ from: accounts[0] });

        // Placeholder response
        const transactionHash = '0x' + require('crypto').randomBytes(32).toString('hex');
        const certificateId = 'cert-' + require('crypto').randomBytes(16).toString('hex');

        console.log(`Issuing certificate for user ${userId} with tx hash ${transactionHash}`);

        res.status(201).json({
            message: 'Certificate issued successfully',
            certificateId: certificateId,
            transactionHash: transactionHash
        });

    } catch (error) {
        console.error("Blockchain transaction failed:", error);
        res.status(500).json({ message: 'Failed to issue certificate on the blockchain' });
    }
});

// @desc    Verify a certificate
// @route   GET /api/verify-certificate/:certificateId
// @access  Public
router.get('/verify-certificate/:certificateId', async (req, res) => {
    const { certificateId } = req.params;

    try {
        // In a real implementation, you would call a 'view' function on the smart contract
        // const contract = new req.app.get('web3').eth.Contract(contractABI, contractAddress);
        // const certificateDetails = await contract.methods.getCertificateDetails(certificateId).call();

        // Placeholder response
        if (certificateId.startsWith('cert-')) {
             res.json({
                isValid: true,
                details: {
                    userId: 'user-' + require('crypto').randomBytes(8).toString('hex'),
                    examId: 'exam-' + require('crypto').randomBytes(8).toString('hex'),
                    score: Math.floor(Math.random() * 100),
                    issueDate: new Date().toISOString()
                }
            });
        } else {
            res.status(404).json({ isValid: false, message: 'Certificate not found' });
        }
    } catch (error) {
        console.error("Certificate verification failed:", error);
        res.status(500).json({ message: 'Error verifying certificate' });
    }
});

module.exports = router;