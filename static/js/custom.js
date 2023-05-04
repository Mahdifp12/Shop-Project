function sendArticleComment() {
    var comment = $("#commentText").val();

    $.get("/articles/add-article-comment", {
        ArticleComment : comment,
        ArticleId : 9,
        ArticleParent : null
    }).then(res => {
        console.log(res);
    });
}