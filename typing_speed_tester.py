import time
import random

# Sample sentences to choose from
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Typing speed depends on practice and accuracy.",
    "Always test your code before submission.",
    "OpenAI develops powerful AI tools like ChatGPT."
]

def calculate_wpm(start_time, end_time, typed_text):
    elapsed_time = end_time - start_time
    word_count = len(typed_text.split())
    wpm = (word_count / elapsed_time) * 60
    return round(wpm, 2)

def typing_test():
    sentence = random.choice(sentences)
    print("\n📜 Type the following sentence as fast and accurately as you can:")
    print(f"👉 {sentence}\n")
    
    input("⏳ Press Enter to start typing...")
    start = time.time()
    typed = input("Your input: ")
    end = time.time()

    print("\n🕒 Time taken: {:.2f} seconds".format(end - start))

    wpm = calculate_wpm(start, end, typed)
    print("💨 Your typing speed: {} WPM".format(wpm))

    if typed.strip() == sentence.strip():
        print("✅ Accuracy: Perfect!")
    else:
        print("⚠️ Accuracy: Some mistakes detected.")

if __name__ == "__main__":
    while True:
        typing_test()
        again = input("\nDo you want to try again? (y/n): ").lower()
        if again != 'y':
            print("👋 Goodbye! Keep practicing!")
            break
