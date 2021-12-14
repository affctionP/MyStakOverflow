from django.db.models.fields.files import FileField


class AudioField(FileField):
    
    def __init__(self, *args, **kwargs):
        """Get allowed file extension type (ex. mp3, wav)
        ext_whitelist = kwargs.pop("ext_whitelist", tuple())
        self.ext_whitelist = [i.lower() for i in ext_whitelist]"""
        super(AudioField, self).__init__(*args, **kwargs)
        
    def formfield(self, **kwargs):
        '''Specify form field and widget to be used on the forms
        from .widgets import AdminAudioFileWidget
        from audiofield.forms import AudioFormField
        kwargs['widget'] = AdminAudioFileWidget
        kwargs['form_class'] = AudioFormField'''

        return super(AudioField, self).formfield(**kwargs)
