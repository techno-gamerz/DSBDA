# Assignment A1: Hadoop Installation and Configuration

## 1. Problem Statement
Install and configure Hadoop in pseudo-distributed (single node) and multi-node modes. Demonstrate the setup by starting the NameNode, DataNode, and ResourceManager services.

## 2. Learning Objectives
- To understand the core components of the Hadoop ecosystem (HDFS and YARN).
- To learn how to configure a pseudo-distributed Hadoop cluster on a single machine.
- To understand the architecture and configuration requirements for a multi-node Hadoop cluster.

## 3. Software Requirements
- **Operating System:** Ubuntu 20.04 LTS or later (Native, VM, or WSL2)
- **Java Development Kit:** JDK 8 or JDK 11
- **SSH:** OpenSSH Server and Client
- **Hadoop:** Apache Hadoop 3.x

## 4. Hardware Requirements
- **RAM:** Minimum 4GB (8GB recommended for multi-node)
- **Storage:** 20GB free space
- **Network:** High-speed internet for downloading binaries

## 5. Implementation Steps (Pseudo-Distributed Mode)

### Reference Files
- **Configuration Templates:** [config/](config/)
  - [core-site.xml](config/core-site.xml)
  - [hdfs-site.xml](config/hdfs-site.xml)
  - [mapred-site.xml](config/mapred-site.xml)
  - [yarn-site.xml](config/yarn-site.xml)
- **Verification Scripts:** [scripts/](scripts/)
  - [verify_env.sh](scripts/verify_env.sh) (Linux/WSL)
  - [verify_env.ps1](scripts/verify_env.ps1) (PowerShell)

### Step 1: Install Prerequisites
Update the package repository and install Java and SSH.
```bash
sudo apt-get update
sudo apt-get install openjdk-8-jdk openssh-server rsync -y
java -version
```

### Step 2: Create a Dedicated Hadoop User
It is a best practice to run Hadoop services under a separate user.
```bash
sudo addgroup hadoop
sudo adduser --ingroup hadoop hduser
sudo adduser hduser sudo
```

### Step 3: Configure Passwordless SSH
Hadoop requires SSH access to manage its nodes.
```bash
su - hduser
ssh-keygen -t rsa -P ""
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
ssh localhost
exit
```

### Step 4: Download and Install Hadoop
Download the stable Hadoop binary from the Apache archive.
```bash
wget https://archive.apache.org/dist/hadoop/core/hadoop-3.3.1/hadoop-3.3.1.tar.gz
tar -xvf hadoop-3.3.1.tar.gz
sudo mv hadoop-3.3.1 /usr/local/hadoop
sudo chown -R hduser:hadoop /usr/local/hadoop
```

### Step 5: Setup Environment Variables
Add the following to `~/.bashrc`:
```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
```
Apply the changes:
```bash
source ~/.bashrc
```

### Step 6: Configure Hadoop XML Files
Update the configuration files in `$HADOOP_HOME/etc/hadoop`. You can use the templates provided in the `config/` directory of this assignment.

1. **core-site.xml:** Define the HDFS NameNode URI and temporary directory.
2. **hdfs-site.xml:** Set replication factor and metadata storage paths.
3. **mapred-site.xml:** Specify YARN as the MapReduce framework.
4. **yarn-site.xml:** Configure ResourceManager and NodeManager services.

### Step 7: Format HDFS and Start Services
Format the NameNode (run once) and start the daemons.
```bash
hdfs namenode -format
start-dfs.sh
start-yarn.sh
```

### Step 8: Verification
Check if all services are running:
```bash
jps
```
Expected output: `NameNode`, `DataNode`, `SecondaryNameNode`, `ResourceManager`, `NodeManager`.

## 6. Multi-Node Configuration Overview
1. **Host Resolution:** Map IP addresses to hostnames in `/etc/hosts`.
2. **SSH Communication:** Copy the master's SSH public key to all worker nodes.
3. **Configuration Sync:** Ensure all nodes have identical Hadoop installations and environment variables.
4. **Workers File:** List worker hostnames in `$HADOOP_HOME/etc/hadoop/workers`.
5. **Replication:** Increase `dfs.replication` in `hdfs-site.xml`.

## 7. Troubleshooting
- **Permission Denied:** Ensure the `hduser` has ownership of `/usr/local/hadoop`.
- **Java Not Found:** Verify `JAVA_HOME` in both `~/.bashrc` and `hadoop-env.sh`.
- **Connection Refused:** Check if SSH is running and passwordless access is configured correctly.
