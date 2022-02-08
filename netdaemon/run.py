from sys import exit

from netdaemon.util.files import get_past_devices, get_config, save_results
from netdaemon.util.network import get_stats, send_email, ssh_scan
from netdaemon.model.classifier import decide

# TODO: Documentation and type-hinting

RETRIES = 2

def main():
    # Read config from file
    settings = get_config()
    verbose = settings['verbose']
    if verbose:
        print(f"[.] Scanning in subnet {settings['subnet']}")
    # Discover devices on the network that accept SSH connections
    device_list = ssh_scan(settings['subnet'])
    if device_list is None:
        exit(1)
    if verbose:
        print("[.] Devices discovered: " + ", ".join(device_list))    

    past_devices = get_past_devices(verbose)
    retry_list = list(past_devices.difference(device_list))
    completed_list = []

    while device_list:
        stats = get_stats(host=device_list[0],
                          user=settings['ssh']['username'],
                          password=settings['ssh']['password'],
                          verbose=verbose)
        if verbose:
            print(f"[.] Stats for {device_list[0]}:")
            print(stats)
        decision = decide(stats, verbose)
        if decision == 0:
            print(f"[.] {device_list[0]} is healthy. Assign a new job.")
            completed_list.append(device_list.pop(0))
        elif decision == 1:
            print(f"[.] {device_list[0]} is busy. Not ready to accept new jobs.")
            completed_list.append(device_list.pop(0))
        else:
            print(f"[x] {device_list[0]} is not responding correctly. Adding to retry list.")
            retry_list.append(device_list.pop(0))
        
    for _ in range(RETRIES):
        i = 0
        while i < len(retry_list):
            stats = get_stats(host=retry_list[i],
                          user=settings['ssh']['username'],
                          password=settings['ssh']['password'],
                          verbose=verbose)
            if verbose:
                print(f"[.] Stats for {retry_list[i]}:")
                print(stats)
            decision = decide(stats, verbose)
            if decision == 0:
                print(f"[.] {retry_list[i]} is healthy. Assign a new job.")
                completed_list.append(retry_list.pop(i))
            elif decision == 1:
                print(f"[.] {retry_list[i]} is busy. Not ready to accept new jobs.")
                completed_list.append(retry_list.pop(i))
            else:
                print(f"[x] {retry_list[i]} is not responding correctly.")
                i += 1
    
    save_results(completed_list, verbose)

    if retry_list:
        send_email( host = settings['smtp']['host'],
                    port = settings['smtp']['port'],
                    id = settings['smtp']['id'],
                    password = settings['smtp']['password'],
                    receipient = settings['admin-email'], 
                    device_list = retry_list,
                    verbose = verbose)
    
if __name__ == "main":
    main()
