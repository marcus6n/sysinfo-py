"""
sysinfo.py - System information report.
"""

import argparse
import json
import platform
import socket
import time

import psutil


def bytes_to_gb(value):
    """Convert bytes to gigabytes with 2 decimal places."""
    return round(value / 1024 / 1024 / 1024, 2)


def get_local_ip():
    """Try to detect the local IP used for outbound traffic."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("8.8.8.8", 80))
            return sock.getsockname()[0]
    except OSError:
        return "IP not found"


def get_host_info():
    """Return hostname, IP, and operating system details."""
    hostname = socket.gethostname()
    ip = get_local_ip()

    return {
        "hostname": hostname,
        "ip": ip,
        "system": platform.system(),
        "release": platform.release(),
    }


def get_cpu_info():
    """Return CPU core count and usage percentage."""
    return {
        "core_count": psutil.cpu_count(),
        "usage_percent": psutil.cpu_percent(interval=1),
    }


def get_memory_info():
    """Return total, used, and percentage of RAM."""
    memory = psutil.virtual_memory()

    return {
        "total_gb": bytes_to_gb(memory.total),
        "used_gb": bytes_to_gb(memory.used),
        "percent": memory.percent,
    }


def get_disk_info():
    """Return root partition usage details."""
    disk = psutil.disk_usage("/")

    return {
        "total_gb": bytes_to_gb(disk.total),
        "used_gb": bytes_to_gb(disk.used),
        "free_gb": bytes_to_gb(disk.free),
        "percent": disk.percent,
    }


def get_uptime():
    """Return time since boot in a human-readable format."""
    uptime_seconds = int(time.time() - psutil.boot_time())
    hours = uptime_seconds // 3600
    minutes = (uptime_seconds % 3600) // 60
    return f"{hours}h {minutes}min"


def get_logged_users():
    """Return a list of currently logged-in users."""
    return [user.name for user in psutil.users()]


def build_report():
    """Build the complete report dictionary."""
    return {
        "host": get_host_info(),
        "cpu": get_cpu_info(),
        "memory": get_memory_info(),
        "disk": get_disk_info(),
        "uptime": get_uptime(),
        "users": get_logged_users(),
    }


def print_report(report):
    """Print a formatted report to the terminal."""
    users = ", ".join(report["users"]) if report["users"] else "No users detected"

    print(
        f"Host: {report['host']['hostname']} "
        f"({report['host']['ip']}) - "
        f"{report['host']['system']} {report['host']['release']}"
    )
    print(
        f"CPU: {report['cpu']['core_count']} cores - "
        f"Usage: {report['cpu']['usage_percent']}%"
    )
    print(
        f"Memory: {report['memory']['total_gb']} GB - "
        f"Used: {report['memory']['used_gb']} GB - "
        f"Percentage: {report['memory']['percent']}%"
    )
    print(
        f"Disk: {report['disk']['total_gb']} GB - "
        f"Used: {report['disk']['used_gb']} GB - "
        f"Free: {report['disk']['free_gb']} GB - "
        f"Percentage: {report['disk']['percent']}%"
    )
    print(f"Uptime: {report['uptime']}")
    print(f"Logged-in users: {users}")


def export_json(report, path="report.json"):
    """Write the report to a JSON file."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(description="Display system information.")

    parser.add_argument(
        "--export",
        choices=["json"],
        help="Export the report to a file",
    )
    parser.add_argument(
        "--output",
        default="report.json",
        help="Output filename",
    )

    args = parser.parse_args()

    report = build_report()

    if args.export == "json":
        export_json(report, args.output)
        print(f"Report exported to {args.output}")
    else:
        print_report(report)


if __name__ == "__main__":
    main()
