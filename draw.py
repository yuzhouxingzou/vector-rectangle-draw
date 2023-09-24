print("您可以使用这个程序为ass文件输出简单的矢量矩形绘图代码")
OriginalWidth = int(input("请输入您想创建的矩形的宽度(包括圆角)"))
OriginalHeight = int(input("请输入您想创建的矩形的高度(包括圆角)"))
CornerLength = int(input("请输入圆角长度,0为不设置圆角"))
if OriginalWidth - 2*CornerLength < 0 or OriginalHeight - 2*CornerLength < 0:
    print("非法输入,圆角长度与矩形高度或宽度关系不合法")
    input()
    exit()
else: 
    if CornerLength == 0:
        print("m 0 0 l",OriginalWidth,"0 l",OriginalWidth,OriginalHeight,"l 0",OriginalHeight)     #执行非圆角矩形计算
        input()
        exit()
Coefficient = float(input("请输入圆角平滑系数"))
if Coefficient > 1 or Coefficient < 0:
    print("非法输入,圆角平滑系数需要在[0,1]范围内")
    input()
    exit()
cornerX = CornerLength                                  #左下圆角末点
cornerY = CornerLength
AnchorPoint1X = 0                                       #左下圆角锚点1
AnchorPoint1Y = int(Coefficient * cornerY)
AnchorPoint2X = int((1-Coefficient) * cornerY)          #左下圆角锚点2
AnchorPoint2Y = CornerLength
output = "m 0 0 b "+ str(AnchorPoint1X) + " " + str(AnchorPoint1Y) + " " + str(AnchorPoint2X) + " " + str(AnchorPoint2Y) + " " + str(cornerX) + " " + str(cornerY) + " l " + str(OriginalWidth - CornerLength) + " " + str(CornerLength)        #本行行末包含曲线后的直线部分
cornerX = OriginalWidth                             #第二条曲线终点,与前一个角做对称
cornerY = 0
AnchorPoint1X = OriginalWidth - AnchorPoint2X       #此为右下角的第一个锚点，与左下角第二个锚点关于直线x=(OriginalWidth/2)对称
temp = AnchorPoint1Y                                #临时存储第一步的AnchorPoint1Y,避免下一行将变量AnchorPoint1Y的值覆盖掉
AnchorPoint1Y = AnchorPoint2Y
AnchorPoint2X = OriginalWidth
AnchorPoint2Y = temp
output = output + " b " + str(AnchorPoint1X) + " " + str(AnchorPoint1Y) + " " + str(AnchorPoint2X) + " " + str(AnchorPoint2Y) + " " + str(cornerX) + " " + str(cornerY) + " l " + str(OriginalWidth) + " " + str(-OriginalHeight + 2*CornerLength)
cornerX = OriginalWidth - CornerLength            #曲线3
cornerY = -OriginalHeight + CornerLength
temp = AnchorPoint1X
AnchorPoint1X = AnchorPoint2X
AnchorPoint1Y = -(OriginalHeight - 2*CornerLength + AnchorPoint2Y)
AnchorPoint2X = temp
AnchorPoint2Y = -OriginalHeight + CornerLength
output = output + " b " + str(AnchorPoint1X) + " " + str(AnchorPoint1Y) + " " + str(AnchorPoint2X) + " " + str(AnchorPoint2Y) + " " + str(cornerX) + " " + str(cornerY) + " l " + str(CornerLength) + " " + str(-OriginalHeight + CornerLength)
cornerX = 0                                         #曲线4
cornerY = cornerY + CornerLength
AnchorPoint1X = OriginalWidth - AnchorPoint2X
temp = AnchorPoint1Y
AnchorPoint1Y = AnchorPoint2Y
AnchorPoint2X = 0
AnchorPoint2Y = temp
output = output + " b " + str(AnchorPoint1X) + " " + str(AnchorPoint1Y) + " " + str(AnchorPoint2X) + " " + str(AnchorPoint2Y) + " " + str(cornerX) + " " + str(cornerY)
print(output)
