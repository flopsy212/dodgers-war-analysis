# ⚾ dodgers-war-analysis

2025年のMLB・ナショナルリーグ西地区（NL West）における、
主力スタメン選手の成績（OPS・WAR・AVG・HRなど）を可視化、予測する Streamlit アプリです。

過去3年分（2022〜2024年）のデータを使い、
**チーム力・補強状況・打線の厚み** を比較・分析できます。

> 本当はリーグ開幕前に公開する予定でしたが、気づけばすでに20試合以上が経過…。  
> その代わり、**開幕前の予測 vs 実際の成績（4/22時点）**も追記しました！  
> 比較対象は、NL西地区の5チーム（Dodgers / Padres / Giants / DBacks / Rockies）のみです。

- Dodgers（ドジャース）
- Padres（パドレス）
- Giants（ジャイアンツ）
- DBacks（ダイヤモンドバックス）
- Rockies（ロッキーズ）

---

## 🗂 ファイル構成

| ファイル名                  | 説明                                                              |
|----------------------------|-------------------------------------------------------------------|
| `streamlit.py`             | Streamlit アプリ本体。CSVを読み込み、指標別に可視化           |
| `generate_3yr_stats.py`    | pybaseballからデータを取得してCSV化するスクリプト（2022〜2024年）|
| `nl_west_2022_2024_stats.csv` | 選手成績データ（OPS, WAR, AVG, HR, 新加入フラグ含む）           |
| `requirements.txt`         | 必要ライブラリのリスト（デプロイ用）                            |

---

## 🔧 機能一覧

- 📋 スタメン45人の成績表示（OPS / WAR / AVG / HR）
- 📊 棒グラフ：指標順で並べ、チーム別に色分け
- 🧯 ヒートマップ：選手 × 指標の成績を濃淡で可視化
- 📈 チーム平均線の表示
- 🆕 補強選手のみ抽出可能（例：大谷翔平、トミー・エドマン）
- 🧭 タブ切替UI：棒グラフ・ヒートマップをスムーズに切り替え

---

## 🚀 使い方

### 1. ライブラリのインストール（初回のみ）
```bash
pip install streamlit pandas matplotlib seaborn
```

### 2. アプリを起動
```bash
streamlit run streamlit.py
```

---

## 📌 補足

- データはFangraphs・Baseball Savant等を参照し、手動でCSV整備しました
- `generate_3yr_stats.py` を用いると、pybaseballから自動で3年分の成績取得が可能です
- アプリは [Streamlit Cloud]([https://dodgers-war-analysis-X.streamlit.app](https://dodgers-war-analysis-n2ayxkwwwkftewh7crwyv4.streamlit.app/)) で公開中です

---

## 💬 今後の展望

- 今後はOPSやWARなど他指標にも予測範囲を拡張予定
- 補強選手の “成功スコア” を定量化し、チーム間での補強インパクトを比較
- チーム戦略や起用法の「数字によるシミュレーション」や「予測 vs 実績の検証」にも挑戦予定


---

> GitHub: [https://github.com/flopsy212/dodgers-war-analysis](https://github.com/flopsy212/dodgers-war-analysis)

