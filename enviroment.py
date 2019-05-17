import viz
import vizact
import viztask
import vizshape
def add_en():
    sky = viz.addChild('resources\\sky_day2.osgb')
def add_matou():
    sky = viz.addChild('resources\\sky_day2.osgb')
    sky.setPosition([13, 1.63, 88])
    matou1 = viz.addChild('\\dimian-3.FBX')
    matou2 = viz.addChild('\\jzx_l3.osgb')

    return matou1
def add_qizhongji():
    qizhong = viz.addChild('\\qizhongji_l.osgb')
    
    qizhong.setScale([0.1, 0.15, 0.1])
    
    qizhong.setPosition([13.2, 1.15, 87.8])
    
    return qizhong
def add_gouzi():
    gouzi = viz.addChild('\\gouzi.fbx')
    gouzi.setScale([0.1, 0.1, 0.1])
    gouzi.setPosition([13.2-2.25, 5.2, 87.8])
    return gouzi
def add_male(sex, look,action):
    if (sex == 0):
        human = viz.addChild('resources\\female_2\\Scan-17.OBJ')
        human.setCenter([0, -(1.77/2), 0])
    elif (sex == 1):
        human = viz.addChild('resources\\vcc_female.cfg')
    elif (sex == 3):
        human = viz.addChild('resources\\female_1\\Scan-1.OBJ')
    elif (sex == 2):
        human = viz.addChild('resources\\vcc_male2.cfg')
    elif (sex == 4):
        human = viz.addChild('resources\\vcc_male.cfg')
#    human.setPosition([x, y, z])
    human.setEuler([look,0,0])
#    human.state(action)
    human.collideMesh()
    human.visible(viz.OFF)
    human.enable(viz.COLLIDE_NOTIFY)
    return human
    
def add_car():
    car_top = viz.addChild('mini.osgx')
    car_top.setPosition([12.85-2.25, 6.65, 87])
    car_top.setEuler([90, 0 ,0])
    car_top.collideMesh()
    return car_top

car_to_front_1 = vizact.moveTo([12.85-2.25, 6.65, 111], speed = 4.8)
car_to_front_2 = vizact.moveTo([12.85+-2.25+5.2, 6.65, 111], speed = 4.8)

qizhongji_front = vizact.moveTo([13.2, 1.15, 111], speed = 4.8)
gouzi_front = vizact.moveTo([13.2-2.25, 5.2, 111], speed = 4.8)
gouzi_change = vizact.move(5.2/3.5, 0, 0, 3.5)
gouzi_front_2 = vizact.moveTo([15.8,5.2,111], speed = 4.8)
car_fall = vizact.fall(1.15)

car_change = vizact.move(0, 0,5.2/3.5,3.5)
