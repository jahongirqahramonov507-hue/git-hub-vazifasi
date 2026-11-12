def majority_element(nums: list) -> int:
    if not nums:
        return -1

    new = {}

    for son in nums:
        if son not in new:
            new[son] = 1
        else:
            new[son] += 1

    natija = max(new, key=new.get)
    return natija


print(majority_element([2, 2, 1, 1, 1, 2, 2]))  
print(majority_element([])) 

# 2-masala

def search_by_genre(cinema, genre):
    natija = []

    for film in cinema:
        if film["genre"] == genre:
            natija.append(film)

    return natija


cinema = [
    {"title": "Avatar", "genre": "Fantastika", "price": 40000},
    {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
    {"title": "Oq yo'l", "genre": "Drama", "price": 25000},
    {"title": "Dune", "genre": "Fantastika", "price": 35000}
]


