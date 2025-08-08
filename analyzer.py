from weak_passwords import weak_passwords

def analyze_password(pw):
    issues = []

    if pw in weak_passwords:
        issues.append(f"Weak password: {weak_passwords[pw]}")

    if len(pw) < 8:
        issues.append("Too short. Use at least 8 characters.")

    if pw.islower() or pw.isupper():
        issues.append("Use both uppercase and lowercase letters.")

    if pw.isalpha():
        issues.append("Add numbers or symbols for stronger security.")

    if not issues:
        return "Password looks strong!"
    return "\n".join(issues)
