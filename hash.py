B, L, D = [int(x) for x in input().split()]

score = [int(x) for x in input().split()]

freq = [0 for i in range(B)]

from heapq import heappop, heappush

import random
calls = 0

class library:
    def __init__(self, count, time, rate, books):
        self.count = count
        self.time = time
        self.rate = rate
        self.books = books
        # random.shuffle(self.books)
        
    def bookOrder(self):
        bookList = []
        
        for book in self.books:
            bookList.append(((score[book] + 1000) / (freq[book]), book))
            
        bookList.sort()
        
        for i in range(len(bookList)):
            bookList[i] = bookList[i][1]
        
        self.books = bookList
    
        
    def heuristic(self):
        
        count = (D - self.time) * self.rate
        if count <= 0: return 0
        
        self.bookOrder()
        
        sumOf = 0
        
        for book in self.books:
            if seen[book]: continue
            sumOf += score[book]
            count -= 1
            if count == 0: break
        
        return (sumOf) / (self.time * self.time)
        
        
libs = []

h = []
seen = [False for b in range(B)]


for l in range(L):
    N, T, M = [int(x) for x in input().split()] # books, time, books/day
    ids = [int(x) for x in input().split()]     # ids of books
    for i in ids:
        freq[i] += 1
        
    libs.append(library(N, T, M, ids))

for l in range(L):
    heappush(h, (-libs[l].heuristic(), l))

sumOf = 0

output = []

while len(h):
    val, l = heappop(h)
    val = -val
    newScore = libs[l].heuristic()
    if libs[l].time >= D:
        continue
        
    if val > newScore:
        heappush(h, (-newScore, l))
        continue
        
    if D < 0: break
    D -= libs[l].time
    
    findable = D * libs[l].rate
    books = libs[l].books
    out = []
    
    for book in books:
        if seen[book]: continue
        seen[book] = True
        out.append(book)
        sumOf += score[book]
        findable -= 1
        if findable == 0: break
    
    if len(out) == 0:
        D += libs[l].time        
        continue 
        
    else:
        output.append((l, len(out)))
        output.append(out)
        for book in libs[l].books:
            freq[book] -= 1

print(len(output) // 2)
for line in output:
    print(*line)

    
"""
python3 hash.py < a.txt > ao.txt | python3 hash.py < b.txt > bo.txt | python3 hash.py < c.txt > co.txt | python3 hash.py < d.txt > do.txt | python3 hash.py < e.txt > eo.txt | python3 hash.py < f.txt > fo.txt
"""
