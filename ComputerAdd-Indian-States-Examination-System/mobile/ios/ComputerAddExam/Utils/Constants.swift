import Foundation

struct Constants {
    
    // API URLs
    static let baseURL = "http://localhost:8000/api/v1"
    static let wsURL = "ws://localhost:8000/ws"
    
    // UserDefaults Keys
    static let authToken = "authToken"
    static let userId = "userId"
    static let userEmail = "userEmail"
    
    // Exam Constants
    static let autoSaveInterval: TimeInterval = 30.0
    static let warningTime: TimeInterval = 300.0
    
    // UI Constants
    static let cornerRadius: CGFloat = 12.0
    static let padding: CGFloat = 16.0
}
