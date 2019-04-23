#???
#BrokenSword_version_V1
#------------------------------------
#导入资源文件路径生成模块
from resource import resource_path
# 导入pygame模块
import pygame
from pygame.locals import *
#导入精灵类
from MYMySprite import MySprite
import sys, time, os, random, threading

class BrokenSword():
    def __init__(self,is_full):
        self.is_full = is_full
        self.backgroundmusic = [resource_path(os.path.join("music","beihanshatan.ogg")),\
        resource_path(os.path.join("music","biyougong.ogg")),\
        resource_path(os.path.join("music","guandaonanbei.ogg")),\
        resource_path(os.path.join("music","lanxianzheng.ogg")),\
        resource_path(os.path.join("music","lanxianzhengwai.ogg")),\
        resource_path(os.path.join("music","penglaidao.ogg")),\
        resource_path(os.path.join("music","qianyuanshan.ogg")),\
        resource_path(os.path.join("music","tianyongcheng.ogg")),\
        resource_path(os.path.join("music","wulongshan.ogg")),\
        resource_path(os.path.join("music","zhongnanshan.ogg"))]
        self.warmusic = [resource_path(os.path.join("music","war1.ogg")),\
        resource_path(os.path.join("music","war2.ogg")),\
        resource_path(os.path.join("music","war3.ogg"))]

        pygame.init()
        #设置全屏FULLSCREEN
        self.screen = pygame.display.set_mode((800,600),self.is_full,32)
        #游戏图标(来源于网络,data2敌法师)
        ICO = pygame.image.load("%s"%resource_path(os.path.join("ImageTxtSource","ICO.png"))).convert_alpha()
        pygame.display.set_icon(ICO)
        #鼠标指针图标
        self.mousee = pygame.image.load("%s"%resource_path(os.path.join("ImageTxtSource","mousee.png"))).convert_alpha()
        self.width, self.height = self.mousee.get_size()
        self.mousee = pygame.transform.smoothscale(self.mousee, (self.width//6, self.height//6))
        #隐藏鼠标
        pygame.mouse.set_visible(False)

        #跑酷游戏是否结束的变量
        self.game = True
        #跑酷游戏内角色是否'移动'的判断的变量
        self.role2_movee = False
        #用于记录跑酷游戏内键盘输入的字符的asscii码值
        self.value = None
        #跑酷计时初始值
        self.timee = 1
        #定义一种字体,显示退出提示
        Myfont_3 = pygame.font.SysFont("arial", 20)
        self.ESCimage = Myfont_3.render("ESC to exit",True, (234,32,0))
        while True:
            #随机加载一个背景音乐
            MusicRandomResult = random.choice(range(0,10))
            #淡出播放时间
            pygame.mixer.music.fadeout(1000)
            #加载音乐
            pygame.mixer.music.load(self.backgroundmusic[MusicRandomResult])
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(10)

            #调用主界面
            self.Main_interfa()

            #初始化变量self.game,循环外变量在游戏过程中实时会被改变，不放进循环
            #游戏主进程退出到主界面前会将设为False，再次进入游戏前将其设为True
            self.game = True
            #初始化游戏时间
            self.timee = 1

            #随机加载一个背景音乐
            MusicRandomResult = random.choice(range(0,3))
            pygame.mixer.music.load(self.warmusic[MusicRandomResult])
            #淡出播放时间
            pygame.mixer.music.fadeout(1000)
            #加载音乐
            pygame.mixer.music.load(self.warmusic[MusicRandomResult])
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(10)

            #调用跑酷游戏
            self.gamestart()

# ------------------------      主界面      --------------------------------------

    def  Main_interfa(self):
        pygame.init()

        #背景图片
        background = pygame.image.load('%s'%resource_path(os.path.join("ImageTxtSource","map_1.png"))).convert_alpha()
        pygame.display.set_caption("破碎之剑")
        font = pygame.font.SysFont("arial", 18)

        #定义一个时钟实例
        framerate = pygame.time.Clock()

        #创建精灵实例
        #角色
        role = MySprite(self.screen)
        role.load("%s"%resource_path(os.path.join("ImageTxtSource","ROLE_.png")), 130, 140, 8)
        chicken = MySprite(self.screen)
        chicken.load("%s"%resource_path(os.path.join("ImageTxtSource","ji006.png")), 50, 47, 15)
        fire = MySprite(self.screen)
        fire.load("%s"%resource_path(os.path.join("ImageTxtSource","fire001.png")), 30, 100, 8)
        fire2 = MySprite(self.screen)
        fire2.load("%s"%resource_path(os.path.join("ImageTxtSource","fire001.png")), 30, 100, 8)
        sword = MySprite(self.screen)
        sword.load("%s"%resource_path(os.path.join("ImageTxtSource","sword.png")), 24, 100, 9)
        boss0 = MySprite(self.screen)
        boss0.load("%s"%resource_path(os.path.join("ImageTxtSource","BosStand.png")), 196, 190, 4)

        #选帧
        fire2.first_frame = 2  #从位图第几张开始，起始索引为0
        fire2.last_frame = 4    #位图第几张位图结束
        fire.first_frame = 2
        fire.last_frame = 4

        #设置位置
        chicken.position = 650, 452
        fire.position = 360, 315
        fire2.position = 263, 290
        role.position = 0, 335
        sword.position = 410, 190
        boss0.position = 525, 0

        #创建精灵组
        group = pygame.sprite.Group()
        group1 = pygame.sprite.Group()
        group2 = pygame.sprite.Group()

        # 将精灵加入组
        group1.add(chicken)
        group1.add(fire)
        group1.add(fire2)
        group1.add(sword)
        group2.add(boss0)
        group.add(role)

        #局部变量判断
        Main_interface  = True
        role_moving = False
        player_health = 0

        #第一次运行如果没有鼠标事件，则初始一个参数给下面
        mouse_x,mouse_y = 400, 320

        #-------------      开始游戏主界面循环(方向只有上下左右)        ------------------------

        while True:
            framerate.tick(15)
            ticks = pygame.time.get_ticks()

            #接收键盘事件
            for event in pygame.event.get():

                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    sys.exit()
                #上下左右
                elif keys[K_UP] or keys[K_w]:
                    role.direction = 1
                elif keys[K_RIGHT] or keys[K_d]:
                    role.direction = 6
                elif keys[K_DOWN] or keys[K_s]:
                    role.direction = 8
                elif keys[K_LEFT] or keys[K_a]:
                    role.direction = 5

                else:
                    #玩家静止
                    role.direction = 0

                # 接收鼠标当前悬浮位置
                if event.type == MOUSEMOTION:
                    mouse_x,mouse_y = event.pos

            #键盘输入esc退出
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                exit()

            #--------------       主界面存活      -------------------------

            if Main_interface :

                #角色的状态帧的起点终点取决于方向direction
                role.first_frame = role.direction * role.columns
                role.last_frame = role.first_frame + role.columns-1
                #???
                if role.frame < role.first_frame:
                    role.frame = role.first_frame

             
                #算出移动距离, 实施移动玩家坐标, 移动距离和 方向 和 速度(速度定义为V, 单位帧移动像素距离) 有关
                V = 7
                if role.direction == 1:
                    role.Y += -V 
                elif role.direction == 5:
                    role.X += -V
                elif role.direction == 6:
                    role.X += V
                elif role.direction == 8:
                    role.Y += V

                # (地图边界)(移动后的X和Y坐标如果大于地图边界，设置保持原来位置)
                if (role.X > 394 and role.Y < 335) or \
                (role.X < 394 and role.Y < 264) or \
                (role.X > 394 and role.Y >335) or \
                (role.X < 0) or\
                (role.Y > 500):
                    if role.direction == 1:
                        role.Y += V
                    elif role.direction == 5:
                        role.X += V
                    elif role.direction == 6:
                        role.X += -V
                    elif role.direction == 8:
                        role.Y += -V

                # (守护者区域)(进入圣剑守护神区域)
                if role.X> 230 and role.X < 394 and role.Y < 266:
                    Main_interface = False
                #更新玩家精灵组
                #???
                group.update(ticks, 50)

            #------------         主界面死亡      ---------------------

            else:
                #结束当前循环，进入下一个循环
                break

            #将地图画在屏幕上
            self.screen.blit(background,(0,0))
            #设置更新帧率
            group.update(ticks)
            group1.update(ticks, 90)
            group2.update(ticks, 120)
            #将精灵画在屏幕上
            group1.draw(self.screen)
            group2.draw(self.screen)
            group.draw(self.screen)
            #将退出提示画在屏幕右上角
            self.screen.blit(self.ESCimage,(710,0))
            #将鼠标图片画在屏幕上,参数是试的
            self.screen.blit(self.mousee,(mouse_x-self.width//2/5,mouse_y-self.height//2/5))
            pygame.display.update()



# --------------------------      跑酷游戏函数    -----------------------------

    def gamestart(self):
        pygame.init()

        #清屏
        self.screen.fill((50,50,100))

        #---------------------------     线程函数    ------------------------------------

        #进程函数
        def ggame(self):
            pygame.init()
            #定变量判断该退出游戏
            game = True

            bg1 = pygame.image.load("%s"%resource_path(os.path.join("ImageTxtSource","map_2.png")))
            bg2 = pygame.image.load("%s"%resource_path(os.path.join("ImageTxtSource","map_21.png")))

            #地图图片的x轴起始点
            pos_x = 0

            #创建一个时钟实例
            framerate = pygame.time.Clock()

            #创建精灵实例
            #猪脚
            role2 = MySprite(self.screen)
            role2.load("%s"%resource_path(os.path.join("ImageTxtSource","ROLE_2.png")), 100, 140, 8)
            role2_dead = MySprite(self.screen)
            role2_dead.load('%s'%resource_path(os.path.join("ImageTxtSource","roleDeaD.png")), 130 , 130, 8)
            #boss
            boss = MySprite(self.screen)
            boss.load("%s"%resource_path(os.path.join("ImageTxtSource","BossRunR.png")), 230, 440, 6)
            boss_dead = MySprite(self.screen)
            boss_dead.load("%s"%resource_path(os.path.join("ImageTxtSource","BossDisappear.png")), 300, 300, 5)
            #小箭头
            tipp = MySprite(self.screen)
            tipp.load("%s"%resource_path(os.path.join("ImageTxtSource","tipp.png")), 70, 100, 12)

            #设置图片帧
            role2.first_frame = 0
            role2.last_frame = 7

            #设置位置
            role2.position = 400, 350
            boss.position = 10, 110
            tipp.position = 115, 470


            #创建精灵组
            group2man = pygame.sprite.Group()
            group2boss = pygame.sprite.Group()
            group2tipp = pygame.sprite.Group()

            # 将精灵加入组(加组顺序注意)
            group2man.add(role2)
            group2boss.add(boss)
            group2tipp.add(tipp)

            #打开英文文本
            f = open('%s'%resource_path(os.path.join("ImageTxtSource","Englishtext.txt")),'rb')

            #打印屏幕的字符串切片索引初始值
            idex = 0

            #初次加载屏幕上的字符串文字，前面加个w
            strTEXT = 'wwe always knew our daughter kendall was going be a performer'

            #  ----------------------    开始跑酷游戏循环    ----------------------------

            while True:
                framerate.tick(60)
                ticks = pygame.time.get_ticks()

                #读取英文文本
                strr = f.readline()
                strr = strr.decode()
                start = len(strr)

                #降低难度减少了很多条件，下面有些判断没有意义
                #判断键盘输入asscii码值和字符串第n个字符码值是否相等
                if self.value == ord(strr[idex]):
                    self.role2_movee = True
                    # 如果当前字符串长度等于1，意味着这是字符串最后一个字符
                    if len(strr[idex::]) == 1:
                        strTEXT = strr[idex:idex+40]
                        #再次循环会获取下一行字符串
                    else:
                        #切出字符串重新赋值给要显示在屏幕上的字符串
                        strTEXT = strr[idex:idex+40]
                        idex += 1
                        #保持角色位置
                        f.seek(-start, 1)
                #匹配错误，回到开头位置再读字符串
                else:
                    f.seek(-start, 1)

                #显示文本
                #创建字体
                Myfont = pygame.font.SysFont("arial", 40)
                Myfont_2 = pygame.font.SysFont("arial", 26)
                #英文句子文本
                textimagee = Myfont.render(strTEXT[1::], True, (207,95,192))
                #得分文本
                LastScore_scoreeimagee_timeeimagee = Myfont_2.render("SECONDS:  "+str(self.timee), True, (1,136,251))

                # -----------------------------------------------------------------------

                #将地图画在屏幕上
                if pos_x >= -4800:
                    self.screen.blit(bg1,(pos_x,0))
                    pos_x += -4
                else:
                    self.screen.blit(bg1,(pos_x,0))
                    self.screen.blit(bg2,(pos_x+4800, 0))
                    pos_x += -4
                    if pos_x == -9600:
                        pos_x = 0

                # -------------------------         角色移动        ------------------------

                #如果角色判断移动的变量为False,减X坐标
                if not self.role2_movee:
                    role2.X += -0.5
                else:
                    #如果变量为True，角色x坐标加上n像素
                    role2.X += 10
                    #移动完重新给判断角色移动变量赋予False
                    self.role2_movee = False

                # ----------------------------     游戏结束   -------------------------------------------

                #冲突检测
                collide_list = pygame.sprite.spritecollideany(role2, group2boss)
                #如果冲突
                if collide_list:
                    #是跑酷游戏存活变量设为 False,同时主线程收到此信号
                    self.game = False
                    #将死亡角色设置为未死亡角色位置
                    role2_dead.position = role2.X, role2.Y
                    #替代角色动画帧
                    group2man.add(role2_dead)
                    group2man.remove(role2)
                    group2boss.remove(boss)
                    group2boss.add(boss_dead)
                    boss_dead.position = 10, 110

                    #--------------     角色冲突不立即退出,刷新完死亡动画      -------------------

                    #如果角色死亡角色帧在最后一帧
                    if role2_dead.frame == role2_dead.last_frame:
                        self.screen.fill((50, 50, 100))
                        winimage = Myfont.render("Defeat !", True, (234,32,0))
                        qqq = 0
                        #刷新显示分数n 遍再退出线程
                        while qqq < 6:
                            self.screen.blit(winimage, (340, 250))
                            #将退出提示画在屏幕右上角
                            self.screen.blit(self.ESCimage,(710,0))
                            pygame.display.update()
                            qqq += 1
                            time.sleep(0.1)
                        self.game = True
                        self.value = None
                        self.role2_movee = False
                        break
                    #如果boss死亡角色帧在最后一帧
                    if boss_dead.frame == boss_dead.last_frame:
                        self.screen.fill((50, 50, 100))
                        winimage = Myfont.render("Defeat !", True, (234,32,0))
                        qqq = 0
                        #刷新显示分数n 遍再退出线程
                        while qqq < 6:
                            self.screen.blit(winimage, (340, 250))
                            #将退出提示画在屏幕右上角
                            self.screen.blit(self.ESCimage,(710,0))
                            pygame.display.update()
                            qqq += 1
                            time.sleep(0.1)
                        self.game = True
                        self.value = None
                        self.role2_movee = False
                        break
                    #否则继续循环直到满足上述条件一种
                

                #如果角色达到右边界
                if role2.X > 800:
                    #是跑酷游戏存活变量设为 False,同时主线程收到此信号
                    self.game = False
                    self.screen.fill((50, 50, 100))
                    winimage = Myfont.render("Victory ! SECONDS: %s"%(str(self.timee)), True, (255, 255, 255))
                    qqq = 0
                    while qqq < 5:
                        self.screen.blit(winimage, (250, 250))
                        #将退出提示画在屏幕右上角
                        self.screen.blit(self.ESCimage,(710,0))
                        pygame.display.update()
                        qqq += 1
                        time.sleep(0.1)
                    self.game = True
                    self.value = None
                    self.role2_movee = False
                    break
 

                # ------------------------    屏幕显示       ---------------------------------------

                #将英文句子显示在屏幕
                self.screen.blit(textimagee, (150, 550))
                #将得分显示在屏幕
                self.screen.blit(LastScore_scoreeimagee_timeeimagee, (330, 0))

                #设置更新帧率
                group2man.update(ticks,70)
                group2boss.update(ticks,160)
                group2tipp.update(ticks,140)
                #将精灵显示在屏幕
                group2man.draw(self.screen)
                group2boss.draw(self.screen)
                group2tipp.draw(self.screen)
                #将退出提示画在屏幕右上角
                self.screen.blit(self.ESCimage,(710,0))

                pygame.display.update()


        # -----------------------       计时线程函数        ----------------------------------
        def tim(self):
            while True:
                time.sleep(1)
                self.timee += 1
                if self.game == False:
                    break
        #创建线程并调用
        KKEY = threading.Thread(target = ggame, args=(self,))
        TTIME = threading.Thread(target = tim, args=(self,))
        #主线程退出，子线程也退出
        KKEY.daemon = True
        TTIME.daemon = True
        KKEY.start()
        TTIME.start()


#  -------------------------       游戏主进程(监听键盘)       ----------------------------

        #主进程监听事件，因为线程中监听不了键盘事件
        while True:
            if self.game == False:
                time.sleep(1)
                self.game = True
                self.role2_movee = False
                self.value = None
                break
            # 获得事件输入
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #主进程直接完全退出
                    sys.exit()

                #键盘按下事件
                if event.type == pygame.KEYDOWN:
                    for ii in range(65,91):
                        if event.key == ii:
                            self.value = ii
                    for mm in range(97,123):
                        if event.key == mm:
                            self.value = mm
                    if event.key == 32:
                        self.value = 32
                            #键盘输入esc退出
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                sys.exit()
