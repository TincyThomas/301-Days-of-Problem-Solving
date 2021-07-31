def city_facts(city):
    return city['name']+" has a population of "+city['population'] +" and is situated in "+ city['continent']
print(city_facts({
  'name': "Paris",
  'population': "2,140,526",
  'continent': "Europe"
}))
