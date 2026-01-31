def estimate_tokens(text):
    return len(text) / 4


def count_words(text):
    return len(text.split())


def analyze_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        char_count = len(content)
        word_count = count_words(content)
        token_estimate = estimate_tokens(content)
        
        print("\n" + "="*50)
        print("FILE ANALYSIS RESULTS")
        print("="*50)
        print(f"File: {filepath}")
        print(f"Character Count: {char_count:,}")
        print(f"Word Count: {word_count:,}")
        print(f"Estimated Tokens: {token_estimate:,.2f}")
        print("="*50)
        
        if char_count > 4000:
            print("\n⚠️  WARNING: This file contains more than 4000 characters!")
            print(f"   Exceeds limit by {char_count - 4000:,} characters")
            print("="*50)
        
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")


def main():
    print("="*50)
    print("TOKEN ESTIMATOR")
    print("="*50)
    print("\nThis tool estimates tokens in a file.")
    print("Assumption: 1 token = 4 characters\n")
    
    filepath = input("Enter the path to your file: ").strip()
    analyze_file(filepath)


if __name__ == "__main__":
    main()
