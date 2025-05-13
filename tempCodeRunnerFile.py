            y=sorted(x,key=(list(comb)+x).index)[2:]
            y.append(insert(comb))
            for i in products(y):
                yield from get1(i)