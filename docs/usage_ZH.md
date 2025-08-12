# OpenManus人工智能助手
## 商品连接
[OpenManus](https://marketplace.huaweicloud.com/hidden/contents/f99f5fc8-4cf1-4dc9-92a7-8ffc4dd2805e#productid=OFFI1135139479874867200)

## 商品说明
[OpenManus](<https://github.com/mannaandpoem/OpenManus)由 MetaGPT 团队精心打造的开源项目，于2025年3月发布。它致力于模仿并改进 Manus 这一封闭式商业 AI Agent 的核心功能，为用户提供无需邀请码、可本地化部署的智能体解决方案。换句话说，OpenManus 就像一位全能的数字助手，能够在你的本地设备上运行，随时听候差遣，完成各种复杂任务。
本商品在鲲鹏云的上Ubuntu24.04和HCE2.0系统中进行安装后以镜像提供给用户使用。

## 商品购买
您可以在云商店搜索“vLLM大模型服务”。<br>
其中，地域、规格、按照推荐配置使用，购买方式根据您的需求选择按需/按月/按年，短
期使用推荐按需，长期使用推荐按月/按年，确认配置后点击“立即购买”。

### 使用 RFS 模板直接部署
![img.png](images/img1.png)
必填项填写后，点击 下一步
![img.png](images/img2.png)
![img.png](images/img3.png)
创建直接计划后，点击 确定
![img.png](images/img4.png)
![img.png](images/img5.png)
点击部署，执行计划
![img.png](images/img6.png)
如下图“Apply required resource success. ”即为资源创建完成
![img.png](images/img7.png)

### ECS控制台配置
#### 准备工作

在使用ECS控制台配置前，需要您提前配置好 **安全组规则**。

> **安全组规则的配置如下：**
> - 入方向规则放通端口8000，源地址内必须包含您的客户端ip，否则无法访问
> - 入方向规则放通 CloudShell 连接实例使用的端口 `22`，以便在控制台登录调试
> - 出方向规则一键放通

#### 创建ECS

前提工作准备好后，选择 ECS 控制台配置跳转到[购买ECS](https://support.huaweicloud.com/qs-ecs/ecs_01_0103.html) 页面，ECS 资源的配置如下图所示：

选择CPU架构
![img.png](images/img8.png)
选择服务器规格
![img_1.png](images/img_1.png)
选择镜像
![img_2.png](images/img_2.png)
其他参数根据实际请客进行填写，填写完成之后，点击立即购买即可
![img_3.png](images/img_3.png)


> **值得注意的是：**
- VPC 您可以自行创建
- 安全组选择 [**准备工作**](#准备工作) 中配置的安全组；
- 弹性公网IP选择现在购买，推荐选择“按流量计费”，带宽大小可设置为5Mbit/s；
- 高级配置需要在高级选项支持注入自定义数据，所以登录凭证不能选择“密码”，选择创建后设置；
- 其余默认或按规则填写即可。

 ## 商品使用
 ### OpenManus 使用

**IP+5172访问UI**

![](.\images\om1.png)



点击系统配置，配置自己模型的 Model Name、  URL和API KEY 三个必填参数，然后保存配置**

![](.\images\om2.png)



再任务输入地址栏输入想要了解的内容；

![](.\images\om3.png)



### 参考文档

[OpenManus手册](lhttps://github.com/FoundationAgents/OpenManus)

