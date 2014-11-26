	==========================================================
	maltfy  Copyright (C) 2014  F. Brezo and Y. Rubio, i3visio
	==========================================================

Description:
============
maltfy is a GPLv3 piece of software conceived to export i3visio OSINT tools to 
Maltego.

License: GPLv3
==============

This is free software, and you are welcome to redistribute it under certain conditions.

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.


Installation:
=============
The installation under Python 2.7 for the release package is as follows:

1.- Download and install Maltego (Community Edition is free)

2.- Run Maltego and Create an account.

3.- Install usufy, entify, apify and maltfy running the following commands in 
each folder:
```
sudo python setup.py install
```

4.- Import the i3visio configuration from the maltfy/maltfy/i3visio-configuration.

5.- Update the Working directory of the loaded transforms to match the appropriate 
directory.
