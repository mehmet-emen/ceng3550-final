pragma solidity ^0.8.0;

contract WeaponTracker {
    
    // Silah Durumları (0: Aktif, 1: Bakımda, 2: Kayıp, 3: Çalıntı, 4: Hurda)
    enum Status { Active, Maintenance, Lost, Stolen, Scrapped }

    struct Weapon {
        string serialNumber;
        string weaponType;
        address currentOwner;
        Status status;
        bool exists;
    }

    mapping(string => Weapon) public weapons;

    //EVENTLER
    event WeaponMinted(string serialNumber, string weaponType, address owner);

    event CustodyTransferred(string serialNumber, address from, address to, uint256 timestamp);

    event MaintenanceLogged(string serialNumber, string description, uint256 timestamp);
    event StatusChanged(string serialNumber, Status newStatus, uint256 timestamp);

    // Silah Üretme
    function mintWeapon(string memory _serialNumber, string memory _weaponType) public {
        require(!weapons[_serialNumber].exists, "Bu seri numarasi zaten kayitli!");

        weapons[_serialNumber] = Weapon({
            serialNumber: _serialNumber,
            weaponType: _weaponType,
            currentOwner: msg.sender,
            status: Status.Active, // Varsayılan: Aktif
            exists: true
        });

        emit WeaponMinted(_serialNumber, _weaponType, msg.sender);
    }

    // Transfer
    function transferCustody(string memory _serialNumber, address _newOwner) public {
        require(weapons[_serialNumber].exists, "Silah bulunamadi!");
        require(weapons[_serialNumber].currentOwner == msg.sender, "Sahibi siz degilsiniz!");
        require(weapons[_serialNumber].status == Status.Active, "Silah transfer edilebilir durumda degil (calinti veya bakimda)!");

        address oldOwner = weapons[_serialNumber].currentOwner;
        weapons[_serialNumber].currentOwner = _newOwner;

        emit CustodyTransferred(_serialNumber, oldOwner, _newOwner, block.timestamp);
    }

    // Bakım Kaydı
    function logMaintenance(string memory _serialNumber, string memory _description) public {
        require(weapons[_serialNumber].exists, "Silah bulunamadi!");
        // Sadece sahibi veya yetkili bakım yapabilir

        emit MaintenanceLogged(_serialNumber, _description, block.timestamp);
    }

    // Durum Bildir
    function reportLostOrStolen(string memory _serialNumber, uint256 _statusCode) public {
        require(weapons[_serialNumber].exists, "Silah bulunamadi!");
        require(weapons[_serialNumber].currentOwner == msg.sender, "Yetkiniz yok!");

        weapons[_serialNumber].status = Status(_statusCode);

        emit StatusChanged(_serialNumber, Status(_statusCode), block.timestamp);
    }

    // Sahibini Sorgula
    function getOwner(string memory _serialNumber) public view returns (address) {
        return weapons[_serialNumber].currentOwner;
    }
}