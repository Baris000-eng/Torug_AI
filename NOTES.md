# Notes (Optional)

This file is optional.

Assumptions I made & : 

In the first question, I assumed that the cancelled orders and the returned orders are seperate. For the monetary order amounts greater than 
1.7976931348623157 * 10^308, they will be rounded to infinity by the float() in my current implementation. As they are seamlessly skipped by 
the 'math.isfinite()', the infinity values are not a problem in my updated implementation. If we want to handle amounts more than this value 
with higher precision, we should use Python's Decimal module, as it supports extremely large values, which is even larger than what the float() 
can support (). 

In the second question, I assumed that the domain names and top-level domain names that are given in the emails actually exists in the publicly or privately available resources such as databases, APIs, and websites. 




Use it only if you want to provide **additional context** for the reviewer that does not fit cleanly in `submission_template.md`.

Examples of appropriate use:
- Assumptions you made
- Known limitations of your solution
- Alternative approaches you considered but did not implement

Do not repeat information already included in `submission_template.md`.

Remove the contents of this file and write your notes.
