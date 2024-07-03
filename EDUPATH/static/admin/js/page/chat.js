"use strict";

$.chatCtrl = function (element, chat) {
  var chat = $.extend({
    position: 'chat-right',
    text: '',
    time: moment(new Date().toISOString()).format('hh:mm'),
    picture: '',
    type: 'text', // or typing
    timeout: 0,
    onShow: function () { }
  }, chat);

  var target = $(element),
    element = '<div class="chat-item ' + chat.position + '" style="display:none">' +
      '<img src="' + chat.picture + '">' +
      '<div class="chat-details">' +
      '<div class="chat-text">' + chat.text + '</div>' +
      '<div class="chat-time">' + chat.time + '</div>' +
      '</div>' +
      '</div>',
    typing_element = '<div class="chat-item chat-left chat-typing" style="display:none">' +
      '<img src="' + chat.picture + '">' +
      '<div class="chat-details">' +
      '<div class="chat-text"><i></i></div>' +
      '</div>' +
      '</div>';

  var append_element = element;
  if (chat.type == 'typing') {
    append_element = typing_element;
  }

  if (chat.timeout > 0) {
    setTimeout(function () {
      target.find('.chat-content').append($(append_element).fadeIn());
    }, chat.timeout);
  } else {
    target.find('.chat-content').append($(append_element).fadeIn());
  }

  var target_height = 0;
  target.find('.chat-content .chat-item').each(function () {
    target_height += $(this).outerHeight();
  });
  setTimeout(function () {
    target.find('.chat-content').scrollTop(target_height, -1);
  }, 100);
  chat.onShow.call(this, append_element);
}

if ($("#chat-scroll").length) {
  $("#chat-scroll").css({
    height: 450
  }).niceScroll();
}

if ($(".chat-content").length) {
  $(".chat-content").niceScroll({
    cursoropacitymin: .3,
    cursoropacitymax: .8,
  });
  $('.chat-content').getNiceScroll(0).doScrollTop($('.chat-content').height());
}

var chats = [
  {
    text: 'How can I help you in your study?',
    position: 'left'
  },
];

for (var i = 0; i < chats.length; i++) {
  var type = 'text';
  if (chats[i].typing != undefined) type = 'typing';
  $.chatCtrl('#mychatbox', {
    text: (chats[i].text != undefined ? chats[i].text : ''),
    picture: (chats[i].position == 'left' ? 'https://webfinge.space/images/user/user-02.png' : 'https://webfinge.space/images/user/user-01.png'),
    position: 'chat-' + chats[i].position,
    type: type
  });
}

const API_KEY = 'bd1c44bd-f68c-4e19-a221-b922e6a75cda'; // Replace with your actual API key (store securely)
const url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium&language=en";

async function chat(question) {
  const payload = {
    "enable_google_results": "true",
    "enable_memory": false,
    "input_text": question,
  };

  const headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": API_KEY,
  };

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error(`API request failed with status: ${response.status}`);
    }

    const data = await response.json();
    console.log(data); // Process the response data here (message or other relevant fields)
    return data; // Optionally return the response data for further use
  } catch (error) {
    console.error('Error:', error);
    return null; // Indicate an error (optional)
  }
}

$("#chat-form").submit(async function (event) {
  event.preventDefault();
  var me = $(this);

  if (me.find('input').val().trim().length > 0) {
    var question = me.find('input').val();

    // Display user's message
    $.chatCtrl('#mychatbox', {
      text: question,
      picture: 'https://webfinge.space/images/user/user-01.png',
      position: 'chat-right'
    });

    me.find('input').val('');

    // Display typing indicator
    var typingIndicator = {
      typing: true,
      picture: 'https://webfinge.space/images/user/user-02.png',
      position: 'left',
      type: 'typing'
    };
    $.chatCtrl('#mychatbox', typingIndicator);

    // Call the API and display the response
    const response = await chat(question);

    // Remove typing indicator
    $('#mychatbox .chat-typing').remove();

    if (response && response.message) {
      $.chatCtrl('#mychatbox', {
        text: response.message,
        picture: 'https://webfinge.space/images/user/user-02.png',
        position: 'chat-left'
      });
    }
  }
  return false;
});
