# ⚾ dodgers-war-analysis

2025年のMLBナ・リーグ西地区（NL West）における主力スタメン選手の成績（OPS・WAR・AVG・HR）を、可視化・分析・予測するStreamlitアプリです。

過去3年分（2022〜2024年）のデータを使い、
**チーム力・補強状況・打線の厚み** を比較・分析できます。

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

📋 スタメン45人の成績表示（OPS / WAR / AVG / HR）
📊 棒グラフ：指標順で並べ、チーム別に色分け
🧯 ヒートマップ：選手 × 指標の成績を濃淡で可視化
📈 チーム平均線の表示
🧭 タブ切替UI：棒グラフ・ヒートマップをスムーズに切り替え
🆕 補強選手の抽出機能
※2025年シーズン開始時点で新たにNL西地区に加わった選手に New=True フラグを設定。移籍タイミングではなく実質的な所属変更をベースに定義しています。

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

## 🖥 Streamlitで作ったアプリUI
![image](https://github.com/user-attachments/assets/0525bad4-9b0b-4e1d-9318-d700ae466535)

選手別に指標を比較したり、補強選手だけを抽出することも可能です。
平均線・チーム別色分け・ヒートマップなども対応済み。

### 📊 棒グラフ画面
![image](https://github.com/user-attachments/assets/1f0f4e00-be07-4123-bbf6-4d6e8744ad56)


### 🔥 ヒートマップ画面
![image](https://github.com/user-attachments/assets/5e815c95-740a-4f41-a811-a1aa7da090f9)


🔗 アプリはこちらから試せます！
https://dodgers-war-analysis-n2ayxkwwwkftewh7crwyv4.streamlit.app/

---
## 🧠 スキル活用ポイント

本プロジェクトでは以下のスキルを総合的に活用しています：

- Python（pandas, matplotlib, seaborn, Streamlit）による**データ加工・可視化**
- pybaseball等のAPI利用による**データ収集・自動化**
- LightGBMを用いた**HR予測モデルの構築と検証**
- フロント〜バックまで**一人で完結できる分析パイプラインの設計力**

---

> qiita: [https://qiita.com/flopsy_tech/items/76eeaff297c819e66e28]

