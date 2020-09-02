"""
This file contains the interface to libsemigroups actions; see

https://libsemigroups.readthedocs.io/en/latest/words.html

for further details.
"""

import cppyy

from cppyy.gbl.libsemigroups import number_of_words

from libsemigroups_cppyy.detail import ForwardRange

from cppyy.gbl.libsemigroups import cbegin_wilo, cend_wilo

from cppyy.gbl.libsemigroups import cbegin_wislo, cend_wislo

from cppyy.gbl.libsemigroups import cbegin_sislo, cend_sislo

from cppyy.gbl.libsemigroups import cbegin_silo, cend_silo

def wilo(n, upper_bound, first, last):
    return ForwardRange(
    cppyy.gbl.libsemigroups.cbegin_wilo(n, upper_bound, first, last),
    cppyy.gbl.libsemigroups.cend_wilo(n, upper_bound, first, last),)

def wislo(n, first, last):
    return ForwardRange(
    cppyy.gbl.libsemigroups.cbegin_wislo(n, first, last),
    cppyy.gbl.libsemigroups.cend_wislo(n, first, last),)

def sislo(alphabet, first, last):
    return ForwardRange(
    cppyy.gbl.libsemigroups.cbegin_sislo(alphabet, first, last),
    cppyy.gbl.libsemigroups.cend_sislo(alphabet, first, last),)

def silo(alphabet, upper_bound, first, last):
    return ForwardRange(
    cppyy.gbl.libsemigroups.cbegin_silo(alphabet, upper_bound, first, last),
    cppyy.gbl.libsemigroups.cend_silo(alphabet, upper_bound, first, last),)
