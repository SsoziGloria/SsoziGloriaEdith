# Assignment 3: Real world application of loop control statements

print("=" * 60)
print(" FIFA WORLD CUP 2026 SIMULATOR ")
print("You are the manager of your national team!")
print("=" * 60)

country = input("Enter your country's name: ").strip() or "Your Country"

# Team stats
morale = 70
strength = 65
injuries = 0
wins = 0
tournament_stage = 0

stages = [
    "Pre-Tournament Preparation",
    "Group Stage Match 1",
    "Group Stage Match 2",
    "Group Stage Match 3",
    "Round of 16",
    "Quarter-Final",
    "Semi-Final",
    "FINAL"
]

print(f"\nGood luck, Manager of {country}!")

# Main simulation loop
while tournament_stage < len(stages):
    current_stage = stages[tournament_stage]
    print(f"\n{'='*20} {current_stage} {'='*20}")
    print(f"Current Stats → Morale: {morale} | Strength: {strength} | Injuries: {injuries} | Wins: {wins}")
    
    # Early termination condition
    if injuries >= 8 or morale <= 10:
        print(" Your team is too injured and demoralized to continue!")
        break
    
    # User choices
    print("\nChoose your strategy:")
    print("1. Intense Training (↑ Strength, ↓ Morale, risk injury)")
    print("2. Recovery & Team Building (↑ Morale)")
    print("3. Light Training + Tactics")
    print("4. Skip this phase (risky)")
    print("5. Future feature placeholder")
    
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == "1":
        # Intense Training
        strength += 12
        morale -= 7
        if strength > 90:
            injuries += 1
            print(" Overtraining caused an injury!")
        print(" Intense training completed.")
        
    elif choice == "2":
        # Recovery
        morale += 15
        if injuries > 0:
            injuries -= 1
            print(" One injury recovered.")
        print(" Team morale significantly improved.")
        
    elif choice == "3":
        # Light Training
        strength += 6
        morale += 5
        print(" Light training and tactics session done.")
        
    elif choice == "4":
        # Skip 
        print(" Skipping this phase...")
        morale -= 10
        print("Team is less prepared for the next match.")
        tournament_stage += 1
        continue   # Skip the rest of this loop iteration
        
    elif choice == "5":
        # Demonstrates pass
        print(" Placeholder for future feature (e.g. scouting)...")
        pass
        
    else:
        print("  Invalid choice. No changes made.")
        pass   # Placeholder for invalid input
    
    # Calculate match performance (deterministic, no random)
    performance = (morale + strength) // 2 - (injuries * 8)
    if performance > 95:
        performance = 95
    elif performance < 25:
        performance = 25
    
    print(f"\nMatch Performance Score: {performance}/100")
    
    # Win or Lose based on performance
    if performance >= 60:
        print(" VICTORY! You advanced to the next stage!")
        wins += 1
        morale += 8
        strength += 4
    else:
        print(" Defeat... Your team has been eliminated!")
        morale -= 20
        injuries += 2
        break   # Exit the loop when you lose
    
    tournament_stage += 1

# Final Result
print("\n" + "=" * 60)
if wins >= 7:
    print(" CHAMPIONS OF THE WORLD! ")
    print(f"{country} has WON the 2026 FIFA World Cup!")
    print("Congratulations, Manager!")
elif wins >= 4:
    print(f"Well done {country}! You had a good run.")
else:
    print(f"Better luck next time, {country}.")
print("=" * 60)