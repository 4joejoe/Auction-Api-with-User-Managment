## Auction App

> Features

- User Can Register and Login
- Authentication via JWT
- Admin Privileges
- All CRUD functionalities
- CRUD on Users
- CRUD on Auction

<h2>
User CRUD
</h2>

> Register User
> <span style="color:yellow">POST</span> http://127.0.0.1:8000/register

> Login User
> <span style="color:yellow">POST</span> http://127.0.0.1:8000/accounts/login

> Get all User
> [Admin] <span style="color:green">GET</span> http://127.0.0.1:8000/all-user

> Delete User
> [Admin] <span style="color:red">DELETE</span> http://127.0.0.1:8000/deleteUser/[username]

> Password Update
> [Authenticated] <span style="color:yellow">POST</span> http://127.0.0.1:8000/accounts/change-password/

<h2>
Auction CRUD
</h2>

> View All Auctions
> [Authenticated] <span style="color:green">GET</span> http://127.0.0.1:8000/auction-view

> Create Auction
> [Admin] <span style="color:yellow">POST</span> http://127.0.0.1:8000/auction-create

> Update Auction
> [Admin] <span style="color:pink">PATCH</span> http://127.0.0.1:8000/auction-update/[auction-id]

> Delete Auction
> [Admin] <span style="color:red">DELETE</span> http://127.0.0.1:8000/auction-delete/[auction-id]

<h2>
Bid APIs
</h2>

> Create Bid
> [Authenticated] <span style="color:yellow">POST</span> http://127.0.0.1:8000/bid-create

> Set Buyer
> [Automatic] <span style="color:pink">PATCH</span> http://127.0.0.1:8000/bid-ended/[auction-id]

> Set Top Bid
> [Automatic] <span style="color:yellow">POST</span> http://127.0.0.1:8000/auction/[auction-id]/set_top_bid/
