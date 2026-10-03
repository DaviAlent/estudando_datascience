from sklearn import tree

X=[
    [175, 70, 41],
    [162, 58, 37],
    [180, 85, 43],
    [168, 62, 38],
    [172, 75, 40],
    [158, 52, 36],
    [185, 90, 44],
    [165, 60, 37],
    [178, 78, 42],
    [170, 68, 39]
]

Y=[
    "male",
    "female",
    "male",
    "female",
    "male",
    "female",
    "male",
    "female",
    "male",
    "female"
]

clf = tree.DecisionTreeClassifier()

clf=clf.fit(X,Y)

prediction= clf.predict([[160, 55, 37]])

print(prediction)