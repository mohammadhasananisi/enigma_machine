Enigma machine with Python
=================
**Without Any Library, Just Gui tkinter**


Library Reference
-----------------

The `library reference <https://docs.python.org/3/library/tkinter.html>`__ documents every publicly accessible object in the library.


Examples
----------
.. image:: https://github.com/mohammadhasananisi/enigma_machine/blob/main/enigma.png?raw=true


See Enigma class in enigma_machine.py

.. code:: python

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

* **Python**  3.3+ (required)
* **Tkinter** 3.10+ (required)


Authors
-------

Keep In Touch with Mohammad Hasan Anisi `Email <mailto:mohammadhasananisiqom@gmail.com>`__ - `github <https://github.com/mohammadhasananisi>`__ - `Telegram <https://t.me/mohammadhasananisi>`__ - `Linkedin <https://linkedin.com/in/mohammadhasan-anisi-159757202>`__.

Please report bugs and suggestions at the `Telegram <https://t.me/mohammadhasananisi>`__ !