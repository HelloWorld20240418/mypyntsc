from ntsc import ntsc

project = ntsc.CreateProject()
project.Connect("192.168.15.97", 80)
project.Login("admin", "admin")
case = project.CreateCase("ICMPSinglePacketAttack", "Server")

case.Config("Interface", "port1")
case.Config("InterfaceCPU", "port1:2")
case.Config("NetworkSubnet", {"port1": {"SubnetNumber": 1, "IpAddrRange": "23.1.1.2", "Netmask": "16", "ServerIPRange": "23.1.1.100"}})
case.Config("TestDuration", 10)

case.Apply(case.case_config)
case.Start()
case.Monitor()
#case.Getresult()
