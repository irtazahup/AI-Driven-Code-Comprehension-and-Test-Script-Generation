import difflib

def get_code_diff(old_code, new_code):
    # This generates a 'diff' string just like Git does
    diff = difflib.unified_diff(
        old_code.splitlines(), 
        new_code.splitlines(), 
        fromfile='old_version', 
        tofile='new_version'
    )
    return '\n'.join(list(diff))

# Simulation
old_version = """
def calculate_discount(price):
    return price * 0.9
"""

new_version = """
def calculate_discount(price):
    if price > 100:
        return price * 0.8
    return price * 0.9
"""

if __name__ == "__main__":
    print("--- Detected Changes ---")
    print(get_code_diff(old_version, new_version))