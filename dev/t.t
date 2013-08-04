************* Module fabfile
W:  9,0: Found indentation with tabs instead of spaces
W: 24,0: Found indentation with tabs instead of spaces
W: 25,0: Found indentation with tabs instead of spaces
C:  1,0: Missing docstring
F:  2,0: Unable to import 'fabric.api'
C:  5,0:setup: Missing docstring
E:  8,9:setup: Undefined variable 'name'
C: 13,0:update: Missing docstring
C: 20,0:clone: Missing docstring
E: 21,10:clone: Undefined variable 'environment'
C: 27,0:updatewithsupport: Comma not followed by a space
def updatewithsupport(user,directory, branch):
                          ^^
W: 27,38:updatewithsupport: Redefining name 'branch' from outer scope (line 42)
C: 27,0:updatewithsupport: Missing docstring
E: 28,10:updatewithsupport: Undefined variable 'environment'
W: 27,38:updatewithsupport: Unused argument 'branch'
C: 32,0:status: Comma not followed by a space
def status(user,location):
               ^^
C: 32,0:status: Missing docstring
C: 36,0:clone_with_support: Missing docstring
E: 37,10:clone_with_support: Undefined variable 'environment'
C: 42,0:branch: Missing docstring
E: 43,10:branch: Undefined variable 'environment'
W:  2,0: Unused import sudo


Report
======
31 statements analysed.

Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |=          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |10     |18       |-8.00      |
+-----------+-------+---------+-----------+
|refactor   |0      |0        |=          |
+-----------+-------+---------+-----------+
|warning    |6      |23       |-17.00     |
+-----------+-------+---------+-----------+
|error      |5      |7        |-2.00      |
+-----------+-------+---------+-----------+



Messages
--------

+-----------+------------+
|message id |occurrences |
+===========+============+
|C0111      |8           |
+-----------+------------+
|E0602      |5           |
+-----------+------------+
|W0312      |3           |
+-----------+------------+
|C0324      |2           |
+-----------+------------+
|W0621      |1           |
+-----------+------------+
|W0613      |1           |
+-----------+------------+
|W0611      |1           |
+-----------+------------+
|F0401      |1           |
+-----------+------------+



Global evaluation
-----------------
Your code has been rated at -3.23/10 (previous run: -14.52/10)

Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |37     |94.87 |31       |+6.00      |
+----------+-------+------+---------+-----------+
|docstring |0      |0.00  |0        |=          |
+----------+-------+------+---------+-----------+
|comment   |0      |0.00  |0        |=          |
+----------+-------+------+---------+-----------+
|empty     |2      |5.13  |2        |=          |
+----------+-------+------+---------+-----------+



Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |1          |=          |0.00        |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|method   |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|function |7      |7          |=          |0.00        |0.00     |
+---------+-------+-----------+-----------+------------+---------+



