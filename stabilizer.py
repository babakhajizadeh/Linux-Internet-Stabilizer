#!/usr/bin/env python3
import subprocess
import time
import requests
import json
import signal
import os


if os.geteuid() != 0:
    exit("You need to grant root privileges to run this script.")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def recovery():
    network_service_restart = subprocess.Popen(['sudo service NetworkManager restart'],
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.STDOUT,
                                               shell=True,)
    time.sleep(10)


def internet():
    ping = subprocess.Popen(['ping www.google.com -c 2'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            shell=True)
    time.sleep(10)
    return_code = ping.poll()

    if return_code == 0:
        return True
    else:
        return False

print("\033c", end="")
print(f"{bcolors.WARNING} ╔──────────────────────Leukocyte's Internet stabilizer ────────────────────╗{bcolors.ENDC}")
print(f"{bcolors.WARNING} | Internet connection stabilizer for persistent Remote Desktop experience. |{bcolors.ENDC}")
print(f"{bcolors.WARNING} ┖──────────────────────────────────────────────────────────────────────────┙{bcolors.ENDC}")

print(" [i] Internet connection persistency control module started.")

while True:
    # uncomment for debug: print(internet())
    if not internet():
        print(f"{bcolors.WARNING} [!] Internet connection failed!.{bcolors.ENDC}")
        print(f"{bcolors.WARNING}     Attempting to recovery...{bcolors.ENDC}")
        recovery()
        while not internet():
            recovery()
        if internet():
            print(f"{bcolors.OKBLUE} [i] Internet connection has been recovered successfully{bcolors.ENDC}")
            print(f"{bcolors.OKBLUE}     No further actions is needed{bcolors.ENDC}")

