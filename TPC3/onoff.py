import sys
import re

def sum_values(values):
    result = 0
    for v in re.findall(r"(\d+)", values):
        result += int(v) 
    return result

def find_on_off(values):
    all_matches = re.findall(r"(?i)on(.*?)(off|\=)", values)

    result = 0
    for match in all_matches:
        result += sum_values(match[0])
        if match[1] == '=':
            print(f"Soma: {result}")
            result = 0

def main():
    text = sys.stdin.read()

    find_on_off(text)

if __name__ == "__main__":
    main()

