#🛡️ Defense Industry Blockchain Network

This project is a Decentralized Application (dApp) designed to track the lifecycle of weapons in the defense industry. By leveraging Ethereum Blockchain technology, it ensures that every weapon's production, custody transfer, maintenance, and status change is recorded immutably and transparently.

🚀 Features
🔫 Mint New Weapon: Register new weapons to the blockchain with unique serial numbers.

🤝 Transfer Custody: Securely transfer weapon ownership between units/personnel.

🔧 Maintenance Logs: Record maintenance activities (e.g., cleaning, repair) on the blockchain.

⚠️ Status Reporting: Flag weapons as Active, Lost, Stolen, or Scrapped.

📜 Audit Trail (History): View the complete, unalterable history of any weapon from production to present.

📊 Live Inventory: Real-time fetching of data directly from the blockchain.

🛠️ Tech Stack
Blockchain: Ethereum (Local via Ganache)

Smart Contract: Solidity (v0.8.0+)

Backend: Python (Flask)

Library: Web3.py (Blockchain interaction)

Frontend: HTML5, CSS3

IDE: Remix IDE (For contract deployment)

⚙️ Installation & Setup
Follow these steps to run the project locally.

1. Clone the Repository

2. Install Dependencies
Ensure you have Python installed. It is recommended to use a virtual environment.

3. Setup Blockchain (Ganache)
Download and install Ganache.

Open Ganache and select "Quickstart".

Note your RPC Server address (usually http://127.0.0.1:7545).

4. Deploy Smart Contract
Open Remix IDE.

Create a new file named WeaponTracker.sol and paste the contract code found in this repo.

Go to the Solidity Compiler tab and compile.

Go to Deploy & Run Transactions tab:

Set Environment to Dev - Ganache Provider.

Connect to your local Ganache RPC.

Select WeaponTracker from the contract dropdown.

Click Deploy.

5. Configure the App
Copy the Contract Address from Remix after deployment.

Open app.py in your code editor.

Update the contract_address variable:

Python

contract_address = ''

6. Run the Application

