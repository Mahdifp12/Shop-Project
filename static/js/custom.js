function sendArticleComment() {
    // console.log("submit article comment");
    var comment = $('#commentText').val();

    $.get("articles/add-article-comment", {
        ArticleComment : comment
    }).then(res => {
        console.log(res);
    })
}