import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init(admin = sp.address('tz1hdQscorfqMzFqYxnrApuS5i6QSTuoAp3w'), name = 'state', ownerToBalance = {}, symbol = 'ST', tokenApprovals = {}, tokenHolderToID = {}, tokenIdToOwner = {}, tokensMinted = sp.set([]))

  @sp.entry_point
  def approve(self, params):
    sp.verify(self.data.tokensMinted.contains(params.token_id))
    sp.verify(sp.sender == self.data.tokenIdToOwner[params.token_id])
    self.data.tokenApprovals[params.token_id] = params.approve_to

  @sp.entry_point
  def burnDataToken(self, params):
    sp.verify(sp.sender == self.data.admin)
    sp.verify(self.data.tokensMinted.contains(params.token_id))
    self.data.tokensMinted.remove(params.token_id)

  @sp.entry_point
  def mintDataToken(self, params):
    sp.verify(sp.sender == self.data.admin)
    sp.verify(~ (self.data.tokensMinted.contains(params.token_id)))
    self.data.tokensMinted.add(params.token_id)
    sp.if (~ (self.data.ownerToBalance.contains(params.address))):
      self.data.tokenHolderToID[params.address] = sp.set([])
    self.data.tokenHolderToID[params.address].add(params.token_id)
    self.data.tokenIdToOwner[params.token_id] = params.address
    sp.if (~ (self.data.ownerToBalance.contains(params.address))):
      self.data.ownerToBalance[params.address] = 0
    self.data.ownerToBalance[params.address] += 1

  @sp.entry_point
  def transfer(self, params):
    sp.verify(self.data.tokensMinted.contains(params.token_id))
    sp.verify(self.data.tokenIdToOwner[params.token_id] == sp.sender)
    self.data.tokenHolderToID[sp.sender].remove(params.token_id)
    sp.if (~ (self.data.ownerToBalance.contains(params.to))):
      self.data.tokenHolderToID[params.to] = sp.set([])
    self.data.tokenHolderToID[params.to].add(params.token_id)
    self.data.tokenIdToOwner[params.token_id] = params.to
    self.data.ownerToBalance[sp.sender] -= 1
    sp.if (~ (self.data.ownerToBalance.contains(params.to))):
      self.data.ownerToBalance[params.to] = 0
    self.data.ownerToBalance[params.to] += 1

  @sp.entry_point
  def transferFrom(self, params):
    sp.verify(self.data.tokensMinted.contains(params.token_id))
    sp.verify(params.f == self.data.tokenIdToOwner[params.token_id])
    sp.verify(sp.sender == self.data.tokenApprovals[params.token_id])
    self.data.tokenHolderToID[params.f].remove(params.token_id)
    sp.if (~ (self.data.ownerToBalance.contains(params.t))):
      self.data.tokenHolderToID[params.t] = sp.set([])
    self.data.tokenHolderToID[params.t].add(params.token_id)
    self.data.tokenIdToOwner[params.token_id] = params.t
    self.data.ownerToBalance[params.f] -= 1
    sp.if (~ (self.data.ownerToBalance.contains(params.t))):
      self.data.ownerToBalance[params.t] = 0
    self.data.ownerToBalance[params.t] += 1