# ⚾ dodgers-war-analysis

2025年のMLB・ナショナルリーグ西地区（NL West）における、  
主力スタメン選手の成績（OPS・WAR・AVG・HRなど）を可視化する Streamlit アプリです。  
過去のデータ（2024年シーズン成績）を基に、チーム力・補強状況・打線の厚みを比較・分析できます。

---

## 📂 ファイル構成

| ファイル名               | 説明                                              |
|--------------------------|---------------------------------------------------|
| `streamlit_app.py`       | Streamlit アプリ本体。CSVを読み込み、指標別に可視化 |
| `nl_west_2024_stats.csv` | Dodgers・Padres・Giantsなどの主力スタメン45人分の成績データ（2024年シーズン） |

---

## 🚀 使い方

### 1. ライブラリのインストール（初回のみ）

```bash
pip install streamlit pandas matplotlib
