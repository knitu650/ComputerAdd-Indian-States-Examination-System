import UIKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication,
                    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        
        // Setup window
        window = UIWindow(frame: UIScreen.main.bounds)
        
        // Check if user is logged in
        if isUserLoggedIn() {
            let mainVC = MainViewController()
            window?.rootViewController = UINavigationController(rootViewController: mainVC)
        } else {
            let authVC = AuthViewController()
            window?.rootViewController = UINavigationController(rootViewController: authVC)
        }
        
        window?.makeKeyAndVisible()
        
        return true
    }
    
    private func isUserLoggedIn() -> Bool {
        return UserDefaults.standard.string(forKey: "authToken") != nil
    }
}
