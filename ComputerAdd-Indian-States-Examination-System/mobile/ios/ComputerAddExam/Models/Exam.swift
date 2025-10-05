import Foundation

struct Exam: Codable {
    let id: String
    let title: String
    let description: String
    let duration: Int
    let totalQuestions: Int
    let totalMarks: Int
    let startDate: Date
    let endDate: Date
    let difficulty: String
    let isActive: Bool
    
    enum CodingKeys: String, CodingKey {
        case id = "_id"
        case title
        case description
        case duration
        case totalQuestions
        case totalMarks
        case startDate
        case endDate
        case difficulty
        case isActive
    }
}
