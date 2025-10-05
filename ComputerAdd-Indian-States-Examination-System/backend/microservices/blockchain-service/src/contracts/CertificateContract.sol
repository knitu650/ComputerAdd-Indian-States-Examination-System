// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CertificateContract {
    
    struct Certificate {
        string certificateId;
        address studentAddress;
        string studentName;
        string examTitle;
        uint256 score;
        uint256 issueDate;
        string ipfsHash;
        bool isValid;
    }
    
    mapping(string => Certificate) public certificates;
    mapping(address => string[]) public studentCertificates;
    
    address public owner;
    
    event CertificateIssued(
        string indexed certificateId,
        address indexed student,
        string examTitle,
        uint256 score
    );
    
    event CertificateRevoked(
        string indexed certificateId,
        address indexed student
    );
    
    constructor() {
        owner = msg.sender;
    }
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    function issueCertificate(
        string memory _certificateId,
        address _studentAddress,
        string memory _studentName,
        string memory _examTitle,
        uint256 _score,
        string memory _ipfsHash
    ) public onlyOwner {
        require(!certificates[_certificateId].isValid, "Certificate already exists");
        
        certificates[_certificateId] = Certificate({
            certificateId: _certificateId,
            studentAddress: _studentAddress,
            studentName: _studentName,
            examTitle: _examTitle,
            score: _score,
            issueDate: block.timestamp,
            ipfsHash: _ipfsHash,
            isValid: true
        });
        
        studentCertificates[_studentAddress].push(_certificateId);
        
        emit CertificateIssued(_certificateId, _studentAddress, _examTitle, _score);
    }
    
    function verifyCertificate(string memory _certificateId) public view returns (bool) {
        return certificates[_certificateId].isValid;
    }
    
    function getCertificate(string memory _certificateId) public view returns (
        address studentAddress,
        string memory studentName,
        string memory examTitle,
        uint256 score,
        uint256 issueDate,
        string memory ipfsHash,
        bool isValid
    ) {
        Certificate memory cert = certificates[_certificateId];
        return (
            cert.studentAddress,
            cert.studentName,
            cert.examTitle,
            cert.score,
            cert.issueDate,
            cert.ipfsHash,
            cert.isValid
        );
    }
    
    function revokeCertificate(string memory _certificateId) public onlyOwner {
        require(certificates[_certificateId].isValid, "Certificate not found");
        
        certificates[_certificateId].isValid = false;
        
        emit CertificateRevoked(_certificateId, certificates[_certificateId].studentAddress);
    }
    
    function getStudentCertificates(address _student) public view returns (string[] memory) {
        return studentCertificates[_student];
    }
}
