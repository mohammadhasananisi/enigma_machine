Enigma machine with Python
=================
**Without Any Library, Just Gui tkinter**


Library Reference
-----------------

The `library reference <https://docs.python.org/3/library/tkinter.html>`__ documents every publicly accessible object in the library.


Examples
----------
![Demo Photo](https://github.com/mohammadhasananisi/enigma_machine/blob/main/enigma.png)


See Enigma class in enigma_machine.py
.. code::python 
    
enigma_class = Enigma(
        rotors = ("I","II","III")
        reflector = "UKW-B"
        ringSettings = "ABC"
        ringPositions = "DEF"
        plugboard = "AT BS DE FM IR KN LZ OW PV XY"
        
        )

        result = enigma_class.encode("code || text")
        print(result)
::

Or

Run with Gui ``python enigma_run_with_gui.py``.



Installing
----------

The easiest way to install this is using ``pip install tk``.


Requirements
------------

To use all of the functionality of the library, you should have:

* **Python** 2.6, 2.7, or 3.3+ (required)
* **Tkinter** 3.10+ (required)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Authors
-------

::

    Uberi <me@anthonyz.ca> (Anthony Zhang)
    Author <mohammadhasananisiqom@gmail.com> (Mohammad Hasan Anisi)

Please report bugs and suggestions at the `Telegram <https://t.me/mohammadhasananisi>`__!

