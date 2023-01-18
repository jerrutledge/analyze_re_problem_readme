import sys

def process(threshold, limit):
    print(threshold)
    print(limit)

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

    process(threshold, limit)

if __name__ == "__main__":
    main()