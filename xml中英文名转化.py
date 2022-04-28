# encoding:utf-8
import os
import xml.etree.ElementTree as ET

count = 0
list_xml = []
dict = {"一次性快餐盒": "其他垃圾_一次性快餐盒",
"书籍纸张": "可回收物_书籍纸张",
"充电宝": "可回收物_充电宝",
"剩饭剩菜": "厨余垃圾_剩饭剩菜",
"包": "可回收物_包",
"垃圾桶": "可回收物_垃圾桶",
"塑料器皿": "可回收物_塑料器皿",
"塑料玩具": "可回收物_塑料玩具",
"塑料衣架": "可回收物_塑料衣架",
"大骨头": "厨余垃圾_大骨头",
"干电池": "有害垃圾_干电池",
"快递纸袋": "可回收物_快递纸袋",
"插头电线": "可回收物_插头电线",
"旧衣服": "可回收物_旧衣服",
"易拉罐": "可回收物_易拉罐",
"枕头": "可回收物_枕头",
"果皮果肉": "厨余垃圾_果皮果肉",
"毛绒玩具": "可回收物_毛绒玩具",
"污损塑料": "其他垃圾_污损塑料",
"污损用纸": "其他垃圾_污损用纸",
"洗护用品": "可回收物_洗护用品",
"烟蒂": "其他垃圾_烟蒂",
"牙签": "其他垃圾_牙签",
"玻璃器皿": "可回收物_玻璃器皿",
"砧板": "可回收物_砧板",
"筷子": "其他垃圾_筷子",
"纸盒纸箱": "可回收物_纸盒纸箱",
"花盆": "其他垃圾_花盆",
"茶叶渣": "厨余垃圾_茶叶渣",
"菜帮菜叶": "厨余垃圾_菜帮菜叶",
"蛋壳": "厨余垃圾_蛋壳",
"调料瓶": "可回收物_调料瓶",
"软膏": "有害垃圾_软膏",
"过期药物": "有害垃圾_过期药物",
"酒瓶": "可回收物_酒瓶",
"金属厨具": "可回收物_金属厨具",
"金属器皿": "可回收物_金属器皿",
"金属食品罐": "可回收物_金属食品罐",
"锅": "可回收物_锅",
"陶瓷器皿": "其他垃圾_陶瓷器皿",
"鞋": "可回收物_鞋",
"食用油桶": "可回收物_食用油桶",
"饮料瓶": "可回收物_饮料瓶",
"鱼骨": "厨余垃圾_鱼骨",
        }

openPath = "../VOCdevkit/VOC2007/Annotations"
savePath = "../VOCdevkit/VOC2007/Annotations1"
fileList = os.listdir(openPath)  # 得到进程当前工作目录中的所有文件名称列表
for fileName in fileList:  # 获取文件列表中的文件
    if fileName.endswith(".xml"):  # 只看xml文件
        print("filename=:", fileName)
        tree = ET.parse(os.path.join(openPath, fileName))
        root = tree.getroot()
        print("root-tag=:", root.tag)  # ',root-attrib:', root.attrib, ',root-text:', root.text)
        for child in root:  # 第一层解析
            if child.tag == "object":  # 找到object标签
                print(child.tag)
                for sub in child:
                    if sub.tag == "name":
                        print("标签名字:", sub.tag, ";文本内容:", sub.text)
                        if sub.text not in list_xml:
                            list_xml.append(sub.text)
                        if sub.text in list(dict.keys()):
                            sub.text = dict[sub.text]
                            print(sub.text)
                            count = count + 1
        tree.write(os.path.join(savePath, fileName), encoding='utf-8')
    print("=" * 20)

print(count)
for i in list_xml:
    print(i)