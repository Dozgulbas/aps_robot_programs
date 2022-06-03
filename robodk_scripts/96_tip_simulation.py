from robodk import robolink    # RoboDK API
from robodk import robomath    # Robot toolbox
import time
# Link to RoboDK

def home(folder_prog, gripper, ref_frame, i, j):

   RDK = robolink.Robolink()

   home1 = RDK.Item("Home",robolink.ITEM_TYPE_TARGET)
   
   new_prog = RDK.AddProgram("Pick_"+str(i)+"_"+str(j))
   new_prog.setParent(folder_prog)
   new_prog.setTool(gripper)
   new_prog.setFrame(ref_frame)

   # new_prog.Pause(2)
   new_prog.MoveL(home1,blocking=True)     
   # new_prog.Pause(2)       

   new_prog.RunProgram()
   
   time.sleep(2)

def pick_pipette_deck():
   
   RDK = robolink.Robolink()

   Pick_Pipette = RDK.Item('Pick_Pipette', robolink.ITEM_TYPE_PROGRAM)
   Pick_Pipette.RunProgram()

   time.sleep(1)

def prepare_sample():

   RDK = robolink.Robolink()

   aspirate = RDK.Item('Aspirate', robolink.ITEM_TYPE_PROGRAM)
   aspirate.RunProgram()

   time.sleep(1)

def drop_pippette():
   pass

def perform_droplet_exp():

   RDK = robolink.Robolink()

   droplet_exp = RDK.Item('Drop_EXP', robolink.ITEM_TYPE_PROGRAM)
   droplet_exp.RunProgram()

   time.sleep(19)

def trash_tip():

   RDK = robolink.Robolink()

   trash_tip = RDK.Item('drop_tip', robolink.ITEM_TYPE_PROGRAM)
   trash_tip.RunProgram()

   time.sleep(1)

def pick_tip(new_target, new_target_app,folder_prog, gripper, ref_frame, i, j):

   RDK = robolink.Robolink()

   ''' Setting up new tip in the line'''
   tip = RDK.Item("tip_col_"+ str(i+1) + "_" + str(j+1))


   '''Creating a program to approach and attach the next tip in the line''' 

   new_prog2 = RDK.AddProgram("Pick2_"+str(i)+"_"+str(j))
   new_prog2.setParent(folder_prog)
   new_prog2.setTool(gripper)
   new_prog2.setFrame(ref_frame)

   '''Creating a program to move above tip location with tp atteched''' 

   new_prog3 = RDK.AddProgram("Pick3_"+str(i)+"_"+str(j))
   new_prog3.setParent(folder_prog)
   new_prog3.setTool(gripper)
   new_prog3.setFrame(ref_frame)

   '''  Approach and attach the next tip in the line '''
   new_prog2.MoveL(new_target)   
   # new_prog2.Pause(3)     
   new_prog2.MoveL(new_target_app)
   # new_prog2.Pause(3)
   time.sleep(3)
   # new_prog2.Pause(3)
   new_prog2.RunProgram()
   time.sleep(3)

   ''' Attach tip to the pippette '''
   gripper.AttachClosest(tolerance_mm = 200, list_objects=[tip])

   ''' move above tip location with tp atteched '''
   # new_prog3.Pause(3)     
   new_prog3.MoveL(new_target) 
   # new_prog3.Pause(3)     
   new_prog3.RunProgram()
   time.sleep(1.5)

def palletizing_droplet_rows(ref_frame, ref_target, folder_prog, gripper, num_row, distance_x, distance_y, app_height, iter1, iter2):

   #If this function was called for num_row times, break this loop and move to next column
   if iter2 == num_row:
      return

   RDK = robolink.Robolink()

   
   new_target = RDK.AddTarget("Pick_Target_"+str(iter1)+"_"+str(iter2),ref_frame)
   new_target_pose = robomath.Offset(ref_target.Pose(), -1*iter1*distance_x, iter2*distance_y ,0)
   new_target.setPose(new_target_pose)

   
   new_target_app = RDK.AddTarget("App_Target_"+str(iter1)+"_"+str(iter2), ref_frame)
   new_target_app_pose = robomath.Offset(new_target.Pose(), 0, 0 ,app_height)
   new_target_app.setPose(new_target_app_pose)

#---------------------------------------------------------------
   home(folder_prog, gripper, ref_frame, iter1, iter2)

#---------------------------------------------------------------
   pick_pipette_deck()

#---------------------------------------------------------------
   pick_tip(new_target, new_target_app, folder_prog, gripper, ref_frame, iter1, iter2)

#---------------------------------------------------------------
   perform_droplet_exp()
#---------------------------------------------------------------

   time.sleep(5)
#---------------------------------------------------------------
   iter2 += 1

   return palletizing_droplet_rows(ref_frame, ref_target, folder_prog, gripper, num_row, distance_x, distance_y, app_height, iter1, iter2)


def palletizing_droplet_columns(ref_frame, ref_target, folder_prog, gripper, num_column, num_row, distance_x, distance_y, app_height, iter1):

   #If this function was called for num_column times, break this loop and complete palletizing
   if iter1 == num_column:
      return

   RDK = robolink.Robolink()
   iter2 = 0

   palletizing_droplet_rows(ref_frame, ref_target, folder_prog, gripper, num_row, distance_x, distance_y, app_height, iter1, iter2)

   iter1 += 1
   return palletizing_droplet_columns(ref_frame, ref_target, folder_prog, gripper, num_column, num_row, distance_x, distance_y, app_height, iter1)



def main():

   RDK = robolink.Robolink()


   column = 2
   row = 2
   distance_x = 9
   distance_y = 9
   app_height = -60


   RDK.Command("AddFolder", "Folder Pick Programs")
   robot = RDK.Item('UR3e', robolink.ITEM_TYPE_ROBOT)
   pippette =  RDK.Item("PIPET_ASSEMBLY", robolink.ITEM_TYPE_OBJECT)
   ref_target = RDK.Item("Approach_tip",robolink.ITEM_TYPE_TARGET)
   ref_frame = RDK.Item("Pipette_Base",robolink.ITEM_TYPE_FRAME)
   gripper = RDK.Item("ATI-9120-011M-000-000")
   folder_prog = RDK.Item("Folder Pick Programs",robolink.ITEM_TYPE_FOLDER)
   approach_pippette = RDK.Item("Approach_pippette",robolink.ITEM_TYPE_TARGET)
   attach_pippete = RDK.Item("Attach_pippette",robolink.ITEM_TYPE_TARGET)
   robot.setPoseTool(gripper)

   iter1 =0
   palletizing_droplet_columns(ref_frame, ref_target, folder_prog, gripper,column, row, distance_x, distance_y, app_height, iter1)



if __name__ == "__main__":
   main()
