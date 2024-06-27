import psutil
import logging
import subprocess

# Configuration
THRESHOLD = 80
LOG_FILE = "system_health.log"

logging.basicConfig(level=logging.DEBUG, filename=LOG_FILE, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

def log_message(message):
    logging.info(message)
    print(message)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > THRESHOLD:
        log_message(f"Alert! High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > THRESHOLD:
        log_message(f"Alert! High memory usage detected: {memory_usage}%")
    return memory_usage

def check_disk_usage():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > THRESHOLD:
        log_message(f"Alert! High disk usage detected: {disk_usage}%")
    return disk_usage

def check_running_processes():
    active_pids = len(psutil.pids())
    result = subprocess.run(["sysctl", "kernel.pid_max"], check=True, capture_output=True, text=True)
    max_pids = int(result.stdout.split('=')[1].strip())

    pid_usage = active_pids / max_pids * 100
    if pid_usage > THRESHOLD:
        log_message(f"Alert! High PID usage detected: {pid_usage}%")
    return active_pids, pid_usage

def main():
    log_message("  ______________________________  ")
    log_message("Starting System Health Monitor...")
    log_message("  ______________________________  ")
    cpu_usage = check_cpu_usage()
    memory_usage = check_memory_usage()
    disk_usage = check_disk_usage()
    active_pids, pid_usage = check_running_processes()

    log_message(f"CPU usage: {cpu_usage}%")
    log_message(f"Memory usage: {memory_usage}%")
    log_message(f"Disk usage: {disk_usage}%")
    log_message(f"Active PIDs: {active_pids}")
    log_message(f"PID usage: {pid_usage}%")
    log_message("______________________________")
    log_message("System Health Monitor finished")
    log_message("______________________________")

if __name__ == "__main__":
    main()