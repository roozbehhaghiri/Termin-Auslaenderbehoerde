from robot import Robot

# Provide actual values for nationality, havePass, and typOfVisa
nationality = "Iran, Islamische Republik"
typOfVisa = "Study-verlängerung"

# Create an instance of Robot with Chrome as the browser option
robotChrome=Robot("Chrome",nationality, typOfVisa)
robotChrome.run()