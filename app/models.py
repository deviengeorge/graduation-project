from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    date = models.DateTimeField()
    teacher = models.ForeignKey(
        "authentication.User",
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lectures"
    )

    def __str__(self):
        return f"{self.date} {self.teacher}"


class Attendance(models.Model):
    student = models.ForeignKey(
        "authentication.User",
        on_delete=models.CASCADE
    )
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


# class Annoncement
