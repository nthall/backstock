(function(backstock, document, $, opts) {
  var url: "//backstock.nthall.com/get";
  var defaults = {
    target: 'body',
    tags: null,
    opts: {
      background-size: 'cover',
    },
  };

  // double-check for jQ
  if (Object.getOwnPropertyNames($).length === 0) {
    head = document.getElementsByTagName('head')[0];
    jq = document.createElement('script');
    jq.src = "//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.min.js";
    jq.type = "text/javascript";
    head.appendChild(jq);
  }

  // merge opts & defaults
  opts = $.extend(defaults, opts);

  $(document).ready(function (url, opts) {
    //todo: add checks for more options and use them :D
    //todo: add either console.log or a small element with some credit & link to original NOS post

    $.get(url, function(response) {
      $(opts.target).css('background-image', 'url(' + response.src + ')')
        .css(opts.css);
    });

})(window.backstock = window.backstock || {}, document, jQuery, {});
