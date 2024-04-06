<h2 align= center> 
SCARA MANIPULATOR


###

<p align="center">  
<img width="600" height="500" src="https://github.com/kimchisteww/Robotics2_FK-IK_Group14_SCARA_2024/assets/157762869/76a4d609-c8b1-4926-ab53-be6296825689"/>


<h2 align= center> ABSTRACT


###

>The SCARA manipulator, known for its Selective Compliance Assembly Robot Arm structure, offers a compelling blend of high-speed operation and efficient workspace utilization. This design prioritizes rapid picking and placing tasks within a cylindrical workspace, making it ideal for applications like assembly lines and pick-and-place automation.


<h2 align= center> INTRODUCTION

  
###


>SCARA manipulators, or Selective Compliance Articulated Robot Arms, are the champions of high-speed pick-and-place tasks in industrial settings. Their name reflects their strengths: selective compliance allows for precise positioning in the horizontal plane, while their articulated arm reaches diverse locations within a compact workspace. This focus on speed and efficiency makes them ideal for repetitive tasks in assembly lines, electronics manufacturing, and product packaging.

>CARAs boast impressive cycle times, meaning they can grab objects, move them quickly, and place them with pinpoint accuracy – all in a fraction of a second. Their design also ensures consistent and reliable movement, crucial for maintaining smooth and uninterrupted automation. Additionally, their compact size makes them a perfect fit for space-constrained environments, allowing for efficient use of valuable production floor real estate.


<h2 align= center>
SOLVING THE DEGREES OF FREEDOM OF A SCARA MANIPULATOR

###

DESCRIPTION

*HOW TO SOLVE THE DEGREES OF FREEDOM OF A SCARA MANIPULATOR?*


STEP-BY-STEP PROCESS



*STEP 1: Identify the number of m joints and n rigid moving links of the manipulator.

*STEP 2: Identify the number of constraints of the joint present in the manipulator.

	For Spatial:						
	[6-Ci]							
 	For Panar:
	[3-Ci]							
*STEP 3: Compute the mobility of the manipulator with the use of grubler’s criterion.

	For Spatial:						For Planar:
	M= 6n-i=1m(6-Ci)					M= 3n-i=1m(3-Ci)

<h2 align= center>
 DH FRAME RULES OF SCARA MANIPULATOR

###
DESCRIPTION

HOW TO ASSIGN THE FRAMES OF A SCARA MANIPULATOR?



STEP-BY-STEP PROCESS

DENAVIT-HARTENBERG (DH) PRELIMINARY RULES

RULE 1: Decide first the 3 views you want to project on your isometric drawing.

RULES 2: Identify the center of the frames.

RULE 3: Then draw your color coded arrows based on your decided 3 views.

RULES 4: Remember to make the arrows of Z and X axes easy to see for future computations.

ㅤ ㅤ

DENAVIT-HARTENBERG (DH) FRAME RULES

RULE 1: The Z axis must be the axis of rotation for a revolute/twisting, or the direction of translation for a prismatic joint.

RULE 2: The X axis must be perpendicular both to its own Z axis and the Z axis of the frame before it.

RULE 3: Rules for complying: Each X axis must intersect the Z axis of the frame before it. Rotate the axis until it hits the other Or translate the axis until it hits the other

RULE 4: All frames must follow the right-hand rule


<h2 align= center>
DH PARAMETRIC TABLE OF SCARA MANIPULATOR



###
DESCRIPTION

HOW TO OBTAIN THE DENAVIT-HARTENBERG PARAMETRIC TABLE OF A SCARA MANIPULATOR?


‣ STEP-BY-STEP PROCESS

DENAVIT-HARTENBERG NOTATION

STEP 1: Assign frames according to the 4 D-H frmae rules (On Task 2)

STEP 2: Fill out the D-H Parametric Table (On Task 3)

STEP 3: Plug the table into the Homogeneous Transformation Matrix (On Task 4)

STEP 4: Multiply the matrices together (On task 4)

<h2 align= center>
 HOMOGENEOUS TRANSFORMATION MATRIX OF SCARA MANIPULATOR

 


<h2 align= center> CONCLUSION


###

>In conclusion, creating a calculator that can efficiently calculate the forward and inverse kinematics of a SCARA manipulator is a valuable tool for engineers and researchers working in the field of robotics. This calculator can provide quick and accurate solutions to complex mathematical problems, allowing users to focus more on the design and implementation of their robot rather than tedious calculations. By automating these calculations, the calculator can streamline the design process and improve the overall efficiency of developing a SCARA manipulator. Ultimately, this tool has the potential to revolutionize the way robots are designed and constructed, making it an invaluable asset in the field of robotics.
