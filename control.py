#read mysql log file and parse it
def parse_mysql_log():
    with open("mysql.txt", "r") as f:
        logs = []
        log_lines = f.readlines()
        for line in log_lines:
            parts = line.strip().split('|')
            if len(parts) < 8:
                continue
            log_entry = {
                    "timestamp": parts[0].strip(),
                    "hostname": parts[1].strip(),
                    "username": parts[2].strip(),
                    "ip": parts[3].strip(),
                    "event": parts[4].strip(),
                    "database": parts[5].strip(),
                    "query": parts[6].strip(),
                    "error": parts[7].strip()
                }
            logs.append(log_entry)
    return logs

# Check if the query is dangerous
def is_danger(logs):
    keywords = ["DROP", "DELETE", "TRUNCATE", "ALTER", "GRANT", "REVOKE", "'1'='1'"]
    return [log for log in logs if log['query'] and any(kw in log['query'].upper() for kw in keywords)]

