import random
import time

def get_random_sentence():
    # List of sentences for the typing test
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "She sells seashells by the seashore.",
        "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
        "Peter Piper picked a peck of pickled peppers.",
        "Sally sells sea shells by the sea shore."
        # Add more sentences here
    ]
    # Choose a random sentence from the list
    return random.choice(sentences)

def calculate_typing_speed(start_time, end_time, typed_text):
    # Calculate the elapsed time in seconds
    elapsed_time = end_time - start_time
    # Calculate the typing speed in words per minute (WPM)
    # We assume that the average word takes 5 characters, including spaces
    typedwords= len(typed_text) / 5
    minutes = elapsed_time / 60
    wpm = typedwords/ minutes
    return wpm

def calculate_accuracy(original_text, typed_text):
    # Split the original and typed texts into individual words
    initialwords = original_text.split()
    typed_words = typed_text.split()

    # Initialize a variable to count the number of correctly typed words
    correct_words = 0

    # Compare each word in the original and typed texts
    for i in range(min(len(initialwords), len(typed_words))):
        if initialwords[i] == typed_words[i]:
            correct_words += 1

    # Calculate the accuracy as a percentage
    accuracy = (correct_words / len(initialwords)) * 100
    return accuracy

def main():
    print("Welcome to the Speed Typing Test! By-Aryan")
    print("Type the following sentence as fast and accurately as possible:")
    # Get a random sentence for the typing test
    sentence = get_random_sentence()
    print(sentence)

    # Prompt the user to start the test
    input("Press Enter when you are ready to start.")
    # Record the starting time
    start_time = time.time()

    # Get the user's typed text
    typed_text = input("Start typing: ")
    # Record the ending time
    end_time = time.time()

    # Calculate and display the typing speed and accuracy
    typing_speed = calculate_typing_speed(start_time, end_time, typed_text)
    accuracy = calculate_accuracy(sentence, typed_text)

    print(f"Typing Speed: {typing_speed:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "_main_":
    main()