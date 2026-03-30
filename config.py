"""ファーマコビジランス最前線 - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "ファーマコビジランス最前線"
BLOG_DESCRIPTION = (
    "医薬品の安全性監視（ファーマコビジランス）の実務知識を毎日更新。"
    "海外の最新PV動向・副作用報告規制を日本語で翻訳・要約し、実務担当者向けに解説。"
)
BLOG_URL = "https://musclelove-777.github.io/pv-frontline"
BLOG_TAGLINE = "海外PV動向を日本語で翻訳・要約"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/pv-frontline"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "副作用報告・ICSR",
    "シグナル検出",
    "PBRER/PSUR/DSUR",
    "MedDRAコーディング",
    "PV最新ニュース",
    "各国PV規制比較",
    "リスクマネジメント・RMP",
    "海外トレンド翻訳",
]

THEME = {
    "primary": "#ea580c",
    "accent": "#9a3412",
    "gradient_start": "#ea580c",
    "gradient_end": "#c2410c",
    "dark_bg": "#1c1917",
    "dark_surface": "#292524",
    "light_bg": "#fff7ed",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 1
SCHEDULE_HOURS = [8]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "Amazon PV書籍": {
        "url": "https://www.amazon.co.jp",
        "text": "Amazonでファーマコビジランス関連書籍を探す",
        "description": "PV・安全性監視の実務参考書",
    },
    "Udemy 安全性管理講座": {
        "url": "https://www.udemy.com",
        "text": "Udemyで医薬品安全性管理講座を探す",
        "description": "動画で学ぶPV実務",
    },
    "楽天 医薬品安全性書籍": {
        "url": "https://www.rakuten.co.jp",
        "text": "楽天で医薬品安全性の書籍を探す",
        "description": "副作用報告・安全性監視の参考書",
    },
    "MedDRA関連": {
        "url": "https://www.meddra.org",
        "text": "MedDRA公式サイトで最新情報を確認",
        "description": "MedDRA用語辞書・コーディングガイド",
    },
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)

DASHBOARD_HOST = "127.0.0.1"
DASHBOARD_PORT = 8094

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-CSFVD34MKK"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}
