# ResearchOps AI Architecture

## Overview

ResearchOps AI is an Agentic AI platform for financial and market intelligence.

The platform uses an MCP-inspired architecture where a planner agent dynamically selects tools, gathers information from multiple sources, performs analysis, and generates multilingual research reports.

---

## High Level Architecture

User Query
    ↓
Language Layer
    ↓
Planner Agent
    ↓
Tool Registry
    ↓
Tool Execution
    ↓
Financial Analysis
    ↓
Report Generation
    ↓
Localization Layer
    ↓
Final Response

---

## Components

### Language Layer

Responsible for:

- Language Detection
- Translation
- Localization
- Hinglish Formatting

Supported Languages:

- English
- Hindi
- Hinglish
- French
- German
- Japanese
- Spanish

---

### Planner Agent

Responsible for:

- Intent Detection
- Execution Planning
- Tool Selection
- Workflow Orchestration

Example:

Query:
Compare TCS and Infosys

Plan:

1. Fetch company data
2. Fetch financial statements
3. Fetch recent news
4. Calculate ratios
5. Generate comparison report

---

### Tool Registry

Provides dynamic discovery and execution of tools.

Examples:

- Stock Data Tool
- News Tool
- Company Information Tool
- Financial Analysis Tool
- Report Tool

---

### Financial Analysis Layer

Performs:

- Revenue Growth Analysis
- Profit Growth Analysis
- Valuation Analysis
- Ratio Calculations
- Risk Assessment

---

### Report Generator

Generates:

- Executive Summary
- Detailed Analyst Report
- Comparison Reports

Formats:

- Markdown
- PDF

---

### Localization Layer

Converts generated report into:

- English
- Hindi
- Hinglish
- French
- German
- Japanese

while preserving financial terminology and context.