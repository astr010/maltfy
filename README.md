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

2.- Run Maltego. It is not necessary to create an account.

3.- We recommend to install the app under a specific folder to let Maltego find the
transforms without further configuration. The installation under a Linux system with 
a folder '/var/i3visio' (in Windows, it should be 'C:/i3visio') already created is
as follows:
```
# Navigate to the folder
cd /var/i3visio
git clone http://github.com/i3visio/maltfy
cd maltfy-master
sudo python setup.py build
sudo python setup.py install
```
or
```
# Navigate to the folder
cd /var/i3visio
wget http://github.com/i3visio/maltfy/archive/master.zip
unzip maltfy-master.zip
cd master
sudo python setup.py build
sudo python setup.py install
```
Superuser privileges are required so as to complete the installation. Afterwards, 
the module will be importable from any python code. You can check this by typing:
```
python -c "import maltfy"
```
If no error is displayed, the installation would have been performed correctly.

4.- Import the i3visio configuration from the maltfy-master/maltfy/i3visio-configuration.

5.- Update the Working directory of the loaded transforms if necessary to match the 
appropriate directory. By default it can be found under:
    - Linux:    /var/i3visio/maltfy-master/maltfy 
    - Windows:  c:/i3visio/maltfy-master/maltfy



