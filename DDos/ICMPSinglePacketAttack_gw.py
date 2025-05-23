from ntsc import ntsc

project = ntsc.CreateProject()
project.Connect("20.1.1.100", 80)
project.Login("admin", "admin")
case = project.CreateCase("ICMPSinglePacketAttack", "Gateway")

#case.Config("TestName", "ztztzt1")
case.Config("Interface", "port1", "port2")
case.Config("InterfaceCPU", "port1:2", "port2:3")
case.Config("NetworkSubnet", {"port1": {"SubnetNumber": 1, "IpAddrRange": "18.1.2.2", "Netmask": "16", "ServerIPRange": "18.1.1.2"}})
case.Config("NetworkSubnet", {"port2": {"SubnetNumber": 1, "IpAddrRange": "18.1.1.2", "Netmask": "16"}})
case.Config("TestDuration", 10)

case.Apply(case.case_config)
case.Start()
case.Monitor()
case.Getresult()
