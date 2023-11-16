# This is a sample Python script.
import NXOpen
import NXOpen_UF
import NXOpen.Features
import NXOpen_GeometricUtilities
import math as np
# from .. import littleHelper
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    session = NXOpen.Session.GetSession()
    lw = session.ListingWindow
    lw.Open()
    lw.WriteLine('Hello NX 12')

def demo1():
    mysession = NXOpen.Session.GetSession()
    myUFsession = NXOpen.UF.UFSession.GetUFSession()
    mylw = mysession.ListingWindow
    workPart = mysession.Parts.Work
    displatPart = mysession.Parts.Display
    myui = NXOpen.UI.GetUI()
    mylw.Open()

    pt1 = myUFsession.Curve.CreatePoint([10., 10., 10.])
    pt2 = myUFsession.Curve.CreatePoint([20., 20., 20.])
    mylw.WriteLine('first point id is %s' % pt1)

def Foads_Hello_World():
    NXOpen_UF.UFSession.GetUFSession().Ui.DisplayMessage("Hello World!", 1)
    # Ui.DisplayMessage：弹窗消息页面

def Foads_Selectable_Text():
    listing_window = NXOpen.Session.GetSession().ListingWindow
    # ListingWindow：可选、可搜索的文本页面
    # NXOpen.Session.GetSession()：获取当前任务对话
    listing_window.Open()
    listing_window.WriteFullline("Hello NX")
    listing_window.Close()

def cylinder_builder(session=NXOpen.Session.GetSession(),
                     work_part=NXOpen.Session.GetSession().Parts.Work,
                     height=100,
                     diameter=50):
    mark_id = session.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Cylinder")

    cylinder = work_part.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    cylinder.Diameter.SetFormula(str(diameter))
    cylinder.Height.SetFormula(str(height))
    nx_object = cylinder.Commit()
    return nx_object, mark_id


def circle_builder(thesession, work_part, centerx, centery, centerz, diameter):


    displayPart = theSession.Parts.Display

    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)

    nXObject1 = sketchInPlaceBuilder1.Commit()

    sketchInPlaceBuilder1.Destroy()

    sketch1 = nXObject1
    sketch1.Activate(NXOpen.Sketch.ViewReorient.FalseValue)

    expression1 = workPart.Expressions.CreateSystemExpression(str(diameter))

    nXMatrix1 = theSession.ActiveSketch.Orientation

    center1 = NXOpen.Point3d(centerx, centery, centerz)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, float(diameter)/2, 0.0, (360.0 * np.pi / 180.0))

    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)

    geom1_1 = NXOpen.Sketch.ConstraintGeometry()

    geom1_1.Geometry = arc1
    geom1_1.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_1.SplineDefiningPointIndex = 0
    geom2_1 = NXOpen.Sketch.ConstraintGeometry()
    theSession.ActiveSketch.Update()
    return sketch1


def paddleExpression(workPart, params, idlist):
    listing_window = NXOpen.Session.GetSession().ListingWindow
    listing_window.Open()
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    for i, e in enumerate(idlist):

        exp_id = e
        exp = str(exp_id) + '=' + str(params[str(exp_id)])
        listing_window.WriteFullline(exp)
        try:
            expression = workPart.Expressions.CreateWithUnits(exp, unit1)
            # 设置参数t=================================================================================
            objects = [NXOpen.NXObject.Null] * 1
            # 创建对象
            objects[0] = expression
            # 对象赋值
            theSession.UpdateManager.MakeUpToDate(objects)
            # 表达式更新
        except:
            expression = workPart.Expressions.FindObject(str(exp_id))
            workPart.Expressions.EditWithUnits(expression, unit1, str(params[str(exp_id)]))
            listing_window.WriteLine('重复:')
            listing_window.WriteLine(str(exp_id))
            pass
    return listing_window

def lawCurve(workPart, list_window, argx, argy):
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "开始")

    lawCurveBuilder1 = workPart.Features.CreateLawCurveBuilder(NXOpen.Features.LawCurve.Null)

    expression5 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)

    expression6 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)

    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)

    lawCurveBuilder1.XLaw.LawType = NXOpen_GeometricUtilities.LawBuilder.Type.ByEquation

    lawCurveBuilder1.XLaw.Value.RightHandSide = "0"

    lawCurveBuilder1.XLaw.StartValue.RightHandSide = "0"

    lawCurveBuilder1.XLaw.EndValue.RightHandSide = "0"

    lawCurveBuilder1.XLaw.Function = argx

    lawCurveBuilder1.YLaw.LawType = NXOpen_GeometricUtilities.LawBuilder.Type.ByEquation

    lawCurveBuilder1.YLaw.Value.RightHandSide = "0"

    lawCurveBuilder1.YLaw.StartValue.RightHandSide = "0"

    lawCurveBuilder1.YLaw.EndValue.RightHandSide = "0"

    lawCurveBuilder1.YLaw.Function = argy

    lawCurveBuilder1.ZLaw.LawType = NXOpen_GeometricUtilities.LawBuilder.Type.ByEquation

    lawCurveBuilder1.ZLaw.Value.RightHandSide = "0"

    lawCurveBuilder1.ZLaw.StartValue.RightHandSide = "0"

    lawCurveBuilder1.ZLaw.EndValue.RightHandSide = "0"

    theSession.SetUndoMarkName(markId18, "规律曲线 对话框")

    lawCurveBuilder1.XLaw.AlongSpineData.Spine.DistanceTolerance = 0.001

    lawCurveBuilder1.XLaw.AlongSpineData.Spine.ChainingTolerance = 0.00095

    lawCurveBuilder1.XLaw.LawCurve.DistanceTolerance = 0.001

    lawCurveBuilder1.XLaw.LawCurve.ChainingTolerance = 0.00095

    lawCurveBuilder1.YLaw.AlongSpineData.Spine.DistanceTolerance = 0.001

    lawCurveBuilder1.YLaw.AlongSpineData.Spine.ChainingTolerance = 0.00095

    lawCurveBuilder1.YLaw.LawCurve.DistanceTolerance = 0.001

    lawCurveBuilder1.YLaw.LawCurve.ChainingTolerance = 0.00095

    lawCurveBuilder1.ZLaw.AlongSpineData.Spine.DistanceTolerance = 0.001

    lawCurveBuilder1.ZLaw.AlongSpineData.Spine.ChainingTolerance = 0.00095

    lawCurveBuilder1.ZLaw.LawCurve.DistanceTolerance = 0.001

    lawCurveBuilder1.ZLaw.LawCurve.ChainingTolerance = 0.00095

    nXObject1 = lawCurveBuilder1.Commit()

    lawCurveBuilder1.Destroy()

    workPart.Expressions.Delete(expression5)

    workPart.Expressions.Delete(expression6)

    workPart.Expressions.Delete(expression7)


def my_curve_builder2(workPart, params, idlist):
    listing_window = paddleExpression(workPart, params, idlist)

    lawCurve(workPart, listing_window, 'xt', 'yt')

    lawCurve(workPart, listing_window, 'x1t', 'y1t')

    listing_window.Close()




def my_curve_builder(theSession, workPart, params):

    listing_window = NXOpen.Session.GetSession().ListingWindow
    listing_window.Open()

    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "开始")
    # markId 是录制时的进程标记,类似于checkpoint,
    listing_window.WriteFullline("markId1:")
    # 启动listing_window并写入
    # expression_list = workPart.Expressions.GetInterpartExpressionNames()
    listing_window.WriteFullline(str(markId1))
    # Features.LawCurve 能找到
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    # 设置单位
    exp1_id = 't'
    exp1 = exp1_id + '=' + str(params[exp1_id])
    listing_window.WriteFullline(exp1)
    try:
        expression1 = workPart.Expressions.CreateWithUnits(exp1, unit1)
        # 设置参数t=================================================================================
        markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Check Circular")
        # 设置参数t标记
        objects1 = [NXOpen.NXObject.Null] * 1
        # 创建对象
        objects1[0] = expression1
        # 对象赋值
        theSession.UpdateManager.MakeUpToDate(objects1, markId5)
        # 表达式更新
    except:
        expression1 = workPart.Expressions.FindObject(exp1_id)
        workPart.Expressions.EditWithUnits(expression1, unit1, str(params[exp1_id]))
        listing_window.WriteLine('重复:')
        listing_window.WriteLine(exp1_id)
        pass

    exp2_id = 'zt'
    exp2 = exp2_id + '=' + str(params[exp2_id])
    listing_window.WriteFullline(exp2)
    try:
        expression2 = workPart.Expressions.CreateWithUnits(exp2, unit1)
        # 设置参数t=================================================================================
        markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Check Circular")
        # 设置参数t标记
        objects2 = [NXOpen.NXObject.Null] * 1
        # 创建对象
        objects2[0] = expression2
        # 对象赋值
        theSession.UpdateManager.MakeUpToDate(objects2, markId6)
        # 表达式更新
    except:
        expression2 = workPart.Expressions.FindObject(exp2_id)
        workPart.Expressions.EditWithUnits(expression2, unit1, str(params[exp2_id]))
        listing_window.WriteLine('重复:')
        listing_window.WriteLine(exp2_id)
        pass

    exp3_id = 'xt'
    exp3 = exp3_id + '=' + str(params[exp3_id])
    listing_window.WriteFullline(exp3)
    try:
        expression3 = workPart.Expressions.CreateWithUnits(exp3, unit1)
        # 设置参数t=================================================================================
        markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Check Circular")
        # 设置参数t标记
        objects3 = [NXOpen.NXObject.Null] * 1
        # 创建对象
        objects3[0] = expression3
        # 对象赋值
        theSession.UpdateManager.MakeUpToDate(objects3, markId7)
        # 表达式更新
    except:
        expression3 = workPart.Expressions.FindObject(exp3_id)
        workPart.Expressions.EditWithUnits(expression3, unit1, str(params[exp3_id]))
        listing_window.WriteLine('重复:')
        listing_window.WriteLine(exp3_id)
        pass

    exp4_id = "yt"
    exp4 = exp4_id + '=' + str(params[exp4_id])
    listing_window.WriteFullline(exp4)
    try:
        expression4 = workPart.Expressions.CreateWithUnits(exp4, unit1)
        # 设置参数t=================================================================================
        markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Check Circular")
        # 设置参数t标记
        objects4 = [NXOpen.NXObject.Null] * 1
        # 创建对象
        objects4[0] = expression4
        # 对象赋值
        theSession.UpdateManager.MakeUpToDate(objects4, markId8)
        # 表达式更新
    except:
        expression4 = workPart.Expressions.FindObject(exp4_id)
        listing_window.WriteFullline(str(expression4))
        workPart.Expressions.EditWithUnits(expression4, unit1, str(params[exp4_id]))
        listing_window.WriteLine('重复:')
        listing_window.WriteLine(exp4_id)
        pass




    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "开始")

    lawCurveBuilder1 = workPart.Features.CreateLawCurveBuilder(NXOpen.Features.LawCurve.Null)

    expression5 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)

    expression6 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)

    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)

    lawCurveBuilder1.XLaw.LawType = NXOpen_GeometricUtilities.LawBuilder.Type.ByEquation

    lawCurveBuilder1.XLaw.Value.RightHandSide = "0"

    lawCurveBuilder1.XLaw.StartValue.RightHandSide = "0"

    lawCurveBuilder1.XLaw.EndValue.RightHandSide = "0"

    lawCurveBuilder1.YLaw.LawType = NXOpen_GeometricUtilities.LawBuilder.Type.ByEquation

    lawCurveBuilder1.YLaw.Value.RightHandSide = "0"

    lawCurveBuilder1.YLaw.StartValue.RightHandSide = "0"

    lawCurveBuilder1.YLaw.EndValue.RightHandSide = "0"

    lawCurveBuilder1.ZLaw.LawType = NXOpen_GeometricUtilities.LawBuilder.Type.ByEquation

    lawCurveBuilder1.ZLaw.Value.RightHandSide = "0"

    lawCurveBuilder1.ZLaw.StartValue.RightHandSide = "0"

    lawCurveBuilder1.ZLaw.EndValue.RightHandSide = "0"

    theSession.SetUndoMarkName(markId18, "规律曲线 对话框")

    lawCurveBuilder1.XLaw.AlongSpineData.Spine.DistanceTolerance = 0.001

    lawCurveBuilder1.XLaw.AlongSpineData.Spine.ChainingTolerance = 0.00095

    lawCurveBuilder1.XLaw.LawCurve.DistanceTolerance = 0.001

    lawCurveBuilder1.XLaw.LawCurve.ChainingTolerance = 0.00095

    lawCurveBuilder1.YLaw.AlongSpineData.Spine.DistanceTolerance = 0.001

    lawCurveBuilder1.YLaw.AlongSpineData.Spine.ChainingTolerance = 0.00095

    lawCurveBuilder1.YLaw.LawCurve.DistanceTolerance = 0.001

    lawCurveBuilder1.YLaw.LawCurve.ChainingTolerance = 0.00095

    lawCurveBuilder1.ZLaw.AlongSpineData.Spine.DistanceTolerance = 0.001

    lawCurveBuilder1.ZLaw.AlongSpineData.Spine.ChainingTolerance = 0.00095

    lawCurveBuilder1.ZLaw.LawCurve.DistanceTolerance = 0.001

    lawCurveBuilder1.ZLaw.LawCurve.ChainingTolerance = 0.00095

    nXObject1 = lawCurveBuilder1.Commit()

    lawCurveBuilder1.Destroy()

    workPart.Expressions.Delete(expression5)

    workPart.Expressions.Delete(expression6)

    workPart.Expressions.Delete(expression7)

    listing_window.Close()
    NXOpen_UF.UFSession.GetUFSession().Ui.DisplayMessage("Finish So Far", 1)


if __name__ == '__main__':
    R = 40
    r = 12
    e = 1
    Rre = R + r + e
    Re = R + e
    alpha_top = (R + r + e) ** 2 - (R + e) ** 2 + R ** 2
    alpha_down = 2 * (R + r + e) * R
    alpha = np.acos(alpha_top / alpha_down)
    idlist = ['t', 'zt', 'xt', 'yt', 'x1t', 'y1t']
    params = {
        't': 1,
        'xt': str(Rre) + '*sin(1.5*3.14+1*t*360)+' + str(Re) + '*sin(0.5*3.14-' + str(alpha) + '+(3*t*360))',
        'yt': str(Rre) + '*cos(1.5*3.14+1*t*360)+' + str(Re) + '*cos(0.5*3.14-' + str(alpha) + '+(3*t*360))',
        'y1t': str(Rre) + '*sin(1.5*3.14+1*t*360)+' + str(Re) + '*sin(0.5*3.14-' + str(alpha) + '+(3*t*360))',
        'x1t': '-(' + str(Rre) + '*cos(1.5*3.14+1*t*360)+' + str(Re) + '*cos(0.5*3.14-' + str(alpha) + '+(3*t*360)))',
        'zt': 0
    }

    # print_hi('PyCharm')
    # Foads_Selectable_Text()
    # demo1()
    # cylinder_builder(height=40, diameter=100)
    theSession = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    my_curve_builder2(workPart, params, idlist)
    recent_sketch = circle_builder(theSession, workPart, 0.0, 0.0, 0.0, R * 2)
    circle_builder(theSession, workPart, 0.0, 0.0, 0.0, r * 2)
    NXOpen_UF.UFSession.GetUFSession().Ui.DisplayMessage("Finish So Far", 1)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
