import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

def generate_network_traffic_data(num_samples):
    data = []
    anomaly_types = ['Normal', 'Intrusion Attempt', 'Port Scanning', 'DDoS Attack']
    
    for _ in range(num_samples):
        timestamp = fake.date_time_between(start_date='-1d', end_date='now')
        source_ip = fake.ipv4()
        destination_ip = fake.ipv4()
        source_port = random.randint(1024, 65535)
        destination_port = random.randint(1, 1023)
        protocol = random.choice(['TCP', 'UDP'])
        packet_length = random.randint(64, 1500)
        payload = fake.text(max_nb_chars=random.randint(10, 100))
        anomaly_type = random.choice(anomaly_types)
        label = 1 if anomaly_type != 'Normal' else 0
        
        data.append([timestamp, source_ip, destination_ip, source_port, destination_port, protocol,
                     packet_length, payload, anomaly_type, label])
    
    return data

num_samples = 10000

network_traffic_data = generate_network_traffic_data(num_samples)

columns = ['Timestamp', 'Source IP', 'Destination IP', 'Source Port', 'Destination Port',
           'Protocol', 'Packet Length', 'Payload', 'Anomaly Type', 'Label']
df = pd.DataFrame(network_traffic_data, columns=columns)

df.to_csv('network_traffic_anomaly_dataset.csv', index=False)
