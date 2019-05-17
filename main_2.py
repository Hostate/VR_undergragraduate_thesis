import viz
import vizact
import viztask
import vizshape
import enviroment as en
import os
import copy
import vizconnect

location = os.path.dirname(os.path.abspath("__file__"))
gouzi = en.add_gouzi()
qizhongji = en.add_qizhongji()
viz.go()
vizconnect.go('only_ori_19422.py')
car_top = en.add_car()
mat = en.add_matou()
mylight = viz.addLight()
mylight.position(0,1,0,0)
viz.phys.enable()
viz.setMultiSample(1000)

global left
global right
#view = viz.MainView
global flag_touch
global trail
trail = 0
flag_touch = 0
global flag_co

#view.setPosition([13, 3.5, 121])
#view.setEuler([-180, 0, 0])



def getpos():
    print viz.MainView.getPosition()
    print viz.MainView.getEuler()
    viz.MainView.setEuler(180,0,0)

vizact.onkeydown('p',getpos)

left = []
right = []
male_3 = []
male_1 = []

male_3.append(en.add_male(0, 180, 4))
male_3.append(en.add_male(4, 0, 14))
male_3.append(en.add_male(3, 270, 0))
male_3.append(en.add_male(2, 270, 0))
male_1.append(en.add_male(1, 0, 1))
shabi= male_3[0]
oneman = male_1[0]
def right_3():
    global left
    global right
    male_3[0].setPosition([9.6, 1.15+0.88, 111])
    male_3[1].setPosition([10.6, 1.15, 110.5])
    male_3[2].setPosition([10.6, 1.15,111.5])
    male_3[3].setPosition([11.6, 1.15, 111])
    male_3[2].setEuler([0, 0, 0])
    male_3[1].setEuler([0, 0, 0])
    male_3[0].setEuler([270, 0, 0])
    male_3[3].setEuler([270, 0, 0])
#    male_3[0].state(4)
    male_3[1].state(14)
    male_3[3].state(4)
    right = copy.copy(male_3)
    for i in male_3:
        i.visible(viz.ON)

def left_3():
    global left
    global right
    male_3[0].setPosition([14.8, 1.15 +0.88, 111])
    male_3[1].setPosition([15.8, 1.15, 110.5])
    male_3[2].setPosition([15.8, 1.15, 111.5])
    male_3[3].setPosition([16.8, 1.15, 111])
    male_3[2].setEuler([0, 0, 0])
    male_3[1].setEuler([0, 0, 0])
    male_3[0].setEuler([270, 0, 0])
    male_3[3].setEuler([270, 0, 0])
    male_3[3].state(4)
    male_3[1].state(14)
#    male_3[2].state(9)
    left = copy.copy(male_3)
    for i in male_3:
        i.visible(viz.ON)

def right_1():
    global left
    global right    
    male_1[0].setPosition([10.6, 1.15, 111])
    male_1[0].visible(viz.ON)
    male_1[0].state(14)
    male_1[0].setEuler([0, 0, 0])
    right = copy.copy(male_1)
    
def left_1():
    global left
    global right
    male_1[0].setPosition([15.8,1.15,111])
    male_1[0].visible(viz.ON)
    male_1[0].setEuler([0, 0, 0])
    male_1[0].state(14)
    left = copy.copy(male_1)
#    print left
def st_1():
    left_3()
    right_1()
    return 1
    
def st_2():
    left_1()
    right_3()
    return 2

def st_3():
    return 3
    
def st_4():
    right_1()
    return 4

def tri(i):
    if i == 1:
        x = st_1()
    elif i == 2:
        x = st_2()
    elif i == 3:
        x = st_3()
    elif i == 4:
        x = st_4()
    return x
    
global lis
#lis = [3,3,3,1,2, 4, 1, 3, 2,2]
lis = [3]
global car_fall
car_fall = 0
def onJdown(key):
    
    global t2 
    global t1
    global car_fall
    global keyx
    
    if (key == "j" and (keyx != 1) and (car_fall == 0)):
        car_top.clearActions()
        gouzi.clearActions()
        qizhongji.clearActions()
        vizact.ontimer2(3.5, 0, qizhongji.addAction, vizact.moveTo([13.2, 1.15, 111], speed = 4.8))
        car_top.addAction(en.car_change)
        car_top.addAction(en.car_to_front_2)
        car_top.addAction(en.car_fall)
        car_fall = 1
        gouzi.addAction(en.gouzi_change)
        gouzi.addAction(en.gouzi_front_2)

        keyx = 1
        t2 = viz.tick()
#        print "jt2 = ", t2
#        print "jt1 = ", t1
#        print "key = ", keyx
def press_f():
    car_top.addAction(en.car_to_front_1)
    car_top.addAction(en.car_fall)
    gouzi.addAction(en.gouzi_front)
    qizhongji.addAction(en.qizhongji_front)
    global t1
    t1 = viz.tick()
    global keyx
    keyx = 0
    viz.callback(viz.KEYDOWN_EVENT, onJdown)
    
def onFdown(key):
    global flag_touch
    global car_fall
    global trail
    if (key == "f" and flag_touch == 0 and trail == 0):
        press_f()

def oncollideman(e):
#    e.obj1.state(8)
    
    global flag_co
    if (e.obj1 != shabi):
        e.obj1.addAction(vizact.spinTo(euler = [0,270,0], time = 0.04))
        if(e.obj1 == oneman):
            viz.playSound('\\fe_dead.wav')
    elif(flag_co == 0):
        print e.obj1
        viz.playSound('\\fe_dead.wav')
        viz.playSound('\\m_dead.wav')
        flag_co = 1
        e.obj1.addAction(vizact.spin(-0.77, 0, 0, 90/0.04, 0.04))


global stjj
trail = 0
trail_datas = []

def onUpdate(e): 
    global flag_touch
    global left
    global right
    global st
    global trail
    global keyx
    global car_fall
    if (car_top.getPosition()[1] < 6.65):
        car_fall = 1
    else:
        car_fall = 0
    if (car_top.getPosition()[1] <= 1.15):
        if(flag_touch == 0):
            flag_touch += 1
            viz.playSound('\crash.wav')
        elif(flag_touch == 1):
            if(keyx == 0):
                trail_data = [str(st), 'f']
            else:
                trail_data = [str(st), 'j', str(t2 - t1), str(t1), str(t2)]
#            print trail_data
            info = ''
            for xx in trail_data:
                info += str(xx)
                info += ','
            info = info[:-1]
            info += '\n'
            print info
            with open('expdata.csv', 'a') as f:
                f.write(info)
                
            trail_datas.append(trail_data)
#            viz.clearcolor(viz.BLACK)
#            viz.waitTime(3)
            flag_touch += 1
        elif(flag_touch == 90):
            car_top.visible(viz.OFF)
            qizhongji.visible(viz.OFF)
            gouzi.visible(viz.OFF)
            for i in left:
                i.visible(viz.OFF)
            for i in right:
                i.visible(viz.OFF)
            flag_touch += 1
        elif(flag_touch == 180):
#            viz.clearcolor(viz.BLACK)
#            viz.waitTime(3)
            car_top.setPosition([12.85-2.25, 6.65, 87])
            car_top.visible(viz.ON)
            qizhongji.visible(viz.ON)
            gouzi.visible(viz.ON)
            qizhongji.setPosition([13.2, 1.15, 87.8])
            gouzi.setPosition([13.2-2.25, 5.2, 87.8])
#            viz.callback(viz.KEYDOWN_EVENT, onFdown)
            flag_touch = 0
            trail += 1
            if (trail < len(lis)):
                st = tri(lis[trail])
                press_f()
#                viz.callback(viz.KEYDOWN_EVENT, onFdown)
                global flag_co
                flag_co = 0
            else:
                print trail_datas
                
                viz.quit()
        else:
            flag_touch += 1
viz.callback(viz.KEYDOWN_EVENT, onFdown)
viz.callback(viz.COLLIDE_BEGIN_EVENT, oncollideman)
viz.callback(viz.UPDATE_EVENT,onUpdate)

st = tri(lis[trail])
flag_co = 0