import UIKit

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
