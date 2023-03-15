from abc import ABC
from rest_framework import serializers
from library.authors.models import Author
from python_models import Author, Article, Book, Biography


def validate_birthday_year(value):
    if value < 0:
        raise serializers.ValidationError('Год рождения не может быть отрицательным')
    return value


class AuthorSerializer(serializers.Serializer, ABC):
    class Meta:
        model = Author
        fields = '__all__'


class BiographySerializer(serializers.Serializer, ABC):
    class Meta:
        model = Biography
        fields = '__all__'


class BookSerializer(serializers.Serializer, ABC):
    class Meta:
        model = Book
        fields = '__all__'


class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = Article
        fields = '__all__'

    def validate(self, attrs):
        if attrs['name'] == 'Пушкин' and attrs['birthday_year'] != 1799:
            raise serializers.ValidationError('Неверный год рождения Пушкина')
        return attrs

    def create(self, validated_data):
        return Author(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
        return instance


author1 = Author('Грин', 1880)
serializer = AuthorSerializer(author1)
print(serializer.data)  # {'name': 'Грин', 'birthday_year': 1880}

biography = Biography('Текст биографии', author1)
serializer = BiographySerializer(biography)
print(serializer.data)  # {'text': 'Текст биографии', 'author':OrderedDict([('name', 'Грин'), ('birthday_year', 1880)])}

article = Article('Некоторая статья', author1)
serializer = ArticleSerializer(article)
print(
    serializer.data)  # {'name': 'Некоторая статья', 'author':OrderedDict([('name', 'Грин'), ('birthday_year', 1880)])}

author2 = Author('Пушкин', 1799)
book = Book('Некоторая книга', [author1, author2])  # {'name': 'Некоторая книга','authors': [OrderedDict([('name',
# 'Грин'), ('birthday_year', 1880)]),OrderedDict([('name', 'Пушкин'), ('birthday_year', 1799)])]}

serializer = BookSerializer(book)

print(serializer.data)

print(serializer.errors)

serializer.is_valid(raise_exception=True)
