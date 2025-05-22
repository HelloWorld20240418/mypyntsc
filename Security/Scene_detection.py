from ntsc import ntsc

project1 = ntsc.CreateProject()
project1.Connect("192.168.15.180", 80)
project1.Login("admin", "admin")

case = project1.CreateCase("ScenarioDescrptionLanguage", "Gateway")
case.Config("Interface", "port1", "port2")
case.Config("NetworkSubnet", {"port1": {"SubnetNumber": 1, "IpAddrRange": "18.1.2.2", "Netmask": "16"}})
case.Config("NetworkSubnet", {"port2": {"SubnetNumber": 1, "IpAddrRange": "18.1.1.2-18.1.1.254", "Netmask": "16"}})
case.Config("SendWaitTime", 0)
case.Config("SendNumCyles", 1)
case.Config("ScenarioTimeout", 20)
case.Config("ScenarioInterval", 0)
case.Config("SockRecvTimeout", 15)

# test_type:ScenarioDescrptionLanguage, object
case.Config("Descrption", "无")    #默认攻击场景检测对象/无
case.Config("App_scenario", "默认应用场景对象")                    #默认应用场景对象/无
case.Config("Malware", "无")                         #默认恶意软件攻击对象/无
case.Config("Mitre", "无")                           #高级威胁组织/战术

case.Apply(case.case_config)
case.Start()
case.Monitor()
case.Getresult()
case.GenerateReport()

# Download Report Files
# case1.DownLoadReport("html, pdf, word")
case.DownLoadReport(down_file_type="word", filepath="F://Scene_detection_report")