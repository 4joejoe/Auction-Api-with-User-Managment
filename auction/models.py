import datetime
from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
from django.db import models
from django.utils import timezone

from users.models import MyUser

# Create your models here.
class Auction(models.Model):
    auction_uuid = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_name = models.CharField(max_length=255)
    top_bid = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    top_bidder = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='top_bids')
    sold_price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    buyer = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='buyer')
    # created_by 
    def __str__(self):
        return f"{self.item_name}"
    
    def update_top_bid(self, top_bidder, top_bid):
        self.top_bidder = top_bidder
        self.top_bid = top_bid
        self.save()

    def set_buyer_on_completion(self,*args,**kwargs):
        if self.end_time and self.end_time<= timezone.now():
            self.buyer = self.top_bidder
            self.save(update_fields=['buyer'])
            return True
        else:
            return False
    
    

class Bid(models.Model):
    bid_uuid = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    auction = models.ForeignKey(Auction, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bid of {self.amount} by {self.user.username} for {self.auction.item_name}"
