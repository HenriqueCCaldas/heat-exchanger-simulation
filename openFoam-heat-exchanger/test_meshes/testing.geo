// Gmsh project created on Tue May 21 07:26:18 2024
SetFactory("OpenCASCADE");
//+
Point(1) = {1, 1, 0, 1.0};
//+
Point(2) = {-1, 1, 0, 1.0};
//+
Point(3) = {-1, -1, 0, 1.0};
//+
Point(4) = {1, -1, 0, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 1};
//+
Curve Loop(1) = {1, 2, 3, 4};
//+
Plane Surface(1) = {1};
//+
Extrude {0, 0, 3} {
  Point{1}; Point{2}; Point{3}; Point{4}; Curve{1}; Curve{2}; Curve{3}; Curve{4}; Surface{1}; 
}
//+
Physical Surface("inlet", 25) = {10};
//+
Physical Surface("outlet", 26) = {1};
//+
Physical Surface("wall", 27) = {3, 4, 5, 2};
//+
Physical Volume("interior", 28) = {1};
