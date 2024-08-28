#!/bin/bash

# Check which shell initialization file is being used (.bashrc or .zshrc)
SHELL_RC="$HOME/.bashrc"
if [ -n "$ZSH_VERSION" ]; then
  SHELL_RC="$HOME/.zshrc"
fi

# Function to add a variable if not already present
add_variable() {
  local var_name="$1"
  local var_value="$2"

  if ! grep -q "export $var_name=" "$SHELL_RC"; then
    echo "export $var_name=\"$var_value\"" >> "$SHELL_RC"
    echo "Added $var_name to $SHELL_RC."
  else
    echo "$var_name is already configured in $SHELL_RC."
  fi
}

# Add a timestamp to the file if it hasn't been added already
if ! grep -q "# Cisco Sandbox environment variables" "$SHELL_RC"; then
  echo "" >> "$SHELL_RC"
  echo "# Cisco Sandbox environment variables (Added on $(date))" >> "$SHELL_RC"
fi

# Define variables to be added
add_variable "IOS_XE_ADDRESS" "sandbox-iosxe-recomm-1.cisco.com"
add_variable "IOS_XE_USERNAME" "admin"
add_variable "IOS_XE_PASSWORD" "C1sco12345"

add_variable "IOS_XR_ADDRESS" "sandbox-iosxr-1.cisco.com"
add_variable "IOS_XR_USERNAME" "admin"
add_variable "IOS_XR_PASSWORD" "C1sco12345"

add_variable "NXOS_ADDRESS" "sandbox-nxos-1.cisco.com"
add_variable "NXOS_USERNAME" "admin"
add_variable "NXOS_PASSWORD" "Admin_1234!"

add_variable "DNA_ADDRESS" "sandboxdnac2.cisco.com"
add_variable "DNA_USERNAME" "devnetuser"
add_variable "DNA_PASSWORD" "Cisco123!"

add_variable "ACI_ADDRESS" "sandboxapicdc.cisco.com"
add_variable "ACI_USERNAME" "admin"
add_variable "ACI_PASSWORD" "!v3G@!4@Y"

add_variable "ISE_ADDRESS" "devnetsandboxise.cisco.com"
add_variable "ISE_USERNAME" "readonly"
add_variable "ISE_PASSWORD" "ISEisC00L"

add_variable "SDWAN_ADDRESS" "sandbox-sdwan-2.cisco.com"
add_variable "SDWAN_USERNAME" "devnetuser"
add_variable "SDWAN_PASSWORD" "RG!_Yw919_83"

add_variable "NSO_ADDRESS" "sandbox-nso-1.cisco.com"
add_variable "NSO_USERNAME" "devnetuser"
add_variable "NSO_PASSWORD" "Services4Ever"

add_variable "MERAKI_ADDRESS" "account.meraki.com/secure/login/dashboard_login"
add_variable "MERAKI_USERNAME" "devnetmeraki@cisco.com"
add_variable "MERAKI_PASSWORD" "Adm!n123!"
add_variable "MERAKI_API" "7923dc84fe6f3a9d3bcac0e0c2bebd96ea72235d"

# Optionally, reload the shell configuration file
echo "To apply the changes, run: source $SHELL_RC"
