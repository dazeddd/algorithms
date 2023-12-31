def simulate(entries):
    """
    :param entries: (list(int)) The numerical record files
    :returns: (list(int)) The record files after running the malware
    """
    # Write your code here

    entries_length = len(entries)
    
    for idx in range(entries_length-1):
        window = entries[idx:]

    return []

# 문제 이해가 안됨
if __name__ == "__main__":
    records = [1, 2, 0, 5, 0, 2, 4, 3, 3, 3]
    print(simulate(records))

    # Expected output
    # [1, 0, 0, 5, 0, 0, 0, 3, 3, 0]