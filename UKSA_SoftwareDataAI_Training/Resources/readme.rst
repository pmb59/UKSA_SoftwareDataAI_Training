================================
Cheat sheet for reStructuredText
================================

See the Sphinx rst primer `here <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_

Or click on the editing icon to see the rst syntax used below

=======
section
=======

----------
subsection
----------

^^^^^^^^^^^^^
subsubsection
^^^^^^^^^^^^^

An external hyperlink is shown below:

For numerours internal refrencing options see `here <https://www.sphinx-doc.org/en/master/usage/referencing.html#ref-role>`_

.. _my-reference-label:

Section to cross-reference
--------------------------


* bullet point
  * nseted bullet point
  
1. This is a numbered list.
2. It has two items too
  i. nested again 


A simple table
=====  =====  
A      B     
=====  =====  
False  False  
True   False 
False  True   
True   True   
=====  =====  

A more complicated table 
+------------------------+------------+
| Header row, column 1   | Header 2   | 
| (header rows optional) |            |
+========================+============+
| body row 1, column 1   | column 2   | 
+------------------------+------------+
| body row 2             | ...        | 
+------------------------+------------+



