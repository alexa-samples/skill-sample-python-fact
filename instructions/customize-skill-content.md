# Build An Alexa Fact Skill
<img src="https://m.media-amazon.com/images/G/01/mobile-apps/dex/alexa/alexa-skills-kit/tutorials/quiz-game/header._TTH_.png" />

Build an engaging facts skill about any topic. Alexa will select a fact at random and share it with the user when the skill is invoked.

## Customize the Skill to be Yours

At this point, you should have a working copy of our Fact skill.  In order to make it your own, you will need to customize it with data and responses that you create.  Here are the things you will need to change:

1.  **New data.** You will need to provide a set of facts for your topic.  We recommend a minimum of 25, but a total closer to 100 offers a better experience.

    1.  Open your code file in the online editor: `language_strings.json`

    2.  Search for your locale's `FACTS` array. You can see that it is a simple list of facts. For example, below is the `FACTS` array for the `en` locale.
        ```js
        "en": {
            ...,
            ...,
            "FACTS": [
                "A year on Mercury is just 88 days long.",
                "Despite being farther from the Sun, Venus experiences higher temperatures than Mercury.",
                "On Mars, the Sun appears about half the size as it does on Earth.",
                "Jupiter has the shortest day of all the planets.",
                "The Sun is an almost perfect sphere."
		    ],
            ...
        } 
        ```
        We can add, delete, or edit any of these facts. For example, if I wanted to include an additional fact about how long a day on Venus was, my `FACTS` array would like like so:
        ```js
        "en": {
            ...,
            ...,
            "FACTS": [
                "A year on Mercury is just 88 days long.",
                "Despite being farther from the Sun, Venus experiences higher temperatures than Mercury.",
                "On Mars, the Sun appears about half the size as it does on Earth.",
                "Jupiter has the shortest day of all the planets.",
                "The Sun is an almost perfect sphere.",
                "A single day on Venus is about 117 days."
		    ],
            ...
        } 
        ```

    3.  Update the facts with new facts, or quotes, jokes, etc.

2.  **New sentences to respond to your users.** There are several sentences and responses that you will want to customize for your skill.

    1.  Go back to **[language_strings.json](../lambda/py/language_strings.json).**

    2.  **Look for the a specific locale such as `en`** This is the beginning of the section where you need to customize several text strings for your skill.

    3.  For each prompt, such as `GET_FACT_MESSAGE`, replace the string contents with any sentence you would like Alexa to respond with instead. For example, the following changes will result in Alexa saying "Your fact is", instead of "Here's your fact", when the `GetNewFactHandler` is triggered.
        
        Before:
        ```js
        "en": {
            ...,
            "GET_FACT_MESSAGE": "Here's your fact: {}",
            ...,
            ...
        }
        ```
        After:
        ```js
        "en": {
            ...,
            'GET_FACT_MESSAGE': "Your fact is: {}",
            ...,
            ...
        }
        ```

        


3.  **New language.** If you are creating this skill for another language other than English, you will need to make sure Alexa's responses are also in that language.

    - For example, if you are creating your skill in German, every single response that Alexa makes has to be in German. You can't use English responses or your skill will fail certification.

4. **Once you have customized the skill's data, languages and/or sentences, return to the [Amazon Developer Portal](https://developer.amazon.com/alexa/console/ask?&sc_category=Owned&sc_channel=RD&sc_campaign=Evangelism2018&sc_publisher=github&sc_content=Survey&sc_detail=fact-nodejs-V2_GUI-5&sc_funnel=Convert&sc_country=WW&sc_medium=Owned_RD_Evangelism2018_github_Survey_fact-nodejs-V2_GUI-5_Convert_WW_beginnersdevs&sc_segment=beginnersdevs) and select your skill from the list.**

5.  **Click on "Distribution" in the top navigation to move on to the publishing and certification of your skill.**


[![Next](https://m.media-amazon.com/images/G/01/mobile-apps/dex/alexa/alexa-skills-kit/tutorials/general/buttons/button_next_publication._TTH_.png)](./submit-for-certification.md)
