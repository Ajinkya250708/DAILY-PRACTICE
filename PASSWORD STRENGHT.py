def password_checker():
    password = input("Enter your password: ")
    
    length_ok = len(password) >= 8
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True
    
    score = sum([length_ok, has_upper, has_lower, has_digit, has_special])
    
    print("\n----- PASSWORD CHECK -----")
    print("Length >= 8:", "✅" if length_ok else "❌")
    print("Has Uppercase:", "✅" if has_upper else "❌")
    print("Has Lowercase:", "✅" if has_lower else "❌")
    print("Has Digit:", "✅" if has_digit else "❌")
    print("Has Special Character:", "✅" if has_special else "❌")
    
    if score == 5:
        print("\nPassword Strength: STRONG 💪")
    elif score >= 3:
        print("\nPassword Strength: MEDIUM 👍")
    else:
        print("\nPassword Strength: WEAK ⚠️")

password_checker()