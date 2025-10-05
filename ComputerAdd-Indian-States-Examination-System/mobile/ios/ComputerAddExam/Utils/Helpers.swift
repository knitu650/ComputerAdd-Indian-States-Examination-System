import Foundation

class Helpers {
    
    static func formatDuration(_ seconds: Int) -> String {
        let hours = seconds / 3600
        let minutes = (seconds % 3600) / 60
        let secs = seconds % 60
        
        if hours > 0 {
            return String(format: "%02d:%02d:%02d", hours, minutes, secs)
        } else {
            return String(format: "%02d:%02d", minutes, secs)
        }
    }
    
    static func formatPopulation(_ population: Int) -> String {
        if population >= 10_000_000 {
            return String(format: "%.1fM", Double(population) / 1_000_000.0)
        } else if population >= 100_000 {
            return String(format: "%.1fL", Double(population) / 100_000.0)
        }
        return "\(population)"
    }
    
    static func calculatePercentage(obtained: Int, total: Int) -> Double {
        guard total > 0 else { return 0 }
        return (Double(obtained) / Double(total)) * 100.0
    }
}
