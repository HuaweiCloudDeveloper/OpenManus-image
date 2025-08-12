## 目录

- [仓库简介](#项目介绍)
- [前置条件](#前置条件)
- [镜像说明](#镜像说明)
- [获取帮助](#获取帮助)
- [如何贡献](#如何贡献)

## 项目介绍

[OpenManus](<https://github.com/mannaandpoem/OpenManus) 是一个开源的 AI 智能体框架，由 MetaGPT 团队开发，旨在复刻并优化商业产品 Manus 的核心功能.

### **核心功能：**

- **多智能体协作**：OpenManus 支持多智能体自主协作，能够将复杂任务拆解为可执行的子任务，并协调执行层工具调用。
- **工具集成**：内置多个实用工具，如 PythonExecute（执行 Python 代码）、GoogleSearch（网络搜索）、BrowserUseTool（浏览器操作）和 FileSaver（文件保存）。
- **实时反馈机制**：任务执行过程中的思考日志和进度更新可视化，用户可以随时了解任务进展。
- **模块化设计**：支持快速接入智能客服、教育知识库、舆情分析等功能模块，开发者可以根据需求自由组合功能模块。
- **强大的工具链**：集成了 Python 代码执行器、网络搜索工具、浏览器自动化和文件处理系统，能够高效完成复杂任务

本项目提供的开源镜像商品 [**OpenHands AI 智能体**]() ，已预先安装Neo4j及其相关运行环境，并提供部署模板。快来参照使用指南，轻松开启“开箱即用”的高效体验吧。

> **系统要求如下：**
>
> - CPU: 2GHz 或更高
> - RAM: 4GB 或更大
> - Disk: 至少 40GB

## 前置条件

[注册华为账号并开通华为云](https://support.huaweicloud.com/usermanual-account/account_id_001.html)

## 镜像说明

| 镜像规格                                                     | 特性说明                                                  | 备注 |
| ------------------------------------------------------------ | --------------------------------------------------------- | ---- |
| [openmanus-v0.3.0-鲲鹏](https://github.com/HuaweiCloudDeveloper/neo4j-image/tree/openmanus-v0.3.0-kunpeng) | 基于 鲲鹏服务器 + Huawei Cloud EulerOS 2.0 64bit 安装部署 |      |

## 获取帮助

- 更多问题可通过 [issue](https://github.com/HuaweiCloudDeveloper/neo4j-image/issues) 或 华为云云商店指定商品的服务支持 与我们取得联系
- 其他开源镜像可看 [open-source-image-repos](https://github.com/HuaweiCloudDeveloper/open-source-image-repos)

## 如何贡献

- Fork 此存储库并提交合并请求
- 基于您的开源镜像信息同步更新 README.md
