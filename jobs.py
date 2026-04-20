import time
from playwright.sync_api import sync_playwright

CACHE = []
LAST_UPDATED = 0

CATEGORIES = {
    "Frontend": "frontend react javascript",
    "Backend": "python django backend",
    "System": "devops aws kubernetes",
    "Fullstack": "fullstack react python",
    "AI/ML": "machine learning ai data scientist python"
}

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?location=Stockholm&f_TPR=r86400"


# SCRAPER CORE
def scrape_category(page, keyword, category):
    url = f"{LINKEDIN_URL}&keywords={keyword}"

    page.goto(url, timeout=60000)
    page.wait_for_timeout(5000)

    cards = page.query_selector_all("a.base-card__full-link")

    jobs = []

    for card in cards[:15]:
        try:
            title = card.inner_text().strip()
            link = card.get_attribute("href")

            if title and link:
                jobs.append({
                    "title": f"{category}: {title}",
                    "link": link,
                    "source": "LinkedIn",
                    "role": category
                })
        except:
            continue

    return jobs


# MAIN SCRAPER (ALL CATEGORIES)
def scrape_all():
    global CACHE, LAST_UPDATED

    print("🔄 Scraping LinkedIn (multi-category)...")

    jobs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for category, keyword in CATEGORIES.items():
            try:
                jobs.extend(scrape_category(page, keyword, category))
            except Exception as e:
                print(f"Scrape error {category}:", e)

        browser.close()

    # remove duplicates
    seen = set()
    unique = []

    for job in jobs:
        key = (job["title"], job["link"])
        if key not in seen:
            seen.add(key)
            unique.append(job)

    CACHE = unique
    LAST_UPDATED = time.time()

    print(f"✅ Jobs scraped: {len(unique)}")
    return CACHE


# FAST API ACCESS (NO SCRAPING)
def get_jobs():
    global CACHE

    if not CACHE:
        return scrape_all()

    return CACHE


# MANUAL REFRESH
def refresh_jobs():
    return scrape_all()