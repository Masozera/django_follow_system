from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
   
    following = models.ManyToManyField('self',through='Contact',related_name='followers',symmetrical=False)
    

    # In the preceding example, you tell Django to use your custom intermediary model 
    # for the relationship by adding through=Contact to the ManyToManyField. This 
    # is a many-to-many relationship from the User model to itself; you refer to 'self'
    # in the ManyToManyField field to create a relationship to the same model.

    # When you need additional fields in a many-to-many relationship, 
    # create a custom model with a ForeignKey for each side of the 
    # relationship. Add a ManyToManyField in one of the related 
    # models and indicate to Django that your intermediary model 
    # should be used by including it in the through parameter

    def get_absolute_url(self):
        return reverse('followapp:user_detail',args=[self.username,])

class Contact(models.Model): #  the Contact model that you will use for user relationships.... intermediary model is necessary when you want to store additional information for the relationship, for example, the date when the relationship was created, or a field that describes the nature of the relationship.
    user_from = models.ForeignKey(CustomUser,related_name='rel_from_set',on_delete=models.CASCADE) # A ForeignKey for the user who creates the relationship
    user_to = models.ForeignKey(CustomUser,related_name='rel_to_set',on_delete=models.CASCADE)     # A ForeignKey for the user being followed
    created = models.DateTimeField(auto_now_add=True,db_index=True)                                # A DateTimeField field with auto_now_add=True to store the time when the relationship was created
    # A database index is automatically created on the ForeignKey fields. You use db_
    # index=True to create a database index for the created field. This will improve 
    # query performance when ordering QuerySets by this field.

    #The related managers, rel_from_set and rel_to_set, will return a QuerySet for the Contact model


    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'

#CustomUser.add_to_class('following',models.ManyToManyField('self',through=Contact,related_name='followers',symmetrical=False))
