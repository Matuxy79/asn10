# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.
# CMPT 145: Object Oriented Programming
# 201901 Assignment 9 Questions 3


import MobilityProfile as MP
import LocationNode as LN 

def str_form(obj, result, exp, reason):
    """
    Purpose:
        Abbreviate test case assertions.
    Preconditions:
        :param obj:  a string
        :param result: a value
        :param reason: a string
    :return: a string
    """
    return ' '.join(['Test fault:',obj,
                     'returned',str(result),
                     '(expected:', str(exp)+')',
                     'on:',reason])

def test_0():
    alocation = LN.LocationNode()
    assert isinstance(alocation, LN.LocationNode), 'Test fault: __init__ failed'

def test_1():
    test_objective = 'set_current_location(), get_current_location()'
    reason = 'current location is set'
    alocation = LN.LocationNode()
    alocation.set_current_location('Airport')
    result = alocation.get_current_location()
    expected = 'Airport'
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_2():
    test_objective = 'set_next_location()'
    reason = 'set the next location'
    alocation = LN.LocationNode()
    nextLocation = LN.LocationNode()
    alocation.set_current_location('Airport')
    alocation.set_next_location(nextLocation)
    result = alocation.get_next_location()
    expected = nextLocation
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_3():
    test_objective = 'set_current_location() value'
    reason = 'set the next location value'
    alocation = LN.LocationNode()
    nextLocation = LN.LocationNode()
    alocation.set_current_location('Airport')
    alocation.set_next_location(nextLocation)
    nextLocation.set_current_location('Bar')
    result = nextLocation.get_current_location()
    expected = 'Bar'
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_4():
    test_objective = 'create location using __init__'
    reason = 'use __init__ to create new location node'
    alocation = LN.LocationNode('Airport')
    result = alocation.get_current_location()
    expected = 'Airport'
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_5():
    patient = MP.MobilityProfile()
    assert isinstance(patient, MP.MobilityProfile), 'Test fault: __init__ failed'

def test_6():
    test_objective = 'create mobility profile using __init__'
    reason = 'use __init__ to create new mobility profile'
    alist = ['Airport','Cafe','Supermart','University','Bar']
    patient = MP.MobilityProfile(alist)
    result = patient.profile.to_string()
    expected = '[ Airport | *-]-->[ Cafe | *-]-->[ Supermart | *-]-->[ University | *-]-->[ Bar | / ]'
    assert result == expected, str_form(test_objective, result, expected, reason)
    
def test_7():
    test_objective = 'create_profile()'
    reason = 'Create new mobility profile'
    alist = ['Airport','Cafe','Supermart','University','Bar']
    patient = MP.MobilityProfile()
    patient.create_profile(alist)
    result = patient.profile.to_string()
    expected = '[ Airport | *-]-->[ Cafe | *-]-->[ Supermart | *-]-->[ University | *-]-->[ Bar | / ]'
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_8():
    test_objective = 'create_profile()'
    reason = 'Create new mobility profile'
    alist = ['Cafe','Cafe','Cafe','Cafe','Cafe']
    patient = MP.MobilityProfile()
    patient.create_profile(alist)
    result = patient.profile.to_string()
    expected = '[ Cafe | *-]-->[ Cafe | *-]-->[ Cafe | *-]-->[ Cafe | *-]-->[ Cafe | / ]'
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_9():
    test_objective = 'compare_profile()'
    reason = 'Both mobility profiles are identical'
    alist = ['Airport','Cafe','Supermart','University','Bar']
    blist = ['Airport','Cafe','Supermart','University','Bar']
    patient = MP.MobilityProfile(alist)
    user = MP.MobilityProfile(blist)
    result = patient.compare_profile(user)
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)    

def test_10():
    test_objective = 'compare_profile()'
    reason = 'Mobility profiles have same location but visit at different time'
    alist = ['Airport','Cafe','Supermart','University','Bar']
    blist = ['Cafe','Airport','University','Bar','Supermart']
    patient = MP.MobilityProfile(alist)
    user = MP.MobilityProfile(blist)
    result = patient.compare_profile(user)
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_11():
    test_objective = 'compare_profile()'
    reason = 'Mobility profiles have visited one location at same time'
    alist = ['Airport','Cafe','Supermart','University','Bar']
    blist = ['Cafe','Airport','Supermart','Bar','University']
    patient = MP.MobilityProfile(alist)
    user = MP.MobilityProfile(blist)
    result = patient.compare_profile(user)
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_12():
    test_objective = 'compare_profile()'
    reason = 'Mobility profiles have visited multiple locations at same time'
    alist = ['Airport','Cafe','Supermart','University','Bar']
    blist = ['Cafe','Airport','Supermart','University','Bar']
    patient = MP.MobilityProfile(alist)
    user = MP.MobilityProfile(blist)
    result = patient.compare_profile(user)
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_13():
    test_objective = 'compare_profile()'
    reason = 'Mobility profiles have visited multiple locations at same time'
    alist = ['Airport','Cafe','Supermart','University','Bar']
    blist = ['Cafe','Airport','Supermart','Gym','Bar']
    patient = MP.MobilityProfile(alist)
    user = MP.MobilityProfile(blist)
    result = patient.compare_profile(user)
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_14():
    test_objective = 'compare_profile()'
    reason = 'Mobility profiles have different locations'
    alist = ['Airport','Cafe','Supermart','University','Bar']
    blist = ['Supermart','Airport','Gym','Gym','Gym']
    patient = MP.MobilityProfile(alist)
    user = MP.MobilityProfile(blist)
    result = patient.compare_profile(user)
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_15():
    test_objective = 'compare_profile()'
    reason = 'Mobility profiles have different locations'
    alist = ['Cafe','Cafe','Cafe','Cafe','Cafe']
    blist = ['Gym','Gym','Gym','Gym','Gym']
    patient = MP.MobilityProfile(alist)
    user = MP.MobilityProfile(blist)
    result = patient.compare_profile(user)
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_16():
    test_objective = 'compare_profile()'
    reason = 'Mobility profiles visited same last location'
    alist = ['Airport','Cafe','Supermart','University','Bar']
    blist = ['Cafe','Gym','University','Supermart','Bar']
    patient = MP.MobilityProfile(alist)
    user = MP.MobilityProfile(blist)
    result = patient.compare_profile(user)
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_17():
    test_objective = 'compare_profile()'
    reason = 'Mobility profiles visited same first location'
    alist = ['Airport','Cafe','Supermart','University','Bar']
    blist = ['Airport','Gym','University','Supermart','Cafe']
    patient = MP.MobilityProfile(alist)
    user = MP.MobilityProfile(blist)
    result = patient.compare_profile(user)
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_18():
    test_objective = 'compare_profile()'
    reason = 'Mobility profiles visited same first location'
    alist = ['Airport','Hospital','Hospital','Hospital','Hospital']
    blist = ['Airport','University','University','Cafe','Cafe']
    patient = MP.MobilityProfile(alist)
    user = MP.MobilityProfile(blist)
    result = patient.compare_profile(user)
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_19():
    test_objective = 'compare_profile()'
    reason = 'Mobility profiles visited one location at same time'
    alist = ['Hospital','Hospital','Hospital','Hospital','Hospital']
    blist = ['University','Gym','Hospital','Supermart','Cafe']
    patient = MP.MobilityProfile(alist)
    user = MP.MobilityProfile(blist)
    result = patient.compare_profile(user)
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)

if __name__ == "__main__":
    all_of_em = [
        test_0,
        test_1,
        test_2,
        test_3,
        test_4,
        test_5,
        test_6,
        test_7,
        test_8,
        test_9,
        test_10,
        test_11,
        test_12,
        test_13,
        test_14,
        test_15,
        test_16,
        test_17,
        test_18,
        test_19,
    ]

    count = 0
    failed = 0
    for t in reversed(all_of_em):
        count += 1
        try: 
            t()
        except Exception as e:
            print("Test failure in function:", t.__name__)
            print(e)
            print()
            failed += 1

    print('Passed', count - failed, 'out of total', count, 'tests')
    if failed > 2:
        print('***Note***\nThe tests were executed in reverse order, so you can\nmore easily see the first test failures.')
