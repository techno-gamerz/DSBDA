Write-Host "JAVA_HOME: $env:JAVA_HOME"
if (-not $env:JAVA_HOME) {
  Write-Host "Set JAVA_HOME before running this script."
  exit 1
}
java -version

Write-Host "HADOOP_HOME: $env:HADOOP_HOME"
if (-not $env:HADOOP_HOME) {
  Write-Host "Set HADOOP_HOME before running this script."
  exit 1
}
& "$env:HADOOP_HOME\bin\hadoop.cmd" version
