# Simple Tournament Manager in Python

class TournamentManager:
    def __init__(self):
        self.teams = {}
    
    def add_team(self, team_name):
        """Add a new team to the tournament"""
        if team_name not in self.teams:
            self.teams[team_name] = 0
            print(f"✅ Team '{team_name}' added!")
        else:
            print("⚠️ Team already exists!")

    def record_match(self, team1, team2, score1, score2):
        """Record match results and update points"""
        if team1 not in self.teams or team2 not in self.teams:
            print("⚠️ Both teams must be registered first!")
            return
        
        if score1 > score2:
            self.teams[team1] += 3  # Win
            print(f"{team1} wins!")
        elif score2 > score1:
            self.teams[team2] += 3  # Win
            print(f"{team2} wins!")
        else:
            self.teams[team1] += 1  # Draw
            self.teams[team2] += 1
            print("It's a draw!")

    def show_standings(self):
        """Display tournament standings"""
        print("\n🏆 Tournament Standings 🏆")
        print("-" * 30)
        sorted_teams = sorted(self.teams.items(), key=lambda x: x[1], reverse=True)
        for i, (team, points) in enumerate(sorted_teams, start=1):
            print(f"{i}. {team} — {points} pts")

# -------------------------------
# Example Run
# -------------------------------

tm = TournamentManager()

while True:
    print("\n--- Tournament Menu ---")
    print("1. Add Team")
    print("2. Record Match")
    print("3. Show Standings")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        team = input("Enter team name: ")
        tm.add_team(team)

    elif choice == "2":
        t1 = input("Enter Team 1: ")
        t2 = input("Enter Team 2: ")
        s1 = int(input(f"Score for {t1}: "))
        s2 = int(input(f"Score for {t2}: "))
        tm.record_match(t1, t2, s1, s2)

    elif choice == "3":
        tm.show_standings()

    elif choice == "4":
        print("Exiting Tournament Manager... 👋")
        break

    else:
        print("Invalid choice! Please try again.")
