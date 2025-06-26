import requests

BASE_URL = "https://restcountries.com/v3.1/name/"

# Map of statistic names → how to pull them from the API response
STAT_MAP = {
    "population": lambda c: c["population"],
    "region":     lambda c: c["region"],
    "subregion":  lambda c: c.get("subregion", "N/A"),
    "capital":    lambda c: ", ".join(c.get("capital", [])) if c.get("capital") else "N/A",
    "area":       lambda c: f"{c['area']} km²",
    "timezones":  lambda c: ", ".join(c["timezones"]),
    "currencies": lambda c: ", ".join(v["name"] for v in c["currencies"].values()),
    "languages":  lambda c: ", ".join(c["languages"].values()),
}

def fetch_country(name: str) -> dict:
    """Return the first country object the API finds."""
    resp = requests.get(f"{BASE_URL}{name}")
    resp.raise_for_status()           # will raise for 404, etc.
    return resp.json()[0]             # API returns a list

def main() -> None:
    country_name = input("Which country? ").strip()
    try:
        country = fetch_country(country_name)
    except requests.HTTPError:
        print("Country not found. Check the spelling and try again.")
        return

    print("\nAvailable statistics:")
    for key in STAT_MAP:
        print(f"  • {key}")

    stat = input("\nWhich statistic? ").strip().lower()
    if stat not in STAT_MAP:
        print("Unknown statistic.")
        return

    value = STAT_MAP[stat](country)
    print(f"\n{stat.capitalize()} for {country['name']['common']}: {value}")

if __name__ == "__main__":
    main()
