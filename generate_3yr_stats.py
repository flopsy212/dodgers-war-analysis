# filename: generate_3yr_stats.py

import pandas as pd
from pybaseball import batting_stats

# 対象選手リスト（チーム混合・姓名形式で統一）
players = [
    "Shohei Ohtani", "Freddie Freeman", "Mookie Betts", "Teoscar Hernandez", "Max Muncy",
    "Will Smith", "Michael Conforto", "Gavin Lux", "Tommy Edman", "Luis Arraez",
    "Fernando Tatis Jr.", "Jackson Merrill", "Manny Machado", "Jake Cronenworth",
    "Xander Bogaerts", "Jason Heyward", "Gavin Sheets", "Elias Diaz"
]

# 対象年（2022～2024）
years = [2022, 2023, 2024]

# 全データをまとめて入れるリスト
all_data = []

for year in years:
    print(f"{year}年のデータを取得中...")
    stats = batting_stats(year)
    stats["Season"] = year  # 年を追加

    for player in players:
        row = stats[stats["Name"] == player]
        if not row.empty:
            row["Name"] = player  # 名前統一
            all_data.append(row)

# 1つのDataFrameに統合
df_all = pd.concat(all_data, ignore_index=True)

# 必要な列だけ抽出（自由に変えてOK）
columns = ["Season", "Name", "Team", "OPS", "AVG", "WAR", "HR"]
df_final = df_all[columns]

# CSVとして保存
df_final.to_csv("player_3yr_stats.csv", index=False, encoding="utf-8-sig")

print("✅ CSV出力完了: player_3yr_stats.csv")
