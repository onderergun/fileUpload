# fileUpload
Parses through inventory downloaded from Arista CloudVision and uploads the file to target directory of every Arista device in the inventory. If not specified target directory defaults to /mnt/flash


# Usage

python fileUpload.py --username user --filename file_to_upload --inventoryname inventoryfile.csv

The above usage copies the file to /mnt/flash. If for example the target directory is /persist/secure/ the usage should be as below:

python fileUpload.py --username user --filename file_to_upload --inventoryname inventoryfile.csv --targetdir /persist/secure/
