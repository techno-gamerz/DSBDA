# Group A1 - Hadoop installation (single node and multi node)

Aim
- Install and configure Hadoop in pseudo-distributed (single node) and multi-node modes.

Tools and environment
- Ubuntu (native or VM/WSL)
- JDK 7+ (JDK 8 or 11 recommended)
- OpenSSH client/server
- Hadoop (examples use 3.0.0, adjust paths if you use another version)

Files
- config/ sample XML files you can copy into $HADOOP_HOME/etc/hadoop
- scripts/verify_env.ps1, scripts/verify_env.sh check Java and Hadoop in PATH

Single node (pseudo-distributed) steps
1. Install Java and SSH:
   ```bash
   sudo apt-get update
   sudo apt-get install default-jdk openssh-server rsync
   java -version
   ```
2. Create a Hadoop user:
   ```bash
   sudo addgroup hadoop
   sudo adduser --ingroup hadoop hduser
   sudo adduser hduser sudo
   ```
3. Download and install Hadoop:
   ```bash
   wget https://archive.apache.org/dist/hadoop/core/hadoop-3.0.0/hadoop-3.0.0.tar.gz
   tar -xvf hadoop-3.0.0.tar.gz
   sudo mv hadoop-3.0.0 /usr/local/hadoop
   sudo chown -R hduser:hadoop /usr/local/hadoop
   ```
4. Set environment variables in ~/.bashrc:
   ```bash
   export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
   export HADOOP_HOME=/usr/local/hadoop
   export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
   export HADOOP_MAPRED_HOME=$HADOOP_HOME
   export HADOOP_COMMON_HOME=$HADOOP_HOME
   export HADOOP_HDFS_HOME=$HADOOP_HOME
   export YARN_HOME=$HADOOP_HOME
   export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
   export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
   ```
   ```bash
   source ~/.bashrc
   ```
5. Set JAVA_HOME in $HADOOP_HOME/etc/hadoop/hadoop-env.sh:
   ```bash
   export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
   ```
6. Configure Hadoop XML files (or copy from config/ and edit values):
   core-site.xml
   ```xml
   <configuration>
     <property>
       <name>fs.defaultFS</name>
       <value>hdfs://localhost:9000</value>
     </property>
   </configuration>
   ```
   mapred-site.xml
   ```xml
   <configuration>
     <property>
       <name>mapreduce.framework.name</name>
       <value>yarn</value>
     </property>
   </configuration>
   ```
   hdfs-site.xml
   ```xml
   <configuration>
     <property>
       <name>dfs.replication</name>
       <value>1</value>
     </property>
     <property>
       <name>dfs.namenode.name.dir</name>
       <value>file:/usr/local/hadoop_tmp/hdfs/namenode</value>
     </property>
     <property>
       <name>dfs.datanode.data.dir</name>
       <value>file:/usr/local/hadoop_tmp/hdfs/datanode</value>
     </property>
   </configuration>
   ```
   ```bash
   sudo mkdir -p /usr/local/hadoop_tmp/hdfs/namenode
   sudo mkdir -p /usr/local/hadoop_tmp/hdfs/datanode
   sudo chown -R hduser:hadoop /usr/local/hadoop_tmp
   ```
   yarn-site.xml
   ```xml
   <configuration>
     <property>
       <name>yarn.nodemanager.aux-services</name>
       <value>mapreduce_shuffle</value>
     </property>
     <property>
       <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
       <value>org.apache.hadoop.mapred.ShuffleHandler</value>
     </property>
   </configuration>
   ```
7. Configure passwordless SSH:
   ```bash
   ssh-keygen -t rsa -P ""
   cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
   ssh localhost
   exit
   ```
8. Format HDFS (run once):
   ```bash
   hadoop namenode -format
   ```
9. Start services:
   ```bash
   start-dfs.sh
   start-yarn.sh
   ```
10. Verify:
   ```bash
   jps
   ```
   - NameNode UI: http://localhost:9870 (Hadoop 3.x) or http://localhost:50070 (Hadoop 2.x)
   - ResourceManager UI: http://localhost:8088

Multi-node steps (1 master, 1+ workers)
1. Ensure hostnames resolve across nodes (update /etc/hosts).
2. Install Java on all nodes, disable IPv6 if required:
   ```bash
   sudo sed -i 's/net.ipv6.bindv6only\ =\ 1/net.ipv6.bindv6only\ =\ 0/' \
     /etc/sysctl.d/bindv6only.conf && sudo invoke-rc.d procps restart
   ```
3. Create a Hadoop user on master and workers, then configure passwordless SSH from master.
4. Install Hadoop on all nodes and set the same ~/.bashrc variables.
5. Update XML configs with master hostname and desired ports. Typical changes:
   - core-site.xml: fs.defaultFS = hdfs://master-host:9000 (or your chosen port)
   - hdfs-site.xml: dfs.replication = 2 (or number of workers)
   - yarn-site.xml: yarn.resourcemanager.* = master-host
6. Update the workers/slaves file on master with one hostname per line.
7. Format NameNode on master and start DFS/YARN from master:
   ```bash
   hadoop namenode -format
   start-dfs.sh
   start-yarn.sh
   ```
8. Verify with jps on master and workers; check ResourceManager UI.

Quick verification script
- PowerShell: scripts/verify_env.ps1
- Bash: scripts/verify_env.sh

Troubleshooting
- If Java is not found, re-check JAVA_HOME and PATH.
- If NameNode fails, clear the namenode/datanode dirs and re-run format.
- If workers do not start, verify SSH access and the workers/slaves file.
