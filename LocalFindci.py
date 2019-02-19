#导入资源文件路径生成模块
from resource import resource_path
import re, os

#分类来检索单词

#所有tell()指针减去5字节(换行符字节),到单词前面位置
#实际如果有大写优先以大写的字母索引为判断标准,大写字母的值比较相比下小些,以下同理

#分段加快查询速度

# A B    C    D E     F     G/H    I    J K L     M     N/O P    Q    R S    T     /U V W    X    Y Z

# #所在指针数减去5字节后的指针位置,用每行遍历的方法的代码查出的指针位置

# X
# #20531459

# T
# #18105744

# Q
# #14395319

# m
# #10675521

# I
# #8904612

# F
# #6378372

# C
# # 2469170


def LLocalfindci(ci):
    f = open('%s'\
    %resource_path(os.path.join("localdirsource","DIR.txt")),'rb')
    f.seek(0,0)

    #实际X
    if ci[0].lower() > "x" or ci[0].lower() == 'x':
        f.seek(20531459,0)
        ##循环读字节数区间内的每行进行正则表达式判断，匹配成功则指针返回开头、结束循环
        while True:
            # print('0000000')
            line = f.readline().decode()
            rresult = re.findall('"%s\\r\\n'%ci,line)
            if rresult:
                # print(rresult)
                #跳过第一行
                line = f.readline().decode()
                #初始化一个字符串
                StrResult = ''
                #检索单词成功后检索单词意义结束位置并返回字符串
                while True:
                    line = f.readline().decode()
                    line2 = line[::-1]
                    rresult = re.findall('\\n\\r;;"',line2)
                    if not rresult:
                        StrResult += line
                    else:
                        StrResult += line
                        f.seek(0,0)
                        f.close()
                        return StrResult
            else:
                if f.tell() > 20625884:
                    # print('没有记录')
                    f.seek(0,0)
                    break
    else:
        #实际T
        #为True跳到T的索引，文本没有t
        if ci[0].lower() > "t" or ci[0].lower() == "t":
            f.seek(18105744,0)
            ##
            while True:
                # print('1111111')
                line = f.readline().decode()
                rresult = re.findall('"%s\\r\\n'%ci,line)
                if rresult:
                    # print(rresult)
                    #跳过第一行
                    line = f.readline().decode()
                    #初始化一个字符串
                    StrResult = ''
                    #检索单词成功后检索单词意义结束位置并返回字符串
                    while True:
                        line = f.readline().decode()
                        line2 = line[::-1]
                        rresult = re.findall('\\n\\r;;"',line2)
                        if not rresult:
                            StrResult += line
                        else:
                            StrResult += line
                            f.seek(0,0)
                            f.close()
                            return StrResult

                else:
                    if f.tell() > 20531459:
                        # print('没有记录')
                        f.seek(0,0)
                        break
        else:
            #实际Q
            if ci[0].lower() > "q" or ci[0].lower() == "q":
                f.seek(14395319,0)
                ##
                while True:
                    # print('33333333')
                    line = f.readline().decode()
                    rresult = re.findall('"%s\\r\\n'%ci,line)
                    if rresult:
                        # print(rresult)
                        #跳过第一行
                        line = f.readline().decode()
                        #初始化一个字符串
                        StrResult = ''
                        #检索单词成功后检索单词意义结束位置并返回字符串
                        while True:
                            line = f.readline().decode()
                            line2 = line[::-1]
                            rresult = re.findall('\\n\\r;;"',line2)
                            if not rresult:
                                StrResult += line
                            else:
                                StrResult += line
                                f.seek(0,0)
                                f.close()
                                return StrResult

                    else:
                        if f.tell() > 18105744:
                            # print('没有记录')
                            f.seek(0,0)
                            break
                        else:
                            continue
            else:
                #实际m
                if ci[0].lower() > 'm' or ci[0].lower() == 'm':
                    f.seek(10675521,0)
                    ##
                    while True:
                        # print('44444444')
                        line = f.readline().decode()
                        rresult = re.findall('"%s\\r\\n'%ci,line)
                        if rresult:
                            # print(rresult)
                            #跳过第一行
                            line = f.readline().decode()
                            #初始化一个字符串
                            StrResult = ''
                            #检索单词成功后检索单词意义结束位置并返回字符串
                            while True:
                                line = f.readline().decode()
                                line2 = line[::-1]
                                rresult = re.findall('\\n\\r;;"',line2)
                                if not rresult:
                                    StrResult += line
                                else:
                                    StrResult += line
                                    f.seek(0,0)
                                    f.close()
                                    return StrResult

                        else:
                            if f.tell() > 14395319:
                                # print('没有记录')
                                f.seek(0,0)
                                break
                            else:
                                continue
                else:
                    #实际I
                    if ci[0].lower() > "i" or ci[0].lower() == 'i':
                        f.seek(8904612,0)
                        ##
                        while True:
                            # print('555555555')
                            line = f.readline().decode()
                            rresult = re.findall('"%s\\r\\n'%ci,line)
                            if rresult:
                                # print(rresult)
                                #跳过第一行
                                line = f.readline().decode()
                                #初始化一个字符串
                                StrResult = ''
                                #检索单词成功后检索单词意义结束位置并返回字符串
                                while True:
                                    line = f.readline().decode()
                                    line2 = line[::-1]
                                    rresult = re.findall('\\n\\r;;"',line2)
                                    if not rresult:
                                        StrResult += line
                                    else:
                                        StrResult += line
                                        f.seek(0,0)
                                        f.close()
                                        return StrResult

                            else:
                                if f.tell() > 10675521:
                                    # print('没有记录')
                                    f.seek(0,0)
                                    break
                                else:
                                    continue

                    else:
                        #实际F
                        if ci[0].lower() > "f" or ci[0].lower() == 'f':
                            f.seek(6378372,0)
                            ##
                            while True:
                                # print('666666666')
                                line = f.readline().decode()
                                rresult = re.findall('"%s\\r\\n'%ci,line)
                                if rresult:
                                    # print(rresult)
                                    #跳过第一行
                                    line = f.readline().decode()
                                    #初始化一个字符串
                                    StrResult = ''
                                    #检索单词成功后检索单词意义结束位置并返回字符串
                                    while True:
                                        line = f.readline().decode()
                                        line2 = line[::-1]
                                        rresult = re.findall('\\n\\r;;"',line2)
                                        if not rresult:
                                            StrResult += line
                                        else:
                                            StrResult += line
                                            f.seek(0,0)
                                            f.close()
                                            return StrResult

                                else:
                                    if f.tell() > 8904612:
                                        # print('没有记录')
                                        f.seek(0,0)
                                        break
                                    else:
                                        continue
                        else:
                            #实际C
                            if ci[0].lower() > "c" or ci[0].lower() == "c":
                                f.seek(2469170,0)
                                ##
                                while True:
                                    # print('77777777')
                                    line = f.readline().decode()
                                    rresult = re.findall('"%s\\r\\n'%ci,line)
                                    if rresult:
                                        # print(rresult)
                                        #跳过第一行
                                        line = f.readline().decode()
                                        #初始化一个字符串
                                        StrResult = ''
                                        #检索单词成功后检索单词意义结束位置并返回字符串
                                        while True:
                                            line = f.readline().decode()
                                            line2 = line[::-1]
                                            rresult = re.findall('\\n\\r;;"',line2)
                                            if not rresult:
                                                StrResult += line
                                            else:
                                                StrResult += line
                                                f.seek(0,0)
                                                f.close()
                                                return StrResult

                                    else:
                                        if f.tell() > 6378372:
                                            # print('没有记录')
                                            f.seek(0,0)
                                            break
                                        else:
                                            continue
                            else:
                                f.seek(0,0)
                                ##
                                while True:
                                    # print('88888888')
                                    line = f.readline().decode()
                                    rresult = re.findall('"%s\\r\\n'%ci,line)
                                    if rresult:
                                        # print(rresult)
                                        #跳过第一行
                                        line = f.readline().decode()
                                        #初始化一个字符串
                                        StrResult = ''
                                        #检索单词成功后检索单词意义结束位置并返回字符串
                                        while True:
                                            line = f.readline().decode()
                                            line2 = line[::-1]
                                            rresult = re.findall('\\n\\r;;"',line2)
                                            if not rresult:
                                                StrResult += line
                                            else:
                                                StrResult += line
                                                f.seek(0,0)
                                                f.close()
                                                return StrResult

                                    else:
                                        if f.tell() > 2469170:
                                            # print('没有记录')
                                            f.seek(0,0)
                                            break
                                        else:
                                            continue

    f.close()



