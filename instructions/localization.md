# Internationalization of Python skill

i18n and l10n are [supported](https://docs.python.org/3.6/library/i18n.html) by the standard python library module `gettext`. However, to make the skill compatible with i18n, we need to follow these steps, as mentioned in the [guide](https://docs.python.org/3.6/library/gettext.html#internationalizing-your-programs-and-modules) : 


1. Prepare your program or module by specially marking translatable strings
2. Run a suite of tools over your marked files to generate raw messages catalogs
3. Create language specific translations of the message catalogs
4. Use the gettext module so that message strings are properly translated


These steps are detailed below.

## Step 1 : Preparing the skill to extract data translatable strings

Mark all the strings that needs to be translated with a special function **`_()`**. This function is used by the tools, to figure out all the data that needs to be extracted for translation.For example, consider your `skill.py` file contains these messages

```
# Contents of skill.py

skill_name = _("Test skill")
welcome_message = _("Welcome. I have more info on eggplant")
```

Remember to exclude string formatting in the underlying string, since the context of the string formatting might change with different languages.

```
# Before i18n marking
custom_hello_message = "Hi " + name + ". How are you doing?"

# Incorrect i18n marking
custom_hello_message = _("Hi ") + name + _(". How are you doing?")

# Correct i18n marking
custom_hello_message = _("Hi {}. How are you doing?").format(name)
```

## Step 2 : Run a tool to extract the messages and generate message catalog

Some distributions of the standard library provide a python program 'pygettext.py', which processes the python program and extract a list of strings to translate. However, it has been observed that not all distributions (particularly in Unix) has this file installed along with the Python standard installation[[1](https://quip-amazon.com/5hH1AOMs2xxq#ZKZ9CAFqwSE)]. For this purpose, and as mentioned in the documentation, we use a third party library called '[Babel](http://babel.pocoo.org/en/latest/cmdline.html)'. 

Run the following commands to install babel and extract message strings from your skill file 'skill.py'.

```
pip install babel
pybabel extract skill.py -o skill.pot
```

This creates a `portable object template (.pot)` file called **skill.pot**, which contains all the messages that needs to be translated and some metadata regarding the locale info. For eg: following is the pot file for the skill containing `skill_name`, `welcome_message` and `custom_hello_message` strings marked for translation.

```
# Translations template for PROJECT.
# Copyright (C) 2018 ORGANIZATION
# This file is distributed under the same license as the PROJECT project.
# FIRST AUTHOR <EMAIL@ADDRESS>, 2018.
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: PROJECT VERSION\n"
"Report-Msgid-Bugs-To: EMAIL@ADDRESS\n"
"POT-Creation-Date: 2018-09-05 09:33-0700\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=utf-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Generated-By: Babel 2.6.0\n"

#: skill.py:1
msgid "Test skill"
msgstr ""

#: skill.py:2
msgid "Welcome. I have more info on eggplant"
msgstr ""

#: skill.py:3
msgid "Hi {}.How are you doing?"
msgstr ""


```

As can be observed, the POT file is a simple file with msgid and msgstr mappings, with msgid mapping from python program to msgstr translated value. This file can be used as a template to fill in translations for different locales.

## Step 3 : Create language specific translations

For this example, we show example message catalogs for English (GB) & Spanish. Create a locales directory under folder where the skill.py is present. This will host all the message catalog files. For each translation, create a folder with the locale code (for exact locale code check the [documentation](https://developer.amazon.com/docs/custom-skills/develop-skills-in-multiple-languages.html)) and a folder in it by name `'LC_MESSAGES'` (This is the standard directory name where the python standard library can check for translations. Create the po files for the locales using the `init` command as follows

```
pybabel init -i skill.pot -l en_GB -o locales/en-GB/LC_MESSAGES/skill.po
pybabel init -i skill.pot -l es_ES -o locales/es-ES/LC_MESSAGES/skill.po
```


Your directory structure should look similar to the following

```
parent_dir
     - skill.py
     - skill.pot
     - locales
            - en-GB
                - LC_MESSAGES
                    - skill.po
            - es-ES
                - LC_MESSAGES
                    - skill.po
```

Update the skill.po for both locales, to provide translated message strings. For example, following are the `en-GB/LC_MESSAGES/skill.po` and `es-ES/LC_MESSAGES/skill.po` files

### en-gb/lc_messages/skill.po

```
# English (United Kingdom) translations for PROJECT.
# Copyright (C) 2018 ORGANIZATION
# This file is distributed under the same license as the PROJECT project.
# FIRST AUTHOR <EMAIL@ADDRESS>, 2018.
#
msgid ""
msgstr ""
"Project-Id-Version: PROJECT VERSION\n"
"Report-Msgid-Bugs-To: EMAIL@ADDRESS\n"
"POT-Creation-Date: 2018-09-05 09:33-0700\n"
"PO-Revision-Date: 2018-09-05 10:50-0700\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language: en_GB\n"
"Language-Team: en_GB <LL@li.org>\n"
"Plural-Forms: nplurals=2; plural=(n != 1)\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=utf-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Generated-By: Babel 2.6.0\n"

#: skill.py:1
msgid "Test skill"
msgstr ""

#: skill.py:2
msgid "Welcome. I have more info on eggplant"
msgstr "Welcome. i have more info on aubergine"

#: skill.py:3
msgid "Hi {}.How are you doing?"
msgstr "Hi {}.How are you doing?"

```

### es-es/lc_messages/skill.po

```
# Spanish (Spain) translations for PROJECT.
# Copyright (C) 2018 ORGANIZATION
# This file is distributed under the same license as the PROJECT project.
# FIRST AUTHOR <EMAIL@ADDRESS>, 2018.
#
msgid ""
msgstr ""
"Project-Id-Version: PROJECT VERSION\n"
"Report-Msgid-Bugs-To: EMAIL@ADDRESS\n"
"POT-Creation-Date: 2018-09-05 09:33-0700\n"
"PO-Revision-Date: 2018-09-05 10:49-0700\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language: es_ES\n"
"Language-Team: es_ES <LL@li.org>\n"
"Plural-Forms: nplurals=2; plural=(n != 1)\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=utf-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Generated-By: Babel 2.6.0\n"

#: skill.py:1
msgid "Test skill"
msgstr "Habilidad de prueba"

#: skill.py:2
msgid "Welcome to my test skill"
msgstr "Bienvenido. Tengo más información sobre berenjena"

#: skill.py:3
msgid "Hi {}.How are you doing?"
msgstr "Hola {}. ¿Cómo estás?"

```


Once filled, we need to translate these po files to mo files (Machine Object - byte code files for faster loading by the program). Babel provides a command to compile these po file to mo files. Run the following command to generate the `mo` files for the `po` files.

```
pybabel compile -i locales/en-GB/LC_MESSAGES/skill.po -o locales/en-GB/LC_MESSAGES/skill.mo
pybabel compile -i locales/es-ES/LC_MESSAGES/skill.po -o locales/es-ES/LC_MESSAGES/skill.mo
```

## Step 4 : Use gettext module for translation

As the [documentation](https://docs.python.org/3.6/library/gettext.html#localizing-your-module) mentions, we use the method `gettext.translation`, to load the translated string and assign the gettext function to variable _. The following code can be used for this purpose

```
import gettext

i18n = gettext.translation('skill', localedir='locales', languages=['en-GB','es-ES'])
_ = i18n.gettext

# The variables in gettext.translation method are : 
# - ".mo" domain name, which is "skill"
# - localedir (relative or absolute locale root folder)
# - languages array in which the translation has to be resolved. 
# If no string is present, then the fallback is the actual string passed to _()
```

The languages array can be changed as per the correct locale to be picked during skill loading. Hence the function can be defined on the request interceptor and the locale information from `handler_input.request_envelope.request.locale` can be used to populate this. The corresponding function `**_()**` can be added as a request attribute and passed along in the skill lifecycle. If there is no string translation in the locale specific mo file, then the actual string passed to function **`_()`** is returned.

```
import gettext
from ask_sdk_core.dispatch_components import AbstractRequestInterceptor
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.skill_builder import SkillBuilder

sb = SkillBuilder()

class LocalizationInterceptor(AbstractRequestInterceptor):
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        locale = handler_input.request_envelope.request.locale
        logger.info("Locale is {}".format(locale))
        i18n = gettext.translation(
            'skill', localedir='locales', languages=[locale], fallback=True)
        handler_input.attributes_manager.request_attributes["_"] = i18n.gettext

sb.add_global_request_interceptor(LocalizationInterceptor())                
```

* * *

## Notes

* Make sure that if there is a change in the po file, then the corresponding mo file is regenerated, before testing the skill.
* If the data resides in a different module (eg: data.py), then import the `gettext` function from `gettext` module and assign that as _, to get around module loading errors during initialization. The message is still translated using the request attributes `_()` function and hence doesn't lead to any issue.
    ```
    # In data.py
    from gettext import gettext as _
        
    skill_name = _("Test skill")
    welcome_message = _("Welcome. I have more info on eggplant")
    ```

* If there are multiple strings involved in string formatting, use `_()` on each string to translate initially and then concatenate. 
     ```
     msg = _("message 1")
     msg += _("message 2")
        
     # If both message 1 and message 2 is used together always, then it is 
     # better to concatenate both strings into one before translation.
    ```
     

## References

[1] : https://docs.python.org/3.6/library/gettext.html#internationalizing-your-programs-and-modules


