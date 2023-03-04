# Microbit_Reaction_Game

Overview: This program tests the player’s reaction time. It counts down from 3 and then randomly displays a target on the screen. The player is supposed to react as fast as possible and the program will scroll their reaction time in milliseconds across the screen.

New Learnings: One new thing learned from this lesson is the running_time() function. This function measure the amount of time the program has been running and helps when a program requires keeping track of time. Another new things learned is the fact that the display.scroll() function takes more than 1 parameter. It also takes two boolean parameters, loop and wait, which are not required. The loop parameter specifies wether the scroll should be infinitely looped and the wait parameter specifies wether the code should wait for the scroll to finish or move on. These parameters made us realize that some functions may take parameters even though they don’t require it, they are just set to default values if not specified.

Previous Lesson Connections: Some connections made with the previous lesson are with creating custom functions and utilzing them effectively. This program clearly displayed the benefits of going through the effort to create custom functions in python programs. These functions help reduce redundancy in code and make it massively easier to read, understand and debug any errors. They also reduce the length of the code without sacrificing any functionality which is always beneficial. 

Application: One application for this is for the medical industry. Doctors frequently conduct a test for a patient’s muscle reflexes with a reflex hammer during physical examinations. Similar to this, a program in python in python could be written utilizing the speaker hardware add-on to the microbit. Instead of a visual reflex test, it would test auditory reflexes. The user would be given an audible countdown and then a sound will be randomly played, the user must then press a button as fast as possible in reaction to the sound. The speaker would then say the reaction time. Another application could be with creating a stopwatch, timer, or clock using the running_time() function. What all of these things have in common is that they all need a way to keep track of time, this is where the running_time() function comes into play. This function could be used to make these programs using the buttons as inputs for things like setting the time or stopping and starting the stopwatch, and the screen as the output for things like displaying the time.

![Image](Flowchart.jpg)
