# aliyun-scripts

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![GitHub all releases](https://img.shields.io/github/downloads/rgglez/aliyun-scripts/total) 
![GitHub issues](https://img.shields.io/github/issues/rgglez/aliyun-scripts) 
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/rgglez/aliyun-scripts)
![GitHub stars](https://img.shields.io/github/stars/rgglez/aliyun-scripts?style=social)
![GitHub forks](https://img.shields.io/github/forks/rgglez/aliyun-scripts?style=social)

Misc tools for "devops" in Aliyun (Alibaba Cloud).

- [aliyun-scripts](#aliyun-scripts)
    - [check-function-acceleration-status.py](#check-function-acceleration-statuspy)

<a name="#check-function-acceleration-status"></a>
### check-function-acceleration-status.py

Checks the status of the Image Acceleration process of a Function Compute container, after you updated the function with a new container (from the Personal Edition of the ECS, for instance).
It presents an indicator while the image is preparing. 

It takes these parameters:

* **-f \<function\>** the FC function name. Required.
* **-s \<service\>** the FC service name. Required.
* **-t \<seconds\>** the time in seconds between checks. Optional. Default: 2 seconds.

Examples:

```bash
python3 check-function-acceleration-status.py -s MyCoolService -f wipe-data
```

```bash
python3 check-function-acceleration-status.py -s MyCoolService -f restore-backup -t 5
```

See the source code for dependencies.

# License

Copyright (c) 2023 Rodolfo González González

Released under [GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html). Read the [LICENSE](LICENSE) file.
