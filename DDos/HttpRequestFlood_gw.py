from ntsc import ntsc

project = ntsc.CreateProject()
project.Connect("192.168.15.180", 80)
project.Login("admin", "admin")
case = project.CreateCase("HttpRequestFlood", "Gateway")

case.Config("Interface", "port1", "port2")
case.Config("InterfaceCPU", "port1:2", "port2:3")
case.Config("NetworkSubnet", {"port1": {"SubnetNumber": 1, "IpAddrRange": "18.1.2.2+200", "Netmask": "16", "ServerIPRange": "18.1.1.2"}})
case.Config("NetworkSubnet", {"port2": {"SubnetNumber": 1, "IpAddrRange": "18.1.1.2", "Netmask": "16"}})
case.Config("TestDuration", 10)
case.Config("CaseObject", {"Variate": "无", "WebTestProjectName": "默认Web攻击测试项目", "FileObject": "默认SlowGet网页请求"})

case.Apply(case.case_config)
case.Start()
case.Monitor()
case.Getresult()
