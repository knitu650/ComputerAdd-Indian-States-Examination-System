import Foundation
import UIKit

class ProctoringService {
    
    static let shared = ProctoringService()
    
    private var timer: Timer?
    private let captureInterval: TimeInterval = 30.0
    
    private init() {}
    
    func startProctoring() {
        timer = Timer.scheduledTimer(withTimeInterval: captureInterval, repeats: true) { [weak self] _ in
            self?.captureAndAnalyze()
        }
    }
    
    func stopProctoring() {
        timer?.invalidate()
        timer = nil
    }
    
    private func captureAndAnalyze() {
        CameraService.shared.capturePhoto { [weak self] image in
            guard let image = image else { return }
            self?.analyzeImage(image)
        }
    }
    
    private func analyzeImage(_ image: UIImage) {
        // TODO: Send image to AI/ML service for analysis
        // Check for multiple faces, phone usage, etc.
    }
    
    func reportViolation(type: String, severity: String) {
        // TODO: Report violation to server
        print("Violation detected: \(type) - Severity: \(severity)")
    }
}
