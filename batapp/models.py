from django.db import models

class Album(models.Model):
  # For the pike number, we keep this as a character and not an int.
  # The reason is now we can have it as 'NA" for non-pike Buckethead albums.
  # And I don't see us doing much math on these numbers.
  pike_number = models.CharField(max_length=200)
  
  # Just a text field to handle the name of the album
  album_name = models.CharField(max_length=200)
  
  # This will give us a drop down box in the admin inteface with these choices.
  # This is done in a key->value type structure.  In this case, the "value"
  # is what gets displayed for each entry in the drop down box.
  
  # A note about the dictionaries.  The admin interface was pulling the "value" aka right
  # side of the choices there.  However the "key" or left side it what is stored in the database.
  # So since I have very little control with the django hooks into html files, I changed the
  # key and vaule to be the same thing, so it shows up correctly both in the admin interface and
  # the html files that pull the data.
  
  album_pace_choices = (
    ('slow', 'slow'),
    ('medium', 'medium'),
    ('fast', 'fast'),
  )
  
  album_pace = models.CharField(max_length=15,
				choices=album_pace_choices,
				default='medium')
  
  
  # Now lets define the heaviness.  This is will use a similar structure to 
  # the album_pace listed above, but with different values.
  album_heaviness_choices = (
    ('soft', 'soft'),
    ('medium', 'medium'),
    ('heavy', 'heavy'),
    ('brutal', 'brutal'),
  )
  
  album_heaviness = models.CharField(max_length=15,
				  choices=album_heaviness_choices,
				  default='medium')
 
  # Lets keep this a generic text / free form field.
  album_genre = models.CharField(max_length=200)
  
  # Now  for the fun part.  Lets see if we can do a variable list 
  # for the track list. 
  # Actually lets just do a textarea:
  album_tracklist = models.TextField(max_length=1024)
  
  
  # Not sure if this is good / necessary / makes sense...
  # If at the console, and you do a Album.objects.all()
  # This will make it return an album name I believe 
  # instead of a generic "Album Object"
  def __unicode__(self):
    return self.album_name


  
  
