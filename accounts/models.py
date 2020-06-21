from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver


class MyUserManager(BaseUserManager):
	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError("Email must be set")
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError("Superuser must have is_staff=True")

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True')

		return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=254, unique=True, null=False)
	is_staff = models.BooleanField(
		ugettext_lazy('Staff Status'),
		default=False,
		help_text=ugettext_lazy('Designates whether the user can log in this site')
		)
	is_active = models.BooleanField(
		ugettext_lazy('Active'),
		default=True,
		help_text=ugettext_lazy('Designate whether this user should be treated as 		active. unselect this instead of deleting accounts')
		)
	USERNAME_FIELD = 'email'
	objects = MyUserManager()

	def __str__(self):
		return self.email

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

class UserProfile(models.Model):

	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	username = models.CharField(max_length=254,blank=True)
	first_name = models.CharField(max_length=100, blank=True)
	last_name = models.CharField(max_length=100, blank=True)
	profile_image = models.ImageField(upload_to='profile/', blank=True)
	address = models.TextField(blank=True)
	zipcode = models.CharField(max_length=10, blank=True)
	city = models.CharField(max_length=50, blank=True)
	country = models.CharField(max_length=50, blank=True)
	contact_no = models.CharField(max_length=15, blank=True)
	joined_at = models.DateField( auto_now_add=True)
	upated_at = models.DateField( auto_now=True)

	class Meta:
		verbose_name = "UserProfile"
		verbose_name_plural = "UserProfiles"

	def __str__(self):
		return self.username + "'s profile"

	@receiver(post_save, sender=User)
	def create_profile(sender, instance, created, **kwargs):
		if created:
			UserProfile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_profile(sender, instance, **kwargs):
		instance.profile.save()

	def get_absolute_url(self):
		return reverse("UserProfile_detail", kwargs={"pk": self.pk})