# Lab Environment

## Host Machine

- **Operating System:** Windows
- **Hypervisor:** Oracle VirtualBox
- **Terminal:** Windows Terminal or PowerShell

## Virtual Machine

- **Operating System:** Ubuntu Server 22.04 LTS
- **Memory:** 2048 MB (2 GB)
- **CPU:** 2 vCPUs
- **Disk:** 25 GB
- **EFI:** Disabled

## Network Configuration

### Adapter 1

- **Type:** NAT
- **Purpose:** Provides internet access for system updates and package installation.

### Adapter 2

- **Type:** Host-Only Adapter
- **Purpose:** Allows SSH access from the Windows host to the Ubuntu Server VM.

Example Host-Only IP:

```text
192.168.56.101
```

## SSH Access

Example command:

```bash
ssh markunfold@192.168.56.101
```

## Initial System Update

```bash
sudo apt update
sudo apt upgrade -y
```

## Basic Tools Installed

```bash
sudo apt install -y \
	git \
	curl \
	wget \
	vim \
	nano \
	htop \
	tree \
	unzip \
	net-tools
```

## Repository Environment

- **Repository:** sysinfo-py
- **Runtime:** Python 3
- **Main Dependency:** psutil==7.2.2
- **Virtual Environment Path:** venv/

## Project Setup

From the repository root:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run Commands

From the repository root with the virtual environment activated:

```bash
python src/sysinfo.py
python src/sysinfo.py --export json
python src/sysinfo.py --export json --output test.json
```

## Expected Outputs

- Terminal report with host, CPU, memory, disk, uptime, and logged-in users.
- JSON report written to report.json by default.
- Custom JSON report when --output is provided.
