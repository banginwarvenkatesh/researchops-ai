from enum import Enum


class Capability(str, Enum):

    STOCK_QUOTE = "stock_quote"

    COMPANY_PROFILE = "company_profile"

    FINANCIAL_STATEMENTS = "financial_statements"

    MARKET_NEWS = "market_news"

    MARKET_SUMMARY = "market_summary"

    LANGUAGE_TRANSLATION = "language_translation"

    REPORT_GENERATION = "report_generation"

    PDF_EXPORT = "pdf_export"