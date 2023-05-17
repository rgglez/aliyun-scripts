# check-function-acceleration-status.py
#
# Checks the status of the Image Acceleration process of a Function
# Compute container, after you updated the function with a new
# container (from the Personal Edition of the ECS, for instance).
# It presents an indicator while the image is preparing.
#
# Copyright (C) 2023 Rodolfo González González.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import subprocess
import json
import time
import sys
import getopt

def main(argv):
    status = 'Preparing'

    check = ''
    service = ''
    ttl = 2

    opts, args = getopt.getopt(argv, "f:s:t:", [])
    for opt, arg in opts:
        if opt == '-f':
            check = arg
        elif opt == '-s':
            service = arg
        elif opt == '-t':
            ttl = arg

    if check != '':
        print(status)
        i = 1
        while status == 'Preparing':
            result = subprocess.run(['aliyun', 'fc-open', 'GET', f'/2021-04-06/services/{service}/functions/{check}'], stdout=subprocess.PIPE)
            out = json.loads(result.stdout)
            status = out['customContainerConfig']['accelerationInfo']['status'].strip()
            if status == 'Preparing':
                i = i + 1
                print("█" * i, end="\r")
                time.sleep(ttl)
            elif status == 'Failed':
                print(status)
                print("\n")
                raise Exception('Image Acceleration failed.')
            elif status == 'Ready':
                print("\nImage Acceleration ready!\n")
    else:
        print("Provide the function and service names.")
# main

if __name__ == "__main__":
   main(sys.argv[1:])