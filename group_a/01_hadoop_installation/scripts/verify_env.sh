#!/usr/bin/env bash
set -euo pipefail

echo "JAVA_HOME: ${JAVA_HOME:-}" 
if [ -z "${JAVA_HOME:-}" ]; then
  echo "Set JAVA_HOME before running this script."
  exit 1
fi
java -version

echo "HADOOP_HOME: ${HADOOP_HOME:-}"
if [ -z "${HADOOP_HOME:-}" ]; then
  echo "Set HADOOP_HOME before running this script."
  exit 1
fi
"$HADOOP_HOME/bin/hadoop" version
