#!/usr/bin/env python3
""" MR OPE PROGRAM """

from pymongo import MongoClient

def main():
    """ GIVE UP """

    # Connect to the MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Count the total number of logs
    total_logs_count = nginx_collection.count_documents({})
    print(f'{total_logs_count} logs')

    # Count the number of logs for each HTTP method
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in http_methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {method_count}')

    # Count the number of logs for status check
    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f'{status_check_count} status check')

    # Find the top 10 IPs by the number of requests
    top_ip_addresses = nginx_collection.aggregate([
        {"$group": {
            "_id": "$ip",
            "count": {"$sum": 1}
        }},
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    # Print the top 10 IPs
    print("IPs:")
    for ip_info in top_ip_addresses:
        ip_address = ip_info.get("ip")
        ip_count = ip_info.get("count")
        print(f'\t{ip_address}: {ip_count}')

if __name__ == "__main__":
    main()
