from django.db import models

class Topic(models.Model):
    """ Um assunto sobre qual o usuário está aprendendo."""

    text = models.CharField(max_length = 200) # max_length = 200 define o tamanho que o campo vai ter em termos de caracteres
    date_added = models.DateTimeField(auto_now_add=True) # Registra a data e hora que o campo text foi resgistrado

    def __str__(self):
        """ Devolve uma representação em string do modelo. """
        return self.text

class Entry(models.Model):
    """Algo específico aprendido sobre o assunto"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE) # Vincula uma chave ao Topic, uma vez que o models.CASCADE e inserido no on_delete se o Topic for apagado o Entry vinculado a ele também será apagado.
    text = models.TextField() # Campo de texto sem limitação maxima de caracteres
    date_added = models.DateTimeField(auto_now_add=True) # Registra a data e hora que o campo text foi resgistrado

    class Meta:
        verbose_name_plural = "Entries"
        """Uma classe que seta a versão do nome da classe no plural"""

    def __str__(self):
        """ Devolve uma representação em string do modelo. """
        return self.text[:50] + '...' # Retorna os 50 primeiros caracteres e add "..." para indicar que ainda há mais texto.
    
