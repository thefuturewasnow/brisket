from django.db import models
from django.contrib.localflavor.us.models import USStateField
from simplepay.models import Transaction, DonationButton
from django.conf import settings
import hashlib
from django.db.models.signals import post_save

BATCH_STATUS_CHOICES = (
    ('not_processed', 'Not processed'),
    ('processing', 'Processing'),
    ('processed', 'Processed'),
    ('at_printer', 'At printer'),
    ('printed', 'Printed'),
    ('mailed', 'Mailed'),
)
class Batch(models.Model):
    name = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=24, choices=BATCH_STATUS_CHOICES, default='not_processed')
    
    def save(self):
        new_record = not self.pk
        
        super(Batch, self).save()
        
        if new_record:
            for card in Postcard.objects.filter(status='paid', batch=None):
                card.batch = self
                card.save()
        
        if self.status == 'mailed':
            for card in self.postcard_set.all():
                card.status = 'sent'
                card.save()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'batches'

POSTCARD_STATUS_CHOICES = (
    ('not_paid', 'Not paid'),
    ('paid', 'Paid'),
    ('payment_failed', 'Payment failed'),
    ('sent', 'Postcard sent'),
    ('send_failed', 'Send failed')
)
class Postcard(models.Model):
    td_id = models.CharField(max_length=32, verbose_name="Candidate")
    location = models.CharField(max_length=12, verbose_name="District", blank=True)
    num_candidates = models.PositiveIntegerField(verbose_name="Number of Candidates", choices=((1, '1'), (2, '2')))
    
    sender_name = models.CharField(max_length=128, verbose_name="Sender Name")
    sender_address1 = models.CharField(max_length=128, verbose_name="Sender Address Line 1")
    sender_address2 = models.CharField(max_length=128, verbose_name="Sender Address Line 2", blank=True)
    sender_city = models.CharField(max_length=128, verbose_name="Sender City")
    sender_state = USStateField(verbose_name="Sender State")
    sender_zip = models.CharField(max_length=10, verbose_name="Sender Zip")
    
    recipient_name = models.CharField(max_length=128, verbose_name="Recipient Name")
    recipient_address1 = models.CharField(max_length=128, verbose_name="Recipient Address Line 1")
    recipient_address2 = models.CharField(max_length=128, verbose_name="Recipient Address Line 2", blank=True)
    recipient_city = models.CharField(max_length=128, verbose_name="Recipient City")
    recipient_state = USStateField(verbose_name="Recipient State")
    recipient_zip = models.CharField(max_length=10, verbose_name="Recipient Zip")
    
    message = models.TextField(default="Check out this campaign finance information from InfluenceExplorer.com.")
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=24, choices=POSTCARD_STATUS_CHOICES, default='not_paid')
    
    amazon_transaction = models.ForeignKey(Transaction, null=True, blank=True)
    pm_id = models.CharField(max_length=24, verbose_name="PostalMethods ID", blank=True)
    
    batch = models.ForeignKey(Batch, null=True, blank=True)
    
    def __str__(self):
        return 'Postcard to %s in %s, %s' % (self.recipient_name, self.recipient_city, self.recipient_state)
    
    def get_code(self):
        return hashlib.md5('%s%s' % (self.pk, settings.SECRET_KEY)).hexdigest()[:5]
    
    def save(self):
        if not self.amazon_transaction:
            transaction = Transaction(button=DonationButton.objects.get(pk=1))
            transaction.save()
            self.amazon_transaction = transaction
        super(Postcard, self).save()

def update_card(sender, **kwargs):
    if 'instance' in kwargs:
        instance = kwargs['instance']
    else:
        return
    if instance.status in ['PS', 'PI']:
        cards = Postcard.objects.filter(amazon_transaction=instance)
        if cards:
            cards[0].status = 'paid'
            cards[0].save()

post_save.connect(update_card, sender=Transaction)