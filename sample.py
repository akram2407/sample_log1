import re
import random

# Open the log file
def create_sections():
  with open('modified_log.txt', 'r') as log_file:
    # Initialize variables
    current_section_name = None
    current_section_lines = []

    # Loop through each line in the log file
    for line in log_file:
        # Check if the line starts with 'Display'
        if line.startswith('Display'):
            # If we're already in a section, print the contents of the previous section
            if current_section_name:
               if current_section_name != "processes" and current_section_name != "memory" and current_section_name != "running-config":
                    file = open(str(current_section_name),'w')
                    file.write(' '.join(current_section_lines))

                # Reset the variables for the new section
               current_section_name = None
               current_section_lines = []

            # Extract the section name from the line
            match = re.search(r'Display\s+(\S+)\s+', line)
            if match:
                current_section_name = match.group(1)

        # Add the line to the current section
        current_section_lines.append(line)

    # Print the last section
    if current_section_name:
        file = open(str(current_section_name),'w')
        file.write(' '.join(current_section_lines))

def random_mac_address():
    mac = [ 0x00, 0x16, 0x3e,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))




# Define a function to generate a random valid IP address
def random_ip_address():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

# Open the log file
with open('sample_log.txt', 'r') as log_file:
    # Read the entire file into memory
    log_data = log_file.read()

    # Use regular expressions to find all the IP addresses in the log file
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ip_addresses = re.findall(ip_pattern, log_data)
    print(ip_addresses)

    # Replace each IP address with a random valid IP address
    for ip_address in set(ip_addresses):
        random_ip = random_ip_address()
        log_data = log_data.replace(ip_address, random_ip)

    p = re.compile(r'([0-9a-f]{2}(?::[0-9a-f]{2}){5})', re.IGNORECASE)
    mac_addresses = re.findall(p, log_data)

    # Replace each MAC address with a random valid MAC address
    for mac_address in set(mac_addresses):
        random_mac = random_mac_address()
        log_data = log_data.replace(mac_address, random_mac)



    # Write the modified log data to a new file
    with open('modified_log.txt', 'w') as output_file:
        output_file.write(log_data)

create_sections()


     