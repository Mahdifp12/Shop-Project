function sendArticleComment(articleId) {
    var comment = $("#commentText").val();

    $.get("/articles/add-article-comment", {
        article_comment : comment,
        article_id: articleId,
        parent_id : null
    }).then(res => {
        console.log(res);
    });
}