"""ファーマコビジランス最前線 - プロンプト定義

海外のファーマコビジランス動向を翻訳・要約し、日本のPV実務担当者向けに再構成するプロンプト。
"""

PERSONA = """あなたはファーマコビジランス・安全性情報管理のエキスパートブロガーです。
PV業務10年以上の経験を持ち、ICSR作成、シグナル検出、PBRER作成の実務経験があります。
海外のPV規制（WHO/EMA/FDA）を日本語に翻訳・要約し、
日本の製薬企業・CROの安全性担当者にわかりやすく伝えます。

【文体ルール】
- 「です・ます」調で親しみやすく
- 専門用語（ICSR, E2B(R3), PRR, EBGM等）には必ず（）で簡単な説明を添える
- 具体的な報告フォーマット例やコーディング例を含める
- 海外ソースの情報は「出典:」を明記する
- 比較記事では必ず表形式を使用
- 記事の最初に「この記事でわかること」を箇条書きで提示

【SEOルール】
- タイトルにメインキーワードを必ず含める
- H2/H3見出しにもキーワードを自然に含める
- 冒頭150文字以内にメインキーワードを入れる
- 「結論から言うと」のパターンで冒頭にまとめを置く

【海外トレンド翻訳ルール】
- 英語の原文ニュアンスを正確に伝えつつ、日本の規制環境に置き換えて解説
- WHO/EMA/FDA要件とPMDA要件の違いを必ず補足
- 海外の事例を日本のPV実務に落とし込むアドバイスを添える
- ICH-E2B(R3)等の国際基準に沿った解説を行う
"""

ARTICLE_FORMAT = """
## この記事でわかること
（3-5個の箇条書き）

## 結論から言うと
（忙しい人向けの3行まとめ）

## {topic}とは？
（初心者向けの基礎解説）

## 実務での対応手順
（ステップバイステップ + 報告フォーマット例）

## 海外の最新動向（WHO/EMA/FDA）
（各規制当局の最新要件、ガイドライン更新情報）

## 日本（PMDA）での対応ポイント
（PMDA固有の要件、国内の実務慣行）

## 各国比較
（主要国の規制要件を表形式で比較）

## よくある質問（FAQ）
（Q&A形式 -- FAQスキーマ対応）

## まとめ
"""

CATEGORY_PROMPTS = {
    "副作用報告・ICSR": (
        "副作用報告（ICSR）の作成・提出に関する実務ガイド。"
        "ICH-E2B(R3)フォーマットに準拠した報告書作成のポイントを解説。"
        "「ICSR 作成」「副作用報告 書き方」「E2B(R3)」をキーワードに。"
    ),
    "シグナル検出": (
        "シグナル検出・評価の統計手法と実務プロセス。"
        "PRR（Proportional Reporting Ratio）、EBGM（Empirical Bayes Geometric Mean）の計算方法と解釈。"
        "「シグナル検出 PV」「PRR 計算」「EBGM 薬剤疫学」をキーワードに。"
    ),
    "PBRER/PSUR/DSUR": (
        "定期的安全性報告書（PBRER/PSUR/DSUR）の作成ガイド。"
        "ICH-E2C(R2)に基づくPBRER構成、ベネフィット・リスク評価の書き方。"
        "「PBRER 作成」「PSUR 書き方」「DSUR ガイド」をキーワードに。"
    ),
    "MedDRAコーディング": (
        "MedDRA（ICH国際医薬用語集）を使ったコーディング実務。"
        "PT/LLT/HLT/SOC各レベルの使い分け、バージョンアップ対応のポイント。"
        "「MedDRA コーディング」「MedDRA バージョン」をキーワードに。"
    ),
    "PV最新ニュース": (
        "ファーマコビジランス業界の最新ニュース・規制変更・ガイドライン更新。速報性重視。"
    ),
    "各国PV規制比較": (
        "日米欧を中心とした各国のPV規制比較。報告期限、報告基準、システム要件の違い。"
        "「PV規制 比較」「各国 副作用報告」をキーワードに。"
    ),
    "リスクマネジメント・RMP": (
        "リスクマネジメントプラン（RMP/EU-RMP/REMS）の作成と運用。"
        "リスク最小化策、追加の安全対策の実務ポイント。"
        "「RMP 作成」「リスクマネジメント 医薬品」をキーワードに。"
    ),
    "海外トレンド翻訳": (
        "海外のPV関連ニュース・ガイドライン・カンファレンス情報の日本語翻訳・要約。"
        "原文の出典URLを必ず記載。日本への影響・対応策を補足。"
    ),
}

KEYWORD_PROMPT_EXTRA = """
ファーマコビジランス（PV）に関連する日本語キーワードを提案してください。
特に以下のパターンを重視:
- 「副作用報告 ○○」「ICSR ○○」系（報告実務系）
- 「シグナル検出 ○○」「PRR ○○」「EBGM ○○」系（統計手法系）
- 「PBRER ○○」「PSUR ○○」「DSUR ○○」系（定期報告系）
- 「MedDRA ○○」系（コーディング系）
- 「PV規制 ○○」「安全性監視 ○○」系（規制対応）
- 「RMP ○○」「リスクマネジメント ○○」系（リスク管理）
- 「ファーマコビジランス 最新」系（ニュース系）
月間検索ボリュームが高いと推測されるキーワードを優先してください。
"""

AFFILIATE_SECTION_TITLE = "## PV実務に役立つリソース"
AFFILIATE_INSERT_BEFORE = "## まとめ"

NEWS_SOURCES = {
    "WHO UMC": "https://who-umc.org/news",
    "EMA Pharmacovigilance": "https://www.ema.europa.eu/en/human-regulatory-overview/pharmacovigilance-overview",
    "FDA FAERS": "https://www.fda.gov/drugs/surveillance/questions-and-answers-fdas-adverse-event-reporting-system-faers",
    "DIA PV": "https://www.diaglobal.org/resources/pharmacovigilance",
    "Drug Safety Journal": "https://link.springer.com/journal/40264",
    "PMDA安全対策": "https://www.pmda.go.jp/safety/info-services/drugs/0001.html",
    "ISPE": "https://www.pharmacoepi.org",
    "CIOMS": "https://cioms.ch/publications",
}

FAQ_SCHEMA_ENABLED = True


def build_keyword_prompt(config):
    categories_text = "\n".join(f"- {cat}" for cat in config.TARGET_CATEGORIES)
    return (
        "ファーマコビジランス最前線用のキーワードを選定してください。\n\n"
        "以下のカテゴリから1つ選び、そのカテゴリで今注目されている"
        "ファーマコビジランス関連のトピック・キーワードを1つ提案してください。\n\n"
        f"カテゴリ一覧:\n{categories_text}\n\n"
        f"{KEYWORD_PROMPT_EXTRA}\n\n"
        "以下の形式でJSON形式のみで回答してください（説明不要）:\n"
        '{"category": "カテゴリ名", "keyword": "キーワード"}'
    )


def build_article_prompt(keyword, category, config):
    category_hint = CATEGORY_PROMPTS.get(category, "")

    return f"""{PERSONA}

以下のキーワードに関する高品質なブログ記事を生成してください。
海外の最新PV動向を日本語で翻訳・要約し、日本の実務に役立つ形で再構成してください。

【基本条件】
- ブログ名: {config.BLOG_NAME}
- キーワード: {keyword}
- カテゴリ: {category}
- 言語: 日本語
- 文字数: {config.MAX_ARTICLE_LENGTH}文字程度

【カテゴリ固有の指示】
{category_hint}

【記事フォーマット】
{ARTICLE_FORMAT}

【SEO要件】
1. タイトルにキーワード「{keyword}」を必ず含めること
2. タイトルは32文字以内で魅力的に
3. H2、H3の見出し構造を適切に使用すること
4. キーワード密度は{config.MIN_KEYWORD_DENSITY}%〜{config.MAX_KEYWORD_DENSITY}%を目安に
5. メタディスクリプションは{config.META_DESCRIPTION_LENGTH}文字以内
6. FAQセクション（よくある質問）を必ず含めること

【海外トレンド翻訳の指示】
- 海外（WHO UMC、EMA、FDA、CIOMS）の最新情報を日本語で正確に翻訳・要約
- 原文の出典を「出典: [サイト名](URL)」の形で記載
- 日本（PMDA）での対応ポイント・違いを必ず補足
- ICH-E2B(R3)やICH-E2C(R2)等の国際基準を引用する場合は正確に記載

【出力形式】
以下のJSON形式で出力してください。JSONブロック以外のテキストは出力しないでください。

```json
{{
  "title": "SEO最適化されたタイトル",
  "content": "# タイトル\\n\\n本文（Markdown形式）...",
  "meta_description": "120文字以内のメタディスクリプション",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "slug": "url-friendly-slug",
  "faq": [
    {{"question": "質問1", "answer": "回答1"}},
    {{"question": "質問2", "answer": "回答2"}}
  ]
}}
```"""
