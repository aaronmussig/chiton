FastANI
=======

`FastANI <https://github.com/ParBLiSS/FastANI>`_  (`Jain, C., Rodriguez-R, L.M., Phillippy, A.M. et al. <https://doi.org/10.1038/s41467-018-07641-9>`_)


Basic usage
-----------

.. code-block:: python

    from chiton.fastani import fastani

    result = fastani(query='query.fna', reference='reference.fna')
    dict_results = result.as_dict()

    # Accessing results
    print(dict_results['query.fna']['reference.fna'].ani)         # 89.1234
    print(dict_results['query.fna']['reference.fna'].n_frag)      # 50
    print(dict_results['query.fna']['reference.fna'].total_frag)  # 100
    print(dict_results['query.fna']['reference.fna'].align_frac)  # 0.5

    # Writing results to disk
    result.to_file('results.txt')


Models
------

Input
^^^^^

.. autofunction:: chiton.fastani.fastani


Output
^^^^^^

.. autoclass:: chiton.fastani.model.FastANIResults
   :members:

.. autoclass:: chiton.fastani.model.FastANIResult
   :members:

Helper classes
^^^^^^^^^^^^^^

.. autoclass:: chiton.fastani.model.FastANIExecution
   :members:

.. autoclass:: chiton.fastani.model.ResultFile
   :members:

.. autoclass:: chiton.fastani.model.FastANIParameters
   :members:
