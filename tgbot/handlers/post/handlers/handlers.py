from email.mime import image
from pyparsing import empty
from telegram.update import Update
from telegram import CallbackQuery, InlineQueryResultArticle, InputMessageContent, InputTextMessageContent
from post.models import Post

def post_search(update: Update, context: CallbackQuery):

    search_field = update.inline_query.query

    queryset = Post.objects.filter(title__icontains=search_field)
    for q in queryset:
        post_id = q.id
        post_title = q.title
        post_description = q.description
        post_img_url = q.image_url

    results = []
    
    results.append(
        InlineQueryResultArticle(
            id = post_id,
            title = post_title,
            description = post_description,
            thumb_url = post_img_url,
            input_message_content= InputTextMessageContent(
                f'Post Title: {post_title} \nDescription: {post_description}'
                )
    ))
    # else:
    #     results.append(
    #         InlineQueryResultArticle(
    #             id = 1,
    #             title = '????',
    #             description='Not found',
    #             thumb_url = 'https://fakeimg.pl/300/?text=book%202',
    #             input_message_content= InputTextMessageContent(
    #                 'Not found!'
    #                 )
    #         )
    #     )

    update.inline_query.answer(results) 
    