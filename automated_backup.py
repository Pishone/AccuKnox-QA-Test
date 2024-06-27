import datetime
import subprocess
import paramiko

# Configuration
SOURCE_DIR = ''
REMOTE_DIR = ''
REMOTE_HOST = ''
REMOTE_USER = ''
# REMOTE_KEY = ''
REMOTE_PORT = 22
LOG_FILE = '/logs/backup.log'

# Message Logger
def log_message(message):
    with open (LOG_FILE, 'a') as f:
        f.write(f"{datetime.datetime.now()}: {message} + /n")
    print(message)

def check_ssh_connection(host, user, port):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, user, port)
        client.close()
        return True

    except Exception as e:
        log_message(f"SSH connection failed: {e}")
        return False

def backup(user, host, local_dir, remote_dir):
    try:
        rsync_command = ["rsync", "-azvP", local_dir, f"{user}@{host}:{remote_dir}"]
        result = subprocess.run(rsync_command, capture_output=True, text=True, check=True)
        if result.returncode == 0:
            log_message("Backup successful")
            log_message(result.stdout)
        else:
            log_message("Backup failed")
            log_message(result.stderr)

    except Exception as e:
        log_message(f"Backup failed due to: {e}")

def main():

    log_message("Starting Backup...")
    if not check_ssh_connection(REMOTE_HOST, REMOTE_USER, REMOTE_PORT):
        log_message("Backup failed due to SSH connection failure")
    if not backup(user=REMOTE_USER, host=REMOTE_HOST, local_dir=SOURCE_DIR, remote_dir=REMOTE_DIR):
        log_message("Connection to the remote server was successful but the backup failed...")


if __name__ == "__main__":
    main()
