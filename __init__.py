# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "ExportForWeb",
    "author" : "UttejK",
    "description" : "A simple Panel made to help with exporting the models for the web (threeJS)",
    "blender" : (3, 4, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Object"
}

import bpy

from .EFW_Op import EFW_OT_ShowNormals, EFW_OT_RecalculateOutside,  EFW_OT_ShowFaceOrientation, EFW_OT_SmartUV, EFW_OT_RecalculateInside, EFW_OT_OptionsForBake
from .EFW_Panel import EFW_PT_Panel,  EFW_PT_Menu

classes = (EFW_PT_Panel, EFW_OT_ShowNormals, EFW_OT_RecalculateOutside, EFW_OT_ShowFaceOrientation, EFW_OT_SmartUV , EFW_OT_RecalculateInside, EFW_OT_OptionsForBake, EFW_PT_Menu)

def register():
    for c in classes:
        bpy.utils.register_class(c)    
    ...

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    ...
