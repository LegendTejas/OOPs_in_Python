# Hybrid Inheritance in Python
# A combination of multiple inheritance types.

class A:
    def feature_a(self):
        print("Feature A from class A")

class B(A):  # Single inheritance from A
    def feature_b(self):
        print("Feature B from class B")

class C(A):
    def feature_c(self):
        print("Feature C from class C")

class D(B, C):  # Multiple inheritance from B and C
    def feature_d(self):
        print("Feature D from class D")

# Using the classes
obj = D()
obj.feature_a()
obj.feature_b()
obj.feature_c()
obj.feature_d()
