import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns

# CSV読み込み
df = pd.read_csv("nl_west_2022~2024_stats.csv", encoding="utf-8")

# チームカラー定義
team_colors = {
    "Dodgers": "#005A9C",
    "Padres": "#2F241D",
    "Giants": "#FD5A1E",
    "DBacks": "#A71930",
    "Rockies": "#33006F"
}

# UI
st.title("2025年 NL西地区 スタメン成績可視化ツール")

metric = st.selectbox("📊 比較する指標を選んでください", ["OPS", "WAR", "AVG", "HR"])
teams = st.multiselect("🏟 比較するチームを選んでください", df["Team"].unique(), default=["Dodgers", "Padres"])
show_only_new = st.checkbox("🆕 補強選手だけを表示", value=False)

# データ選択
df_selected = df[df["Team"].isin(teams)].copy()
if show_only_new:
    df_selected = df_selected[df_selected["New"] == True]
df_selected["Label"] = df_selected["Name"] + " (" + df_selected["Team"] + ")"
df_selected = df_selected.sort_values(by=metric, ascending=False)
colors = df_selected["Team"].map(team_colors)

# タブ分岐
tab1, tab2 = st.tabs(["📊 棒グラフ", "🧯 ヒートマップ"])

with tab1:
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(df_selected["Label"], df_selected[metric], color=colors)
    ax.set_title(f"{' vs '.join(teams)} の選手別 {metric}", fontsize=14)
    ax.set_ylabel(metric)
    ax.set_xticks(range(len(df_selected)))
    ax.set_xticklabels(df_selected["Label"], rotation=45, ha='right')

    # 平均線
    for team in teams:
        team_df = df_selected[df_selected["Team"] == team]
        avg_value = team_df[metric].mean()
        ax.axhline(y=avg_value, linestyle='--', linewidth=1.2, color=team_colors[team], alpha=0.6, label=f"{team} 平均")

    # 数値ラベル
    for bar in bars:
        height = bar.get_height()
        label = f"{height:.3f}" if metric in ["OPS", "AVG"] else f"{height:.1f}"
        ax.annotate(label, xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9)

    # 凡例（平均線とチーム色を合体）
    custom_legend = [Patch(facecolor=color, label=team) for team, color in team_colors.items() if team in teams]
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))  # 重複除去
    combined_legend = list(by_label.values()) + custom_legend
    ax.legend(combined_legend, list(by_label.keys()) + [t for t in teams], title="チームと平均")

    st.pyplot(fig)

with tab2:
    heat_df = df[df["Team"].isin(teams)].copy()
    if show_only_new:
        heat_df = heat_df[heat_df["New"] == True]
    heat_df["Label"] = heat_df["Name"] + " (" + heat_df["Team"] + ")"
    heat_df = heat_df.set_index("Label")[["OPS", "WAR", "AVG", "HR"]]

    st.write("#### 選手 × 指標のヒートマップ（濃いほど高い）")
    fig2, ax2 = plt.subplots(figsize=(10, len(heat_df) * 0.4))
    sns.heatmap(heat_df, annot=True, fmt=".3f", cmap="YlGnBu", ax=ax2)
    st.pyplot(fig2)
