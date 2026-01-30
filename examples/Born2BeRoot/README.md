# Born2BeRoot

## Description
A system administration project where you set up a virtual machine with specific configurations (LVM, SSH, UFW).

## Configuration

### LVM (Logical Volume Manager)
- Partition the disk using LVM for flexible storage management
- Create physical volumes, volume groups, and logical volumes
- Commands: `lvdisplay`, `vgdisplay`, `pvdisplay`

### SSH Configuration
- Install and configure OpenSSH server
- Change default SSH port (commonly to 4242)
- Disable root login via SSH
- Configuration file: `/etc/ssh/sshd_config`

### UFW (Uncomplicated Firewall)
- Install and enable UFW firewall
- Configure rules to allow only necessary ports
- Common commands:
  - `sudo ufw status`
  - `sudo ufw allow <port>`
  - `sudo ufw enable`

### Additional Requirements
- Configure sudo with strict rules
- Set up a strong password policy
- Create users and groups
- Implement monitoring script (optional)

## Verification
Check your configuration:
```bash
# Check LVM setup
sudo lvdisplay
sudo vgdisplay

# Check SSH status
sudo systemctl status ssh
grep Port /etc/ssh/sshd_config

# Check UFW status
sudo ufw status verbose
```
