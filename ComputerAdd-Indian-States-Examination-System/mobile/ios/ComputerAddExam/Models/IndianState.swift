import Foundation

struct IndianState: Codable {
    let name: String
    let capital: String
    let population: Int
    let area: Double
    let language: String
    let code: String
    let imageUrl: String?
    
    enum CodingKeys: String, CodingKey {
        case name
        case capital
        case population
        case area
        case language
        case code
        case imageUrl
    }
}
