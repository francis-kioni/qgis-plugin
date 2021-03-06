# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ShapefileLoader
                                 A QGIS plugin
 this plugin loads a shapefile and displays county name.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-02-05
        copyright            : (C) 2020 by GEGIS GROUP 2
        email                : jkuatgegis2015@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ShapefileLoader class from file ShapefileLoader.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .shafile_loader import ShapefileLoader
    return ShapefileLoader(iface)
