export const prot_type = {
  0: "tcp",
  1: "udp",
  2: "icmp",
};

export const service_type = {
  0: "http",
  1: "smtp",
  2: "finger",
  3: "domain_u",
  4: "auth",
  5: "telnet",
  6: "ftp",
  7: "eco_i",
  8: "ntp_u",
  9: "ecr_i",
  10: "other",
  11: "private",
  12: "pop_3",
  13: "ftp_data",
  14: "rje",
  15: "time",
  16: "mtp",
  17: "link",
  18: "remote_job",
  19: "gopher",
  20: "ssh",
  21: "name",
  22: "whois",
  23: "domain",
  24: "login",
  25: "imap4",
  26: "daytime",
  27: "ctf",
  28: "nntp",
  29: "shell",
  30: "IRC",
  31: "nnsp",
  32: "http_443",
  33: "exec",
  34: "printer",
  35: "efs",
  36: "courier",
  37: "uucp",
  38: "klogin",
  39: "kshell",
  40: "echo",
  41: "discard",
  42: "systat",
  43: "supdup",
  44: "iso_tsap",
  45: "hostnames",
  46: "csnet_ns",
  47: "pop_2",
  48: "sunrpc",
  49: "uucp_path",
  50: "netbios_ns",
  51: "netbios_ssn",
  52: "netbios_dgm",
  53: "sql_net",
  54: "vmnet",
  55: "bgp",
  56: "Z39_50",
  57: "ldap",
  58: "netstat",
  59: "urh_i",
  60: "X11",
  61: "urp_i",
  62: "pm_dump",
  63: "tftp_u",
  64: "tim_i",
  65: "red_i",
};

export const flag_types = {
  0: "SF",
  1: "S1",
  2: "REJ",
  3: "S2",
  4: "S0",
  5: "S3",
  6: "RSTO",
  7: "RSTR",
  8: "RSTOS0",
  9: "OTH",
  10: "SH",
};

export interface nid_data {
  duration: Number;
  protocol_type: Number;
  service: Number;
  flag: Number;
  src_bytes: Number;
  dst_bytes: Number;
  land: Number;
  wrong_fragment: Number;
  urgent: Number;
  hot: Number;
  num_failed_logins: Number;
  logged_in: Number;
  num_compromised: Number;
  root_shell: Number;
  su_attempted: Number;
  num_root: Number;
  num_file_creations: Number;
  num_shells: Number;
  num_access_files: Number;
  num_outbound_cmds: Number;
  is_host_login: Number;
  is_guest_login: Number;
  count: Number;
  srv_count: Number;
  serror_rate: Number;
  srv_serror_rate: Number;
  rerror_rate: Number;
  srv_rerror_rate: Number;
  same_srv_rate: Number;
  diff_srv_rate: Number;
  srv_diff_host_rate: Number;
  dst_host_count: Number;
  dst_host_srv_count: Number;
  dst_host_same_srv_rate: Number;
  dst_host_diff_srv_rate: Number;
  dst_host_same_src_port_rate: Number;
  dst_host_srv_diff_host_rate: Number;
  dst_host_serror_rate: Number;
  dst_host_srv_serror_rate: Number;
  dst_host_rerror_rate: Number;
  dst_host_srv_rerror_rate: Number;
  pred: String;
}

export const class_type = {
  0: "normal",
  1: "buffer_overflow",
  2: "loadmodule",
  3: "perl",
  4: "neptune",
  5: "smurf",
  6: "guess_passwd",
  7: "pod",
  8: "teardrop",
  9: "portsweep",
  10: "ipsweep",
  11: "land",
  12: "ftp_write",
  13: "back",
  14: "imap",
  15: "satan",
  16: "phf",
  17: "nmap",
  18: "multihop",
  19: "warezmaster",
  20: "warezclient",
  21: "spy",
  22: "rootkit",
};

// “protocol_type”:{‘tcp': 0, 'udp': 1, 'icmp': 2}
// “service”:{‘http': 0, 'smtp': 1, 'finger': 2, 'domain_u': 3, 'auth': 4, 'telnet': 5, 'ftp': 6, 'eco_i': 7, 'ntp_u': 8, 'ecr_i': 9, 'other': 10, 'private': 11, 'pop_3': 12, 'ftp_data': 13, 'rje': 14, 'time': 15, 'mtp': 16, 'link': 17, 'remote_job': 18, 'gopher': 19, 'ssh': 20, 'name': 21, 'whois': 22, 'domain': 23, 'login': 24, 'imap4': 25, 'daytime': 26, 'ctf': 27, 'nntp': 28, 'shell': 29, 'IRC': 30, 'nnsp': 31, 'http_443': 32, 'exec': 33, 'printer': 34, 'efs': 35, 'courier': 36, 'uucp': 37, 'klogin': 38, 'kshell': 39, 'echo': 40, 'discard': 41, 'systat': 42, 'supdup': 43, 'iso_tsap': 44, 'hostnames': 45, 'csnet_ns': 46, 'pop_2': 47, 'sunrpc': 48, 'uucp_path': 49, 'netbios_ns': 50, 'netbios_ssn': 51, 'netbios_dgm': 52, 'sql_net': 53, 'vmnet': 54, 'bgp': 55, 'Z39_50': 56, 'ldap': 57, 'netstat': 58, 'urh_i': 59, 'X11': 60, 'urp_i': 61, 'pm_dump': 62, 'tftp_u': 63, 'tim_i': 64, 'red_i': 65}
// “flag”:{‘SF': 0, 'S1': 1, 'REJ': 2, 'S2': 3, 'S0': 4, 'S3': 5, 'RSTO': 6, 'RSTR': 7, 'RSTOS0': 8, 'OTH': 9, 'SH': 10}
