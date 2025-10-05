import Foundation

struct Answer: Codable {
    let questionId: String
    let answer: String
    var isCorrect: Bool?
    var marksObtained: Int?
    let timeSpent: TimeInterval
    
    enum CodingKeys: String, CodingKey {
        case questionId
        case answer
        case isCorrect
        case marksObtained
        case timeSpent
    }
}
