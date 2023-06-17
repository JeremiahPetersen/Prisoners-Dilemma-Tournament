import random

class Player:
    def __init__(self, strategy):
        self.strategy = strategy
        self.opponent_last_move = "C" # Start with 'C' for 'tit_for_tat' strategy

    def make_decision(self):
        if self.strategy == "cooperate":
            return "C"
        elif self.strategy == "defect":
            return "D"
        elif self.strategy == "tit_for_tat":
            return self.opponent_last_move
        else:
            raise ValueError("Invalid strategy")

def prisoner_dilemma(player1, player2, rounds=10):
    history1 = []
    history2 = []

    for _ in range(rounds):
        decision1 = player1.make_decision()
        decision2 = player2.make_decision()
        
        player1.opponent_last_move = decision2
        player2.opponent_last_move = decision1

        history1.append(decision1)
        history2.append(decision2)

    return list(zip(history1, history2))

def calculate_payoff(history):
    payoff_matrix = {
        ("C", "C"): (3, 3),
        ("C", "D"): (0, 5),
        ("D", "C"): (5, 0),
        ("D", "D"): (1, 1)
    }

    scores = [0, 0]

    for decision1, decision2 in history:
        payoff = payoff_matrix[(decision1, decision2)]
        scores[0] += payoff[0]
        scores[1] += payoff[1]

    return scores

def main():
    strategies = ["cooperate", "defect", "tit_for_tat"]
    total_scores = {"cooperate": 0, "defect": 0, "tit_for_tat": 0}
    rounds = 10
    matches = 10

    for i in range(len(strategies)):
        for j in range(i, len(strategies)):
            for _ in range(matches):
                player1 = Player(strategies[i])
                player2 = Player(strategies[j])

                history = prisoner_dilemma(player1, player2, rounds)
                scores = calculate_payoff(history)

                total_scores[strategies[i]] += scores[0]
                total_scores[strategies[j]] += scores[1]

    for strategy in total_scores:
        total_scores[strategy] /= matches * len(strategies) * rounds

    print("Average Scores:", total_scores)

if __name__ == "__main__":
    main()