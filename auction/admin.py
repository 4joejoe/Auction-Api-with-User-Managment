from django.contrib import admin

from auction.models import Auction, Bid

# Register your models here.
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'top_bid', 'start_price','end_time','sold_price')
    # list_filter = ('top_bid','start_price','sold_price','end_time','start_time')
    # readonly_fields = ('top_bid','start_price','sold_price','end_time','start_time')
    
class BidAdmin(admin.ModelAdmin):
    list_display = ('auction', 'user', 'amount','bid_datetime')
    # list_filter = ('user','amount','bid_datetime','auction')
    # readonly_fields = ('auction','user','amount','end_time','bid_datetime')

admin.site.register(Auction,AuctionAdmin)
admin.site.register(Bid,BidAdmin)