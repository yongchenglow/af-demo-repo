# 🚀 Quick Start - 3 Minutes to Demo

## Setup (30 seconds)

```bash
cd /Users/yongchenglow/sites/af-demo-repo

# View all branches
git branch -a
```

## Create Demo PRs (1 minute)

```bash
# Branch 1: Security Issues (SQL Injection)
gh pr create --base main --head feature/sql-injection-demo \
  --title "🔐 Add user authentication" \
  --body "Implements login endpoint with database integration"

# Branch 2: Code Quality Issues
gh pr create --base main --head feature/code-quality-issues \
  --title "📊 Add analytics dashboard" \
  --body "User engagement metrics and reporting"

# Branch 3: Performance Issues
gh pr create --base main --head feature/performance-issues \
  --title "💳 Add payment processing" \
  --body "Credit card payment gateway integration"
```

## What Each Branch Demonstrates

### 🔴 Branch 1: `feature/sql-injection-demo`
**File:** `auth.py`
- SQL Injection vulnerabilities (CRITICAL)
- Hardcoded API keys and passwords
- Sensitive data exposure

### 🟠 Branch 2: `feature/code-quality-issues`
**File:** `analytics.py`
- 60+ line function (too long)
- 10+ cyclomatic complexity
- Missing docstrings
- Poor naming conventions

### 🟡 Branch 3: `feature/performance-issues`
**File:** `payments.py`
- Blocking operations (time.sleep)
- N+1 query pattern
- No pagination (100k records!)
- Sensitive data in logs

## Watch the Magic (1-2 minutes)

The AI agent automatically:
1. ✅ Reviews code in **5-8 seconds**
2. ✅ Posts detailed comments with 🔴🟠🟡 severity
3. ✅ Generates validated fixes
4. ✅ Creates fix PRs (or pushes directly)

## Key Stats to Mention

- **Speed:** 60% faster than manual review
- **Cost:** $0.14/1M tokens (DeepSeek) vs $15/1M (GPT-4)
- **Accuracy:** Catches OWASP Top 10 vulnerabilities
- **Auto-fix rate:** 94% (16/17 issues)
- **Validation:** 3-attempt retry loop with linting

## One-Liner Pitch

> "An AI code reviewer powered by AgentField that finds security bugs, code smells, and performance issues in seconds - then fixes them automatically for $25/month."

---

**Need more details?** See `DEMO_GUIDE.md`
