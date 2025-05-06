<p align="center">
  <h1 align="center">Flink Stream Data Analysis Tool</h1>
  <p align="center">
    <a href="README_ZH.md"><strong>简体中文</strong></a> | <strong>English</strong>
  </p>
</p>

## Table of Contents

- [Repository Introduction](#repository-introduction)  
- [Prerequisites](#prerequisites)  
- [Image Specifications](#image-specifications)
- [Getting Help](#getting-help)
- [How to Contribute](#how-to-contribute)

## Repository Introduction  
‌[OpenManus](https://github.com/FoundationAgents/OpenManus) is an open-source, general-purpose AI agent framework developed by the MetaGPT team. It aims to replicate and enhance the core functionalities of Manus—a closed-source commercial AI agent—by providing a solution that requires no invitation code and supports local deployment.

**Core Features:**
1. **Modular Design:** Utilizes pluggable toolchains and system prompts, facilitating rapid expansion of functional modules.
2. **Multi-Agent Collaboration:** Incorporates roles such as the main agent (task coordination), planning agent (task decomposition), and tool-calling agent (execution of specific operations). 
3. **Toolchain Support:**

    Python code executor: Generates and runs code in real-time.

    Browser automation tools: Simulates human interactions to access web pages and extract information.

    File processing system: Supports document generation, management, and formatted output.

    Web search tools: Automatically retrieves online data to provide real-time support for tasks.


4. **Real-Time Feedback Mechanism**: Visualizes the agent's thought processes, progress updates, and intermediate results in log format, aiding user tracking and debugging.

This project offers pre-configured [**Flink Stream Analysis Tool**](https://marketplace.huaweicloud.com/hidden/contents/992480da-64a3-4ba8-90cb-686d1832e96a#productid=OFFI1111485128289529856) images with Flink and its runtime environment pre-installed, along with deployment templates. Follow the guide to enjoy an "out-of-the-box" experience.

> **System Requirements:**
> - CPU: 2GHz or higher  
> - RAM: 4GB or more  
> - Disk: At least 40GB  

## Prerequisites  
[Register a Huawei account and activate Huawei Cloud](https://support.huaweicloud.com/usermanual-account/account_id_001.html)

## Image Specifications  

| Image Version | Description | Notes |  
|--------------|-------------|-------|  
| [OpenManus-v0.3.0-arm-v1.0](https://github.com/HuaweiCloudDeveloper/flink-image/tree/Flink1.13.0-arm-v1.0?tab=readme-ov-file) | Deployed on Kunpeng servers with Huawei Cloud EulerOS 2.0 64bit |  | 


## Getting Help
- Submit an [issue](https://github.com/HuaweiCloudDeveloper/Flink-image/issues)
- Contact Huawei Cloud Marketplace product support

## How to Contribute
- Fork this repository and submit a merge request.
- Update README.md synchronously based on your open-source mirror information.
