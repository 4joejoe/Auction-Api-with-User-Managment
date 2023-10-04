from rest_framework import serializers

from auction.models import Auction, Bid

class AuctionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = "__all__"
    
    def save(self):
        auction = Auction(end_time=self.validated_data['end_time'],start_price=self.validated_data['start_price'],item_name = self.validated_data['item_name'])
        auction.save()
        return auction
    
class AuctionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = "__all__"

class BidCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = "__all__"
    
    def save(self):
        bid = Bid(auction=self.validated_data['auction'],user=self.validated_data['user'],amount = self.validated_data['amount'])

        bid.save()
        return bid
class BidViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = "__all__"