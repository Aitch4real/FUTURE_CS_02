# Basic Firewall Setup on Kali Linux

This project demonstrates how to set up a basic firewall on a Kali Linux virtual machine using UFW (Uncomplicated Firewall).

## Steps

1. **Install UFW:**

   ```bash
   sudo apt update
   sudo apt install ufw
2. **Enable UFW:**


sudo ufw enable
Configure Major Firewall Rules:

Allow SSH:


sudo ufw allow ssh
Allow HTTP:


sudo ufw allow 80/tcp
Allow HTTPS:

sudo ufw allow 443/tcp
Block FTP:


sudo ufw deny 21
Allow MySQL:


sudo ufw allow 3306/tcp
Allow Specific IP:


sudo ufw allow from 192.168.1.10
Deny Specific IP:


sudo ufw deny from 203.0.113.5
Allow Specific Subnet:


sudo ufw allow from 192.168.1.0/24
Deny Specific Subnet:


sudo ufw deny from 203.0.113.0/24
Allow Port Range:


sudo ufw allow 1000:2000/tcp
Deny Port Range:


sudo ufw deny 6000:7000/tcp
Allow Outbound Traffic:


sudo ufw default allow outgoing
Deny Outbound Traffic:


sudo ufw default deny outgoing
Allow Established Connections:


sudo ufw allow in on eth0 to any port 1024:65535 proto tcp
sudo ufw allow in on eth0 to any port 1024:65535 proto udp
Check UFW Status:


sudo ufw status verbose
