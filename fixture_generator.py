# Tournament Fixture Generator in Python

def generate_fixtures(teams):
    """Generate round-robin fixtures for the given teams"""
    if len(teams) % 2 != 0:
        teams.append("Bye")  # Add a dummy team if odd number

    num_teams = len(teams)
    num_rounds = num_teams - 1
    fixtures = []

    for round in range(num_rounds):
        round_matches = []
        for i in range(num_teams // 2):
            team1 = teams[i]
            team2 = teams[num_teams - 1 - i]
            if team1 != "Bye" and team2 != "Bye":
                round_matches.append((team1, team2))
        fixtures.append(round_matches)

        # Rotate the list (except the first team)
        teams.insert(1, teams.pop())
    
    return fixtures


# -------------------------------
# Example Run
# -------------------------------
print("⚽ Tournament Fixture Generator ⚽")
teams = []

n = int(input("Enter number of teams: "))
for i in range(n):
    name = input(f"Enter team {i+1} name: ")
    teams.append(name)

fixtures = generate_fixtures(teams)

# Display Fixtures
print("\n🏆 Tournament Fixtures 🏆")
for i, round_matches in enumerate(fixtures, start=1):
    print(f"\n--- Round {i} ---")
    for match in round_matches:
        print(f"{match[0]} vs {match[1]}")
