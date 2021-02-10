def tournamentWinner(competitions, results):
    mx = ('', 0)
    scores = {}
    for i, comp in enumerate(competitions):
        idx = 0 if results[i] else 1
        winner = comp[idx]
        scores[winner] = scores.get(winner, 0) + 3
        if scores[winner] > mx[1]:
            mx = (winner, scores[winner])
    return mx[0]

print(tournamentWinner([["AlgoMasters", "FrontPage Freebirds"],
                        ["Runtime Terror", "Static Startup"],
                        ["WeC#", "Hypertext Assassins"],
                        ["AlgoMasters", "WeC#"],
                        ["Static Startup", "Hypertext Assassins"],
                        ["Runtime Terror", "FrontPage Freebirds"],
                        ["AlgoMasters", "Runtime Terror"],
                        ["Hypertext Assassins", "FrontPage Freebirds"],
                        ["Static Startup", "WeC#"],
                        ["AlgoMasters", "Static Startup"],
                        ["FrontPage Freebirds", "WeC#"],
                        ["Hypertext Assassins", "Runtime Terror"],
                        ["AlgoMasters", "Hypertext Assassins"],
                        ["WeC#", "Runtime Terror"],
                        ["FrontPage Freebirds", "Static Startup"]],
                        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]))