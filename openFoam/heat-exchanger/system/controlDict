/*--------------------------------*- C++ -*----------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           | Version:  11
     \\/     M anipulation  |
\*---------------------------------------------------------------------------*/
FoamFile
{
    format      ascii;
    class       dictionary;
    location    "system";
    object      controlDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

application     foamMultiRun; //Loads and executes an OpenFOAM solver modules for each region of a multiregion simulation e.g. for conjugate heat transfer

solver          twoPhaseVoFSolver; //Solver module base-class for for 2 immiscible ﬂuids using a VOF (volume of ﬂuid) phase-fraction based interface capturing approach, with optional mesh motion and mesh topology changes including adaptive re-meshing

startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         2000;

deltaT          1;

writeControl    timeStep;

writeInterval   100;

purgeWrite      0;

writeFormat     ascii;

writePrecision  6;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable true;

cacheTemporaryObjects
(
    kEpsilon:G
);

functions
{
    #includeFunc streamlinesLine
    (
        name=streamlines,
        start=(-0.0205 0.001 0.00001),
        end=(-0.0205 0.0251 0.00001),
        nPoints=10,
        fields=(p k U)
    )

    #includeFunc writeObjects(kEpsilon:G)
}

// ************************************************************************* //
