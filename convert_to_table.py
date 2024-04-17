import json
import requests
import markdown as md

#TODO
# if getting JSON data from an API endpoint
# response = requests.get('')
# game_score = json.loads()

def convert(game_scores):
    rows = []
    table_header = list(game_scores[0].keys())
    col_width = max(len(col) for col in game_scores[0]) + 5

    rows.append('|'.join(s.ljust(col_width) for s in table_header))
    rows.append('|'.join('-' * col_width for _ in range(len(table_header))))
    for score in game_scores:
        rows.append('|'.join(str(v).ljust(col_width) for k, v in score.items() if k in table_header))
    for row in rows:
        print(f'|{row}|')
    return rows

# def write_md(results, f):
#     for row in results:
#         # f.write(f'')
#         f.write(f"| {row[0]} | {row[1]} | {row[2]} |\n")

if __name__ == "__main__":
    with open('files/game_scores.json', 'r') as f:
        game_scores = json.load(f)
    game_score_md = convert(game_scores)
    print(game_score_md)

    # with open('leaderboard.markdown', 'w') as f:
    #     write_md(game_score_md, 'test.markdown')

