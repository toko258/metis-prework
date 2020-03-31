# Python 2 & 3 Compatibility
from __future__ import print_function, division

import sys
import re

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if not test:
        continue
    if re.match('(".+"|^[a-z0-9._+]+)@([a-z0-9._+]+\.)+[a-z]+$', test,
                re.IGNORECASE):
        print("true")
    else:
        print("false")

test_cases.close()
"""
Validating emails is actually harder than this,
and involves making design choices, in practice.

See this thoughtful and relevant write-up:
http://www.bjaress.com/2011/12/job-posting-asks-me-to-write-little.html

Here, all our code needs to do is pass the 20 test cases.
You can get CodeEval to show them to you
by using an `Exception` message, which it will display.

Here are the ten valid examples. The last one is tricky.

    b@d.net
    1@d.net
    b@domain.net
    bob123@alice123.com
    very.common@example.com
    niceandsimple@example.com
    a.little.lengthy.but.fine@dept.example.com
    disposable.style.email.with+156@example.com
    disposable.style.email.with+symbol@example.com
    "very.unusual.@.unusual.com"@example.com

And here are the ten invalid examples:

    hfij#kjdfvkl
    Abc.example.com
    this is not true
    <invalid>@foo.com
    A@b@c@example.com
    asterisk_domain@foo.*
    just"not"right@example.com
    this is"not\allowed@example.com
    a"b(c)d,e:f;g<h>i[j\\k]l@example.com
    this\ still\"not\\allowed@example.com

"""
