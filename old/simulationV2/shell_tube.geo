// Define the length of the extrusion
length = 20;
tube = 1.0;
ratio = 4.1;
coupleWall = 1.1;

// Define points
Point(1) = {0, 0, 0, 1.0};
Point(2) = {tube, 0, 0, 1.0};
Point(3) = {0, tube, 0, 1.0};
Point(4) = {0, -tube, 0, 1.0};
Point(5) = {-tube, 0, 0, 1.0};
Point(6) = {ratio, 0, 0, 1.0};
Point(7) = {-ratio, 0, 0, 1.0};
Point(8) = {0, ratio, 0, 1.0};
Point(9) = {0, -ratio, 0, 1.0};
Point(10) = {coupleWall, 0, 0, 1.0};
Point(11) = {-coupleWall, 0, 0, 1.0};
Point(12) = {0, coupleWall, 0, 1.0};
Point(13) = {0, -coupleWall, 0, 1.0};

// Define circles
Circle(1) = {2, 1, 3};
Circle(2) = {3, 1, 5};
Circle(3) = {5, 1, 4};
Circle(4) = {4, 1, 2};
Circle(5) = {6, 1, 8};
Circle(6) = {8, 1, 7};
Circle(7) = {7, 1, 9};
Circle(8) = {9, 1, 6};
Circle(9) = {10, 1, 12};
Circle(10) = {12, 1, 11};
Circle(11) = {11, 1, 13};
Circle(12) = {13, 1, 10};

// Define curve loops
Curve Loop(1) = {4, 1, 2, 3};
Curve Loop(2) = {5, 6, 7, 8};
Curve Loop(3) = {9, 10, 11, 12};

// Define surfaces
Plane Surface(1) = {1};
Plane Surface(2) = {2,3};
Plane Surface(77) = {1,3};

// Extrude surfaces and curves
Extrude {0, 0, length} {
  Surface{1};
}
Extrude {0, 0, length} {
  Surface{2};
}

Extrude {0, 0, lenght} {
  Surface{77}
}
// Define physical groups
Physical Surface("tube_inlet", 105) = {1};
Physical Surface("tube_outlet", 106) = {30};
Physical Surface("shell_wall", 108) = {59, 63, 67, 71};
Physical Surface("shell_outlet", 109) = {2};
Physical Surface("shell_inlet", 110) = {72};
Physical Volume("shell_fluid", 111) = {2};
Physical Volume("tube_fluid", 112) = {1};

