from flask import Flask, render_template, request, redirect
from web3 import Web3
import json
import os

# FLASK VE DOSYA AYARLARI
current_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(current_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

# BLOCKCHAIN BAĞLANTISI
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Bağlantı testi
if web3.is_connected():
    print("✅ Blockchain'e (Ganache) bağlandı!")
else:
    print("❌ Bağlantı hatası! Ganache açık mı?")

# SMART CONTRACT AYARLARI
contract_address = '0x1377bAC1132D3a79D86D4eBC6220BBFdB2Fcf7Be'

contract_abi_string = """[
   {
      "anonymous": false,
      "inputs": [
         {
            "indexed": false,
            "internalType": "string",
            "name": "serialNumber",
            "type": "string"
         },
         {
            "indexed": false,
            "internalType": "address",
            "name": "from",
            "type": "address"
         },
         {
            "indexed": false,
            "internalType": "address",
            "name": "to",
            "type": "address"
         },
         {
            "indexed": false,
            "internalType": "uint256",
            "name": "timestamp",
            "type": "uint256"
         }
      ],
      "name": "CustodyTransferred",
      "type": "event"
   },
   {
      "anonymous": false,
      "inputs": [
         {
            "indexed": false,
            "internalType": "string",
            "name": "serialNumber",
            "type": "string"
         },
         {
            "indexed": false,
            "internalType": "string",
            "name": "description",
            "type": "string"
         },
         {
            "indexed": false,
            "internalType": "uint256",
            "name": "timestamp",
            "type": "uint256"
         }
      ],
      "name": "MaintenanceLogged",
      "type": "event"
   },
   {
      "anonymous": false,
      "inputs": [
         {
            "indexed": false,
            "internalType": "string",
            "name": "serialNumber",
            "type": "string"
         },
         {
            "indexed": false,
            "internalType": "enum WeaponTracker.Status",
            "name": "newStatus",
            "type": "uint8"
         },
         {
            "indexed": false,
            "internalType": "uint256",
            "name": "timestamp",
            "type": "uint256"
         }
      ],
      "name": "StatusChanged",
      "type": "event"
   },
   {
      "anonymous": false,
      "inputs": [
         {
            "indexed": false,
            "internalType": "string",
            "name": "serialNumber",
            "type": "string"
         },
         {
            "indexed": false,
            "internalType": "string",
            "name": "weaponType",
            "type": "string"
         },
         {
            "indexed": false,
            "internalType": "address",
            "name": "owner",
            "type": "address"
         }
      ],
      "name": "WeaponMinted",
      "type": "event"
   },
   {
      "inputs": [
         {
            "internalType": "string",
            "name": "_serialNumber",
            "type": "string"
         }
      ],
      "name": "getOwner",
      "outputs": [
         {
            "internalType": "address",
            "name": "",
            "type": "address"
         }
      ],
      "stateMutability": "view",
      "type": "function"
   },
   {
      "inputs": [
         {
            "internalType": "string",
            "name": "_serialNumber",
            "type": "string"
         },
         {
            "internalType": "string",
            "name": "_description",
            "type": "string"
         }
      ],
      "name": "logMaintenance",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
   },
   {
      "inputs": [
         {
            "internalType": "string",
            "name": "_serialNumber",
            "type": "string"
         },
         {
            "internalType": "string",
            "name": "_weaponType",
            "type": "string"
         }
      ],
      "name": "mintWeapon",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
   },
   {
      "inputs": [
         {
            "internalType": "string",
            "name": "_serialNumber",
            "type": "string"
         },
         {
            "internalType": "uint256",
            "name": "_statusCode",
            "type": "uint256"
         }
      ],
      "name": "reportLostOrStolen",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
   },
   {
      "inputs": [
         {
            "internalType": "string",
            "name": "_serialNumber",
            "type": "string"
         },
         {
            "internalType": "address",
            "name": "_newOwner",
            "type": "address"
         }
      ],
      "name": "transferCustody",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
   },
   {
      "inputs": [
         {
            "internalType": "string",
            "name": "",
            "type": "string"
         }
      ],
      "name": "weapons",
      "outputs": [
         {
            "internalType": "string",
            "name": "serialNumber",
            "type": "string"
         },
         {
            "internalType": "string",
            "name": "weaponType",
            "type": "string"
         },
         {
            "internalType": "address",
            "name": "currentOwner",
            "type": "address"
         },
         {
            "internalType": "enum WeaponTracker.Status",
            "name": "status",
            "type": "uint8"
         },
         {
            "internalType": "bool",
            "name": "exists",
            "type": "bool"
         }
      ],
      "stateMutability": "view",
      "type": "function"
   }
]"""

contract_abi = json.loads(contract_abi_string)

# Sözleşme nesnesini oluştur
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Varsayılan hesap
web3.eth.default_account = web3.eth.accounts[0]


#ENVANTER LISTESI
@app.route('/')
def inventory():
    print("------------------------------------------------")
    print("1. ENVANTER SORGUSU BAŞLADI...")

    weapon_list = []

    try:
        all_minted_events = contract.events.WeaponMinted.get_logs(from_block=0)

        print(f"2. Bulunan Silah Sayısı: {len(all_minted_events)}")

        for event in all_minted_events:
            args = event['args']
            serial_no = args.get('serialNumber')
            weapon_type = args.get('weaponType')

            current_owner = "Bilinmiyor"
            try:
                current_owner = contract.functions.getOwner(serial_no).call()
            except:
                pass

            weapon_list.append({
                'serial': serial_no,
                'type': weapon_type,
                'owner': current_owner
            })

    except Exception as e:
        print(f"ENVANTER HATASI: {e}")
        return render_template('index.html', weapons=[])

    return render_template('index.html', weapons=weapon_list)


# SİLAH KAYDETME (MINT)
@app.route('/mint', methods=['POST'])
def mint():
    serial = request.form['serial']
    w_type = request.form['type']

    try:
        tx_hash = contract.functions.mintWeapon(serial, w_type).transact()
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        print("------------------------------------------")
        print(f"İŞLEM DURUMU (1=Başarılı, 0=Hata): {receipt['status']}")
        print(f"HARCANAN GAZ: {receipt['gasUsed']}")
        print(f"OLUŞAN LOG SAYISI: {len(receipt['logs'])}")
        print("------------------------------------------")

        if receipt['status'] == 0:
            return "HATA: İşlem blokzincir tarafından reddedildi (Revert)!"

        return redirect('/')
    except Exception as e:
        return f"Hata: {str(e)}"


# TRANSFER
@app.route('/transfer', methods=['POST'])
def transfer():
    serial = request.form['serial']

    new_owner_address = request.form.get('new_owner')

    if not new_owner_address or "Ganache" in new_owner_address:
        new_owner_address = web3.eth.accounts[1]

    try:
        tx_hash = contract.functions.transferCustody(serial, new_owner_address).transact()
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Transfer yapıldı: {serial} -> {new_owner_address}")
        return redirect('/')
    except Exception as e:
        return f"Transfer Hatası: {str(e)}"


# BAKIM KAYDI
@app.route('/maintenance', methods=['POST'])
def maintenance():
    serial = request.form['serial']
    description = request.form['description']

    try:
        tx_hash = contract.functions.logMaintenance(serial, description).transact({'from': web3.eth.accounts[0]})
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Bakım Kaydedildi: {serial}")
    except Exception as e:
        print(f"BAKIM HATASI: {e}")

    return redirect('/')


# DURUM BİLDİRİMİ
@app.route('/report', methods=['POST'])
def report_status():
    serial = request.form['serial']
    new_status = request.form['status']

    try:
        status_code = int(new_status)
        tx_hash = contract.functions.reportLostOrStolen(serial, status_code).transact({'from': web3.eth.accounts[0]})
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Durum Güncellendi: {serial} -> {new_status}")
    except Exception as e:
        print(f"RAPOR HATASI: {e}")

    return redirect('/')


# GEÇMİŞ (HISTORY)
@app.route('/history/<serial>')
def weapon_history(serial):
    history_logs = []

    try:
        # A) Transfer Geçmişi (Event adı: CustodyTransferred)
        transfer_events = contract.events.CustodyTransferred.get_logs(from_block=0)

        for event in transfer_events:
            if event['args']['serialNumber'] == serial:
                history_logs.append({
                    'type': 'Transfer',
                    'detail': f"{event['args']['from'][:8]}... -> {event['args']['to'][:8]}...",
                    'block': event['blockNumber']
                })

        # B) Bakım Geçmişi (Event adı: MaintenanceLogged)
        maintenance_events = contract.events.MaintenanceLogged.get_logs(from_block=0)
        for event in maintenance_events:
            if event['args']['serialNumber'] == serial:
                history_logs.append({
                    'type': 'Bakım',
                    'detail': event['args']['description'],
                    'block': event['blockNumber']
                })

        # C) Durum Değişikliği (Event adı: StatusChanged)
        status_events = contract.events.StatusChanged.get_logs(from_block=0)
        status_names = ["Aktif", "Bakımda", "Kayıp", "Çalıntı", "Hurda"]
        for event in status_events:
            if event['args']['serialNumber'] == serial:
                status_idx = event['args']['newStatus']
                status_text = status_names[status_idx] if status_idx < len(status_names) else str(status_idx)

                history_logs.append({
                    'type': 'Durum',
                    'detail': f"Yeni Durum: {status_text}",
                    'block': event['blockNumber']
                })

        history_logs.sort(key=lambda x: x['block'], reverse=True)

    except Exception as e:
        print(f"Geçmiş çekilirken hata: {e}")

    return render_template('history.html', serial=serial, logs=history_logs)


if __name__ == '__main__':
    app.run(debug=True)