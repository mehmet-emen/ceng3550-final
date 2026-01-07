<p align="center">
  <img src="https://img.shields.io/badge/Blockchain-Ethereum-blueviolet?style=for-the-badge">
  <img src="https://img.shields.io/badge/Smart%20Contract-Solidity-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/Backend-Flask-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Prototype-orange?style=for-the-badge">
</p>

<h1 align="center">🛡️ Defense Industry Blockchain Network</h1>

<p align="center">
A decentralized blockchain-based system for tracking the full lifecycle of defense weapons with immutable, transparent, and auditable records.
</p>

---

## 📌 Project Overview

**Defense Industry Blockchain Network** is a **Decentralized Application (dApp)** that enables secure tracking of weapons throughout their entire lifecycle.

Using **Ethereum blockchain technology**, the system ensures that all critical events—such as weapon registration, custody transfer, maintenance, and status updates—are recorded **immutably** and **tamper-proof**.

This project demonstrates how blockchain can be applied to **high-security, audit-sensitive domains** like the defense industry.

---

## 🧩 System Capabilities

| Feature | Description |
|------|------------|
| 🔫 **Weapon Registration** | Mint new weapons with unique serial numbers on-chain |
| 🤝 **Custody Transfer** | Secure ownership transfer between authorized units or personnel |
| 🔧 **Maintenance Tracking** | Log maintenance and repair events immutably |
| ⚠️ **Status Management** | Mark weapons as Active, Lost, Stolen, or Scrapped |
| 📜 **Audit History** | Full, verifiable lifecycle history per weapon |
| 📊 **Live Inventory** | Real-time data fetched directly from the blockchain |

---

## 🚀 Core Features

### 🔫 Mint New Weapon
Register newly manufactured weapons with a unique identifier stored permanently on the blockchain.

### 🤝 Transfer Custody
Transfer weapon ownership securely between authorized parties while preserving historical records.

### 🔧 Maintenance Logs
Store maintenance actions such as inspections, repairs, and servicing as immutable events.

### ⚠️ Status Reporting
Instantly update weapon status (Active, Lost, Stolen, Scrapped) with full traceability.

### 📜 Audit Trail
Retrieve a complete, chronological history of any weapon from creation to present.

### 📊 Live Inventory
Fetch real-time weapon data directly from the Ethereum network.

---

## 🛠️ Technology Stack

### 🔗 Blockchain Layer
- **Ethereum** (Local development via **Ganache**)

### 📜 Smart Contracts
- **Solidity** `^0.8.0`

### 🧠 Backend
- **Python**
- **Flask**

### 🔌 Blockchain Interaction
- **Web3.py**

### 🎨 Frontend
- **HTML5**
- **CSS3**

### 🧪 Development Tools
- **Remix IDE** (Smart contract compilation & deployment)
- **Ganache** (Local Ethereum network)

---

## ⚙️ Installation & Setup
Follow the steps below to run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/defense-blockchain-network.git
cd defense-blockchain-network
 ```

### 2️⃣ Install Backend Dependencies
- Make sure Python 3.x is installed.
- Using a virtual environment is recommended.

### 3️⃣ Setup Local Blockchain (Ganache)
1. Download and install Ganache
2. Launch Ganache and select Quickstart Ethereum
2. Note the RPC Server address:

```cpp
http://127.0.0.1:7545
```

### 4️⃣ Deploy Smart Contract
- Open Remix IDE
- Create a new file:

```cpp
WeaponTracker.sol
```
- Paste the smart contract code from this repository
- Compile using Solidity
- Go to Deploy & Run Transactions
- Environment: Dev - Ganache Provider
- Connect to local RPC
- Deploy the WeaponTracker contract

### 5️⃣ Configure Backend Application
1. Copy the contract address from Remix

2. Open app.py

3. Update the following variable:

```python
contract_address = "YOUR_CONTRACT_ADDRESS"
```

### 6️⃣ Run the Application
1. python app.py

2. The application will now interact with the deployed smart contract on your local blockchain.


<p align="center"> ⚔️ Built with Blockchain for Secure Defense Asset Tracking </p>
