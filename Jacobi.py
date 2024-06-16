import numpy as np

class Jacobi:
    def __init__(self, a, b, tol_error, max_iterations):
        self.a = a
        self.b = b
        self.tol_error = tol_error
        self.max_iterations = max_iterations
        self.n = len(b)
        self.x = np.zeros(self.n)
        self.iterations = 0

    def iterate(self):
        x_new = np.zeros(self.n)
        for k in range(self.max_iterations):
            for i in range(self.n):
                s = sum(self.a[i][j] * self.x[j] for j in range(self.n) if j != i)
                x_new[i] = (self.b[i] - s) / self.a[i][i]
            print(f'Iteration {k+1}: ' + ', '.join(f'x{i+1} = {val:.4f}' for i, val in enumerate(x_new)))
            if np.allclose(self.x, x_new, atol=self.tol_error):
                break
            self.x = np.copy(x_new)
            self.iterations = k + 1
        print(f'\nSolution after {self.iterations} iterations: ' + ', '.join(f'x{i+1} = {val:.4f}' for i, val in enumerate(self.x)))

def main():
    a = np.array([[5, 2, 0],
                  [2, 5, 2],
                  [0, 2, 1]], dtype=float)
    b = np.array([29, 33, 10], dtype=float)
    
    tol_error = float(input('Enter tolerable error: '))
    max_iterations = int(input('Enter maximum number of iterations: '))
    
    jacobi_solver = Jacobi(a, b, tol_error, max_iterations)
    jacobi_solver.iterate()

if __name__ == "__main__":
    main()
