from django.contrib import admin

# Register your models here.
from models import ApplicationForm


# admin.site.disable_action('delete_selected')

@admin.register(ApplicationForm)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'email',
        'position_sought',
        'posted_date', 
        'status',
     )
    readonly_fields = ['get_readonly_fields']
    actions = ['make_approve','make_reject']

    def get_readonly_fields(self, request, obj=None):
        """
        Make all fields as ready only while viewing it in admin dashboard
        """

        if obj:
            self.readonly_fields = [field.name for field in obj.__class__._meta.fields]
        return self.readonly_fields

    def make_approve(self, request, queryset):
        """
        Function to update the status as Approved
        """
        rows = queryset.update(status='Approved')
        self.status_message(request, rows, 'Approved')
    make_approve.short_description = 'Approve'


    def make_reject(self, request, queryset):
        """
        Function to update the status as Rejected
        """

        rows = queryset.update(status='Rejected')
        self.status_message(request, rows, 'Rejected')
    make_reject.short_description = 'Reject'

    def status_message(self, request, rows_updated, status):
        """
        Update status message after updating status
        """

        if rows_updated == 1:
            message_bit = "1 application was"
        else:
            message_bit = "%s applications were" % rows_updated
        self.message_user(request, "%s successfully %s ." % (message_bit, status))

