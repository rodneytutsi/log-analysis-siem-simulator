import json
import re

class LogParser:
    def __init__(self, log_data):
        self.log_data = log_data

    def parse_json(self):
        try:
            logs = json.loads(self.log_data)
            return [self.extract_fields(log) for log in logs]
        except json.JSONDecodeError:
            print("Error decoding JSON")
            return None

    def parse_text(self):
        logs = self.log_data.strip().split('\n')
        return [self.extract_fields_from_text(log) for log in logs]

    def extract_fields(self, log):
        return {
            'timestamp': log.get('timestamp'),
            'source_ip': log.get('source_ip'),
            'destination_ip': log.get('destination_ip'),
            'event_type': log.get('event_type'),
            'severity_level': log.get('severity_level')
        }

    def extract_fields_from_text(self, log):
        pattern = re.compile(r"(?P<timestamp>[\d\-: ]+) - (?P<source_ip>[\d\.]+) -> (?P<destination_ip>[\d\.]+) : (?P<event_type>[\w\s]+) \[(?P<severity_level>[\w\s]+)\]")
        match = pattern.match(log)
        if match:
            return match.groupdict()
        else:
            return None

# Example usage (this would normally be replaced with real log data):
# log_data_json = '[{"timestamp": "2026-03-29T20:00:00Z", "source_ip": "192.168.1.1", "destination_ip": "192.168.1.2", "event_type": "login", "severity_level": "info"}]'
# log_data_text = '2026-03-29 20:00:00 - 192.168.1.1 -> 192.168.1.2 : login [info]'
# parser = LogParser(log_data_json)
# print(parser.parse_json())
# parser = LogParser(log_data_text)
# print(parser.parse_text())