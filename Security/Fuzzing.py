from ntsc import ntsc

project1 = ntsc.CreateProject()
project1.Connect("192.168.15.97", 80)
project1.Login("admin", "admin")

case1 = project1.CreateCase("AdvancedFuzzing", "Gateway")
# case1 = project1.CreateCase("HttpCps", "Client")
case1.Config("Interface", "port1", "port2")
case1.Config("NetworkSubnet", {"port1": {"SubnetNumber": 1, "IpAddrRange": "18.1.2.2", "Netmask": "16", "ServerIPRange":"18.1.1.2"}})
case1.Config("NetworkSubnet", {"port2": {"SubnetNumber": 1, "IpAddrRange": "18.1.1.2", "Netmask": "16"}})


# test_type: AdvancedFuzzing
case1.Config("IndexStart", 1)
case1.Config("IndexEnd", "")
case1.Config("FuzzDbKeepOnlyNPassCases", 0)
case1.Config("ReuseTargetConnection", "yes")
case1.Config("Fuzzing", "UDP协议模糊测试模板")
case1.Config("ServerPort", 6001)
#UDP协议模糊测试模板,AMS协议模糊测试模版
case1.Config("TestDuration", 99999)


case1.Apply(case1.case_config)
case1.Start()
case1.Monitor()
case1.AnalysisResult()
case1.Getresult()
#case1.DownLoadLogFile(filepath="F:\\FuzzingLog")

