from robodk import robolink    # RoboDK API
from robodk import robomath    # Robot toolbox
import time
# Link to RoboDK

def attach_tip():
    RDK = robolink.Robolink()


    column = 1
    row = 1
    distance_x = 9
    distance_y = 9
    app_height = -60


    RDK.Command("AddFolder", "Folder Pick Programs")
    robot = RDK.Item('UR3e', robolink.ITEM_TYPE_ROBOT)
    pippette =  RDK.Item("PIPET_ASSEMBLY", robolink.ITEM_TYPE_OBJECT)
    tip1 = RDK.Item("300ul_tip_1")
    ref_target = RDK.Item("Approach_tip",robolink.ITEM_TYPE_TARGET)
    ref_frame = RDK.Item("Pipette_Base",robolink.ITEM_TYPE_FRAME)
    gripper = RDK.Item("ATI-9120-011M-000-000")
    folder_prog = RDK.Item("Folder Pick Programs",robolink.ITEM_TYPE_FOLDER)
    robot.setPoseTool(gripper)

    gripper.AttachClosest(tolerance_mm= 300, list_objects=[tip1])

if __name__ == "__main__":
    attach_tip()