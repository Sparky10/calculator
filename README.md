# Python calculator

The implementation of a simple calculator in Python.

**To run the calculator**

From the 'scripts' directory issue:

```
python calculator.py
```

**To run the tests**

From the 'tests' directory issue:

```
python test_calculator.py -v
```

**Architectural overview**

`Script`
A simple script is run from the command line to provide an io interface.

`Models`
The Calculator model uses the compute service to co-ordinate calculator actions.

The ComputeEngine models handle parsing and calculations.  There are two compute engine models available:

* SimpleComputeEngine
* ComplexComputeEngine

The ComplexComputeEngine is a subclass of the SimpleComputeEngine.

The simple engine provides +, -, * and / operations on integers only.  Input must be space delimited.
The complex engine adds ^ (power) and % (modulus) operations and can handle floats.  Space delimiting is not required for inputs.

`Services`

The ComputeService is used to inject ComputeEngine dependencies into the Calculator model.




