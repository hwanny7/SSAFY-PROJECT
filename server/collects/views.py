from django.shortcuts import render

# Create your views here.
# def test(request):
#     collection = Collection.objects.get(pk=1)
#     choices = collection.movie_choice_set.all()

#     collection_json = []
#     for choice in choices:
#         a = {
#             'title': collection.title,
#             'content': collection.content,
#             'movie' : choice.movie_id,
#             'movies content': choice.content,
#         }
        
#         collection_json.append(a)
#     print(collection_json)
#     return JsonResponse(collection_json, safe=False)