import Foundation

struct Question: Codable {
    let id: String
    let questionText: String
    let type: String
    let options: [String]
    let correctAnswer: String?
    let marks: Int
    let difficulty: String
    let imageUrl: String?
    
    enum CodingKeys: String, CodingKey {
        case id = "_id"
        case questionText
        case type
        case options
        case correctAnswer
        case marks
        case difficulty
        case imageUrl
    }
}
