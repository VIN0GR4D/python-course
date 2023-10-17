users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

stats = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

stats["Общее количество"] = len(users)
stats["Уникальные посещения"] = len(set(users))

print(stats)
