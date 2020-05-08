**Its an NFT based Data Sharing Platform where info can be shared and allowed to be shared and with transferrable ownership**
------------------------------------------------------------------------

> The contract is made just to play around with the ownership of a
> string. This implementation can be carried for sharing of ownership of
> any signed document ( obviously cryptographically ) over the public
> blockchain network.


**Contract Deployed in Carthagenet :**
KT1SmvWyN6npuJXpLYLmu3TpHSkGDh4zEa2F

**SmartPy Explorer to Play Around with the tokenizer :** 
https://smartpy.io/dev/explorer.html?address=KT1SmvWyN6npuJXpLYLmu3TpHSkGDh4zEa2F

Features:
--------

**MintDataToken :** Whenever a new token is to be managed in the smartContract, it can be handled by the admin of the contract.

**BurnDataToken :** Burning the Data Token when it is not managed by the smartContract anymore, only the admin has the access to do it with the allowance of the original owner.

**Transfer :** It transfers the owned token data to another user with the tokenID specified

**Approve :** Owner can approve someone ( Address ) to handle certain asset so they can transfer the 

**Transfer From :** Only approved addresses for a particular asset token can have the ability to transfer from the owner to any other address without actually owing the data token.

****

Stack used :
------------
- [x] **SmartPy** for developing Smart Contract.
- [x]  **ConseilJs** for deployment and interaction.
- [x] **Tezster Bundle** for Local Development with testing.
- [x] **Tezster CLI ** for local Deployment.
- [ ] Lacks UI

**Testing Ops and Results :**

    Comment...
     h2: Accounts
    Computing sp.list([sp.test_account("Administrator"), sp.test_account("Alice"), sp.test_account("Bob"), sp.test_account("Robert"), sp.test_account("Dibyo")])...
     => sp.list([sp.record(seed = 'Administrator', address = sp.address('tz1hdQscorfqMzFqYxnrApuS5i6QSTuoAp3w'), public_key = sp.key('edpktzrjdb1tx6dQecQGZL6CwhujWg1D2CXfXWBriqtJSA6kvqMwA2'), public_key_hash = sp.key_hash('tz1hdQscorfqMzFqYxnrApuS5i6QSTuoAp3w'), secret_key = sp.secret_key('edskRqFp3Z9AqoKrMNFb9bnWNwEsRzbjqjBhzmFMLF9UqB6VBmw7F8ppTiXaAnHtysmi6xFxoHf6rMUz6Y1ipiDz2EgwZQv3pa')), sp.record(seed = 'Alice', address = sp.address('tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi'), public_key = sp.key('edpkuvNy6TuQ2z8o9wnoaTtTXkzQk7nhegCHfxBc4ecsd4qG71KYNG'), public_key_hash = sp.key_hash('tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi'), secret_key = sp.secret_key('edskRijgcXx8gzqkq7SCBbrb6aDZQMmP6dznCQWgU1Jr4qPfJT1yFq5A39ja9G4wahS8uWtBurZy14Hy7GZkQh7WnopJTKtCQG')), sp.record(seed = 'Bob', address = sp.address('tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C'), public_key = sp.key('edpkufVmvzkm4oFQ7WcF5NJbq9BFB2mWRsm4Dyh2spMDuDxWSQWHuT'), public_key_hash = sp.key_hash('tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C'), secret_key = sp.secret_key('edskRq1xuW7TCYzdFm1JQLi1Hz4MNDVP6ukQHVEEh3bVqyuzv7pXXjaGsXZuMbwtd3kQFp3LQ7GQzkLeprNEijKhQKzsxrYrUz')), sp.record(seed = 'Robert', address = sp.address('tz1Ns3YQJR6piMZ8GrD2iYu94Ybi1HFfNyBP'), public_key = sp.key('edpkvThfdv8Efh1MuqSTUk5EnUFCTjqN6kXDCNXpQ8udN3cKRhNDr2'), public_key_hash = sp.key_hash('tz1Ns3YQJR6piMZ8GrD2iYu94Ybi1HFfNyBP'), secret_key = sp.secret_key('edskRiaffUWqB9zgaEhuX6EmejbLzk2xcpSEXLv3G4cDfcbY75c71ASyGnFHXuaTAVMPt2bJLGGye1gm24oBmAc2k5VDHHo5Ua')), sp.record(seed = 'Dibyo', address = sp.address('tz1L7pxNZvvgi88XeceL7h6EpMUYzEpziduh'), public_key = sp.key('edpkvDnBfq5qWg8ov6TKaM1QPeKzv6i9dnZL16b71GgsoqZPLJgbrg'), public_key_hash = sp.key_hash('tz1L7pxNZvvgi88XeceL7h6EpMUYzEpziduh'), secret_key = sp.secret_key('edskRisEgQRB6TfCTJ8fi1wzJnCkCVT2dYgej8YT5VuP6wzHL14CuX8VJmLXiEwFqzB8FcotKy3eWS4eSvKE8DPVi3XLZADY6M'))])
    Creating contract
     -> (Pair (Pair (Pair (Pair (Pair (Pair (Pair "tz1hdQscorfqMzFqYxnrApuS5i6QSTuoAp3w" "state") {}) "ST") {}) {}) {}) {})
     => ./test-build/testContractTypes.0.2.tz 2
    Error in generated contract
     => ./test-build/testContractCode.0.2.tz 1115
     => ./test-build/testContractCode.0.2.tz.json 320
     => ./test-build/testPrettyPrint.0.2.py 59
    Comment...
     h2: Admin minting Tokens
    Executing mintDataToken(sp.record(address = sp.reduce(sp.test_account("Alice").address), token_id = 'Kitty1'))...
     -> (Pair (Pair (Pair (Pair (Pair (Pair (Pair "tz1hdQscorfqMzFqYxnrApuS5i6QSTuoAp3w" "state") {Elt "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi" 1}) "ST") {}) {Elt "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi" {"Kitty1"}}) {Elt "Kitty1" "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi"}) {"Kitty1"})
    Executing mintDataToken(sp.record(address = sp.reduce(sp.test_account("Bob").address), token_id = 'Kitty2'))...
     -> (Pair (Pair (Pair (Pair (Pair (Pair (Pair "tz1hdQscorfqMzFqYxnrApuS5i6QSTuoAp3w" "state") {Elt "tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C" 1; Elt "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi" 1}) "ST") {}) {Elt "tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C" {"Kitty2"}; Elt "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi" {"Kitty1"}}) {Elt "Kitty1" "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi"; Elt "Kitty2" "tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C"}) {"Kitty1"; "Kitty2"})
    Executing mintDataToken(sp.record(address = sp.reduce(sp.test_account("Bob").address), token_id = 'Kitty3'))...
     -> (Pair (Pair (Pair (Pair (Pair (Pair (Pair "tz1hdQscorfqMzFqYxnrApuS5i6QSTuoAp3w" "state") {Elt "tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C" 2; Elt "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi" 1}) "ST") {}) {Elt "tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C" {"Kitty2"; "Kitty3"}; Elt "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi" {"Kitty1"}}) {Elt "Kitty1" "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi"; Elt "Kitty2" "tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C"; Elt "Kitty3" "tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C"}) {"Kitty1"; "Kitty2"; "Kitty3"})
    Executing burnDataToken(sp.record(token_id = 'Kitty4'))...
     -> --- Expected failure in transaction --- WrongCondition in line 50: self.data.tokensMinted.contains(params.token_id)
    Executing transfer(sp.record(to = sp.reduce(sp.test_account("Robert").address), token_id = 'Kitty2'))...
     -> (Pair (Pair (Pair (Pair (Pair (Pair (Pair "tz1hdQscorfqMzFqYxnrApuS5i6QSTuoAp3w" "state") {Elt "tz1Ns3YQJR6piMZ8GrD2iYu94Ybi1HFfNyBP" 1; Elt "tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C" 1; Elt "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi" 1}) "ST") {}) {Elt "tz1Ns3YQJR6piMZ8GrD2iYu94Ybi1HFfNyBP" {"Kitty2"}; Elt "tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C" {"Kitty3"}; Elt "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi" {"Kitty1"}}) {Elt "Kitty1" "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi"; Elt "Kitty2" "tz1Ns3YQJR6piMZ8GrD2iYu94Ybi1HFfNyBP"; Elt "Kitty3" "tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C"}) {"Kitty1"; "Kitty2"; "Kitty3"})
    Executing approve(sp.record(approve_to = sp.reduce(sp.test_account("Dibyo").address), token_id = 'Kitty2'))...
     -> (Pair (Pair (Pair (Pair (Pair (Pair (Pair "tz1hdQscorfqMzFqYxnrApuS5i6QSTuoAp3w" "state") {Elt "tz1Ns3YQJR6piMZ8GrD2iYu94Ybi1HFfNyBP" 1; Elt "tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C" 1; Elt "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi" 1}) "ST") {Elt "Kitty2" "tz1L7pxNZvvgi88XeceL7h6EpMUYzEpziduh"}) {Elt "tz1Ns3YQJR6piMZ8GrD2iYu94Ybi1HFfNyBP" {"Kitty2"}; Elt "tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C" {"Kitty3"}; Elt "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi" {"Kitty1"}}) {Elt "Kitty1" "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi"; Elt "Kitty2" "tz1Ns3YQJR6piMZ8GrD2iYu94Ybi1HFfNyBP"; Elt "Kitty3" "tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C"}) {"Kitty1"; "Kitty2"; "Kitty3"})
    Executing transferFrom(sp.record(f = sp.reduce(sp.test_account("Robert").address), t = sp.reduce(sp.test_account("Alice").address), token_id = 'Kitty2'))...
     -> (Pair (Pair (Pair (Pair (Pair (Pair (Pair "tz1hdQscorfqMzFqYxnrApuS5i6QSTuoAp3w" "state") {Elt "tz1Ns3YQJR6piMZ8GrD2iYu94Ybi1HFfNyBP" 0; Elt "tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C" 1; Elt "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi" 2}) "ST") {Elt "Kitty2" "tz1L7pxNZvvgi88XeceL7h6EpMUYzEpziduh"}) {Elt "tz1Ns3YQJR6piMZ8GrD2iYu94Ybi1HFfNyBP" {}; Elt "tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C" {"Kitty3"}; Elt "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi" {"Kitty1"; "Kitty2"}}) {Elt "Kitty1" "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi"; Elt "Kitty2" "tz1WxrQuZ4CK1MBUa2GqUWK1yJ4J6EtG1Gwi"; Elt "Kitty3" "tz1Rp4Bv8iUhYnNoCryHQgNzN2D7i3L1LF9C"}) {"Kitty1"; "Kitty2"; "Kitty3"})

