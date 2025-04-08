import sys
import csv

def evaluate_jmeter_results(file_path):
    success_count = 0
    total_count = 0
    total_response_time = 0

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)  # Skip header
        for row in reader:
            total_count += 1
            if row[7] == 'true':  # success column
                success_count += 1
            total_response_time += int(row[1])  # elapsed time column

    success_rate = (success_count / total_count) * 100
    avg_response_time = total_response_time / total_count

    print(f"Success rate: {success_rate:.2f}%")
    print(f"Average response time: {avg_response_time:.2f} ms")

    # Define thresholds
    if success_rate < 95:
        print("ERROR: Success rate below threshold of 95%")
        return 1
    if avg_response_time > 500:
        print("ERROR: Average response time above threshold of 500 ms")
        return 1

    print("SUCCESS: All performance metrics within acceptable thresholds")
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python evaluate_performance.py results.jtl")
        sys.exit(1)

    exit_code = evaluate_jmeter_results(sys.argv[1])
    sys.exit(exit_code)
