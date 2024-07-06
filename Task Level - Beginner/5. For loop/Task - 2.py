'''
Imagine you are doing a workout routine, and you have to complete 100 jumping jacks.
Write a program that:
Asks you to perform 10 jumping jacks at a time.
After each set, it asks, "Are you tired?"
If you reply "yes" or "y," it should ask if you want to skip the remaining sets.
If you reply "yes" or "y," it should break and print, "You completed a total of jumping jacks."
'''

total_jumping_jacks = 100
completed_jumping_jacks = 0

while completed_jumping_jacks < total_jumping_jacks:
    print(f"Perform 10 jumping jacks ({completed_jumping_jacks + 1} to {completed_jumping_jacks + 10})")
    tired_response = input("Are you tired? (yes/y to skip remaining sets): ").lower()

    if tired_response in ["yes", "y"]:
        break


    completed_jumping_jacks += 10
    remaining_jumps = total_jumping_jacks - completed_jumping_jacks
    print(f"{remaining_jumps} jumping jacks remaining.")
    print(f"You completed a total number of {completed_jumping_jacks} jumping jacks")

if completed_jumping_jacks == total_jumping_jacks:
    print("Congratulations! You completed the workout.")
