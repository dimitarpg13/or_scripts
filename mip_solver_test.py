from __future__ import print_function
from ortools.linear_solver import pywraplp

def main():
    solver = pywraplp.Solver('SolveIntegerProblem', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    x = solver.IntVar(0.0, solver.infinity(), 'x')
    y = solver.IntVar(0.0, solver.infinity(), 'y')

    constraint1 = solver.Constraint(-solver.infinity(), 17.5)
    constraint1.SetCoefficient(x, 1)
    constraint1.SetCoefficient(y, 7)

    constraint2 = solver.Constraint(-solver.infinity(), 3.5)
    constraint2.SetCoefficient(x, 1)
    constraint2.SetCoefficient(y, 0)

    objective = solver.Objective()
    objective.SetCoefficient(x, 1)
    objective.SetCoefficient(y, 10)
    objective.SetMaximization()


    """Solve problem and print solution"""
    result_status = solver.Solve()

    assert result_status == pywraplp.Solver.OPTIMAL

    assert solver.VerifySolution(1e-7, True)

    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())

    print('Optimal objective value = %d' % solver.Objective().Value())
    print()
    variable_list = [x, y]

    for variable in variable_list:
        print('%s = %d' % (variable.name(), variable.solution_value()))

if __name__ == '__main__':
    main()

