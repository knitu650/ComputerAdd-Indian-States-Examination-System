import UIKit

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
