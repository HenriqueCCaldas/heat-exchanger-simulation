// Gmsh project created on Fri May 10 05:46:50 2024
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 0, 1, 1.0};
//+
Point(2) = {0, 1, 1, 1.0};
//+
Point(3) = {0, -1, 1, 1.0};
//+
Point(4) = {1, 0, 1, 1.0};
//+
Point(5) = {0.4, 0.4, 1, 1.0};
//+
Point(6) = {0.4, 0.45, 1, 1.0};
//+
Point(7) = {0.45, 0.4, 1, 1.0};
//+
Point(8) = {0.4, 0.35, 1, 1.0};
//+
Point(9) = {0.35, 0.4, 1, 1.0};
//+
Point(10) = {0.35, -0.4, 1, 1.0};
//+
Point(11) = {0.4, -0.4, 1, 1.0};
//+
Point(12) = {0.4, -0.45, 1, 1.0};
//+
Point(13) = {0.45, -0.4, 1, 1.0};
//+
Point(14) = {0.4, -0.35, 1, 1.0};
//+
Point(15) = {0.7, 0, 1, 1.0};
//+
Point(16) = {0.75, 0, 1, 1.0};
//+
Point(17) = {0.65, 0, 1, 1.0};
//+
Point(18) = {0.7, 0.05, 1, 1.0};
//+
Point(19) = {0.7, -0.05, 1, 1.0};
//+
Circle(1) = {3, 1, 4};
//+
Circle(2) = {4, 1, 2};
//+
Circle(3) = {12, 12, 11};
//+
Circle(3) = {12, 11, 13};
//+
Circle(4) = {13, 11, 14};
//+
Circle(5) = {14, 11, 10};
//+
Circle(6) = {10, 11, 12};
//+
Circle(7) = {19, 15, 16};
//+
Circle(8) = {16, 15, 18};
//+
Circle(9) = {18, 15, 17};
//+
Circle(10) = {17, 15, 19};
//+
Circle(11) = {8, 5, 7};
//+
Circle(12) = {7, 5, 6};
//+
Circle(13) = {6, 5, 9};
//+
Circle(14) = {9, 5, 8};
//+
Line(15) = {2, 2};
//+
Line(15) = {2, 1};
//+
Line(16) = {1, 3};
//+
Transfinite Curve {16, 15, 1, 2} = 5 Using Progression 1;
//+
Transfinite Curve {3, 6, 5, 4, 10, 7, 7, 8, 9, 9, 11, 14, 14, 13, 12} = 2 Using Progression 1;
//+
Extrude {0, 0, 2} {
  Curve{1}; Curve{2}; Curve{7}; Curve{10}; Curve{9}; Curve{8}; Curve{3}; Curve{6}; Curve{5}; Curve{4}; Curve{11}; Curve{14}; Curve{13}; Curve{12}; Layers {5}; Recombine;
}
//+
Curve Loop(15) = {16, 1, 2, 15};
//+
Curve Loop(16) = {13, 14, 11, 12};
//+
Curve Loop(17) = {9, 10, 7, 8};
//+
Curve Loop(18) = {5, 6, 3, 4};
//+
Curve Loop(19) = {1, 2, 15, 16};
//+
Plane Surface(15) = {16, 17, 18, 19};
//+
Line(46) = {22, 20};
//+
Curve Loop(20) = {19, 21, 46};
//+

//+
Curve Loop(21) = {19, 21, 46};
//+
Curve Loop(22) = {40, 45, 44, 42};
//+
Curve Loop(23) = {29, 28, 26, 24};
//+
Curve Loop(24) = {37, 36, 34, 32};
//+
Plane Surface(16) = {21, 22, 23, 24};
//+
Transfinite Curve {46} = 10 Using Progression 1;
//+
Extrude {0, 0, 2} {
  Curve{21}; Curve{19}; Curve{24}; Curve{29}; Curve{28}; Curve{26}; Curve{40}; Curve{42}; Curve{44}; Curve{45}; Curve{32}; Curve{37}; Curve{36}; Curve{34}; Layers {5}; Recombine;
}
//+
Line(76) = {37, 36};
//+
Curve Loop(39) = {51, 49, -76};
//+
Curve Loop(40) = {62, 67, 66, 64};
//+
Curve Loop(41) = {56, 58, 59, 54};
//+
Curve Loop(42) = {70, 72, 74, 75};
//+
Plane Surface(31) = {39, 40, 41, 42};
//+
Point(50) = {0, 0, 0, 1.0};
//+
Point(51) = {-1, 0, 0, 1.0};
//+
Point(52) = {0, 1, 0, 1.0};
//+
Point(53) = {0, -1, 0, 1.0};
//+
Circle(77) = {53, 50, 51};
//+
Circle(78) = {51, 50, 52};
//+
Line(79) = {52, 50};
//+
Line(80) = {50, 53};
//+
Circle(81) = {-0.4, 0.4, 0, 0.05, 0, 2*Pi};
//+
Circle(82) = {-0.4, -0.4, 0, 0.05, 0, 2*Pi};
//+
Circle(83) = {-0.7, 0, 0, 0.05, 0, 2*Pi};
//+
Transfinite Curve {80, 79, 78, 77} = 5 Using Progression 1;
//+
Transfinite Curve {82, 83, 81} = 8 Using Progression 1;
//+
Extrude {0, 0, 2} {
  Curve{78}; Curve{77}; Curve{83}; Curve{82}; Curve{81}; Layers {5}; Recombine;
}
//+
Line(95) = {59, 58};
//+
Curve Loop(48) = {86, -95, 88};
//+
Curve Loop(49) = {94};
//+
Curve Loop(50) = {90};
//+
Curve Loop(51) = {92};
//+
Plane Surface(37) = {48, 49, 50, 51};
//+
Curve Loop(52) = {80, 77, 78, 79};
//+
Curve Loop(53) = {83};
//+
Curve Loop(54) = {81};
//+
Curve Loop(55) = {82};
//+
Plane Surface(38) = {52, 53, 54, 55};
//+
Extrude {0, 0, 2} {
  Curve{88}; Curve{86}; Curve{90}; Curve{94}; Curve{92}; Layers {5}; Recombine;
}
//+
Extrude {0, 0, -1} {
  Curve{3}; Curve{4}; Curve{5}; Curve{6}; Curve{8}; Curve{9}; Curve{10}; Curve{7}; Curve{12}; Curve{11}; Curve{14}; Curve{13}; Layers {5}; Recombine;
}
//+
Extrude {0, 0, 1} {
  Curve{106}; Curve{102}; Curve{104}; Layers {5}; Recombine;
}
//+
Transfinite Curve {95, 95} = 10 Using Progression 1;
//+
Circle(137) = {-0.3, 0, 5, 0.2, 0, 2*Pi};
//+
Circle(138) = {0.3, 0, 0, 0.2, 0, 2*Pi};
//+
Transfinite Curve {138, 137, 76} = 10 Using Progression 1;
//+
Circle(139) = {53, 50, 52};
//+
Circle(140) = {52, 50, 53};
//+
Point(86) = {0, 0, 5, 1.0};
//+
Circle(141) = {36, 86, 37};
//+
Circle(142) = {37, 86, 36};
//+
Transfinite Curve {76, 142, 137, 138, 138, 140, 140} = 10 Using Progression 1;
//+
Extrude {0, 0, -1} {
  Curve{1}; Layers {5}; Recombine;
}
//+
Extrude {0, 0, 2} {
  Curve{1}; Layers {40}; Recombine;
}
//+
Extrude {0, 0, 2} {
  Curve{19}; Layers {40}; Recombine;
}
//+
Extrude {0, 0, 2} {
  Curve{2}; Layers {40}; Recombine;
}
//+
Extrude {0, 0, 2} {
  Curve{21}; Layers {40}; Recombine;
}
//+
Extrude {0, 0, 2} {
  Curve{78}; Curve{139}; Curve{86}; Curve{88}; Layers {40}; Recombine;
}
//+
Extrude {0, 0, 2} {
  Curve{77}; Layers {40}; Recombine;
}
//+
Extrude {0, 0, 1} {
  Curve{140}; Curve{100}; Curve{98}; Layers {5}; Recombine;
}
//+
Curve Loop(89) = {142, -76};
//+
Curve Loop(90) = {137};
//+
Curve Loop(91) = {136};
//+
Curve Loop(92) = {134};
//+
Curve Loop(93) = {132};
//+
Plane Surface(72) = {89, 90, 91, 92, 93};
//+
Curve Loop(94) = {80, -140, 79, 80, -140, 79, 80};
//+
Circle(179) = {52, 50, 87};
//+
Circle(180) = {87, 50, 52};
//+
Circle(181) = {0, 0, 5, 1, 0, Pi};
//+
Point(112) = {1, 1, 5, 1.0};
//+
Point(113) = {1, -1, 5, 1.0};
//+
Point(114) = {1, 1, 5, 1.0};
//+
Point(115) = {1, , 5, 1.0};
//+
Point(115) = {1, , 5, 1.0};
//+
Point(115) = {1, , 5, 1.0};
//+
Point(115) = {1, 1, 0, 1.0};
//+
Point(116) = {1, -1, 0, 1.0};
//+
Line(182) = {115, 52};
//+
Line(183) = {116, 115};
//+
Line(184) = {116, 87};
//+
Transfinite Curve {183} = 10 Using Progression 1;
//+
Transfinite Curve {184, 182} = 5 Using Progression 1;
//+
Circle(185) = {87, 50, 88};
//+
Circle(186) = {88, 50, 52};
//+
Line(187) = {50, 87};
//+
Line(188) = {52, 50};
//+
Curve Loop(94) = {140, -80, -79};
//+
Curve Loop(95) = {138};
//+
Curve Loop(96) = {127, 125, 130, 129};
//+
Curve Loop(97) = {122, 117, 119, 121};
//+
Curve Loop(98) = {109, 111, 113, 114};
//+
Plane Surface(73) = {94, 95, 96, 97, 98};
//+
Extrude {0, 0, -1} {
  Curve{138}; Layers {5}; Recombine;
}
//+
Transfinite Curve {137} = 5 Using Progression 1;
//+
Extrude {0, 0, 1} {
  Curve{137}; Layers {5}; Recombine;
}
//+
Extrude {0, 0, 1} {
  Curve{136}; Curve{134}; Curve{132}; Curve{67}; Curve{62}; Curve{64}; Curve{66}; Curve{72}; Curve{70}; Curve{75}; Curve{74}; Curve{56}; Curve{54}; Curve{59}; Curve{58}; Layers {5}; Recombine;
}
//+
Extrude {0, 0, -1} {
  Curve{83}; Curve{82}; Curve{81}; Curve{127}; Curve{125}; Curve{130}; Curve{129}; Curve{122}; Curve{117}; Curve{119}; Curve{121}; Curve{109}; Curve{111}; Curve{113}; Curve{114}; Layers {5}; Recombine;
}
//+
Extrude {0, 0, 1} {
  Curve{186}; Curve{145}; Curve{100}; Curve{98}; Layers {20}; Recombine;
}
//+
Extrude {0, 0, 1} {
  Curve{186}; Layers {20}; Recombine;
}
//+
Extrude {0, 0, -1} {
  Curve{2}; Layers {20}; Recombine;
}
