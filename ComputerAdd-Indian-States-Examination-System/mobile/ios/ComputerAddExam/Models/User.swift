import Foundation

struct User: Codable {
    let id: String
    let email: String
    let firstName: String
    let lastName: String
    let phoneNumber: String?
    let role: String
    let avatar: String?
    
    var fullName: String {
        return "\(firstName) \(lastName)"
    }
    
    enum CodingKeys: String, CodingKey {
        case id = "_id"
        case email
        case firstName
        case lastName
        case phoneNumber
        case role
        case avatar
    }
}
