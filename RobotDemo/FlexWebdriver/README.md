Demo of FlexPilot plus RF-Selenium2Library js API
=================================================

* Build the Flex application under test with [*FlexPilot.swf*](https://code.google.com/p/robotframework-seleniumlibrary/wiki/FlexTesting)   (https://github.com/mde/flex-pilot/wiki/api) (https://github.com/mde/flex-pilot/downloads)

* Start the application
`python -m SimpleHTTPServer 8000`

* Open `index.html` in Firefox with *Flash debug version*

* use FlashFirebug to inspect element locator, then verify in Firebug Console (which API can be out into test library):
<pre>
document.loginApp.fp_type({'name':'username_field', 'text':'abc'})
document.loginApp.fp_click({'name':'login_button'})
</pre>

* When run `Execute Javascript` keyword of Seleniu2Library, better to add `Set Selenium Speed  1` before it, to wait the Flex completely loaded, otherwise, the js API may not be ready.
<pre>
    Open Browser    http://127.0.0.1:8000/
    Set Selenium Speed  1
    Wait Until Page Contains Element    id=loginApp
    ${ret}  Execute Javascript  window.document.loginApp.fp_type({name:'username_field', text:'abc'});
</pre>

* BTW, if want to load extensions, then update Selenium2Library\keywords\_browsermanagement.py with:
<pre>
   def _make_ff(self , remote , desired_capabilites , profile_dir):
        if not profile_dir: profile_dir = FIREFOX_PROFILE_DIR
        profile = webdriver.FirefoxProfile(profile_dir)
        profile.add_extension('D:/python/Lib/site-packages/Selenium2Library/resources/firefoxprofile/extensions/firebug-1.12.1.xpi'); #
  </pre>