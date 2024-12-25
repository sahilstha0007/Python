country={
    "Nepal":"Kathmandu",
    "India":"New Delhi"
}
print(country["Nepal"])
print(country["India"])
print(country)
type(country)
country["USA"]="Washington DC"
del country["India"]
print(country)
# country.clear() #clears all the elements in the dictionary
# print(country)
country["Nepal"]="Bagmati"
print(country)
