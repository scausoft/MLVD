
import numpy as np
import pandas as pd
from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.utils.timezone import now, localtime
from django.views.decorators.csrf import csrf_exempt
from . import models, forms
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from joblib import dump, load

###读取文件
import os
import hashlib
import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)
    return data

def getALL(bytecode):
    set = []
    file_path_access = 'D:/pyProjects/VulnerabilityDetnSys/web/detectContractModels/set/data/acccessProject.csv'  # 你的CSV文件路径
    csv_data_access = read_csv_file(file_path_access)
    for i in csv_data_access:
        set.append(i)

    file_path_Ari = 'D:/pyProjects/VulnerabilityDetnSys/web/detectContractModels/set/data/arithmeticProject.csv'  # 你的CSV文件路径
    csv_data_Ari = read_csv_file(file_path_Ari)
    for i in csv_data_Ari:
        set.append(i)

    file_path_dos = 'D:/pyProjects/VulnerabilityDetnSys/web/detectContractModels/set/data/dosProject.csv'  # 你的CSV文件路径
    csv_data_dos = read_csv_file(file_path_dos)
    for i in csv_data_dos:
        set.append(i)

    file_path_tod = 'D:/pyProjects/VulnerabilityDetnSys/web/detectContractModels/set/data/frontProject.csv'  # 你的CSV文件路径
    csv_data_tod = read_csv_file(file_path_tod)
    for i in csv_data_tod:
        set.append(i)

    file_path_reen = 'D:/pyProjects/VulnerabilityDetnSys/web/detectContractModels/set/data/reentrancyProject.csv'  # 你的CSV文件路径
    csv_data_reen = read_csv_file(file_path_reen)
    for i in csv_data_reen:
        set.append(i)

    file_path_time = 'D:/pyProjects/VulnerabilityDetnSys/web/detectContractModels/set/data/timeProject.csv'  # 你的CSV文件路径
    csv_data_time = read_csv_file(file_path_time)
    for i in csv_data_time:
        set.append(i)

    file_path_uncheck = 'D:/pyProjects/VulnerabilityDetnSys/web/detectContractModels/set/data/uncheckedProject.csv'  # 你的CSV文件路径
    csv_data_uncheck = read_csv_file(file_path_uncheck)
    for i in csv_data_uncheck:
        set.append(i)

    print(len(set))
    data=''
    for list in set:
        if list[1].__eq__(bytecode):
            data=list[0]
    return data
def execCmd(cmd):
  r = os.popen(cmd)
  text = r.read()
  r.close()
  return text
def pic_list(request):
  return render(request, "pic_list.html")

def Smote_csv_list(request):
  return render(request, "test3000.html")

def loophole_list(request):
  return render(request, "loophole_list.html")

def setPassword(password):
    """
    加密密码，算法单次md5
    :param apssword: 传入的密码
    :return: 加密后的密码
    """
    md5 = hashlib.md5()
    md5.update(password.encode())
    password = md5.hexdigest()
    return str(password)

def register(request):
    if request.method=="POST" and request.POST:
        data=request.POST
        username=data.get("username")
        password=data.get("password")
        models.Users.objects.create(
            username=username,
            password=password,
        )
        return JsonResponse({'isSuccess': 'true'})
        # return render(request, 'register_success.html')
        # return redirect('login')
    return render(request, "register.html")

# 用request方式
def login(request):
    # 如果请求方式是get,就返回本页面，否则（post方式）就获取页面提交的内容
    # 和数据库的用户名/密码做对比，相同就登录，不同就报错
    if request.method == "GET":
        return render(request, 'login.html')
    # user对应html文件<input type="" name="user">输入框，pwd同理
    name = request.POST.get('user')
    print(name)
    pwd = request.POST.get('pwd')
    print(pwd)
    # 从数据库web中的web_userinfo表中取出所有数据
    data_list = models.Users.objects.all()
    print(data_list)
    # 从每条数据中取得name和password字段进行比较
    for data in data_list:
        if data.username == name and data.password == pwd:
            #auth.login(request,user_obj)
            # 登录成功跳转到我主页
            return render(request, 'Smote_list.html')
    # 登录不成功就返回本页面，并给出错误信息
    return render(request, 'login.html', {"error_msg": "用户名或错误"})

def logout(request):
    #auth.logout(request)
    return redirect('login')

def orm(request):
    # 检索出web_admin表中所有数据
    data = models.Users.objects.all()
    # 输出<QuerySet [<Admin: Admin object (1)>, <Admin: Admin object (2)>, <Admin: Admin object (3)>]>
    for Users in data:
        print(Users.username, Users.password)
    return HttpResponse('成功')
def main(request):
    return render(request, 'Smote_list.html')
# 用户管理
def user_list(request):
    # 用orm方式从web_admin表中获取数据
    data_list = models.Users.objects.all()
     # 直接把数据返回到user_list.html中
    return render(request, 'user_list.html', {'data': data_list})

def user_info(request):
    """
       查询结果必须是json格式:{"total": 2,"rows": [{},{}]}
       """
    if request.method == "GET":
        # search_kw = request.GET.get('search_kw', None)
        # 获取分页参数用于查询对应页面数据，page为第几页，size为每页数据条数
        page_num = request.GET.get('page', 1)
        size = request.GET.get('size', 10)

        username = request.GET.get('username')
        password = request.GET.get('password')

        # 查询全部
        if username or password:
            post_list = models.Users.objects.filter(username__icontains=username,
                                                            password__icontains=password)
        else:
            post_list = models.Users.objects.all()
        print("request.user")
        print(request.user)
        # 使用分页器返回查询的页数和size
        paginator = Paginator(post_list, per_page=size)
        page_object = paginator.page(page_num)

        # 总数
        total = post_list.count()
        # 查询list of dict
        rows = [model_to_dict(i) for i in page_object]
        # print(rows)
        return JsonResponse({'total': total, 'rows': rows})
def user_edit(request):
    if request.method == "POST":
       nid = request.POST.get('id')
       print(nid)
       name= request.POST.get('username')
       print(name)
       password = request.POST.get('password')
       print(password)
       models.Users.objects.filter(id=nid).update(username=name, password=password)
       result = 'success'
       print(result)
       return JsonResponse({'result': result})
@csrf_exempt
def user_delete(request):
    if request.method == "POST":
        ids = request.body
        list=str(ids).split(':')
        str1=list[1].lstrip('"')
        str2=str1.strip('}\'')
        str3 = str2.strip('"')
        idTure=int(str3)
        models.Users.objects.filter(id=idTure).delete()
        result='success'
    return JsonResponse({'result':result})

def page(deploy_list, limit, offset):  # 查询分页，调用此方法需要传获取的数据列表，页面大小，页码
    # 取出该表所有数据
    try:
        paginator = Paginator(deploy_list, limit)  # 每页显示10条数据
    except Exception:
        print ("error")
    page = int(int(offset) / int(limit) + 1)
    data = paginator.page(page)
    response_data = {'total': deploy_list.count(),
                     'rows': []}  # 必须带有rows和total这2个key，total表示总页数，rows表示每行的内容，这两个是Bootstrap需要的
    return {"data": data, "response_data": response_data}

# Smote
def Smote_list(request):
    # 用orm方式从web_admin表中获取数据
    #data_list = models.SmartContract.objects.all().values().order_by('create_time')
    data_list = models.Smote.objects.all().order_by('-create_time')
    print('data_list')
    print(data_list[0])
    #i=0
    #while i < len(data_list):
        #print(data_list[i].create_time.strftime("%Y-%m-%d %H:%M:%S"))
        #i=i+1
    # 直接把数据返回到user_list.html中
    return render(request, 'Smote_list.html', {'data': data_list})
def Smote_info(request):
    """
    查询结果必须是json格式:{"total": 2,"rows": [{},{}]}
    """
    if request.method == "GET":
        # search_kw = request.GET.get('search_kw', None)
        # 获取分页参数用于查询对应页面数据，page为第几页，size为每页数据条数
        page_num = request.GET.get('page',  1)
        size = request.GET.get('size', 10)

        # contractType = request.GET.get('contractType')
        contractName = request.GET.get('contractName')

        # 查询全部
        if contractName:
            post_list = models.Smote.objects.filter(contractName__icontains=contractName)
        else:
            post_list = models.Smote.objects.all().order_by('-create_time')
        # 使用分页器返回查询的页数和size
        paginator = Paginator(post_list, per_page=size)
        page_object = paginator.page(page_num)

        # 总数
        total = post_list.count()
        # 查询list of dict
        rows = [model_to_dict(i) for i in page_object]
        # print(rows)
        return JsonResponse({'total': total, 'rows': rows})
#lightGBMSmoteNN
def Smote_save(request):
    if request.method == "POST":
        bytecode = request.POST.get('byteCodes')
        #
        x_pred=getALL(bytecode)
        print(x_pred)
        x_pred=x_pred.split(',')
        csvfile = open("D:/pyProjects/VulnerabilityDetnSys/web/vecText.csv", 'w', encoding="utf-8")
        writer = csv.writer(csvfile)
        newrow = []
        for i in x_pred:  # 逐个追加数组内容
            newrow.append(i)
        writer.writerow(newrow)
        csvfile.close()

        data = pd.read_csv('D:/pyProjects/VulnerabilityDetnSys/web/vecText.csv', header=None)
        x_pred = np.array(data.head(1))
        print(x_pred)

        clf = load('D:/pyProjects/VulnerabilityDetnSys/web/detectContractModels/model/lightGBM.joblib')
        y_pred = [round(value) for value in clf.predict(x_pred)]
        lType = y_pred[0]
        print("lType")
        print(lType)
        # RF加载模型
        clf = load('D:/pyProjects/VulnerabilityDetnSys/web/detectContractModels/model/rf.joblib')
        y_pred = [round(value) for value in clf.predict(x_pred)]
        rType = y_pred[0]
        print("rType")
        print(rType)
        #XGBoost加载模型
        clf = load('D:/pyProjects/VulnerabilityDetnSys/web/detectContractModels/model/xgboost.joblib')
        y_pred = [round(value) for value in clf.predict(x_pred)]
        xType = y_pred[0]
        print("xType")
        print(xType)
        # AdaBoost加载模型
        clf = load('D:/pyProjects/VulnerabilityDetnSys/web/detectContractModels/model/adaboost.joblib')
        y_pred = [round(value) for value in clf.predict(x_pred)]
        aType = y_pred[0]
        print("aType")
        print(aType)
        # SVM加载模型
        clf = load('D:/pyProjects/VulnerabilityDetnSys/web/detectContractModels/model/svm.joblib')
        y_pred = [round(value) for value in clf.predict(x_pred)]
        create_time = now().strftime("%Y-%m-%d %H:%M:%S")
        create_time = str(create_time).strip('.000000')
        sType = y_pred[0]
        print("sType")
        print(sType)
        models.Smote.objects.create(byteCodes=bytecode, lType=lType,rType=rType,xType=xType,aType=aType,sType=sType,create_time =create_time)
        result='success'
    return JsonResponse({'result':result})
@csrf_exempt
def Smote_delete(request):
    if request.method == "POST":
        ids = request.body
        list=str(ids).split(':')
        str1=list[1].lstrip('"')
        str2=str1.strip('}\'')
        str3 = str2.strip('"')
        idTure=int(str3)
        models.Smote.objects.filter(id=idTure).delete()
        result='success'
    return JsonResponse({'result':result})



# python manage.py runserver 127.0.0.1:8000
#http://localhost:8000/
#create user 'root'@'localhost' identified by '123456';
#grant all on *.* to 'root'@'localhost';
#grant all privileges on djangoProject.* to 'root'@'localhost';
#python manage.py makemigrations
#python manage.py migrate

