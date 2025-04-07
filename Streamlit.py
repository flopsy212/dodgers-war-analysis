import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# データ読み込み
df = pd.read_csv("nl_west_2024_stats.csv")

# 指標とチームを選ぶ
metric = st.selectbox("📊 比較する指標を選んでください", ["OPS", "WAR", "AVG", "HR"])
teams = st.multiselect("🏟 比較するチームを選んでください", df["Team"].unique(), default=["Dodgers", "Padres"])

# 選択チームのデータだけ抽出
df_selected = df[df["Team"].isin(teams)]

# 選手名の表示形式を「名前（チーム）」にしてわかりやすく
df_selected["Label"] = df_selected["Name"] + " (" + df_selected["Team"] + ")"

# 棒グラフ表示
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(df_selected["Label"], df_selected[metric], color="mediumseagreen")

# ラベル調整
ax.set_title(f"{' vs '.join(teams)} の選手別 {metric}", fontsize=14)
ax.set_ylabel(metric)
ax.set_xticks(range(len(df_selected)))
ax.set_xticklabels(df_selected["Label"], rotation=45, ha='right')

# 数値表示
for bar in bars:
    height = bar.get_height()
    label = f"{height:.3f}" if metric in ["OPS", "AVG"] else f"{height:.1f}"
    ax.annotate(label, xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9)

# 表示
st.pyplot(fig)
