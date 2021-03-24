import socket
from datetime import datetime
from argparse import ArgumentParser
import pyfiglet

parser = ArgumentParser(description="Network Scanner Build in python for windows ",epilog="""This is a description usage
    python networkscanner.py -H 192.168.1.1/24 -S 1 -L 200 """)

req_parser = parser.add_argument_group('Required Argument')

req_parser.add_argument('-H','--host',dest='host',type=str,help="specify host address",required=True)
req_parser.add_argument('-S','--start',dest='start',type=int,help="enter the starting number  ",required=True)
req_parser.add_argument('-L','--last',dest='last',type=int,help="enter the last number  ",required=True)

args= parser.parse_args()
host = args.host
start = args.start
last = args.last



class NetworkScanner(object):
   """docstring for NetworkScanner"""
   def __init__(self,host,start,last):
      self.host = host.split('.')
      self.host.pop()
      self.host = ".".join(self.host)
      self.start = start
      self.last = last
      self.Banner("Network Scanner")



   def Banner(self,name):
      banner = pyfiglet.figlet_format(name )
      print(banner)
      print("-"*50)

   def scan(self,addr):
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      socket.setdefaulttimeout(1)
      result = s.connect_ex((addr,135))
      if result == 0:
         return 1
      else:
         return 0

   def check(self):
      for ip in range(self.start,self.last+1):
         addr = self.host+str(".")+str(ip)
         if self.scan(addr):
            print(addr, "is live")

   def main(self):
      t1 = datetime.now()
      self.check()
      t2 = datetime.now()
      t = t2-t1
      print ("Network Scan is completed in: " , t)


if __name__ == '__main__':
   n = NetworkScanner(host,start,last)
   n.main()
