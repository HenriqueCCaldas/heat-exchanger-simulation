// Gmsh project created on Thu May 16 20:32:33 2024
SetFactory("OpenCASCADE");
//+
Circle(1) = {0, 0, 0, 0.05, 0, Pi};
//+
Circle(2) = {0, 0, 0, 0.1, 0, Pi};
//+
Circle(3) = {0, 0, 0, 0.12, 0, Pi};
//+
Circle(4) = {0, 0, 0, 0.15, 0, Pi};
//+
Circle(5) = {0, 0, 0, 0.2, 0, Pi};
//+
Line(6) = {2, 1};
//+
Line(7) = {1, 3};
//+
Line(8) = {3, 5};
//+
Line(9) = {5, 7};
//+
Line(10) = {7, 9};
//+
Line(11) = {2, 4};
//+
Line(12) = {4, 6};
//+
Line(13) = {6, 8};
//+
Line(14) = {8, 10};
//+
Transfinite Curve {5, 4, 3, 2, 1} = 50 Using Progression 1;
//+
Transfinite Curve {6} = 50 Using Progression 1;
//+
Transfinite Curve {14, 13, 12, 8, 9, 10} = 10 Using Progression 1;
//+
Circle(15) = {0, 0, 0, 0.08, 0, Pi};
//+
Transfinite Curve {2} = 50 Using Progression 1;
//+
Transfinite Curve {15, 15} = 50 Using Progression 1;
//+
Line(16) = {12, 2};
//+
Line(17) = {2, 1};
//+
Line(18) = {1, 11};
//+
Transfinite Curve {6} = 50 Using Progression 1;
//+
Transfinite Curve {11, 7} = 10 Using Progression 1;
//+
Curve Loop(1) = {6, 7, 2, -11};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {14, -5, -10, -9, -8, 2, 12, 13};
//+
Plane Surface(2) = {2};
//+
Transfinite Curve {6, 6} = 10 Using Progression 1;
//+
Extrude {0, 0, 1} {
  Surface{1}; Surface{2}; Layers {50}; Recombine;
}
