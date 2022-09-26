from __future__ import print_function
import os
import sys
import platform
import sysconfig
os.system("CLS")
print("\n\n\n\t\tSYSTEM INFORMATION\n\n")

print("os.name                      ",  os.name)
print("sys.platform                 ",  sys.platform)
print("platform.system()            ",  platform.system())
print("sysconfig.get_platform()     ",  sysconfig.get_platform())
print("platform.machine()           ",  platform.machine())
print("platform.architecture()      ",  platform.architecture())


# def linux_distribution():
#   try:
#     return platform.linux_distribution()
#   except:
#     return "N/A"

# def dist():
#   try:
#     return platform.dist()
#   except:
#     return "N/A"

# print("""Python version: %s
# dist: %s
# linux_distribution: %s
# system: %s
# machine: %s
# platform: %s
# uname: %s
# version: %s
# mac_ver: %s
# """ % (
# sys.version.split('\n'),
# str(dist()),
# linux_distribution(),
# platform.system(),
# platform.machine(),
# platform.platform(),
# platform.uname(),
# platform.version(),
# platform.mac_ver(),
# ))  
