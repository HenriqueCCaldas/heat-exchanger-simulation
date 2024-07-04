// Gmsh project created on Thu May 16 20:21:37 2024
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {5, 0, 0, 1.0};
//+
Line(1) = {1, 2};
//+
Transfinite Curve {1, 1} = 50 Using Progression 1;
//+
Extrude {0, 0.1, 0} {
  Curve{1}; Layers {3}; Recombine;
}
//+
Extrude {0, -0.1, 0} {
  Curve{1}; Layers {3}; Recombine;
}
//+
Extrude {0, 0.2, 0} {
  Curve{4}; Layers {10}; Recombine;
}
//+
Extrude {0, 0.2, 0} {
  Curve{10}; Layers {5}; Recombine;
}
//+
Extrude {0, 0.2, 0} {
  Curve{13}; Layers {2}; Recombine;
}
//+
Extrude {0, -0.2, 0} {
  Curve{7}; Layers {10}; Recombine;
}
//+
Extrude {0, -0.2, 0} {
  Curve{19}; Layers {5}; Recombine;
}
//+
Extrude {0, -0.2, 0} {
  Curve{22}; Layers {2}; Recombine;
}
