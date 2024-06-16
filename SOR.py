"""
Python code related to the numerical linear algebra -> a system of linear equations with SOR method

Professor's name: Dr. Tabrizi Doz
"""

"""real answer : X1 =  3  X2 =  7  X3 =  -4""" 


class SOR:
    def __init__(self, tol_error, relaxation_factor):
        self.x = 0
        self.y = 0
        self.z = 0
        self.tol_error = tol_error
        self.relaxation_factor = relaxation_factor
        self.count = 1

    def f1(self, x, y, z):
        return (29 - (2 * y) + (0 * z)) / 5

    def f2(self, x, y, z):
        return (33 - (2 * x) - (2 * z)) / 5

    def f3(self, x, y, z):
        return (10 - (2 * y) + (0 * x)) / 1

    def iterate(self):
        while True:
            x1 = (1 - self.relaxation_factor) * self.x + self.relaxation_factor * self.f1(self.x, self.y, self.z)
            y1 = (1 - self.relaxation_factor) * self.y + self.relaxation_factor * self.f2(x1, self.y, self.z)
            z1 = (1 - self.relaxation_factor) * self.z + self.relaxation_factor * self.f3(x1, y1, self.z)
            
            print(f'{self.count}\t{x1:.4f}\t{y1:.4f}\t{z1:.4f}\n')
            
            e1 = abs(self.x - x1)
            e2 = abs(self.y - y1)
            e3 = abs(self.z - z1)
            
            if e1 <= self.tol_error and e2 <= self.tol_error and e3 <= self.tol_error:
                break
            
            self.count += 1
            self.x, self.y, self.z = x1, y1, z1

        print(f'\nSolution: x = {x1:.3f}, y = {y1:.3f}, z = {z1:.3f}\n')

def main():
    tol_error = float(input('Enter tolerable error: '))
    relaxation_factor = float(input("Enter relaxation factor: "))
    
    sor_solver = SOR(tol_error, relaxation_factor)
    print('\nCount\tx\ty\tz\n')
    sor_solver.iterate()

if __name__ == "__main__":
    main()



