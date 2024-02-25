disp('SCARA MANIPULATOR')

syms a1 a2 a3 a4 a5

%% Link lengths

a1 = 10;

a2 = 10;

a3 = 10;

a4 = 10;

a5 = 10;

%% D-H Parameters [theta, d, r, alpha, offset]

% if prismatic joint: theta = theta, d = 0, offset = 1, after offset put the value of d

% if revolute joint: theta = 0,offset = 0, after offset put the value of theta

H0_1 = Link([0,a1,a2,0,0,0]);

H0_1.qlim = pi/180*[-90 90];

H1_2 = Link([0,a3,a4,(180*pi)/180,0,0]);

H1_2.qlim = pi/180*[-90 90];

H2_3 = Link([0,0,0,0,1,a5]);

H2_3.qlim = [0 15];

Scara = SerialLink([H0_1 H1_2 H2_3], 'name', 'SCARA MANIPULATOR')

Scara.plot([0 0 0], 'workspace', [-5 30 -30 30 0 30])

Scara.teach

%% Forward Kinemtics

%syntax: FK = robot_variable.fkine(joint_variables)

Af = ([5,pi/2,pi/2]); %joint_variables FK = Scara_V3.fkine(Af)