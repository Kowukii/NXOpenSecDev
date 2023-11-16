import NXOpen
import NXOpen_UF
import NXOpen.Features
import NXOpen_GeometricUtilities
import math


if __name__ == '__main__':
    theSession = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display

    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)

    nXObject1 = sketchInPlaceBuilder1.Commit()

    sketchInPlaceBuilder1.Destroy()

    sketch1 = nXObject1
    sketch1.Activate(NXOpen.Sketch.ViewReorient.FalseValue)

    expression1 = workPart.Expressions.CreateSystemExpression("200")

    nXMatrix1 = theSession.ActiveSketch.Orientation

    center1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 100.0, 0.0, (360.0 * math.pi / 180.0))

    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)

    geom1_1 = NXOpen.Sketch.ConstraintGeometry()

    geom1_1.Geometry = arc1
    geom1_1.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_1.SplineDefiningPointIndex = 0
    geom2_1 = NXOpen.Sketch.ConstraintGeometry()
    theSession.ActiveSketch.Update()