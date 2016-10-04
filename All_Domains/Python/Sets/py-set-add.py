import sys

[_, *countries] = list(sys.stdin)
countries = (country.strip() for country in countries)
distinct_countries = set()
for country in countries:
    distinct_countries.add(country)
print(len(distinct_countries))
