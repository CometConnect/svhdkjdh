$(document).ready(() => {
    $('#button').click(() => {
        let text_value = $('#text').val();
        let input_text = { data: text_value };
        $.ajax({
            type: 'POST',
            url: '/getemotion',
            data: JSON.stringify(input_text),
            dataType: 'json',
            contentType: 'application/json',
            success: (result) => {
                const { emotion, url } = result;
                console.log(url)
                $("#sentiment").text(emotion);
                $("#emoji").attr("src", url);
            },
            error: (result) => {
                console.error(result);
            }
        })
        $('#text').val("");
    })

})