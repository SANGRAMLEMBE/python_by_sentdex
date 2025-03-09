game = [[1,0,1],
        [0,0,1],
        [2,2,1],]

columns = [0, 1, 2]
for col in columns:
        check = []

        for row in game:
                check.append(row[col])

        if check.count(check[0]) == len(check) and check[0]!=0:
                print("Winner!!")
