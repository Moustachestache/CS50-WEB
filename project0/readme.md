# NOTES

Your website must meet the following requirements:

On the Google Image Search page, the user should be able to type in a query, click a search button, and be taken to the Google Image search results for that page.

On the Google Advanced Search page, the user should be able to provide input for the following four fields (taken from Google’s own advanced search options)

Find pages with… “all these words:”

Find pages with… “this exact word or phrase:”

Find pages with… “any of these words:”

Find pages with… “none of these words:”

Like Google’s own Advanced Search page, the four options should be stacked vertically, and all of the text fields should be left aligned.

Consistent with Google’s own CSS, the “Advanced Search” button should be blue with white text.

When the “Advanced Search” button is clicked, the user should be taken to the search results page for their given query.

Add an “I’m Feeling Lucky” button to the main Google Search page. Consistent with Google’s own behavior, clicking this link should take users directly to the first Google search result for the query, bypassing the normal results page.

You may encounter a redirect notice when using the “I’m Feeling Lucky” button. Not to worry! This is an expected consequence of a security feature implemented by Google.

The CSS you write should resemble Google’s own aesthetics.


Hints

To determine what the parameter names should be, you’re welcome to experiment with making Google searches, and looking at the resulting URL. It may also be helpful to open the “Network” inspector (accessible in Google Chrome by choosing View -> Developer -> Developer Tools) to view details about requests your browser makes to Google.

Any <input> element (whether its type is text, submit, number, or something else entirely) can have name and value attributes that will become GET parameters when a form is submitted.

You may also find it helpful to look at Google’s own HTML to answer these questions. In most browsers, you can control-click or right-click on a page and choose “View Page Source” to view the page’s underlying HTML.

To include an input field in a form that users cannot see or modify, you can use a “hidden” input field.

------

https://www.google.com/search
    ?sca_esv=6c97737eef5bcf41
    &sxsrf=ADLYWILaEgURvYaLEkT4y4bQhPc19yrvkQ:1720094550476
    &q=hehe
    &udm=2
    &fbs=AEQNmHeE4
    &sa=X
    &ved=2ahUKEwi526TFq42HAxX1TKQEHaznCG4QtKgLegQIGxAB
    &biw=1135
    &bih=961
    &dpr=1

https://www.google.com/search
    ?q=asdasdasdasd
    &sca_esv=6c97737eef5bcf41
    &sxsrf=ADLYWII_MMKiBqM094363591
    &source=hp
    &biw=1135&bih=961
    &ei=m46GZpCXIu-ghbIP6MmqyAY
    &iflsig=AL9hbdzStWIvSYg0n7n3S9SU6b
    &ved=0ahUKEwjQ0JTsqo2HAxVvUEECAc
    &uact=5
    &oq=asdasdasdasd
    &gs_lp=EgNpbWciDGFzZGFzZGFzZGFzZDIHEAsQMYgwEYigXCAgQQABgemAMLkgcEMTEuMaAHozM
    &sclient=img
    &udm=2

https://www.google.com/search
    ?q=test
    &btnI=J%27ai+de+la+chance
    &sca_esv=e8adb66333914b08
    &sxsrf=ADLYWIKOh2e3-w-SkkSjDB8C0EBrk9jSeQ%3A1720095831977
    &source=hp
    &ei=V5SGZtbOOYqUhbIPqoWNkAw
    &iflsig=AL9hbdgAAAAAZoaiZ-f5KsAz0H4mXoo3vKjZzYIoHGje