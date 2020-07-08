#coding:utf-8
import torch
import torch.nn.functional as F
from torch.autograd import Variable
import matplotlib.pyplot as plt

# #fake data
# x=torch.linspace(-5,5,200)#从-5到5中取两百个点 此时是tensor类型
# x=Variable(x)
# x_np=x.data.numpy()
#
# #制作激励函数
# y_relu=torch.relu(x).data.numpy()#这些函数是系统自带的 库。函数关系。数据类型
# y_sigmoid=torch.sigmoid(x).data.numpy()
# y_tanh=torch.tanh(x).data.numpy()
# y_softplus=F.softplus(x).data.numpy()
#
# #画图部分
# plt.figure(1,figsize=(8,6))#一般要显示多图形是会调用，第一个参数表示编号，第二个表示图表的长宽
# plt.subplot(221)#子绘图区域
# plt.plot(x_np,y_relu,c='red',label='relu')#设定x y 轴的数据，图形颜色，标题
# plt.ylim((-1,5))#设置y参数范围
# plt.legend(loc='best')#绘制多条曲线，加个线型注释
#
# plt.subplot(222)#子绘图区域
# plt.plot(x_np,y_sigmoid,c='red',label='sigmoid')#设定x y 轴的数据，图形颜色，标题
# plt.ylim((-0.2,1.2))#设置y参数范围
# plt.legend(loc='best')#绘制多条曲线，加个线型注释
#
# plt.subplot(223)#子绘图区域
# plt.plot(x_np,y_tanh,c='red',label='tanh')#设定x y 轴的数据，图形颜色，标题
# plt.ylim((-1.2,1.2))#设置y参数范围
# plt.legend(loc='best')#绘制多条曲线，加个线型注释
#
# plt.subplot(224)#子绘图区域
# plt.plot(x_np,y_softplus,c='red',label='softplus')#设定x y 轴的数据，图形颜色，标题
# plt.ylim((-0.2,6))#设置y参数范围
# plt.legend(loc='best')#绘制多条曲线，加个线型注释
#
# plt.show()

#
# 3.2分类
# fake data
n_data=torch.ones(100,2)
x0=torch.normal(2*n_data,1)#x0依然是一个100行2列的矩阵，其中每个元素来q自于 均值=2*n_data，方差=1的正态分布中随机生成
y0=torch.zeros(100)#标签全为0

x1=torch.normal(-2*n_data,1)
y1=torch.ones(100)#标签全为1

x=torch.cat((x0,x1),0).type(torch.FloatTensor)#合并为数据
y=torch.cat((y0,y1), ).type(torch.LongTensor)#合并为标签

x,y=Variable(x),Variable(y)#神经网络只能输入Variable的形式
#keshih
# plt.scatter(x.data.numpy()[:,0],x.data.numpy()[:,1],c=y.data.numpy(),s=100,lw=0,cmap=0)# 绘制散点图 绘图又只能用numpy的形式
# plt.show()

#搭建神经网络
class Net(torch.nn.Module):#继承从torch来的模块
    def __init__(self,n_features,n_hidden,n_output):
        '''
        搭建层所需要的信息
        '''
        super(Net,self).__init__()#继承父模块
        #定义输入输出信息
        self.hidden=torch.nn.Linear(n_features,n_hidden)#搭建隐藏层的神经网路 特征有几个，输入就有几个
        self.predict=torch.nn.Linear(n_hidden,n_output)#输出的是预测值，所以只有一个输出
        pass
    def forward(self,x):
        '''
        前向传递的过程（流程图
        :return:
        '''
        x=torch.relu(self.hidden(x))#用激活函数激活隐藏层 ，通过n个hidden输出n个hidden unit
        x=self.predict(x)
        return x
    pass
net=Net(2,10,2)
print(net)
#将其可视化
plt.ion()#实时打印
plt.show()

optimizer=torch.optim.SGD(net.parameters(),lr=0.02)#优化神经网络参数，学习率一般小于1
loss_func=torch.nn.CrossEntropyLoss()#计算概率误差

for t in range(100):#训练一百步 出图
    out=net(x)
    loss=loss_func(out,y)#预测值在前，真实值在后，计算误差

    # 优化步骤：
    optimizer.zero_grad()#将上一步的梯度降为0
    loss.backward()#反向传递过程，给每一个神经网络结点赋上梯度
    optimizer.step()#不断优化梯度

    #可视化 优化的过程
    if t%10==0:#每五步打印一次
        plt.cla()
        prediction=torch.max(F.softmax(out),1)[1]
        pred_y=prediction.data.numpy().squeeze()
        target_y=y.data.numpy()
        plt.scatter(x.data.numpy()[:,0],x.data.numpy()[:,1],c=y.data.numpy(),s=100,lw=0)
        accuracy=sum(pred_y==target_y)/200
        plt.text(1.5,-4,'Loss=%.2f'%accuracy,fontdict={'size':20,'color':'red'})
        plt.pause(0.1)
        pass
    pass
plt.ioff()
plt.show()