import psutil
import subprocess

def get_system_info():
    """System ka CPU, RAM, aur Disk usage return karta hai."""
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent
    }

def check_docker():
    """Running Docker containers ki list nikalta hai."""
    try:
        result = subprocess.run(
            ["docker", "ps", "--format", "{{.Names}} | {{.Status}}"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode != 0:
            return "Docker chal nahi raha ya permission issue hai."
        return result.stdout.strip() if result.stdout.strip() else "Koi running container nahi hai."
    except FileNotFoundError:
        return "Docker installed nahi hai."

def analyze_log_file(file_path):
    """Log file padh kar INFO, WARNING, ERROR count karta hai."""
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        
        # Simple counting logic
        info_count = text.upper().count("INFO")
        warning_count = text.upper().count("WARNING")
        error_count = text.upper().count("ERROR")
        
        return f"Log Analysis: INFO={info_count}, WARNING={warning_count}, ERROR={error_count}"
    except FileNotFoundError:
        return "Error: Log file nahi mili."