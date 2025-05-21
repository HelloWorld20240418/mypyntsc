from ntsc import ntsc

project1 = ntsc.CreateProject()
project1.Connect("192.168.15.97", 80)
project1.Login("admin", "admin")

case1 = project1.CreateCase("AdvancedFuzzing", "Gateway")
# case1 = project1.CreateCase("HttpCps", "Client")

case1.Config("Interface", "port1", "port2")
case1.Config("NetworkSubnet", {"port1": {"SubnetNumber": 1, "IpAddrRange": "18.1.2.2", "Netmask": "16", "ServerIPRange":"18.1.1.2"}})
case1.Config("NetworkSubnet", {"port2": {"SubnetNumber": 1, "IpAddrRange": "18.1.1.2", "Netmask": "16"}})


case1.Apply(case1.case_config)
case1.Start()
case1.Monitor()
case1.Getresult()

