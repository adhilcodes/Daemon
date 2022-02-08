# Net-Daemon

 - Daemon is a ML-based Network Administration System
 - The data for ML model is synthetically generated
 - Decision by ML model is based on the features RAM free space, Swap memmory free space, Disk free space ,CPU idle and Load average in 3 levels
 -



### Installation  
From the root directory of the project, use the following commands install the dependencies and the command-line script.  
```bash
pip install -r requirements.txt
pip install -e .
```
A virtual environment is recommended, though not required.

### Running the Program
**Important!** Make sure that `config.yaml` is filled, and present in the working directory. The [template file](https://github.com/Mr-Skully/net-daemon/blob/main/docs/config.yaml) can be found in the `docs` directory. A [sample](https://github.com/Mr-Skully/net-daemon/blob/main/docs/example-config.yaml) config file has also been included for reference. 

To run the program, use the CLI command:
```bash
netdaemon
```
  
### To-do

- Need to automate completly using unsupervised learning
