n = int(input())
forum = {}
themes = {}
message_counter = 0
theme_counter = 0
last_was_message = False

while message_counter != n:
    message = input()
    if message == '0':
        new_theme = True
        theme_counter += 1
    else:
        if new_theme:
            new_theme = False
            is_last_theme = True
            last_theme_counter = theme_counter
            last_theme = message
            forum[message] = set()
            themes[theme_counter] = message
        else:
            if is_last_theme:
                message_counter += 1
                forum[last_theme].add(message_counter)
                is_last_theme = False
            else:
                if message.isdigit():
                    message_counter += 1
                    for last_theme_info, messages in forum.items():
                        if int(message) in messages:
                            forum[last_theme_info].add(message_counter)
                            break

max_messages = max(forum, key=lambda x: len(forum.get(x)))

for index, name in sorted(themes.items()):
    if max_messages == name:
        print(name)
        break
