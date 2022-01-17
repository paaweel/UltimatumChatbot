# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import random


class ActionUltimatumGame(Action):
    def name(self) -> Text:
        return "action_play_ultimatum"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        user_proposition = tracker.get_slot("ultimatum_user_propsition")
        dispatcher.utter_message(text=f"Podałeś {user_proposition}, oki")

        if self.__agent_decision(user_proposition):
            dispatcher.utter_message(text=f"Akceptuję!")
        else:
            dispatcher.utter_message(text="Nie akceptuję!")

        dispatcher.utter_message(
            text=f"Moja propozycja to: {self.__agent_proposal()}, co Ty na to?"
        )

        return []

    def __agent_decision(self, user_proposition: int) -> bool:
        return bool(random.getrandbits(1))

    def __agent_proposal(self) -> int:
        return random.randint(1, 9)
