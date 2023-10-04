from django.urls import path

from auction.views import AllBidView, AuctionCreationView, AuctionsDelete, AuctionsUpdate,AuctionsView, CreateBidView, SetBuyerView, SetTopBidView

urlpatterns = [
    path("auction-create",AuctionCreationView.as_view()),
    path("auction-view",AuctionsView.as_view()),
    path("auction-update/<uuid:auction_uuid>",AuctionsUpdate.as_view()),
    path("auction-delete/<uuid:auction_uuid>",AuctionsDelete.as_view()),
    path("bid-create",CreateBidView.as_view()),
    path("bid-view",AllBidView.as_view()),
    path("bid-ended/<uuid:auction_uuid>",SetBuyerView.as_view()),
    path('auction/<uuid:auction_id>/set_top_bid/', SetTopBidView.as_view()),

]