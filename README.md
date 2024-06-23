# Ausländerbehörde-Berlin-Termin
This Python application automates the process of finding available appointments at the Ausländerbehörde Berlin. Users can specify the type of visa request, and the application will search for free appointments based on the provided criteria. When an appointment is found, the program will notify the user with a sound alert.

**Please Note**: Currently, this program is compatible only with Chrome and Safari browsers. Support for other browsers is currently under development.

## Code Structure
* app.py: Main entry point of the application. It initializes and runs the Robot class.
* robot.py: Contains the Robot class which handles the appointment searching process.
* driver.py: Contains the BrowserDriver class which initializes the web driver.

## Features
- **Automated Appointment Search**: Automatically searches for available appointments at the Ausländerbehörde Berlin.
- **Visa Type Specification**: Users can specify the type of visa they are applying for, such as study, work, or other visa types.
- **Real-time Notifications**: Notifies users when a free appointment is found using a sound alert.

## Supported Visa Types
As of now, the application supports the following visa types :
- New and extension of visas for studying (§ 16b) **(Study-verlängerung or Study-neue)**
- New and extension Residence permit for skilled workers with vocational training (§ 18a) **(Work-Ausbildung-verlängerung or Work-Ausbildung-neue)**

## Additional Specifications
- **Number of Applicants**: The application is designed for booking appointments for one person only.
- **Living with Partner**: Currently supports scenarios where the applicant does not live with a partner.

## Installation
- git clone [https://github.com/roozbehhaghiri/Termin-Auslaenderbehoerde.git]
- Setup a virtual environments
- Install requirements via **pip3 install -r requirements.txt**
- Download a [Chromedriver](https://developer.chrome.com/docs/chromedriver/downloads?hl=de) and save it's path in .env
- Configure app.py according to your visa's type
- Start the app.py
