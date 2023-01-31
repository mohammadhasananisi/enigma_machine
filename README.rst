Enigma machine with Python
=================
**Without Any Library, Just Gui tkinter**


Library Reference
-----------------

The `library reference <https://docs.python.org/3/library/tkinter.html>`__ documents every publicly accessible object in the library.


Examples
----------
![Demo Photo](./enigma.png)


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

This usually happens when you're using a Raspberry Pi board, which doesn't have audio input capabilities by itself. This causes the default microphone used by PyAudio to simply block when we try to read it. If you happen to be using a Raspberry Pi, you'll need a USB sound card (or USB microphone).

Once you do this, change all instances of ``Microphone()`` to ``Microphone(device_index=MICROPHONE_INDEX)``, where ``MICROPHONE_INDEX`` is the hardware-specific index of the microphone.

To figure out what the value of ``MICROPHONE_INDEX`` should be, run the following code:

.. code:: python

    import speech_recognition as sr
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

This will print out something like the following:

::

Authors
-------

::

    Uberi <me@anthonyz.ca> (Anthony Zhang)
    Author <mohammadhasananisiqom@gmail.com> (Mohammad Hasan Anisi)

Please report bugs and suggestions at the `Telegram <https://t.me/mohammadhasananisi>`__!

