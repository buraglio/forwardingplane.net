+++
title = "{{ replace .TranslationBaseName "-" " " | title }}"
date = "{{ now.Format "2006-01-02T15:04:05-07:00" }}"
location = ""
start_date = "{{ (now.AddDate 0 0 1).Format "2006-01-02T15:04:05-07:00" }}"
#doors_open = "{{ (now.AddDate 0 0 1).Format "2006-01-02T15:04:05-07:00" }}"
end_date = "{{ (now.AddDate 0 0 2).Format "2006-01-02T15:04:05-07:00" }}"
hide_authorbox = true
disable_comments = true
draft = true
+++
