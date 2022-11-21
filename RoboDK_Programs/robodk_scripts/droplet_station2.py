def MainProgram():
  # Global parameters:
  global speed_ms    = 0.250
  global speed_rads  = 0.750
  global accel_mss   = 1.200
  global accel_radss = 1.200
  global blend_radius_m = 0.001
  global ref_frame = p[0,0,0,0,0,0]
  
  #--------------------------
  # Add any default subprograms here
  # For example, to drive a gripper as a program call:
  # def Gripper_Open():
  #   ...
  # end
  #
  # Example to drive a spray gun:
  def SprayOn(value):
    # use the value as an output:
    DO_SPRAY = 5
    if value == 0:
      set_standard_digital_out(DO_SPRAY, False)
    else:
      set_standard_digital_out(DO_SPRAY, True)
    end
  end

  # Example to drive an extruder:
  def Extruder(value):
    # use the value as an output:
    if value < 0:
      # stop extruder
    else:
      # start extruder
    end
  end
  
  # Example to move an external axis
  def MoveAxis(value):
    # use the value as an output:
    DO_AXIS_1 = 1
    DI_AXIS_1 = 1
    if value <= 0:
      set_standard_digital_out(DO_AXIS_1, False)
      
      # Wait for digital input to change state
      #while (get_standard_digital_in(DI_AXIS_1) != False):
      #  sync()
      #end
    else:
      set_standard_digital_out(DO_AXIS_1, True)
      
      # Wait for digital input to change state
      #while (get_standard_digital_in(DI_AXIS_1) != True):
      #  sync()
      #end
    end
  end
  #--------------------------
  
  # Subprogram Replace_objects
  def Replace_objects():
    # Replace objects
  end
  
  # Subprogram Pick_Pipette
  def Pick_Pipette():
    ref_frame = p[-0.304700, 0.161802, 0.191856, 0.000000, 0.000000, 0.000000]
    set_tcp(p[0.000000, 0.000000, 0.034000, 0.000000, 0.000000, 0.000000])
    movej([2.851030, -1.843155, -1.046072, -1.824375, -4.707502, 2.849983],accel_radss,speed_rads,0,0)
    movel([2.852339, -1.831898, -1.513073, -1.368644, -4.707502, 2.851292],accel_mss,speed_ms,0,0)
    # Attach to ATI-9120-011M-000-000
    movel([2.851030, -1.843155, -1.046072, -1.824375, -4.707502, 2.849983],accel_mss,speed_ms,0,0)
  end
  
  # Subprogram pick_tip
  def pick_tip():
    movej([1.579146, -2.131588, -1.744282, -0.841332, -4.711900, 0.004339],accel_radss,speed_rads,0,0)
    movel([1.579225, -2.316349, -1.785210, -0.615647, -4.711900, 0.004417],accel_mss,speed_ms,0,0)
    # Attach to ATI-9120-011M-000-000
    movel([1.579146, -2.131588, -1.744282, -0.841332, -4.711900, 0.004339],accel_mss,speed_ms,0,0)
  end
  
  # Subprogram Aspirate
  def Aspirate():
    movej([1.472791, -1.625024, -2.386022, -0.706179, -4.712406, -0.102015],accel_radss,speed_rads,0,0)
    movel([1.472787, -1.913160, -2.470898, -0.333155, -4.712406, -0.102019],accel_mss,speed_ms,0,0)
    movel([1.472791, -1.625024, -2.386022, -0.706179, -4.712406, -0.102015],accel_mss,speed_ms,0,0)
    movel([1.585541, -1.604082, -2.472224, -0.640902, -4.711865, 0.010734],accel_mss,speed_ms,0,0)
    movel([1.585635, -1.843958, -2.539594, -0.333653, -4.711865, 0.010827],accel_mss,speed_ms,0,0)
    movel([1.585541, -1.604082, -2.472224, -0.640902, -4.711865, 0.010734],accel_mss,speed_ms,0,0)
    movel([1.461989, -1.502449, -2.453968, -0.760819, -4.712459, -0.112816],accel_mss,speed_ms,0,0)
    movel([1.461972, -1.846715, -2.565704, -0.304810, -4.712459, -0.112835],accel_mss,speed_ms,0,0)
    movel([1.461989, -1.502449, -2.453968, -0.760819, -4.712459, -0.112816],accel_mss,speed_ms,0,0)
    movel([1.585541, -1.604082, -2.472224, -0.640902, -4.711865, 0.010734],accel_mss,speed_ms,0,0)
    movel([1.585635, -1.843958, -2.539594, -0.333653, -4.711865, 0.010827],accel_mss,speed_ms,0,0)
    movel([1.585541, -1.604082, -2.472224, -0.640902, -4.711865, 0.010734],accel_mss,speed_ms,0,0)
  end
  
  # Subprogram Drop_Pipette
  def Drop_Pipette():
    movej([2.851030, -1.843155, -1.046072, -1.824375, -4.707502, 2.849983],accel_radss,speed_rads,0,0)
    movel([2.852339, -1.831898, -1.513073, -1.368644, -4.707502, 2.851292],accel_mss,speed_ms,0,0)
    # Detach from ATI-9120-011M-000-000
    movel([2.851030, -1.843155, -1.046072, -1.824375, -4.707502, 2.849983],accel_mss,speed_ms,0,0)
  end
  
  # Subprogram pick_pipette_with_tip
  def pick_pipette_with_tip():
    movej([2.851030, -1.843155, -1.046072, -1.824375, -4.707502, 2.849983],accel_radss,speed_rads,0,0)
    movel([2.852339, -1.831898, -1.513073, -1.368644, -4.707502, 2.851292],accel_mss,speed_ms,0,0)
    # Attach to ATI-9120-011M-000-000
    # Attach to ATI-9120-011M-000-000
    movel([2.851030, -1.843155, -1.046072, -1.824375, -4.707502, 2.849983],accel_mss,speed_ms,0,0)
  end
  
  # Subprogram drop_tip
  def drop_tip():
    movej([1.410025, -1.952046, -2.000374, -0.764805, -4.712703, -0.164780],accel_radss,speed_rads,0,0)
    movej([1.409891, -2.498544, -2.015751, -0.202912, -4.712703, -0.164914],accel_radss,speed_rads,0,0)
    # Detach from ATI-9120-011M-000-000
    # Hide 300ul_tip_1
    # Attach to ATI-9120-011M-000-000
    movej([1.410025, -1.952046, -2.000374, -0.764805, -4.712703, -0.164780],accel_radss,speed_rads,0,0)
  end
  
  
  # Main program:
  # Program generated by RoboDK v5.4.0 for UR3e on 27/05/2022 18:27:49
  # Using nominal kinematics.
  Replace_objects()
  # Show 300ul_tip_1
  movej([2.454753, -1.227993, -0.868425, -2.618989, -4.708357, 2.453689],accel_radss,speed_rads,0,0) # end trace
  Pick_Pipette()
  pick_tip()
  Aspirate()
  Drop_Pipette()
  pick_pipette_with_tip()
  drop_tip()
  Drop_Pipette()
  # End of main program
end

MainProgram()
