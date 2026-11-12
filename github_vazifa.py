# def majority_element(nums: list) -> int:
#     if not nums:
#         return -1

#     new = {}

#     for son in nums:
#         if son not in new:
#             new[son] = 1
#         else:
#             new[son] += 1

#     natija = max(new, key=new.get)
#     return natija


# print(majority_element([2, 2, 1, 1, 1, 2, 2]))  
# print(majority_element([])) 

# 2-masala

# def search_by_genre(cinema, genre):
#     natija = []

#     for film in cinema:
#         if film["genre"] == genre:
#             natija.append(film)

#     return natija


# cinema = [
#     {"title": "Avatar", "genre": "Fantastika", "price": 40000},
#     {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
#     {"title": "Oq yo'l", "genre": "Drama", "price": 25000},
#     {"title": "Dune", "genre": "Fantastika", "price": 35000}
# ]


#------------------- 3talik masalalar --------

# 3-masala
# def merge_unique_ids(active_users, new_users):
#     natija= list(set(active_users+new_users))
#     return natija


# active_users = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001'] 
# new_users = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']
# print(merge_unique_ids(active_users,new_users))




