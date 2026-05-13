import time
from playwright.sync_api import sync_playwright

CACHE = []
LAST_UPDATED = 0

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?location=Stockholm&f_TPR=r86400"

KEYWORDS = {
    "Frontend": "frontend developer react javascript",
    "Backend": "backend developer python django",
    "Fullstack": "full stack engineer",
    "Software": "software engineer",
    "AI/ML": "machine learning engineer ai",
    "System": "devops engineer aws kubernetes"
}


def scrape_jobs():
    global CACHE, LAST_UPDATED

    print("🔄 Scraping LinkedIn (SAFE MODE)...")

    jobs = []

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True,
                args=["--no-sandbox", "--disable-dev-shm-usage"]
            )
            page = browser.new_page()

            for role, kw in KEYWORDS.items():

                url = f"{LINKEDIN_URL}&keywords={kw}"

                try:
                    page.goto(url, timeout=60000)
                    page.wait_for_timeout(3000)

                    cards = page.query_selector_all("a.base-card__full-link")

                    for card in cards[:20]:

                        title = card.inner_text()
                        link = card.get_attribute("href")

                        if title and link:

                            # jobs.append({
                            #     "title": title.strip(),
                            #     "link": link,
                            #     "source": "LinkedIn",
                            #     "role": role
                            # })
                            clean_title = title.strip().lower()

                            scores = {
                                "Frontend": 0,
                                "Backend": 0,
                                "Fullstack": 0,
                                "AI/ML": 0,
                                "System": 0
                            }

                            def add_score(role, keywords):
                                for kw in keywords:
                                    if kw in clean_title:
                                        scores[role] += 1

                            add_score("Frontend", [
                                "frontend", "front end", "react", "nextjs", "ui", "javascript", "typescript"
                            ])

                            add_score("Backend", [
                                "backend", "back end", "api", "django", "flask", "fastapi", "node", "python"
                            ])

                            add_score("Fullstack", [
                                "full stack", "fullstack"
                            ])

                            add_score("AI/ML", [
                                "machine learning", "ai", "ml", "data scientist", "deep learning", "data engineer"
                            ])

                            add_score("System", [
                                "devops", "aws", "kubernetes", "docker", "terraform", "cloud"
                            ])

                            # pick best match
                            best_role = max(scores, key=scores.get)

                            # fallback
                            if scores[best_role] == 0:
                                best_role = "Software"

                            job_role = best_role

                            jobs.append({
                                "title": title.strip(),
                                "link": link,
                                "source": "LinkedIn",
                                "role": job_role
                            })

                except Exception as e:
                    print("Scrape error:", e)

            browser.close()

    except Exception as e:
        print("❌ Playwright crash:", e)
        return CACHE  # fallback

    # remove duplicates
    seen = set()
    unique = []

    for j in jobs:
        key = (j["title"], j["link"])
        if key not in seen:
            seen.add(key)
            unique.append(j)

    CACHE = unique
    LAST_UPDATED = time.time()

    print(f"✅ Jobs scraped: {len(unique)}")
    return CACHE


def get_jobs():
    if not CACHE:
        return scrape_jobs()
    return CACHE


def refresh_jobs():
    return scrape_jobs()
