
# Import the ntsc module
import ntsc

# Create a new project object
project = ntsc.CreateProject()

# Connect to the server at IP address 192.168.15.100 and port 80
project.Connect("192.168.15.100", 80)

# Log in to the server with username "admin" and password "admin"
project.Login("admin", "admin")

# Create a new test case of type "Rfc2544Throughput" with the name "Gateway"
case = project.CreateCase("Rfc2544Throughput", "Gateway")

# Configure the interfaces for the test case, using port1 and port2
case.Config("Interface", "port1", "port2")

# Bind interfaces to CPU cores:
# - Bind port1 to CPU core 2
# - Bind port2 to CPU core 3
case.Config("InterfaceCPU", "port1:2", "port2:3")

# Configure network subnet settings:
# - For port1: Subnet number 1, IP address range 18.1.2.2, netmask 16 bits, server IP range 18.1.1.2
case.Config("NetworkSubnet", {"port1": {"SubnetNumber": 1, "IpAddrRange": "18.1.2.2", "Netmask": "16", "ServerIPRange": "18.1.1.2"}})

# - For port2: Subnet number 1, IP address range 18.1.1.2, netmask 16 bits
case.Config("NetworkSubnet", {"port2": {"SubnetNumber": 1, "IpAddrRange": "18.1.1.2", "Netmask": "16"}})

# Modify the variables in CaseObject. If not modified, use the default values
# case.Config("CaseObject", {"Monitor": "无"})
# case.Config("CaseObject", {"Variate": "默认邮件变量列表"})
# case.Config("CaseObject", {"WebTestProjectName": "默认网络设备测试项目"})
# case.Config("CaseObject", {"FileObject": "默认根网页请求"})
# case.Config("CaseObject", {"Monitor": "无", "Variate": "默认邮件变量列表", "WebTestProjectName": "默认网络设备测试项目", "FileObject": "默认根网页请求"})

# Modify TestDuration. If not modified, use the default values
# case.Config("TestDuration", 300)

# Modify SimUser. If not modified, use the default values
# case.Config("SimUser", 1)

# Delay jitter calculation， values: disable, enable
case.Config("Latency", "enable")

# Flow direction; the available values are: enable, disable, both.
# "enable" indicates two-way; "disable" indicates one-way; "both" means first one-way, then two-way
case.Config("DualFlowMode", "both")

# When the type of load transformation is fixed load, random load or custom load, this item needs to be specified.
case.Config("FrameSizePolicy", {
    # Frame length transformation mode; the available values are: List, Step, Random, iMix.
    # "SizeChangeMode": "List",
    # "FrameSizeFormat": "64,128,256,512,1024,1280,1518"

    "SizeChangeMode": "Step",
    "FrameSizeFormat": "64-128|+64"

    # "SizeChangeMode": "Random",
    # "FrameSizeFormat": "128-256"

    # "SizeChangeMode": "iMix"
})

# The unit of test duration; the available values are: TimeSecond, PacketCount
# case.Config("CycleDurationPolicy", {"CycleDurationUnit": "TimeSecond", "InitialCycleSecond": "600"})
case.Config("CycleDurationPolicy", {"CycleDurationUnit": "PacketCount", "InitialCyclePacket": "5000"})

# Apply all configurations to the test case
case.Apply(case.case_config)

# Start the test case
case.Start()

# Monitor the test execution
case.Monitor()

# Retrieve and get the test results layer2
case.Getresult()
