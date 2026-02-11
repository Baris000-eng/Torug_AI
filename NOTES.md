# Notes:

Assumptions I made & Known Limitations of My Solution: 

In the first question, I assumed that the cancelled orders and the returned orders are seperate. For the monetary order amounts greater than 
the 1.7976931348623157 * 10^308 (upper boundary value of the float()), they will be rounded to infinity by the float() in my current implementation. 
As they are seamlessly skipped by the 'math.isfinite()', the infinity values are not a problem in my updated implementation. For my updated 
implementation of the first task, the monetary order amounts are assumed to be smaller than the 1.7976931348623157 * 10^308. If the amounts more 
than this value are to be handled with higher precision, Python's Decimal module should be used, as it supports extremely large values, which is 
even larger than the values which the float() can support. 

In the second question, I assumed that the domain names and top-level domain names that are given in the emails actually exists in the publicly or privately available resources such as databases, APIs, and websites. 

In the third question, for the values greater than 1.7976931348623157 * 10^308 (upper boundary value of the float()), they will be rounded to infinity by the float() in my current implementation. As they are seamlessly skipped by the 'math.isfinite()', the infinity values are not a problem in my updated code. For my corrected implementation of the third task, the valid values are assumed to be smaller than the 1.7976931348623157 * 10^308. If the amounts more than this value are to be handled with higher precision, Python's Decimal module should be used, as it supports extremely large values, which is even larger than the values which the float() can support. 

I have assumed that a valid 'orders' parameter in the first question and a valid 'emails' parameter in the second question can be a list, tuple, or set. In addition, I have assumed that a valid 
