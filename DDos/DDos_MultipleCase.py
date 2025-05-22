from ntsc import ntsc

project1 = ntsc.CreateProject()
project1.Connect("192.168.15.248", 80)
project1.Login("admin", "admin")


result = []
for test_type in ['Ipv4FragAttack', 'ICMPSinglePacketAttack', 'IGMPv4SinglePacketAttack', 'ARPv4SinglePacketAttack', 'TCPSinglePacketAttack', 'UDPSinglePacketAttack', 'UDPPayloadAttack', 'SipSinglePacketAttack', 'DnsServiceAttack', 'DnsAmplificationAttack', 'SSDPAttack', 'NtpAmplificationAttack', 'MemcachedAmplificationAttack', 'UnknownProtocolSinglePacketAttack', 'MultiTypeFlood', 'TcpSessionFlood', 'TCPWinnuke', 'HttpRequestFlood', 'HttpMultipleRequest', 'HttpRecursionRequest', 'HTTPSlowRequestFlood', 'HttpConcurrentSlowRead', 'HttpConcurrentSlowRequest', 'HttpsFlood', 'UnicastStorm', 'BroadcastStorm', 'MulticastStorm', 'SVStormTest', 'GooseStormTest', 'MmsConnectStorm', 'LLDPStormTest']:
    case1 = project1.CreateCase(test_type, "Gateway")
    case1.Config("Interface", "port1", "port3")
    case1.Config("InterfaceCPU", "port1:2", "port3:3")
    case1.Config("NetworkSubnet", {"port1": {"SubnetNumber": 1, "IpAddrRange": "18.1.2.2", "Netmask": "16", "ServerIPRange":"18.1.1.2"}})
    case1.Config("NetworkSubnet", {"port3": {"SubnetNumber": 1, "IpAddrRange": "18.1.1.2", "Netmask": "16"}})
    case1.Config("TestDuration", 10)
    case1.Apply(case1.case_config)
    case1.Start()

    ret = case1.TestedResult()
    result.append(ret)

for ret in result:
    print(ret)