attack_vals = {
    '京巴':30,
    '藏獒':80
}


def dog(name,d_type):
    data = {
        'name':name,
        'd_type':d_type,
        'life_val':100
    }
    if d_type in attack_vals:
        data['attack_val']=attack_vals[d_type]
    else:
        data['attack_val'] = 15

    return data

def person(name,age):
    data = {
        'name':name,
        'age':age,
        'life_val':100
    }
    if age>18:
        data['attack_val'] = 50
    else:
        data['attack_val'] = 30

    return data

def dog_bite(dog_obj,person_obj): #要知道咬了谁 谁咬的 把对象传进来
    person_obj['life_val'] -= dog_obj['attack_val']
    print('dog[%s]bites person[%s],lose blood[%s],blood lefts[%s]'%(dog_obj['name'],
                                                                    person_obj['name'],
                                                                    dog_obj['attack_val'],
                                                                    person_obj['life_val']))
#每个obj就是你创建的函数实例 而每个实例又是一个字典 所以想知道一个属性值 调用字典key

def beat(person_obj,dog_obj):
    dog_obj['life_val'] -= person_obj['attack_val']
    print('person[%s]beats dog[%s],lose blood[%s],blood lefts[%s]'%(person_obj['name'],
                                                                    dog_obj['name'],
                                                                    person_obj['attack_val'],
                                                                    dog_obj['life_val']
                                                                    ))

p1 = person('john',30)
d1 = dog('ll','京巴')
dog_bite(d1,p1)
beat(p1,d1)

print(d1,p1)
