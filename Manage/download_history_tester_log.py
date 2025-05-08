from ntsc import ntsc

project1 = ntsc.CreateProject()
# Connect to the NTSC server
project1.Connect("192.168.15.180", 80)
# Login
project1.Login("admin", "admin")
# Download history tester log
project1.DownloadHistoryTesterLog("20250507-19_11_28")