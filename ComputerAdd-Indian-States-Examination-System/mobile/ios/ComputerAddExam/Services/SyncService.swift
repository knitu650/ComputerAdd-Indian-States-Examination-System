import Foundation

class SyncService {
    
    static let shared = SyncService()
    
    private init() {}
    
    func syncData(completion: @escaping (Bool) -> Void) {
        // Sync offline data with server
        syncPendingAnswers { success in
            if success {
                self.syncExams { examSuccess in
                    completion(examSuccess)
                }
            } else {
                completion(false)
            }
        }
    }
    
    private func syncPendingAnswers(completion: @escaping (Bool) -> Void) {
        // TODO: Upload pending answers
        completion(true)
    }
    
    private func syncExams(completion: @escaping (Bool) -> Void) {
        // TODO: Download new exams and content
        completion(true)
    }
}
