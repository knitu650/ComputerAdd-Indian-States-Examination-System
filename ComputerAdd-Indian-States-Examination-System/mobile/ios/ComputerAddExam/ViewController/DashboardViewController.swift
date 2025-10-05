import UIKit

class DashboardViewController: UIViewController {
    
    private let welcomeLabel = UILabel()
    private let statsStackView = UIStackView()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        title = "Dashboard"
        view.backgroundColor = .systemBackground
        
        setupUI()
        loadDashboardData()
    }
    
    private func setupUI() {
        welcomeLabel.font = .systemFont(ofSize: 24, weight: .bold)
        welcomeLabel.textAlignment = .center
        welcomeLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(welcomeLabel)
        
        statsStackView.axis = .vertical
        statsStackView.spacing = 16
        statsStackView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(statsStackView)
        
        NSLayoutConstraint.activate([
            welcomeLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 20),
            welcomeLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),
            welcomeLabel.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20),
            
            statsStackView.topAnchor.constraint(equalTo: welcomeLabel.bottomAnchor, constant: 40),
            statsStackView.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),
            statsStackView.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20)
        ])
    }
    
    private func loadDashboardData() {
        welcomeLabel.text = "Welcome back!"
        
        let statsData = [
            ("Exams Taken", "15"),
            ("Average Score", "85%"),
            ("Rank", "#42")
        ]
        
        for (label, value) in statsData {
            let statView = createStatView(label: label, value: value)
            statsStackView.addArrangedSubview(statView)
        }
    }
    
    private func createStatView(label: String, value: String) -> UIView {
        let container = UIView()
        container.backgroundColor = .secondarySystemBackground
        container.layer.cornerRadius = 12
        container.translatesAutoresizingMaskIntoConstraints = false
        container.heightAnchor.constraint(equalToConstant: 80).isActive = true
        
        let labelText = UILabel()
        labelText.text = label
        labelText.font = .systemFont(ofSize: 14)
        labelText.textColor = .secondaryLabel
        labelText.translatesAutoresizingMaskIntoConstraints = false
        
        let valueText = UILabel()
        valueText.text = value
        valueText.font = .systemFont(ofSize: 28, weight: .bold)
        valueText.textColor = .label
        valueText.translatesAutoresizingMaskIntoConstraints = false
        
        container.addSubview(labelText)
        container.addSubview(valueText)
        
        NSLayoutConstraint.activate([
            labelText.topAnchor.constraint(equalTo: container.topAnchor, constant: 12),
            labelText.leadingAnchor.constraint(equalTo: container.leadingAnchor, constant: 16),
            
            valueText.topAnchor.constraint(equalTo: labelText.bottomAnchor, constant: 8),
            valueText.leadingAnchor.constraint(equalTo: container.leadingAnchor, constant: 16)
        ])
        
        return container
    }
}
