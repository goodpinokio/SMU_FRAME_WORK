from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    #이미지 저장하는 경로
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/',blank=True) 
    #파일 저장하는 경로
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    #해당 데이터가 생성된 날짜와 시간을 자동으로 저장합니다.
    created_at = models.DateTimeField(auto_now_add=True)
    
    #해당 데이터가 마지막으로 수정된 날짜와 시간을 자동으로 저장합니다.
    updated_at = models.DateTimeField(auto_now=True)
    # author: 추후 작성 예정

#__str__() 메소드는 해당 객체를 출력할 때 출력될 문자열을 반환합니다. 
# 위 코드에서는 [해당 객체의 pk] 제목 형식의 문자열을 반환하도록 구현되어 있습니다.
    def __str__(self):
        return f'[{self.pk}] {self.title}'
 
 #메소드는 해당 Post 객체의 상세 페이지 URL을 반환하는 메소드입니다. 위 코드에서는 /blog/<게시물번호>/ 
 #형태로 반환하도록 구현되어 있습니다. 이를 urls.py와 연결하여 상세 페이지를 생성할 수 있습니다.
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'