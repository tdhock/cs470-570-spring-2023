# test 2.2
x=Searcher("50test.txt", searchType="DEPTH", verbose=False)
x.setStart('m')
x.setGoals(['c', 'af', 'ak'])
x.search()
x.stats()

x=Searcher("50test.txt", searchType="BREADTH", verbose=False)
x.setStart('m')
x.setGoals(['c', 'af', 'ak'])
x.search()
x.stats()

x=Searcher("50test.txt", searchType="BEST", verbose=False)
x.setStart('m')
x.setGoals(['c', 'af', 'ak'])
x.search()
x.stats()

x=Searcher("50test.txt", searchType="A*", verbose=False)
x.setStart('m')
x.setGoals(['c', 'af', 'ak'])
x.search()
x.stats()

x=Searcher("50test.txt", searchType="A*", verbose=False)
x.setStart('m')
x.setGoals(['c', 'af'])
x.search()
x.myViz.save("50test.png")
x.stats()

