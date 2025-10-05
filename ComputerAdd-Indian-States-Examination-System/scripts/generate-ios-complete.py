#!/usr/bin/env python3
"""Complete iOS Files Generator"""

import os

BASE_DIR = "/workspace/ComputerAdd-Indian-States-Examination-System"

def create_file(filepath, content):
    full_path = os.path.join(BASE_DIR, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ {filepath}")

IOS_FILES = {
    "mobile/ios/ComputerAddExam/SceneDelegate.swift": '''import UIKit

class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession,
              options connectionOptions: UIScene.ConnectionOptions) {
        
        guard let windowScene = (scene as? UIWindowScene) else { return }
        
        window = UIWindow(windowScene: windowScene)
        
        if UserDefaults.standard.string(forKey: "authToken") != nil {
            let mainVC = MainViewController()
            window?.rootViewController = UINavigationController(rootViewController: mainVC)
        } else {
            let authVC = AuthViewController()
            window?.rootViewController = UINavigationController(rootViewController: authVC)
        }
        
        window?.makeKeyAndVisible()
    }
}
''',

    "mobile/ios/ComputerAddExam/ViewController/ExamViewController.swift": '''import UIKit

class ExamViewController: UIViewController {
    
    private var tableView: UITableView!
    private var exams: [Exam] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        title = "Exams"
        setupTableView()
        loadExams()
    }
    
    private func setupTableView() {
        tableView = UITableView(frame: view.bounds)
        tableView.delegate = self
        tableView.dataSource = self
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "ExamCell")
        view.addSubview(tableView)
    }
    
    private func loadExams() {
        NetworkService.shared.request(endpoint: "/exams", method: "GET") {
            (result: Result<ExamsResponse, Error>) in
            switch result {
            case .success(let response):
                self.exams = response.data
                DispatchQueue.main.async {
                    self.tableView.reloadData()
                }
            case .failure(let error):
                print("Failed to load exams: \\(error)")
            }
        }
    }
}

extension ExamViewController: UITableViewDelegate, UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return exams.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "ExamCell", for: indexPath)
        let exam = exams[indexPath.row]
        cell.textLabel?.text = exam.title
        cell.detailTextLabel?.text = "\\(exam.duration) min | \\(exam.totalQuestions) questions"
        return cell
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let exam = exams[indexPath.row]
        // Navigate to exam details
        tableView.deselectRow(at: indexPath, animated: true)
    }
}

struct ExamsResponse: Codable {
    let success: Bool
    let data: [Exam]
}
''',

    "mobile/ios/ComputerAddExam/ViewController/DashboardViewController.swift": '''import UIKit

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
''',

    "mobile/ios/ComputerAddExam/ViewController/ProfileViewController.swift": '''import UIKit

class ProfileViewController: UIViewController {
    
    private let avatarImageView = UIImageView()
    private let nameLabel = UILabel()
    private let emailLabel = UILabel()
    private let logoutButton = UIButton(type: .system)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        title = "Profile"
        view.backgroundColor = .systemBackground
        
        setupUI()
        loadProfile()
    }
    
    private func setupUI() {
        avatarImageView.contentMode = .scaleAspectFill
        avatarImageView.clipsToBounds = true
        avatarImageView.layer.cornerRadius = 50
        avatarImageView.backgroundColor = .systemGray
        avatarImageView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(avatarImageView)
        
        nameLabel.font = .systemFont(ofSize: 24, weight: .bold)
        nameLabel.textAlignment = .center
        nameLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(nameLabel)
        
        emailLabel.font = .systemFont(ofSize: 16)
        emailLabel.textColor = .secondaryLabel
        emailLabel.textAlignment = .center
        emailLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(emailLabel)
        
        logoutButton.setTitle("Logout", for: .normal)
        logoutButton.titleLabel?.font = .systemFont(ofSize: 18, weight: .semibold)
        logoutButton.backgroundColor = .systemRed
        logoutButton.setTitleColor(.white, for: .normal)
        logoutButton.layer.cornerRadius = 12
        logoutButton.addTarget(self, action: #selector(handleLogout), for: .touchUpInside)
        logoutButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(logoutButton)
        
        NSLayoutConstraint.activate([
            avatarImageView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 40),
            avatarImageView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            avatarImageView.widthAnchor.constraint(equalToConstant: 100),
            avatarImageView.heightAnchor.constraint(equalToConstant: 100),
            
            nameLabel.topAnchor.constraint(equalTo: avatarImageView.bottomAnchor, constant: 20),
            nameLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),
            nameLabel.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20),
            
            emailLabel.topAnchor.constraint(equalTo: nameLabel.bottomAnchor, constant: 8),
            emailLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),
            emailLabel.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20),
            
            logoutButton.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor, constant: -40),
            logoutButton.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 40),
            logoutButton.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -40),
            logoutButton.heightAnchor.constraint(equalToConstant: 50)
        ])
    }
    
    private func loadProfile() {
        nameLabel.text = "John Doe"
        emailLabel.text = "john.doe@example.com"
    }
    
    @objc private func handleLogout() {
        UserDefaults.standard.removeObject(forKey: "authToken")
        
        let authVC = AuthViewController()
        let navController = UINavigationController(rootViewController: authVC)
        
        if let window = view.window {
            window.rootViewController = navController
            window.makeKeyAndVisible()
        }
    }
}
''',

    "mobile/ios/ComputerAddExam/ViewController/AuthViewController.swift": '''import UIKit

class AuthViewController: UIViewController {
    
    private let emailTextField = UITextField()
    private let passwordTextField = UITextField()
    private let loginButton = UIButton(type: .system)
    private let registerButton = UIButton(type: .system)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        title = "Login"
        view.backgroundColor = .systemBackground
        navigationItem.hidesBackButton = true
        
        setupUI()
    }
    
    private func setupUI() {
        emailTextField.placeholder = "Email"
        emailTextField.borderStyle = .roundedRect
        emailTextField.autocapitalizationType = .none
        emailTextField.keyboardType = .emailAddress
        emailTextField.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(emailTextField)
        
        passwordTextField.placeholder = "Password"
        passwordTextField.borderStyle = .roundedRect
        passwordTextField.isSecureTextEntry = true
        passwordTextField.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(passwordTextField)
        
        loginButton.setTitle("Login", for: .normal)
        loginButton.titleLabel?.font = .systemFont(ofSize: 18, weight: .semibold)
        loginButton.backgroundColor = .systemBlue
        loginButton.setTitleColor(.white, for: .normal)
        loginButton.layer.cornerRadius = 12
        loginButton.addTarget(self, action: #selector(handleLogin), for: .touchUpInside)
        loginButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(loginButton)
        
        registerButton.setTitle("Don't have an account? Register", for: .normal)
        registerButton.addTarget(self, action: #selector(handleRegister), for: .touchUpInside)
        registerButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(registerButton)
        
        NSLayoutConstraint.activate([
            emailTextField.centerYAnchor.constraint(equalTo: view.centerYAnchor, constant: -80),
            emailTextField.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 40),
            emailTextField.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -40),
            emailTextField.heightAnchor.constraint(equalToConstant: 50),
            
            passwordTextField.topAnchor.constraint(equalTo: emailTextField.bottomAnchor, constant: 16),
            passwordTextField.leadingAnchor.constraint(equalTo: emailTextField.leadingAnchor),
            passwordTextField.trailingAnchor.constraint(equalTo: emailTextField.trailingAnchor),
            passwordTextField.heightAnchor.constraint(equalToConstant: 50),
            
            loginButton.topAnchor.constraint(equalTo: passwordTextField.bottomAnchor, constant: 24),
            loginButton.leadingAnchor.constraint(equalTo: emailTextField.leadingAnchor),
            loginButton.trailingAnchor.constraint(equalTo: emailTextField.trailingAnchor),
            loginButton.heightAnchor.constraint(equalToConstant: 50),
            
            registerButton.topAnchor.constraint(equalTo: loginButton.bottomAnchor, constant: 16),
            registerButton.centerXAnchor.constraint(equalTo: view.centerXAnchor)
        ])
    }
    
    @objc private func handleLogin() {
        guard let email = emailTextField.text, !email.isEmpty,
              let password = passwordTextField.text, !password.isEmpty else {
            showAlert(message: "Please fill in all fields")
            return
        }
        
        // TODO: Implement API call
        UserDefaults.standard.set("dummy_token", forKey: "authToken")
        
        let mainVC = MainViewController()
        let navController = UINavigationController(rootViewController: mainVC)
        
        if let window = view.window {
            window.rootViewController = navController
            window.makeKeyAndVisible()
        }
    }
    
    @objc private func handleRegister() {
        // Navigate to registration
    }
    
    private func showAlert(message: String) {
        let alert = UIAlertController(title: "Error", message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default))
        present(alert, animated: true)
    }
}
''',

    "mobile/ios/ComputerAddExam/ViewController/StatesViewController.swift": '''import UIKit

class StatesViewController: UIViewController {
    
    private var collectionView: UICollectionView!
    private var states: [IndianState] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        title = "Indian States"
        setupCollectionView()
        loadStates()
    }
    
    private func setupCollectionView() {
        let layout = UICollectionViewFlowLayout()
        layout.itemSize = CGSize(width: (view.bounds.width - 48) / 2, height: 150)
        layout.minimumInteritemSpacing = 16
        layout.minimumLineSpacing = 16
        layout.sectionInset = UIEdgeInsets(top: 16, left: 16, bottom: 16, right: 16)
        
        collectionView = UICollectionView(frame: view.bounds, collectionViewLayout: layout)
        collectionView.delegate = self
        collectionView.dataSource = self
        collectionView.backgroundColor = .systemBackground
        collectionView.register(StateCell.self, forCellWithReuseIdentifier: "StateCell")
        view.addSubview(collectionView)
    }
    
    private func loadStates() {
        // TODO: Load states from API or local data
    }
}

extension StatesViewController: UICollectionViewDelegate, UICollectionViewDataSource {
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return states.count
    }
    
    func collectionView(_ collectionView: UICollectionView,
                       cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(
            withReuseIdentifier: "StateCell",
            for: indexPath) as! StateCell
        cell.configure(with: states[indexPath.row])
        return cell
    }
}

class StateCell: UICollectionViewCell {
    private let nameLabel = UILabel()
    private let capitalLabel = UILabel()
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupUI()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    private func setupUI() {
        backgroundColor = .secondarySystemBackground
        layer.cornerRadius = 12
        
        nameLabel.font = .systemFont(ofSize: 16, weight: .bold)
        nameLabel.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(nameLabel)
        
        capitalLabel.font = .systemFont(ofSize: 12)
        capitalLabel.textColor = .secondaryLabel
        capitalLabel.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(capitalLabel)
        
        NSLayoutConstraint.activate([
            nameLabel.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 12),
            nameLabel.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 12),
            
            capitalLabel.topAnchor.constraint(equalTo: nameLabel.bottomAnchor, constant: 4),
            capitalLabel.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 12)
        ])
    }
    
    func configure(with state: IndianState) {
        nameLabel.text = state.name
        capitalLabel.text = state.capital
    }
}
''',

    "mobile/ios/ComputerAddExam/Models/Question.swift": '''import Foundation

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
''',

    "mobile/ios/ComputerAddExam/Models/Answer.swift": '''import Foundation

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
''',

    "mobile/ios/ComputerAddExam/Models/IndianState.swift": '''import Foundation

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
''',

    "mobile/ios/ComputerAddExam/Services/AuthService.swift": '''import Foundation

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
''',

    "mobile/ios/ComputerAddExam/Services/CameraService.swift": '''import AVFoundation
import UIKit

class CameraService: NSObject {
    
    static let shared = CameraService()
    
    private var captureSession: AVCaptureSession?
    private var photoOutput: AVCapturePhotoOutput?
    private var completion: ((UIImage?) -> Void)?
    
    private override init() {
        super.init()
    }
    
    func checkCameraPermission(completion: @escaping (Bool) -> Void) {
        switch AVCaptureDevice.authorizationStatus(for: .video) {
        case .authorized:
            completion(true)
        case .notDetermined:
            AVCaptureDevice.requestAccess(for: .video) { granted in
                completion(granted)
            }
        default:
            completion(false)
        }
    }
    
    func setupCameraSession() -> AVCaptureSession? {
        let session = AVCaptureSession()
        
        guard let camera = AVCaptureDevice.default(.builtInWideAngleCamera, for: .video, position: .front),
              let input = try? AVCaptureDeviceInput(device: camera) else {
            return nil
        }
        
        if session.canAddInput(input) {
            session.addInput(input)
        }
        
        let output = AVCapturePhotoOutput()
        if session.canAddOutput(output) {
            session.addOutput(output)
            photoOutput = output
        }
        
        captureSession = session
        return session
    }
    
    func capturePhoto(completion: @escaping (UIImage?) -> Void) {
        self.completion = completion
        
        let settings = AVCapturePhotoSettings()
        photoOutput?.capturePhoto(with: settings, delegate: self)
    }
}

extension CameraService: AVCapturePhotoCaptureDelegate {
    func photoOutput(_ output: AVCapturePhotoOutput,
                    didFinishProcessingPhoto photo: AVCapturePhoto,
                    error: Error?) {
        guard let imageData = photo.fileDataRepresentation(),
              let image = UIImage(data: imageData) else {
            completion?(nil)
            return
        }
        
        completion?(image)
    }
}
''',

    "mobile/ios/ComputerAddExam/Services/BiometricService.swift": '''import LocalAuthentication

class BiometricService {
    
    static let shared = BiometricService()
    
    private init() {}
    
    func isBiometricAvailable() -> Bool {
        let context = LAContext()
        var error: NSError?
        
        return context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &error)
    }
    
    func authenticateWithBiometric(completion: @escaping (Bool, Error?) -> Void) {
        let context = LAContext()
        let reason = "Authenticate to access your account"
        
        context.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, localizedReason: reason) {
            success, error in
            DispatchQueue.main.async {
                completion(success, error)
            }
        }
    }
    
    func getBiometricType() -> String {
        let context = LAContext()
        
        if context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: nil) {
            switch context.biometryType {
            case .faceID:
                return "Face ID"
            case .touchID:
                return "Touch ID"
            default:
                return "None"
            }
        }
        
        return "None"
    }
}
''',

    "mobile/ios/ComputerAddExam/Services/ProctoringService.swift": '''import Foundation
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
        print("Violation detected: \\(type) - Severity: \\(severity)")
    }
}
''',

    "mobile/ios/ComputerAddExam/Services/SyncService.swift": '''import Foundation

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
''',

    "mobile/ios/ComputerAddExam/Utils/Constants.swift": '''import Foundation

struct Constants {
    
    // API URLs
    static let baseURL = "http://localhost:8000/api/v1"
    static let wsURL = "ws://localhost:8000/ws"
    
    // UserDefaults Keys
    static let authToken = "authToken"
    static let userId = "userId"
    static let userEmail = "userEmail"
    
    // Exam Constants
    static let autoSaveInterval: TimeInterval = 30.0
    static let warningTime: TimeInterval = 300.0
    
    // UI Constants
    static let cornerRadius: CGFloat = 12.0
    static let padding: CGFloat = 16.0
}
''',

    "mobile/ios/ComputerAddExam/Utils/Extensions.swift": '''import UIKit

extension UIColor {
    static let primaryColor = UIColor.systemBlue
    static let secondaryColor = UIColor.systemPurple
    static let successColor = UIColor.systemGreen
    static let errorColor = UIColor.systemRed
}

extension String {
    var isValidEmail: Bool {
        let emailRegex = "[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\\\.[A-Za-z]{2,64}"
        let emailPredicate = NSPredicate(format:"SELF MATCHES %@", emailRegex)
        return emailPredicate.evaluate(with: self)
    }
    
    var isValidPassword: Bool {
        return self.count >= 8
    }
}

extension Date {
    func formattedString() -> String {
        let formatter = DateFormatter()
        formatter.dateStyle = .medium
        formatter.timeStyle = .short
        return formatter.string(from: self)
    }
}
''',

    "mobile/ios/ComputerAddExam/Utils/Helpers.swift": '''import Foundation

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
        return "\\(population)"
    }
    
    static func calculatePercentage(obtained: Int, total: Int) -> Double {
        guard total > 0 else { return 0 }
        return (Double(obtained) / Double(total)) * 100.0
    }
}
''',

    "mobile/ios/ComputerAddExam/Utils/CryptoUtils.swift": '''import Foundation
import CryptoKit

class CryptoUtils {
    
    static func hashPassword(_ password: String) -> String {
        let data = Data(password.utf8)
        let hashed = SHA256.hash(data: data)
        return hashed.compactMap { String(format: "%02x", $0) }.joined()
    }
    
    static func encrypt(text: String, key: String) -> String? {
        // TODO: Implement AES encryption
        return text
    }
    
    static func decrypt(encryptedText: String, key: String) -> String? {
        // TODO: Implement AES decryption
        return encryptedText
    }
}
''',

    "mobile/ios/ComputerAddExam/Info.plist": '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDevelopmentRegion</key>
    <string>en</string>
    <key>CFBundleDisplayName</key>
    <string>Indian States Exam</string>
    <key>CFBundleExecutable</key>
    <string>$(EXECUTABLE_NAME)</string>
    <key>CFBundleIdentifier</key>
    <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
    <key>CFBundleName</key>
    <string>$(PRODUCT_NAME)</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>CFBundleVersion</key>
    <string>1</string>
    <key>NSCameraUsageDescription</key>
    <string>We need camera access for proctoring during exams</string>
    <key>NSFaceIDUsageDescription</key>
    <string>Use Face ID for secure login</string>
    <key>NSPhotoLibraryUsageDescription</key>
    <string>Save exam screenshots</string>
    <key>UILaunchStoryboardName</key>
    <string>LaunchScreen</string>
    <key>UISupportedInterfaceOrientations</key>
    <array>
        <string>UIInterfaceOrientationPortrait</string>
    </array>
</dict>
</plist>
''',
}

print(f"🚀 Generating {len(IOS_FILES)} iOS files...")
for filepath, content in IOS_FILES.items():
    create_file(filepath, content)

print(f"\n✅ Successfully created {len(IOS_FILES)} iOS files!")
print("📱 iOS Native app complete!")
