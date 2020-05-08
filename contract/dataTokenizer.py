# Data Tokenizer

import smartpy as sp

class DataTokenizer(sp.Contract):
    def __init__(self, _name, _symbol, _admin):
        self.init(
            name = _name,
            symbol = _symbol,
            admin = _admin,
            tokensMinted = sp.set( t= sp.TString),
            tokenHolderToID = sp.big_map(tkey = sp.TAddress, tvalue = sp.TSet(sp.TString)),
            ownerToBalance = sp.big_map(tkey = sp.TAddress, tvalue = sp.TInt),
            tokenIdToOwner = sp.big_map(tkey = sp.TString, tvalue = sp.TAddress),
            tokenApprovals = sp.big_map(tkey = sp.TString, tvalue = sp.TAddress),
            )
            
    # @params : f, t, token_id
    def transderDataToken(self, f, t, token_id):
        self.data.tokenHolderToID[f].remove(token_id)
        sp.if ~self.data.ownerToBalance.contains(t):
            self.data.tokenHolderToID[t] = sp.set()
        self.data.tokenHolderToID[t].add(token_id)
        self.data.tokenIdToOwner[token_id] = t
        self.data.ownerToBalance[f] -= 1
        sp.if ~self.data.ownerToBalance.contains(t):
            self.data.ownerToBalance[t] = 0
        self.data.ownerToBalance[t] += 1

            
    # @params : token_id, address
    @sp.entry_point
    def mintDataToken(self,params):
        sp.verify(sp.sender == self.data.admin)
        sp.verify(~self.data.tokensMinted.contains(params.token_id))
        self.data.tokensMinted.add(params.token_id)
        sp.if ~self.data.ownerToBalance.contains(params.address):
            self.data.tokenHolderToID[params.address] = sp.set()
        self.data.tokenHolderToID[params.address].add(params.token_id)
        self.data.tokenIdToOwner[params.token_id] = params.address
        sp.if ~self.data.ownerToBalance.contains(params.address):
            self.data.ownerToBalance[params.address] = 0
        self.data.ownerToBalance[params.address] += 1
    
    
    # @params : token_id,
    @sp.entry_point
    def burnDataToken(self, params):
        sp.verify(sp.sender == self.data.admin)
        sp.verify(self.data.tokensMinted.contains(params.token_id))
        self.data.tokensMinted.remove(params.token_id)
    
    
    # @params : to, token_id
    @sp.entry_point
    def transfer(self,params):
        sp.verify(self.data.tokensMinted.contains(params.token_id))
        sp.verify(self.data.tokenIdToOwner[params.token_id] == sp.sender)
        self.transderDataToken(sp.sender, params.to, params.token_id)

    
    # @params : approve_to, token_id
    @sp.entry_point
    def approve(self,params):
        sp.verify(self.data.tokensMinted.contains(params.token_id))
        sp.verify( sp.sender == self.data.tokenIdToOwner[params.token_id])
        self.data.tokenApprovals[params.token_id] = params.approve_to

    
    # @params : f, t, token_id
    @sp.entry_point
    def transferFrom(self, params):
        # check if token exists
        sp.verify(self.data.tokensMinted.contains(params.token_id))
        # check if approver has the token
        sp.verify( params.f == self.data.tokenIdToOwner[params.token_id])
        # check for approval
        sp.verify(sp.sender == self.data.tokenApprovals[params.token_id])
        # transfer
        self.transderDataToken(params.f, params.t, params.token_id)


# We evaluate a contract with parameters.
contract = DataTokenizer("state","ST",sp.address("tz1hdQscorfqMzFqYxnrApuS5i6QSTuoAp3w"))


# We need to export the compile the contract.
# It can be done with the following.
import smartpybasic as spb
spb.compileContract(contract,targetBaseFilename = "./contract_build/Contract")
print("Contract compiled in ./contract_build/ContractCode.tz")