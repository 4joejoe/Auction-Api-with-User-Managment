import json
import pandas as pd
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import  Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from auction.models import Auction, Bid
from auction.serializers import AuctionCreateSerializer, AuctionUpdateSerializer, BidCreateSerializer, BidViewSerializer
from users.models import MyUser
# Create your views here.

# Auction Create
class AuctionCreationView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self,request):
        serializer = AuctionCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# Auction View
class AuctionsView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        get_all_auction = Auction.objects.all()
        serializer = AuctionCreateSerializer(get_all_auction,many=True)
        # data = pd.DataFrame(get_all_auction)
        # print(data)
        return Response(serializer.data,status.HTTP_200_OK)

# Auction Update

class AuctionsUpdate(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    def patch(self,request,auction_uuid):
        get_auction = Auction.objects.get(auction_uuid=auction_uuid)
        serializer = AuctionUpdateSerializer(get_auction,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AuctionsDelete(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    def delete(self,request,auction_uuid):
        get_auction = Auction.objects.get(auction_uuid=auction_uuid)
        get_auction.delete()
        return Response({"Auction Deleted"})

class CreateBidView(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        # Create bidserializer instance
        serializer = BidCreateSerializer(data=request.data)
        if serializer.is_valid():
            # print("user_id",auction_id, user_id)
            auction_id = request.data.get('auction')
            user_id = request.data.get('user')
            # auction = Auction.objects.get(auction_uuid=auction_id)
            # user = MyUser.objects.get(id=user_id)

            bid = serializer.save()
            return Response(BidCreateSerializer(bid).data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AllBidView(APIView):
    permission_classes=[IsAuthenticated,]

    def get(self,request):
        get_all_bids = Bid.objects.all()
        serializer = BidViewSerializer(get_all_bids,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
        
class SetTopBidView(APIView):
    permission_classes=[IsAuthenticated,IsAdminUser]

    def patch(self,request,auction_id):
        auction = Auction.objects.get(auction_uuid=auction_id)

        highest_bid = Bid.objects.filter(auction=auction).order_by("-amount").first()

        auction.update_top_bid(highest_bid.user,highest_bid.amount)
        return Response({"msg":"Top Bid Updated"},status=status.HTTP_202_ACCEPTED)

class SetBuyerView(APIView):
    permission_classes=[IsAuthenticated,IsAdminUser]

    def patch(self,request,auction_uuid):
        auction = Auction.objects.get(auction_uuid=auction_uuid)
        auction.set_buyer_on_completion()
        

