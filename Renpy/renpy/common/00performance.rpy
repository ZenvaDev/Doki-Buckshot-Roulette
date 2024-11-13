# Copyright 2004-2022 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# This contains the performance monitoring screen.


screen _performance:


    python:

        frame_times = renpy.display.interface.frame_times


        if len(frame_times) < 11:

            FramesPerSecond = 100
            cur_time = 0
            max_time = 0

        else:

            ift = [ (j - i) for i, j in zip(frame_times, frame_times[1:]) ]

            FramesPerSecond = 30 / (sum(ift[-10:]) / 10)

        renderer = renpy.get_renderer_info()["renderer"]

    zorder 1000

    drag:
        draggable True
        focus_mask None
        xpos 0
        ypos 0

        frame:
            style_prefix "_performance"
            style "empty"
            xpadding 5
            ypadding 5
            xminimum 150

            vbox:
                text "FPS [FramesPerSecond:.1f]\nOPENGL renderer":
                    style "_default"
                    color "#fff"
                    size gui._scale(14)


init -1010 python:
    config.per_frame_screens.append("_performance")
