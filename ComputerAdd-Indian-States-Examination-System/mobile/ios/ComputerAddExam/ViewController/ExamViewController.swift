import UIKit

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
                print("Failed to load exams: \(error)")
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
        cell.detailTextLabel?.text = "\(exam.duration) min | \(exam.totalQuestions) questions"
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
