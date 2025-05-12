import random

def coin_flip_simulation():
    try:
        people = int(input("Enter number of people (0–1000): "))
        flips_per_person = int(input("Enter number of flips per person (0–1000): "))

        if not (0 <= people <= 1000 and 0 <= flips_per_person <= 1000):
            print("Please enter values between 0 and 1000.")
            return

        results = []

        for person in range(people):
            flips = [random.choice(["Heads", "Tails"]) for _ in range(flips_per_person)]
            heads = flips.count("Heads")
            tails = flips.count("Tails")
            results.append((heads, tails))

        # Summary
        print("\nSimulation Summary:")
        for i, (heads, tails) in enumerate(results, start=1):
            print(f"Person {i}: {heads} Heads, {tails} Tails")

    except ValueError:
        print("Please enter valid integers.")

coin_flip_simulation()
