#coding:utf-8
#!/usr/bin/python

import pcap
import dpkt
import sys
import ethernettype
import ethernetmac
import ethernetip
import binascii

pc = pcap.pcap()

#pc.setfilter('tcp port 80')
pc.setfilter('arp')

for i,j in pc:
        #print i
        #print pc
        tem = dpkt.ethernet.Ethernet(j)
        print "Layer2 Info:"
        print "eth.type: " + ethernettype.toName(tem.type)
        print "eth.src: " +  ethernetmac.add_colons_to_mac(binascii.hexlify(tem.src))
        print "eth.dst: " +  ethernetmac.add_colons_to_mac(binascii.hexlify(tem.dst))
        print "arp.opcode: " + str(tem.arp.op)
        print "arp.src.hw_mac " + ethernetmac.add_colons_to_mac(binascii.hexlify(tem.arp.sha))
        print "arp.dst.hw_mac " + ethernetmac.add_colons_to_mac(binascii.hexlify(tem.arp.tha))
        print "arp.src.proto_ipv4 " + ethernetip.add_point_to_ip(binascii.hexlify(tem.arp.spa))
        print "arp.dst.proto_ipv4 " + ethernetip.add_point_to_ip(binascii.hexlify(tem.arp.tpa))
        print
