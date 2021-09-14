#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""3d Viewer example, with remote control.

This is an example of how you can use the 3D viewer with a program, and the
3D Viewer and controls will work automatically.
"""

import asyncio

import anki_vector
from anki_vector import opengl_viewer


async def my_function():
    await asyncio.sleep(20)
    print("done")


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial,
                           show_viewer=True,
                           enable_camera_feed=True,
                           enable_face_detection=True,
                           enable_custom_object_detection=True,
                           enable_nav_map_feed=True) as robot:
        viewer = opengl_viewer.OpenGLViewer(robot=robot)
        viewer.run(my_function)


if __name__ == "__main__":
    main()