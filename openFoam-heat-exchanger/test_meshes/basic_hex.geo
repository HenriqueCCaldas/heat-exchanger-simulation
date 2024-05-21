// Gmsh project created on Tue May 21 13:04:17 2024
SetFactory("OpenCASCADE");
Point(19) = {-2, 0, 0, 1.0};
//+
Point(20) = {-2, 0.2, 0, 1.0};
//+
Point(21) = {-2, 0, 0.2, 1.0};
//+
Point(22) = {-2, -0.2, 0, 1.0};
//+
Point(23) = {-2, 0, -0.2, 1.0};
//+
Circle(26) = {23, 19, 20};
//+
Circle(27) = {20, 19, 21};
//+
Circle(28) = {21, 19, 22};
//+
Circle(29) = {22, 19, 23};
//+
Curve Loop(11) = {27, 28, 29, 26};
//+
Plane Surface(11) = {11};
//+
Extrude {2, 0, 0} {
  Point{21}; Point{22}; Point{20}; Point{23}; Curve{28}; Curve{27}; Curve{29}; Curve{26}; Surface{11}; 
}
Point(36) = {0, 1, 0, 1.0};
//+
Point(37) = {0, 0, 1, 1.0};
//+
Point(38) = {0, -1, 0, 1.0};
//+
Point(39) = {0, 0, -1, 1.0};
//+
Point(40) = {0, 0, 0, 1.0};
//+
Circle(50) = {37, 40, 38};
//+
Circle(51) = {38, 40, 39};
//+
Circle(52) = {39, 40, 36};
//+
Circle(53) = {36, 40, 37};

//+
Curve Loop(32) = {40, 41, 38, 36};
//+
Plane Surface(31) = {32};
//+
Extrude {5, 0, 0} {
  Point{25}; Curve{40}; Curve{36}; Curve{38}; Point{24}; Curve{41}; Surface{20}; Point{27}; Point{26}; 
}
//+

//+
Curve Loop(42) = {51, 52, 53, 50};
//+
Curve Loop(43) = {38, 36, 40, 41};
//+
Plane Surface(41) = {42, 43};
//+
Curve Loop(44) = {51, 52, 53, 50};
//+
Extrude {5, 0, 0} {
  Surface{41}; Curve{52}; Point{39}; Curve{51}; Point{36}; Curve{53}; Curve{50}; Point{37}; Point{38}; 
}
//+
Extrude {2, 0, 0} {
  Curve{60}; Point{41}; Curve{62}; Point{42}; Curve{64}; Point{44}; Surface{40}; Curve{65}; 
}
/*
Point(81) = {-0.5, 0.7, 0, 1.0};
//+
Point(82) = {-0.5, 0.8, 0, 1.0};
//+
Point(83) = {-0.5, 0.6, 0, 1.0};
//+
Point(84) = {-0.5, 0.7, 0.1, 1.0};
//+
Point(85) = {-0.5, 0.7, -0.1, 1.0};
//+
Circle(121) = {85, 81, 82};
//+
Circle(122) = {82, 81, 84};
//+
Circle(123) = {84, 81, 83};
//+
Circle(124) = {83, 81, 85};
//+
Curve Loop(68) = {124, 121, 122, 123};
//+
Plane Surface(64) = {68};
//+
Extrude {0.5, 0, 0} {
  Curve{123}; Curve{122}; Curve{121}; Curve{124}; Surface{64}; 
}
//+
Point(94) = {5, -0.7, 0, 1.0};
//+
Point(95) = {5, -0.8, 0, 1.0};
//+
Point(96) = {5, -0.6, 0, 1.0};
//+
Point(97) = {5, -0.7, 0.1, 1.0};
//+
Point(98) = {5, -0.7, -0.1, 1.0};
//+
Circle(141) = {98, 94, 96};
//+
Circle(142) = {96, 94, 97};
//+
Circle(143) = {97, 94, 95};
//+
Circle(144) = {95, 94, 98};
//+
Curve Loop(78) = {141, 142, 143, 144};
//+
Plane Surface(74) = {78};
//+
Extrude {0.5, 0, 0} {
  Curve{142}; Curve{143}; Curve{144}; Curve{141}; Surface{74}; 
}
BooleanDifference{
	Surface{41};
	Delete;
}{
	Surface{73};
	Delete;}
	
BooleanDifference{
	Surface{54};
	Delete;
}{
	Surface{74};
	Delete;
}
*/
//+
Physical Surface("outershell", 121) = {42, 43, 45, 44, 54, 41};
//+
Physical Surface("innershell", 122) = {35, 33, 34, 32};
//+
Physical Surface("outpipe_shell", 123) = {56, 58, 55, 57};
//+
Physical Surface("outpipe_exit", 124) = {63};
//+
Physical Surface("inpipe_shell", 125) = {14, 15, 12, 13};
//+
Physical Surface("inpipe_entry", 126) = {11};
//+
Physical Surface("pipe_out", 127) = {40};
//+
Physical Surface("pipe_in", 128) = {20};
//+
Physical Volume("pipe", 129) = {2};
//+
Physical Volume("shell", 130) = {3};
//+
Physical Volume("inpipe", 131) = {1};
//+
Physical Volume("outpipe", 132) = {4};
