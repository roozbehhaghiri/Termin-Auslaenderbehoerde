from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BrowserDriver():
    def __init__(self, driverPath,browser ):
        # Set the driver's path
        self._service=Service(executable_path=driverPath)
        # Initialize Webdriver based on browser type
        match(browser):
            case "chrome":
                # Chrome options setup
                _options=webdriver.ChromeOptions()
                # Keep the browser open after execution
                _options.add_experimental_option("detach", True)
                # Needed to avoid session-timeout
                _options.add_argument("--disable-blink-features=AutomationControlled")
                _options.add_argument('--no-sandbox')
                _options.add_argument('--start-maximized')
                _options.add_argument('--disable-infobars')
                # Create a chrome-driver instance
                self._driver=webdriver.Chrome(service=self._service, options=_options)
                 
            #Safari under development
            case "safari":
                raise NotImplementedError("Safari browser support is under development.")
    
    def get_driver(self):
        return self._driver