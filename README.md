# Comp4102 - League Tracker
Author: Andrew Dybka

To run any file use command "python filename.py"

<h3>testTemplateMatching.py</h3>
This file demonstrates the various methods of template matching provided by opencv

<h3>videoRapidTemplateMatching.py</h3>
This files tracks the characters purely with template matching.
On line 4 you can change the value to track different characters. The current options are 'karma', 'cho', 'tf', 'kayn' and 'fiora'

<h3>Tracker.py</h3>
This file implements object tracking and is my current final solution.
On line 4 you can change the value to track different characters. The current options are 'karma', 'cho', 'tf', 'kayn' and 'fiora'
This file will also output important events in the code such as a failure to find the character or the first success to initialize the tracking along with the frame they happpened on. The output is in the 'log' file.
