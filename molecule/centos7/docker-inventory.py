# Connect to the Docker API on localhost port 4243 and format the JSON output
DOCKER_HOST="tcp://localhost:4243 /ressources/docker-inventory.py --pretty"

# Any container's ssh port exposed on 0.0.0.0 will be mapped to
# another IP address (where Ansible will attempt to connect via SSH)
DOCKER_DEFAULT_IP="$$$_MYIP_$$$ /ressources/docker-inventory.py --pretty"