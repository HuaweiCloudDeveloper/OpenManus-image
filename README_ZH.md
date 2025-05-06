<p align="center">
  <h1 align="center">OpenManus人工智能助手</h1>
  <p align="center">
    <a href="README.md"><strong>English</strong></a> | <strong>简体中文</strong>
  </p>
</p>

## 目录

- [仓库简介](#项目介绍)
- [前置条件](#前置条件)
- [镜像说明](#镜像说明)
- [获取帮助](#获取帮助)
- [如何贡献](#如何贡献)

## 项目介绍
‌[OpenManus](https://github.com/FoundationAgents/OpenManus) 是由 MetaGPT 团队开发的开源通用型 AI 智能体框架，旨在复刻并优化 Manus（一款封闭式商业 AI Agent）的核心功能，提供无需邀请码、本地化部署的智能体解决方案。

**核心特性：**
1. 模块化设计：采用可插拔的工具链和系统提示，支持快速扩展功能模块
2. 多智能体协作：包括主代理（协调任务）、规划代理（任务分解）和工具调用代理（执行具体操作）等角色。
3. 工具链支持：

    Python 代码执行器：实时生成并运行代码。

    浏览器自动化工具：模拟人类操作访问网页、提取信息。

    文件处理系统：支持文档生成、管理和格式化输出。

    网络搜索工具：自动检索网络数据，为任务提供实时支持。
4. 任务执行过程中的思考逻辑、进度更新和中间结果以日志形式可视化，便于用户追踪和调试。


本项目提供的开源镜像商品 [**`OpenManus人工智能助手`**](https://marketplace.huaweicloud.com/hidden/contents/992480da-64a3-4ba8-90cb-686d1832e96a#productid=OFFI1111485128289529856)，已预先安装 Flink 软件及其相关运行环境，并提供部署模板。快来参照使用指南，轻松开启“开箱即用”的高效体验吧。

> **系统要求如下：**
> - CPU: 2GHz 或更高
> - RAM: 4GB 或更大
> - Disk: 至少 40GB

## 前置条件
[注册华为账号并开通华为云](https://support.huaweicloud.com/usermanual-account/account_id_001.html)

## 镜像说明

| 镜像规格 | 特性说明 | 备注 |
| --- | --- | --- |
| [OpenManus-v0.3.0-arm-v1.0](https://github.com/HuaweiCloudDeveloper/flink-image/tree/Flink1.13.0-arm-v1.0?tab=readme-ov-file) | 基于 鲲鹏服务器 + Huawei Cloud EulerOS 2.0 64bit 安装部署 |  |

## 获取帮助
- 更多问题可通过 [issue](https://github.com/HuaweiCloudDeveloper/Flink-image/issues) 或 华为云云商店指定商品的服务支持 与我们取得联系
- 其他开源镜像可看 [open-source-image-repos](https://github.com/HuaweiCloudDeveloper/open-source-image-repos)

## 如何贡献
- Fork 此存储库并提交合并请求
- 基于您的开源镜像信息同步更新 README.md
