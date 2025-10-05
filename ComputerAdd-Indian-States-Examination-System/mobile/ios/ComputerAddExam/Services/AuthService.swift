import Foundation

class AuthService {
    
    static let shared = AuthService()
    
    private init() {}
    
    func login(email: String, password: String, completion: @escaping (Result<AuthResponse, Error>) -> Void) {
        let loginData = ["email": email, "password": password]
        
        guard let jsonData = try? JSONEncoder().encode(loginData) else {
            completion(.failure(NSError(domain: "Invalid data", code: -1)))
            return
        }
        
        NetworkService.shared.request(
            endpoint: "/auth/login",
            method: "POST",
            body: jsonData,
            completion: completion
        )
    }
    
    func register(userData: [String: Any], completion: @escaping (Result<AuthResponse, Error>) -> Void) {
        guard let jsonData = try? JSONSerialization.data(withJSONObject: userData) else {
            completion(.failure(NSError(domain: "Invalid data", code: -1)))
            return
        }
        
        NetworkService.shared.request(
            endpoint: "/auth/register",
            method: "POST",
            body: jsonData,
            completion: completion
        )
    }
    
    func logout() {
        UserDefaults.standard.removeObject(forKey: "authToken")
    }
}

struct AuthResponse: Codable {
    let success: Bool
    let data: AuthData
}

struct AuthData: Codable {
    let token: String
    let user: User
}
