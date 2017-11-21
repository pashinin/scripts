# -*- mode: hcl -*-


# node_name = "server451"  # By default this is the hostname of the machine.
datacenter = "moscow"

bootstrap = false
server = true
data_dir = "/var/consul"

# TRACE DEBUG INFO WARN ERR
log_level = "ERR"

bind_addr="10.254.239.0"

addresses {
  http = "0.0.0.0"
  dns = "0.0.0.0"
}

# telemetry {
#   statsite_address = "10.254.239.1:2180"
# }

# performance {
#   raft_multiplier = 1
#   rpc_hold_timeout = "1s"
# }
enable_script_checks = true

services = [
  {
    id = "red0"
    name = "redis"
    tags = [
      "primary"
    ]
    address = ""
    port = 6000
    checks = [
      {
        script = "service redis-server status"
        interval = "60s"
      }
    ]
  }
]
