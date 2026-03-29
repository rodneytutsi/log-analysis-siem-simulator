# alert_engine.py

# This module defines alert rules for detecting suspicious activities.

class AlertEngine:
    def __init__(self):
        self.alerts = []

    def detect_failed_login_attempts(self, login_attempts):
        if len(login_attempts) > 5:
            self.alerts.append("Multiple failed login attempts detected")

    def detect_port_scanning(self, connections):
        # Simple heuristic for port scanning detection
        scanned_ports = [connection['port'] for connection in connections]
        if len(set(scanned_ports)) > 10:
            self.alerts.append("Potential port scanning detected")

    def detect_brute_force_attack(self, login_attempts):
        # For brevity, simply checking failed attempts; this can be expanded
        self.detect_failed_login_attempts(login_attempts)
        if self.alerts:
            self.alerts.append("Brute force attack suspected")

    def detect_unusual_outbound_connections(self, outbound_connections):
        # Heuristic: If any outbound connection is to a known malicious IP
        known_malicious_ips = ["192.0.2.1", "198.51.100.1"]  # Example IPs
        for connection in outbound_connections:
            if connection['destination_ip'] in known_malicious_ips:
                self.alerts.append("Unusual outbound connection detected")

    def get_alerts(self):
        return self.alerts

if __name__ == '__main__':
    engine = AlertEngine()
    
    # Example usage
    # Suppose we have some log data to analyze:
    failed_logins = [{"username": "user1", "status": "failed"}] * 6
    connections = [{"port": 80}, {"port": 22}] * 6
    engine.detect_failed_login_attempts(failed_logins)
    engine.detect_port_scanning(connections)

    print(engine.get_alerts())