
# Import the ntsc module
from ntsc import ntsc

# Create a new project object
project = ntsc.CreateProject()

# Connect to the server at IP address 192.168.15.100 and port 80
project.Connect("192.168.15.180", 80)

# Log in to the server with username "admin" and password "admin"
project.Login("admin", "admin")

# Create a new test case of type "HttpCps" with the name "Gateway"
case = project.CreateCase("Ipv4FragAttack", "Gateway")

case.Apply(case.case_config)

# Start the test case
# case.Start()

# Start the test case by name
case.StartExistExample("20250507-17_47_17")

# Monitor the test execution
case.Monitor()

# Retrieve and get the test results layer2
case.Getresult()

# Generate Report
case.Generate_Report()

# Get Summary
case.Get_Summary()

# Download Report Files
# case1.Down_Report("html")
# case1.Down_Report("html, pdf")
# case1.Down_Report("html, pdf, word")
case.DownLoad_Report("html,pdf,word,excel")
