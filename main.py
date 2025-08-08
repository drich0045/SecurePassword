from analyzer import analyze_password

def main():
    print("Welcome to SecurePass Vault – Password Analyzer")
    while True:
        pw = input("Enter a password to check (or type 'exit'): ")
        if pw.lower() == 'exit':
            print("Exiting.")
            break
        result = analyze_password(pw)
        print(result, "\n")

if __name__ == "__main__":
    main()
