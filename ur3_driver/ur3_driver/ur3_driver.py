#!/usr/bin/env python3

import robotiq_gripper
from urx import Robot
from ur_dashboard import UR_DASHBOARD
import epics

from multiprocessing.connection import wait
from copy import deepcopy
import threading
from time import sleep
class ur3(UR_DASHBOARD):
    

    def __init__(self, IP:str = "164.54.116.129", PORT: int = 29999):

        super().__init__(IP=IP, PORT=PORT)

        # self.initialize() # Initilialize the robot

        # ur3 SETUP:
        i = 1
        while True:
            try:
                self.ur3 = Robot(self.IP)
                sleep(0.2)
                print('Successful ur3 connection on attempt #{}'.format(i))
                break

            except:
                print('Failed attempt #{}'.format(i))
                i+=1

        self.acceleration = 0.5
        self.velocity = 0.2
        self.speed_ms    = 0.750
        self.speed_rads  = 0.750
        self.accel_mss   = 1.200
        self.accel_radss = 1.200
        self.blend_radius_m = 0.001
        self.ref_frame = [0,0,0,0,0,0]

        self.home = [0.07965465094358973, 0.1331286487752626, 0.46622559375534944, 0.8893786745124569, -1.4184312527016423, -1.5680218376629318]
        self.home_J = [2.017202138900757, -1.137721137409546, -0.9426093101501465, -2.6425615749754847, -4.693090263997213, -3.8424256483661097]
        self.pipette_loc = [-0.30710397664568057, 0.2223363316295067, 0.25346649921490616, 0.9780579194931717, -1.3456500374612195, -1.5122814896417478]
        self.pipette_loc_J = [2.8711442947387695, -1.8251310787596644, -1.5156354904174805, -1.3721376222423096, -4.720762554799215, -3.0886977354632776]
        self.pipette_approach = [-0.30710468347240427, 0.22234393663902577, 0.2793166289891617, 0.977973715529265, -1.3455795650125528, -1.512392593568845]
        self.pipette_approach_J = [2.8711442947387695, -1.8102451763548792, -1.412275791168213, -1.4902585309794922, -4.720990244542257, -3.088721577321188]
        self.pipette_above = [-0.3075719688934094, 0.2227307810713913, 0.40515454739546075, 0.9815940238325527, -1.3416684284127856, -1.504904936327573]
        self.pipette_above_J = [2.869802236557007, -1.9749981365599574, -0.5613865852355957, -2.1772977314391078, -4.720307175313131, -3.0981438795672815]

        self.tip1_loc = [0.049076405377552826, 0.35130426249264163, 0.063, 0.9759108742683295, -1.3350220046082053, -1.5092226077826993]
        self.tip1_approach = [0.049076095756735466, 0.3513032390285145, 0.083, 0.9758916159413838, -1.3350252553821587, -1.5092057412143818]
        self.tip1_above = [0.04908221782054774, 0.3513003341332178, 0.138, 0.9758574103691817, -1.3350463108315163, -1.5091909291569083]
        self.tip2_loc = [0.04909177440821851, 0.3411316353820866, 0.0628, 0.977119433532159, -1.3337829736507698, -1.5108373189678133]
        self.tip2_approach = [0.04909177440821851, 0.3411316353820866, 0.083, 0.977119433532159, -1.3337829736507698, -1.5108373189678133]
        self.tip2_above = [0.04909177440821851, 0.3411316353820866, 0.138, 0.977119433532159, -1.3337829736507698, -1.5108373189678133]

        self.sample1 = [0.15220619381604186, 0.21043816573205595, 0.09618091909170277, 1.444826407763332, -0.2548060433102738, -0.31289353129621067]
        self.sample1_above = [0.15220723461648447, 0.2104311001071656, 0.14402782259610025, 1.4448359749910735, -0.2548206714588542, -0.31295915781137074]
        self.sample2_above = [0.15279755520703087, 0.18939793717407497, 0.14402267332894347, 1.444821393022025, -0.25485812796155616, -0.3128929822914916]
        self.sample2 = [0.15186061464767017, 0.18822197623964088, 0.09490910394912143, 1.4440966224799245, -0.255613147568461, -0.3122426586441542]

        self.empty_tube = [0.15203368788019977, 0.16531582069324421, 0.12185568609417977, 1.4402850302548993, -0.2846256403901101, -0.3468228184833902]
        self.empty_tube_above = [0.15203001904780783, 0.16531236663764431, 0.14222620538915642, 1.4402337440190125, -0.2846450307479814, -0.346876615018759]


        self.well1 = [0.12772478460859046, 0.21370236710062357, 0.08390608100945282, 1.4380130231592743, -0.2414629895555231, -0.2954608172533908]
        self.well1_above = [0.12773445855037924, 0.21371308008717516, 0.1271232135439438, 1.4380596200664426, -0.24151536289689018, -0.2954919320386042]
        self.trash_bin_above = [0.187412530306272, 0.2868009561100828, 0.12712991727750073, 1.438076830279249, -0.2414934112798892, -0.2954944172453427]
        self.trash_bin = [0.1874179391982658, 0.2867862635600429, 0.013156853887081085, 1.438022625162957, -0.24148065729851562, -0.2954808450568972]
    
    
        

        # CAMERA SETUP ON EPPICS:
        self.cam_acquire =  epics.PV("8idiARV1:cam1:Acquire")
        self.cam_image = epics.PV("8idiARV1:Pva1:Image")
        self.cam_capture =  epics.PV("8idiARV1:Pva1:Capture")

        # self.cam_acquire_busy = epics.PV("dp_eiger_xrd4:cam1:AcquireBusy")
        # self.cam_num_images = epics.PV("dp_eiger_xrd4:cam1:NumImages")
        # self.hdf_capture =  epics.PV("dp_eiger_xrd4:HDF1:Capture")
        # self.softglue_trigger =  epics.PV("8idi:softGlueA:MUX2-1_IN0_Signal")

        # PIPETTE SETUP:
        self.pipette = epics.PV("8idQZpip:m1.VAL")
        self.pipette_drop_tip_value = -8
        self.pipette_aspirate_value = 2.0
        self.pipette_dispense_value = -2.0
        self.droplet_value = 0.3
      
        # # TOOL CHANGER SETUP
        self.tool_changer = epics.PV("8idSMC100PIP:LJT7:1:DO0")

    def home_robot(self):
        # ref_frame = p[-0.304700, 0.161802, 0.191856, 0.000000, 0.000000, 0.000000]
        self.ur3.movej(self.home_J, self.accel_radss, self.speed_ms, 0, 0)
        sleep(4)

        print("Homing the robot")
        # End of main program

    def get_joint_angles(self):
        joint_angles = self.ur3.getl()
        return joint_angles

    def pick_pipette(self):
        """Picks up the pipette from docking location"""
        print("Picking up pipette")
        accel_mss   = 1.00
        speed_ms = 1.00
        try:
            sleep(1)
            self.ur3.movel(self.pipette_above,self.accel_mss,speed_ms,0,0)
            sleep(2)
            self.ur3.movel(self.pipette_approach,self.accel_mss,speed_ms,0,0)
            speed_ms = 0.01
            sleep(1)
            self.ur3.movel(self.pipette_loc,self.accel_mss,speed_ms,0,0)
            sleep(5)
            # LOCK THE TOOL CHANGER TO ATTACH THE PIPETTE HERE
            self.lock_tool_changer()
            sleep(5.0)
            self.ur3.movel(self.pipette_approach,self.accel_mss,speed_ms,0,0)
            sleep(1)
            speed_ms = 0.1
            self.ur3.movel(self.pipette_above,self.accel_mss,speed_ms,0,0)
            sleep(2)
        except Exception as err:
            print(err)

    def place_pipette(self):
        """Places the pipette onto docking location"""
        speed_ms = 0.5
        self.ur3.movel(self.pipette_above,self.accel_radss, self.speed_ms,0,0)
        sleep(2)
        self.ur3.movel(self.pipette_approach,self.accel_mss,speed_ms,0,0) 
        sleep(1)
        speed_ms = 0.01
        self.ur3.movel(self.pipette_loc,self.accel_mss,speed_ms,0,0)
        sleep(5)
        # Detach pipette
        self.unlock_tool_changer()
        sleep(5.0)
        self.ur3.movel(self.pipette_approach,self.accel_mss,speed_ms,0,0)
        sleep(1)
        speed_ms = 0.500
        self.ur3.movel(self.pipette_above,self.accel_mss,speed_ms,0,0)
        sleep(2)

    def pick_tip(self, x=0, y=0):
        """Picks up a new tip"""
        speed_ms = 0.100

        self.ur3.movel(self.tip1_above,self.accel_radss,self.speed_rads,0,0)
        sleep(2)
        speed_ms = 0.01
        self.ur3.movel(self.tip1_approach,self.accel_radss,self.speed_rads,0,0)
        sleep(2)    
        self.ur3.movel(self.tip1_loc,self.accel_mss,speed_ms,0,0)
        sleep(3)
        self.ur3.movel(self.tip1_approach,self.accel_mss,speed_ms,0,0)
        sleep(2)
        speed_ms = 0.1
        self.ur3.movel(self.tip1_above,self.accel_mss,speed_ms,0,0)
        sleep(2)

    def pick_tip2(self, x=0, y=0):
        """Picks up a new tip"""
        speed_ms = 0.100
        self.ur3.movel(self.tip2_above,self.accel_radss,self.speed_rads,0,0)
        sleep(2)
        speed_ms = 0.01
        self.ur3.movel(self.tip2_approach,self.accel_radss,self.speed_rads,0,0)
        sleep(2)    
        self.ur3.movel(self.tip2_loc,self.accel_mss,speed_ms,0,0)
        sleep(3)
        self.ur3.movel(self.tip2_approach,self.accel_mss,speed_ms,0,0)
        sleep(2)
        speed_ms = 0.1
        self.ur3.movel(self.tip2_above,self.accel_mss,speed_ms,0,0)
        sleep(2)    
    
    def make_sample(self):
        """Makes a new sample on the 96 well plate"""
        speed_ms = 0.1
        # MOVE WATER LOCATION
        self.ur3.movel(self.sample1_above,self.accel_mss,self.speed_ms,0,0)
        sleep(2)
        self.ur3.movel(self.sample1,self.accel_mss,speed_ms,0,0)
        sleep(2)
        # ASPIRATE FIRST SAMPLE
        self.aspirate_pipette()
        # sleep(1)
        self.ur3.movel(self.sample1_above,self.accel_mss,speed_ms,0,0)
        sleep(1)
        # MOVE TO THE 1ST WELL
        self.ur3.movel(self.well1_above,self.accel_mss,speed_ms,0,0)
        sleep(1)
        self.ur3.movel(self.well1,self.accel_mss,speed_ms,0,0)
        sleep(1)
        # DISPENSE FIRST SAMPLE INTO FIRST WELL
        self.dispense_pipette()
        # sleep(1)
        self.ur3.movel(self.well1_above,self.accel_mss,speed_ms,0,0)
        sleep(1)

        # Changing tip
        self.drop_tip_to_trash()
        self.pick_tip2()

        # MOVE SILICA LOCATION
        self.ur3.movel(self.sample2_above,self.accel_mss,self.speed_ms,0,0)
        sleep(3)
        self.ur3.movel(self.sample2,self.accel_mss,speed_ms,0,0)
        sleep(2)
        # ASPIRATE SECOND SAMPLE
        self.aspirate_pipette()       
        # sleep(1)
        self.ur3.movel(self.sample2_above,self.accel_mss,speed_ms,0,0)
        sleep(1)
        # MOVE TO THE 1ST WELL
        self.ur3.movel(self.well1_above,self.accel_mss,speed_ms,0,0)
        sleep(1)    
        self.ur3.movel(self.well1,self.accel_mss,speed_ms,0,0)
        sleep(1)
        # DISPENSE SECOND SAMPLE INTO FIRST WELL
        self.dispense_pipette()
        # sleep(1)
        # MIX SAMPLE
        for i in range(3):
            self.aspirate_pipette()
            # sleep(1)
            self.dispense_pipette()
            # sleep(1)
        # Aspirate all the liquid   
        self.aspirate_pipette()
        # sleep(1)
        self.aspirate_pipette()
        # sleep(1)
        self.ur3.movel(self.well1_above,self.accel_mss,speed_ms,0,0)
        sleep(1)

    def get_tool_changer_status(self):
        
        status = self.tool_changer.get()
        return status

    def lock_tool_changer(self):
        """Locks the tool changer"""
        self.tool_changer.put(1)

    def unlock_tool_changer(self):
        """Unlock the tool changer"""
        self.tool_changer.put(0)

    def take_camera_measurement(self):
        """Controls the camera to take the measurements"""
        pass

    def aspirate_pipette(self):
        current_value = self.pipette.get()
        self.pipette.put(float(current_value) + self.pipette_aspirate_value)
        sleep(1)

    def dispense_pipette(self):
        current_value = self.pipette.get()
        self.pipette.put(float(current_value)+ self.pipette_dispense_value)
        sleep(1)

    def create_droplet(self):
        """Drives pipette to create a droplet"""
        current_value = self.pipette.get()
        self.pipette.put(float(current_value) - self.droplet_value)
        sleep(10)

    def retrieve_droplet(self):
        """Retrieves the droplet back into the pipette tip"""
        current_value = self.pipette.get()
        self.pipette.put(float(current_value) + self.droplet_value + 0.5)
        sleep(1)

    def drop_tip_to_trash(self):
        self.ur3.movel(self.trash_bin_above, self.accel_mss, self.speed_ms,0,0)
        sleep(2)
        self.ur3.movel(self.trash_bin, self.accel_mss, self.speed_ms, 0, 0)
        sleep(2)
        self.eject_tip()
        sleep(1)
        self.ur3.movel(self.trash_bin_above, self.accel_mss, self.speed_ms,0,0)
        sleep(2)

    def eject_tip(self):
        """Ejects the pipette tip"""
        self.pipette.put(self.pipette_drop_tip_value)
        sleep(2)
        self.pipette.put(0)
        sleep(2)

    def empty_tip(self):
        
        speed_ms = 0.5
        # MOVE Empty Tube LOCATION
        self.ur3.movel(self.empty_tube_above,self.accel_mss,self.speed_ms,0,0)
        sleep(2)
        speed_ms = 0.1
        self.ur3.movel(self.empty_tube,self.accel_mss,speed_ms,0,0)
        sleep(2)

        # Dispense everything
        for i in range(3):
            self.dispense_pipette()
            sleep(1)

        self.ur3.movel(self.empty_tube_above,self.accel_mss,speed_ms,0,0)
        sleep(1)

    def droplet_exp(self):
        """Runs the full droplet experiment"""
        # self.home_robot()
        self.pick_pipette()
        self.home_robot()
        self.pick_tip()
        self.make_sample()
        self.home_robot()
        self.place_pipette()
        self.create_droplet()
        self.retrieve_droplet()
        self.pick_pipette()
        self.home_robot()
        self.empty_tip()
        self.drop_tip_to_trash()
        self.home_robot()
        self.place_pipette()
        self.disconnect_ur_robot()

    def disconnect_ur_robot(self):
        self.ur3.close()

"""
    def pick(self, pick_goal):

        '''Pick up from first goal position'''

        above_goal = deepcopy(pick_goal)
        above_goal[2] += 0.20

        print('Moving to home position')
        self.ur3.movel(self.home, self.acceleration, self.velocity)

        print('Moving to above goal position')
        self.ur3.movel(above_goal, self.acceleration, self.velocity)

        print('Moving to goal position')
        self.ur3.movel(pick_goal, self.acceleration, self.velocity)

        print('Closing gripper')
        self.gripper.move_and_wait_for_pos(self.gripper_close, self.gripper_speed, self.gripper_force)

        print('Moving back to above goal position')
        self.ur3.movel(above_goal, self.acceleration, self.velocity)

        print('Moving to home position')
        self.ur3.movel(self.home, self.acceleration, self.velocity)

"""

if __name__ == "__main__":

    robot = ur3()
    # robot.pick_pipette()
    # robot.pick_tip()

    # robot.retrieve_droplet()
    # robot.make_sample()
    # robot.place_pipette()
    # robot.create_droplet()
    # robot.pick_pipette()
    # robot.home_robot()
    # robot.empty_tip()
    # robot.drop_tip_to_trash()
    # robot.disconnect()
    # robot.unlock_tool_changer()
    robot.droplet_exp()
    # robot.home_robot()
    # robot.pick_pipette()
    # robot.pick_tip()
    # robot.aspirate_pipette()
    # robot.dispense_pipette()
    # sleep(5)
    # robot.create_droplet()
    # sleep(5)
    # robot.retrieve_droplet()
    # sleep(5)
    # robot.eject_tip()
    # robot.make_sample()
    # robot.place_pipette()

