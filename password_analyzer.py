# === Personal Password Analyzer ===

def analyze_password(password):
    score = 0
    tips = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        tips.append("Make it at least 8 characters long.")

    # Check for uppercase letters
    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Add some uppercase letters.")

    # Check for lowercase letters
    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Add some lowercase letters.")

    # Check for numbers
    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Add some numbers.")

    # Check for special characters
    special_chars = "!@#$%^&*()-_+=<>?/|"
    if any(c in special_chars for c in password):
        score += 1
    else:
        tips.append("Add special characters like !@#$%^&*.")

    # Display strength
    if score == 5:
        print("Password strength: Excellent! 🔒")
    elif score >= 3:
        print("Password strength: Good 🙂")
    else:
        print("Password strength: Weak ⚠️")

    # Display tips
    if tips:
        print("\nTips to improve your password:")
        for tip in tips:
            print("-", tip)

# Main program
print("=== Personal Password Analyzer ===")
user_password = input("Enter your password to check: ")
analyze_password(user_password)