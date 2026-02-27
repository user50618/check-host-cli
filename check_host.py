#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author : Mehdi Rezaei Far

import requests
import json
import time
from urllib.parse import quote

BASE_URL = "https://check-host.net"

def normalize_node_name(node_input):
    """Convert short node names to full format"""
    node_input = node_input.strip()
    if node_input.endswith('.node.check-host.net'):
        return node_input
    elif len(node_input) <= 5 and any(c.isdigit() for c in node_input):
        return f"{node_input}.node.check-host.net"

    return node_input

def print_json(data):
    """Print data in readable JSON format"""
    print(json.dumps(data, indent=2, ensure_ascii=False))
def get_nodes_info():
    """Get and parse the complete list of checking nodes"""
    print("\n📡 Fetching nodes list...")
    try:
        response_hosts = requests.get(f"{BASE_URL}/nodes/hosts", headers={"Accept": "application/json"})
        response_hosts.raise_for_status()
        data_hosts = response_hosts.json()
        response_ips = requests.get(f"{BASE_URL}/nodes/ips", headers={"Accept": "application/json"})
        response_ips.raise_for_status()
        data_ips = response_ips.json()
        
        nodes = data_hosts.get("nodes", {})
        
        if not nodes:
            print("❌ No nodes found in the response.")
            return None
            
        print(f"\n✅ Total nodes received: {len(nodes)}")
        display_nodes_summary(nodes, data_ips.get("nodes", {}))
        return nodes
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network/HTTP error fetching nodes list: {e}")
    except json.JSONDecodeError as e:
        print(f"❌ Error decoding JSON response: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    return None

def display_nodes_summary(nodes_hosts, nodes_ips={}):
    """Display nodes information in a formatted table"""
    print("\n" + "=" * 100)
    print("🌍 AVAILABLE CHECK NODES SUMMARY")
    print("=" * 100)
    
    print(f"{'#':<4} {'Node Name':<30} {'Country':<12} {'City':<20} {'IP Address':<15} {'ASN':<12}")
    print("-" * 100)
    
    sorted_nodes = sorted(nodes_hosts.items())
    
    for idx, (node_name, node_info) in enumerate(sorted_nodes, 1):
        location = node_info.get('location', ['N/A', 'N/A', 'N/A'])
        country_code = location[0] if len(location) > 0 else 'N/A'
        country_name = location[1] if len(location) > 1 else 'N/A'
        city = location[2] if len(location) > 2 else 'N/A'
        
        country_display = f"{country_code} - {country_name}"[:12]
        
        ip = node_info.get('ip', 'N/A')
        asn = node_info.get('asn', 'N/A')
        
        if ip == 'N/A' and node_name in nodes_ips:
            ip = nodes_ips[node_name].get('ip', 'N/A')
            asn = nodes_ips[node_name].get('asn', 'N/A')
        
        ip_display = ip if len(ip) <= 15 else ip[:12] + "..."
        
        print(f"{idx:<4} {node_name:<30} {country_display:<12} {city:<20} {ip_display:<15} {asn:<12}")
    
    print("=" * 100)
    print(f"📊 Summary: Total {len(nodes_hosts)} nodes available worldwide.")
    print("💡 Tip: Use the node name (first column) when specifying specific nodes.")
    
    print("\n📈 Quick stats by region:")
    regions = {}
    for node_name, node_info in nodes_hosts.items():
        location = node_info.get('location', ['N/A'])
        country_code = location[0] if len(location) > 0 else 'N/A'
        if country_code in ['us', 'ca']:
            region = 'North America'
        elif country_code in ['gb', 'de', 'fr', 'nl', 'pl', 'se', 'no', 'fi', 'it', 'es', 'ch', 'at', 'be', 'ie', 'dk', 'cz', 'hu', 'pt', 'ro', 'bg', 'rs', 'ua', 'lt', 'si', 'hr', 'ee', 'lv', 'sk']:
            region = 'Europe'
        elif country_code in ['ir', 'tr', 'il', 'ae', 'sa', 'qa', 'kw']:
            region = 'Middle East'
        elif country_code in ['jp', 'kr', 'cn', 'tw', 'hk', 'sg', 'in', 'id', 'vn', 'th', 'my', 'ph']:
            region = 'Asia-Pacific'
        elif country_code in ['br', 'ar', 'cl', 'co', 'pe']:
            region = 'South America'
        elif country_code in ['za', 'ng', 'ke', 'eg']:
            region = 'Africa'
        else:
            region = 'Other'
        
        regions[region] = regions.get(region, 0) + 1
    
    for region, count in regions.items():
        print(f"   {region}: {count} nodes")
        
def get_node_display_name(node_name):
    """Convert full node name to shorter display name"""
    # Node name format: ir1.node.check-host.net
    parts = node_name.split('.')
    if len(parts) >= 1:
        # Return just the first part (e.g., "ir1")
        return parts[0]
    return node_name

def get_node_location_code(node_name):
    """Extract location code from node name"""
    # Extract country code from node name (e.g., "ir1" -> "IR")
    parts = node_name.split('.')
    if len(parts) >= 1:
        # Get the first part and extract letters (e.g., "ir1" -> "ir")
        node_code = parts[0]
        # Extract only alphabetic characters
        country_code = ''.join(c for c in node_code if c.isalpha()).upper()
        return country_code if country_code else "UNK"
    return "UNK"

def parse_http_results(results_data):
    """Parse and format HTTP check results"""
    parsed = {}
    for node, node_data in results_data.items():
        if node_data is None:
            parsed[node] = {"status": "pending", "message": "Still checking..."}
        elif not node_data or node_data == [[]]:
            parsed[node] = {"status": "error", "message": "No results"}
        else:
            try:
                result = node_data[0] if isinstance(node_data[0], list) else node_data
                if len(result) >= 5:
                    success = result[0]
                    response_time = result[1]
                    message = result[2]
                    status_code = result[3]
                    ip = result[4] if len(result) > 4 else "N/A"
                    
                    parsed[node] = {
                        "status": "success" if success == 1 else "failed",
                        "success": success == 1,
                        "response_time": response_time,
                        "message": message,
                        "status_code": status_code,
                        "ip": ip
                    }
                else:
                    parsed[node] = {"status": "error", "message": "Invalid data format"}
            except Exception as e:
                parsed[node] = {"status": "error", "message": f"Parse error: {str(e)}"}
    
    return parsed

def display_http_summary(parsed_results):
    """Display HTTP results in a nice table format with short node names"""
    print("\n" + "=" * 90)
    print("📊 HTTP CHECK RESULTS SUMMARY")
    print("=" * 90)
    
    # Table header with shorter column widths
    print(f"{'Node':<8} {'Country':<8} {'Status':<10} {'Code':<6} {'Time(ms)':<10} {'IP':<15} {'Message':<20}")
    print("-" * 90)
    
    for node, data in parsed_results.items():
        short_name = get_node_display_name(node)
        country = get_node_location_code(node)
        
        if data["status"] == "success":
            status = "✅ Success" if data["success"] else "⚠️ Failed"
            code = data.get("status_code", "N/A")
            time_ms = f"{data['response_time']*1000:.1f}" if data.get('response_time') else "N/A"
            ip = data.get("ip", "N/A")[:15]  # Truncate IP if too long
            message = data.get("message", "")[:20]  # Truncate message
            print(f"{short_name:<8} {country:<8} {status:<10} {code:<6} {time_ms:<10} {ip:<15} {message:<20}")
        elif data["status"] == "pending":
            print(f"{short_name:<8} {country:<8} {'⏳ Pending':<10} {'-':<6} {'-':<10} {'-':<15} {'-':<20}")
        else:
            status = "❌ Failed"
            message = data.get("message", "Error")[:30]
            # For failed connections, show the error message
            print(f"{short_name:<8} {country:<8} {status:<10} {'-':<6} {'-':<10} {'-':<15} {message:<30}")

def perform_check(check_type, host, max_nodes=3, nodes=None):
    """
    Perform a specific type of check
    
    Args:
        check_type: Type of check (ping, http, tcp, dns)
        host: Host address
        max_nodes: Maximum number of nodes
        nodes: List of specific nodes (optional)
    """
    print(f"\n🔄 Performing {check_type.upper()} check for {host}...")
    
    # Build URL
    url = f"{BASE_URL}/check-{check_type}?host={quote(host)}"
    
    # IMPORTANT FIX: If specific nodes are provided, DON'T use max_nodes
    if nodes and len(nodes) > 0:
        # Add each specific node
        for node in nodes:
            url += f"&node={quote(node)}"
        print(f"   📌 Using {len(nodes)} specific nodes")
    else:
        # Only use max_nodes when no specific nodes are provided
        url += f"&max_nodes={max_nodes}"
        print(f"   🌐 Using up to {max_nodes} random nodes")
    
    try:
        # Send check request
        response = requests.get(url, headers={"Accept": "application/json"})
        response.raise_for_status()
        result = response.json()
        
        if result.get("ok") != 1:
            print("❌ Error creating check request")
            return None
        
        print(f"\n✅ Check request registered:")
        print(f"   📋 Request ID: {result['request_id']}")
        print(f"   🔗 Permanent link: {result['permanent_link']}")
        print(f"   🌐 Number of nodes: {len(result['nodes'])}")
        
        # Check if the nodes returned match what we requested
        if nodes:
            requested_nodes = set(nodes)
            returned_nodes = set(result['nodes'].keys())
            missing_nodes = requested_nodes - returned_nodes
            if missing_nodes:
                # Convert full names to short names for display
                missing_short = [get_node_display_name(n) for n in missing_nodes]
                print(f"   ⚠️ Warning: These nodes were not found: {', '.join(missing_short)}")
        
        print("\n⏳ Waiting for results...")
        time.sleep(3)  # Wait for check to complete
        
        # Get results
        return get_check_results(result['request_id'], check_type)
        
    except Exception as e:
        print(f"❌ Error performing check: {e}")
        return None

def get_check_results(request_id, check_type):
    """Get results of a check and parse them"""
    try:
        # Get extended results
        url = f"{BASE_URL}/check-result-extended/{request_id}"
        response = requests.get(url, headers={"Accept": "application/json"})
        response.raise_for_status()
        results = response.json()
        
        print("\n📊 Raw check results (JSON):")
        print_json(results)
        
        # Parse results based on check type
        parsed_results = None
        if "results" in results:
            if check_type == "http":
                parsed_results = parse_http_results(results["results"])
                display_http_summary(parsed_results)
        
        return results
        
    except Exception as e:
        print(f"❌ Error getting results: {e}")
        return None

def main():
    """Main program with interactive menu"""
    
    print("=" * 60)
    print("🖥  Host Check Tool using check-host.net API")
    print("=" * 60)
    
    while True:
        print("\n📋 Main Menu:")
        print("   1. 🌐 Ping Check")
        print("   2. 🌐 HTTP Check")
        print("   3. 🌐 TCP Check")
        print("   4. 🌐 DNS Check")
        print("   5. 📡 View Nodes List")
        print("   6. 🚪 Exit")
        
        choice = input("\n🔷 Select option (1-6): ").strip()
        
        if choice == '6':
            print("\n👋 Goodbye!")
            break
            
        if choice == '5':
            get_nodes_info()
            continue
            
        if choice not in ['1', '2', '3', '4']:
            print("❌ Invalid option!")
            continue
        
        # Get host information
        host = input("\n🔷 Enter host address (example: google.com or https://example.com): ").strip()
        if not host:
            print("❌ Host address cannot be empty!")
            continue
        
        # Get number of nodes
        try:
            max_nodes = input("🔷 Maximum number of nodes (default 3, press Enter for default): ").strip()
            max_nodes = int(max_nodes) if max_nodes else 3
        except ValueError:
            print("⚠️  Invalid number, using default value 3")
            max_nodes = 3
        
        # Ask for specific nodes
        use_specific_nodes = input("🔷 Do you want to specify specific nodes? (y/n): ").strip().lower()
        nodes = None
        if use_specific_nodes == 'y':
            nodes_input = input("🔷 Enter node names separated by commas (example: ir1,de1,us1): ").strip()
            if nodes_input:
                raw_nodes = [n.strip() for n in nodes_input.split(',')]
                # Convert short names to full names
                nodes = [normalize_node_name(n) for n in raw_nodes]
                print(f"   📝 Converted to: {', '.join(nodes)}")
        
        # Perform check based on user choice
        check_types = {
            '1': 'ping',
            '2': 'http',
            '3': 'tcp',
            '4': 'dns'
        }
        
        check_type = check_types[choice]
        perform_check(check_type, host, max_nodes, nodes)
        
        input("\n⏎ Press Enter to continue...")

if __name__ == "__main__":
    main()