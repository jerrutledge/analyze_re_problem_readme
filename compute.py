import sys

def process(threshold, limit, in_numbers):
    sum = 0
    for num in in_numbers:
        result = max(0, float(num) - threshold)
        if sum + result < limit:
            print(f'{result:.1f}')
            sum += result
        elif sum < limit:
            print(f'{limit - sum:.1f}')
            sum = limit
        else:
            print("0.0")
    print(f'{sum:.1f}')
    

def print_help():
    print("Usage: python ./compute.py threshold limit")

def main():
    if len(sys.argv) != 3:
        print_help()
        return
    try:
        threshold = float(sys.argv[1])
        limit = float(sys.argv[2])
    except ValueError as verr:
        print("Error: threshold and limit must be numbers")
        print_help()
        return

    lines = sys.stdin.readlines()
    process(threshold, limit, lines)

if __name__ == "__main__":
    main()