import UIKit

class MainViewController: UIViewController {
    
    private let tabBarController = UITabBarController()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        setupTabBar()
    }
    
    private func setupTabBar() {
        let dashboardVC = DashboardViewController()
        dashboardVC.tabBarItem = UITabBarItem(title: "Dashboard",
                                              image: UIImage(systemName: "house"),
                                              tag: 0)
        
        let examVC = ExamViewController()
        examVC.tabBarItem = UITabBarItem(title: "Exams",
                                         image: UIImage(systemName: "doc.text"),
                                         tag: 1)
        
        let statesVC = StatesViewController()
        statesVC.tabBarItem = UITabBarItem(title: "States",
                                           image: UIImage(systemName: "map"),
                                           tag: 2)
        
        let profileVC = ProfileViewController()
        profileVC.tabBarItem = UITabBarItem(title: "Profile",
                                            image: UIImage(systemName: "person"),
                                            tag: 3)
        
        tabBarController.viewControllers = [
            UINavigationController(rootViewController: dashboardVC),
            UINavigationController(rootViewController: examVC),
            UINavigationController(rootViewController: statesVC),
            UINavigationController(rootViewController: profileVC)
        ]
        
        addChild(tabBarController)
        view.addSubview(tabBarController.view)
        tabBarController.didMove(toParent: self)
    }
}
