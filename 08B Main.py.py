from Empire import Empire, strong_soldiers, SaveEmpire, load_empire
vijayanagar = Empire("Vijayanagar")

# Citizens
vijayanagar.add_citizen("Krishna")
vijayanagar.add_citizen("Arjun")
vijayanagar.add_citizen("Ravi")
# Soldiers
vijayanagar.recruit_soldier("Veer", 90, 100)
vijayanagar.recruit_soldier("Raj", 60, 80)
# Iterator - Citizens
print("\nCitizens:")
citizens = vijayanagar.citizen_iterator()
while True:
    try:
        print(next(citizens))
    except StopIteration:
        break
# Iterator - Soldiers
print("\nSoldiers:")
soldiers = vijayanagar.soldier_iterator()
while True:
    try:
        print(next(soldiers))
    except StopIteration:
        break
# Generator - Strong Soldiers
print("\nStrong Soldiers:")
for soldier in strong_soldiers(vijayanagar.soldiers):
    print(soldier)
# King Permission Test
print("\nTax Collection:")
vijayanagar.collect_tax(500)
# Food Storage
print("\nFood Storage:")
vijayanagar.add_food(300)
# Gold Treasury
vijayanagar.treasury()
# Army Report
vijayanagar.army_report()
# Context Manager
print("\nSaving Empire...")
with SaveEmpire(vijayanagar):
    print("Managing the Empire...")
# Load Saved Empire
print("\nLoading Empire...")
load_empire()
