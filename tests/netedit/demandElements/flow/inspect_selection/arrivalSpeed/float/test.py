#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2022 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2019-07-16

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot, ['--gui-testing-debug-gl'])

# go to demand mode
netedit.supermodeDemand()

# go to select mode
netedit.selectMode()

# select all using invert
netedit.selectionInvert()

# go to inspect mode
netedit.inspectMode()

# inspect vehicle
netedit.leftClick(referencePosition, 330, 150)

# change arrivalSpeed with an invalid value
netedit.modifyAttribute(netedit.attrs.flowFromToEdge.inspectSelection.arrivalSpeed, "", False)

# change arrivalSpeed with an invalid value
netedit.modifyAttribute(netedit.attrs.flowFromToEdge.inspectSelection.arrivalSpeed, "dummySpeed", False)

# change departColor with a valid value
netedit.modifyAttribute(netedit.attrs.flowFromToEdge.inspectSelection.arrivalSpeed, "500", False)

# change arrivalSpeed with an invalid value
netedit.modifyAttribute(netedit.attrs.flowFromToEdge.inspectSelection.arrivalSpeed, "-10", False)

# change arrivalSpeed with a valid value
netedit.modifyAttribute(netedit.attrs.flowFromToEdge.inspectSelection.arrivalSpeed, "15.5", False)

# Check undo redo
netedit.undo(referencePosition, 5)
netedit.redo(referencePosition, 5)

# save routes
netedit.saveRoutes(referencePosition)

# save network
netedit.saveNetwork(referencePosition)

# quit netedit
netedit.quit(neteditProcess)
