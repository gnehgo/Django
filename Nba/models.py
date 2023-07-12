from django.db import models


class Player(models.Model):
    name = models.CharField(db_column='Name', max_length=50)
    jersey = models.IntegerField(db_column='Jersey')
    team = models.CharField(db_column='Team', max_length=50)
    nationality = models.CharField(db_column='Nationality', max_length=50)

    class Meta:
        db_table = 'Player'

    def __str__(self):
        return self.name


class Stat(models.Model):
    number = models.OneToOneField(Player, models.DO_NOTHING, db_column='Number', primary_key=True)
    name = models.CharField(db_column='Name', max_length=50)
    wins = models.IntegerField(db_column='Wins')
    points = models.IntegerField(db_column='Points')
    rebounds = models.IntegerField(db_column='Rebounds')
    assists = models.IntegerField(db_column='Assists')

    class Meta:
        db_table = 'Stat'

    def __str__(self):
        return self.name + " " + str(self.points) + " " + str(self.rebounds) + " " + str(self.assists)


class GameStat(models.Model):
        data = models.DateField(db_column='Date')
        team1 = models.CharField(db_column='team1', max_length=50)
        team2 = models.CharField(db_column='team2', max_length=50)
        score = models.CharField(db_column='score', max_length=50)


        class Meta:
            db_table = 'GameStat'
