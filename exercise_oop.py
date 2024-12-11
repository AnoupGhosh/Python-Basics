class Player:

    def __init__(self, name):
        self.name = name
        self.runs = 0

    def __str__(self):
        return f"Player Name: {self.name}, Runs: {self.runs}"


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def __str__(self):
        team_summary = ""
        for player in self.players:
            team_summary = team_summary + str(player) + "\n"

        return team_summary.strip()


class Match:
    def __init__(self, team):
        self.team = team
        self.score = 0
        self.wickets = 0

    def record_run(self, player_name, runs):

        for player in self.team.players:
            if player.name == player_name:
                player.runs += runs
                break
        self.score += runs

    def record_wicket(self, player_name):
        self.wickets += 1

    def summary(self):
        summary = f"Match Summary:\n"
        summary += f"Team: {self.team.team_name}\n"
        summary += f"Total Score: {self.score}\n"
        summary += f"Wickets Fallen: {self.wickets}\n"
        summary += f"Player Performances:\n"
        for player in self.team.players:
            summary += f"  {player.name}: {player.runs} runs\n"
        return summary.strip()


if __name__ == "__main__":
    # Step 1: Create a team
    team_a = Team("Team A")

    # Step 2: Add players to the team
    team_a.add_player(Player("Player A1"))
    team_a.add_player(Player("Player A2"))

    # Step 3: Start a match with Team A batting
    match = Match(team_a)

    # Step 4: Record some runs and wickets
    match.record_run("Player A1", 4)  # Player A1 hits a boundary
    match.record_run("Player A1", 1)  # Player A1 scores a single
    match.record_wicket("Player A1")  # Player A1 is out

    match.record_run("Player A2", 6)  # Player A2 hits a six

    # Step 5: Display match summary
    print(match.summary())
