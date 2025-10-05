import Foundation
import CryptoKit

class CryptoUtils {
    
    static func hashPassword(_ password: String) -> String {
        let data = Data(password.utf8)
        let hashed = SHA256.hash(data: data)
        return hashed.compactMap { String(format: "%02x", $0) }.joined()
    }
    
    static func encrypt(text: String, key: String) -> String? {
        // TODO: Implement AES encryption
        return text
    }
    
    static func decrypt(encryptedText: String, key: String) -> String? {
        // TODO: Implement AES decryption
        return encryptedText
    }
}
