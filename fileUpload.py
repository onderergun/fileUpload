import paramiko
from scp import SCPClient
import csv
from getpass import getpass
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--username', required=True)
parser.add_argument('--filename', required=True)
parser.add_argument('--inventoryname', required=True)
parser.add_argument('--targetdir', default="/mnt/flash/")


args = parser.parse_args()
username = args.username
filename = args.filename
inventory = args.inventoryname
targetdir = args.targetdir
password = getpass()

cwd = os.getcwd()
  
def ssh_scp_files(ssh_host, ssh_user, ssh_password, ssh_port, source_volume, destination_volume):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(ssh_host, username=ssh_user, password=ssh_password, look_for_keys=False)

    with SCPClient(ssh.get_transport()) as scp:
        scp.put(source_volume, recursive=False, remote_path=destination_volume)

filepathSource = cwd + "/"+ filename
filepathTarget = targetdir + filename
with open(inventory) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for iter,row in enumerate(csv_reader):
       if iter == 0 :
           for num,column in enumerate(row):
               if column == "IP Address" or column == "IPAddress":
                   hostIndex=num
       else:
           ssh_host=row[hostIndex]
           print ssh_host
           ssh_scp_files(ssh_host, username, password, "22", filepathSource,filepathTarget)
     
