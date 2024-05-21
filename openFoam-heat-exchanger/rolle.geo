// Gmsh project created on [Date]
SetFactory("OpenCASCADE");

// Define the inner pipe
Cylinder(1) = {0, 0, 0, 5, 0, 0, 0.2, 2*Pi}; // Small cylinder (inner pipe)

// Define the outer shell
Cylinder(2) = {0, 0, 0, 5, 0, 0, 1, 2*Pi}; // Large cylinder (outer shell)

// Subtract the inner pipe volume from the outer shell volume
BooleanDifference{Volume{2};Delete;} {Volume{1};}

BooleanFragments{Surface{2};} {Surface{1};}

// Assign volumes to physical groups for OpenFOAM
Physical Volume("shell_fluid") = {2};
Physical Volume("pipe_fluid") = {1};

//Assign surface to physical groups for OpenFoam
Physical Surface("shell_inlet", 9) = {5};
Physical Surface("shell_wall", 10) = {4};
Physical Surface("shell_outlet", 11) = {6};
Physical Surface("tube_outlet", 12) = {2};
Physical Surface("tube_inlet", 13) = {3};
//Physical Surface("pipe", 14) = {1};
