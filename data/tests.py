import data_cleaning

def test_noneMissing(test_dict):
    """Should run through dict keys and assert there are 76 in order (0-75) """
    test_keys = sorted(test_dict.keys())
    
    for i, el in enumerate(test_keys):
        assert(i==el)
    pass

def test_noDups(test_dict):
    """Should run through dict vals and assert there are no duplicates"""
    test_vals = test_dict.values()
    assert(len(test_vals)==len(set(test_vals)))
    pass

if __name__=='main':
    test_dict = data_cleaning.getColumnLabels()
    
    test_noneMissing(test_dict)
    test_noDups(test_dict)
