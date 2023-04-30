from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    name = models.CharField(max_length=255)
    qr_exp_mins = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    teacher = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="lectures"
    )

    def __str__(self):
        return f"{self.date} {self.teacher}"


class Attendance(models.Model):
    student = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    teacher = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="announcements"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(
                fields=[
                    "teacher_id",
                    "course_id",
                ]
            ),
        ]
