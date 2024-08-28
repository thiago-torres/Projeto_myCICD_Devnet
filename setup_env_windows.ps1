# Define variables
$envVars = @{
    "IOS_XE_ADDRESS" = "sandbox-iosxe-recomm-1.cisco.com"
    "IOS_XE_USERNAME" = "admin"
    "IOS_XE_PASSWORD" = "C1sco12345"
    "IOS_XR_ADDRESS" = "sandbox-iosxr-1.cisco.com"
    "IOS_XR_USERNAME" = "admin"
    "IOS_XR_PASSWORD" = "C1sco12345"
    "NXOS_ADDRESS" = "sandbox-nxos-1.cisco.com"
    "NXOS_USERNAME" = "admin"
    "NXOS_PASSWORD" = "Admin_1234!"
    "DNA_ADDRESS" = "sandboxdnac2.cisco.com"
    "DNA_USERNAME" = "devnetuser"
    "DNA_PASSWORD" = "Cisco123!"
    "ACI_ADDRESS" = "sandboxapicdc.cisco.com"
    "ACI_USERNAME" = "admin"
    "ACI_PASSWORD" = "!v3G@!4@Y"
    "ISE_ADDRESS" = "devnetsandboxise.cisco.com"
    "ISE_USERNAME" = "readonly"
    "ISE_PASSWORD" = "ISEisC00L"
    "SDWAN_ADDRESS" = "sandbox-sdwan-2.cisco.com"
    "SDWAN_USERNAME" = "devnetuser"
    "SDWAN_PASSWORD" = "RG!_Yw919_83"
    "NSO_ADDRESS" = "sandbox-nso-1.cisco.com"
    "NSO_USERNAME" = "devnetuser"
    "NSO_PASSWORD" = "Services4Ever"
    "MERAKI_ADDRESS" = "account.meraki.com/secure/login/dashboard_login"
    "MERAKI_USERNAME" = "devnetmeraki@cisco.com"
    "MERAKI_PASSWORD" = "Adm!n123!"
    "MERAKI_API" = "7923dc84fe6f3a9d3bcac0e0c2bebd96ea72235d"
}

# Add environment variables globally
foreach ($var in $envVars.GetEnumerator()) {
    [System.Environment]::SetEnvironmentVariable($var.Key, $var.Value, [System.EnvironmentVariableTarget]::User)
    Write-Output "Added $($var.Key) to environment variables."
}
