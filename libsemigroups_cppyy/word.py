"""
This file contains the interface to libsemigroups words; see

    https://libsemigroups.readthedocs.io/en/latest/words.html

for further details.
"""

import cppyy

from cppyy.gbl.libsemigroups import number_of_words

from libsemigroups_cppyy.detail import ForwardRange

from cppyy.gbl.libsemigroups import cbegin_wilo, cend_wilo


def wilo(n, upper_bound, first, last):
    return ForwardRange(
        cppyy.gbl.libsemigroups.cbegin_wilo(n, upper_bound, first, last),
        cppyy.gbl.libsemigroups.cend_wilo(n, upper_bound, first, last),
    )
