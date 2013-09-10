Demo of FlexPilot with js API
=============================

* Encapsult [FlexPilot.swf](https://code.google.com/p/robotframework-seleniumlibrary/wiki/FlexTesting)   (https://github.com/mde/flex-pilot/wiki/api) (https://github.com/mde/flex-pilot/downloads)

* Start the demo
`python -m SimpleHTTPServer 8000`

* Open `index.html` in Firefox with Flash debug version

* use FlashFirebug to inspect element locator, then verify in Firebug Console (which API can be test library):

<pre>
document.loginApp.fp_type({'name':'username_field', 'text':'abc'})
document.loginApp.fp_click({'name':'login_button'})
</pre>