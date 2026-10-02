#   This project - `security_report_analyzer.py` can eventually combine **all these data types**.

report = {
    "scan_name": "Nmap Scan",
    "target": "192.168.1.10",
    "ports": [22, 80, 443],
    "vulnerabilities": {
        "critical": 2,
        "high": 5,
        "medium": 10
    },
    "unique_ips": {
        "192.168.1.10",
        "192.168.1.11"
    },
    "scan_status": None
}

print(type(report))

#output:
 python security-report-analyzer.py
#{'scan_name': vulnerabilities': {'critical': 2, 'high': 5, 'medium': 10}, 'unique_ips': {'192.168.1.10', '192.168.1.11'}, 'scan_status': None}
#<class 'dict'>