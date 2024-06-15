// Define the length of the extrusion
length = 2;

// Define points
Point(1) = {0, 0, 0, 0.1};
Point(2) = {0.1, 0, 0, 0.1};
Point(3) = {0, 0.1, 0, 0.1};
Point(4) = {0, -0.1, 0, 0.1};
Point(5) = {-0.1, 0, 0, 0.1};
Point(6) = {0.4, 0, 0, 0.1};
Point(7) = {-0.4, 0, 0, 0.1};
Point(8) = {0, 0.4, 0, 0.1};
Point(9) = {0, -0.4, 0, 0.1};

// Define circles
Circle(1) = {2, 1, 3};
Circle(2) = {3, 1, 5};
Circle(3) = {5, 1, 4};
Circle(4) = {4, 1, 2};
Circle(5) = {6, 1, 8};
Circle(6) = {8, 1, 7};
Circle(7) = {7, 1, 9};
Circle(8) = {9, 1, 6};

// Define curve loops
Curve Loop(1) = {4, 1, 2, 3};
Curve Loop(2) = {5, 6, 7, 8};

// Define surfaces
Plane Surface(1) = {1};
Plane Surface(2) = {1,2};

// Extrude surfaces and curves
Extrude {0, 0, length} {
  Surface{1};
}
Extrude {0, 0, length} {
  Surface{2};
}

// Define physical groups
Physical Surface("tube_inlet", 105) = {1};
Physical Surface("tube_outlet", 106) = {30};
//Physical Surface("tube_wall", 107) = {17, 21, 25, 29};
Physical Surface("shell_wall", 108) = {59, 63, 67, 71};
Physical Surface("shell_outlet", 109) = {2};
Physical Surface("shell_inlet", 110) = {72};
Physical Volume("shell_fluid", 111) = {2};
Physical Volume("tube_fluid", 112) = {1};

