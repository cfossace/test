import datetime

from mongoengine import Document, EmbeddedDocument
from mongoengine import StringField, ListField
from mongoengine import EmbeddedDocumentField

from django.conf import settings

from crits.core.crits_mongoengine import CritsDocument, CritsSchemaDocument
from crits.core.crits_mongoengine import CritsBaseAttributes, CritsDocumentFormatter
from crits.core.crits_mongoengine import CritsSourceDocument
from crits.core.fields import CritsDateTimeField
from crits.indicators.migrate import migrate_indicator

from crits.vocabulary.indicators import (
    IndicatorAttackTypes,
    IndicatorThreatTypes
)


class IndicatorAction(CritsDocument, CritsSchemaDocument, Document):
    """
    Indicator Action type class.
    """

    meta = {
        "collection": settings.COL_IDB_ACTIONS,
        "crits_type": 'IndicatorAction',
        "latest_schema_version": 1,
        "schema_doc": {
            'name': 'The name of this Action',
            'active': 'Enabled in the UI (on/off)',
            'preferred': 'List of TLOs this is preferred for'
        },
    }

    name = StringField()
    active = StringField(default="on")
    preferred = ListField(StringField())

class EmbeddedAction(EmbeddedDocument, CritsDocumentFormatter):
    """
    Indicator action class.
    """

    action_type = StringField()
    active = StringField()
    analyst = StringField()
    begin_date = CritsDateTimeField(default=datetime.datetime.now)
    date = CritsDateTimeField(default=datetime.datetime.now)
    end_date = CritsDateTimeField(default=datetime.datetime.now)
    performed_date = CritsDateTimeField(default=datetime.datetime.now)
    reason = StringField()

class EmbeddedActivity(EmbeddedDocument, CritsDocumentFormatter):
    """
    Indicator activity class.
    """

    analyst = StringField()
    end_date = CritsDateTimeField(default=datetime.datetime.now)
    date = CritsDateTimeField(default=datetime.datetime.now)
    description = StringField()
    start_date = CritsDateTimeField(default=datetime.datetime.now)

class EmbeddedConfidence(EmbeddedDocument, CritsDocumentFormatter):
    """
    Indicator confidence class.
    """

    analyst = StringField()
    rating = StringField(default="unknown")

class EmbeddedImpact(EmbeddedDocument, CritsDocumentFormatter):
    """
    Indicator impact class.
    """

    analyst = StringField()
    rating = StringField(default="unknown")


class Indicator(CritsBaseAttributes, CritsSourceDocument, Document):
    """
    Indicator class.
    """

    meta = {
        "collection": settings.COL_INDICATORS,
        "crits_type": 'Indicator',
        "latest_schema_version": 3,
        "schema_doc": {
            'type': 'The type of this indicator.',
            'threat_type': 'The threat type of this indicator.',
            'attack_type': 'The attack type of this indicator.',
            'value': 'The value of this indicator',
            'created': 'The ISODate when this indicator was entered',
            'modified': 'The ISODate when this indicator was last modified',
            'actions': 'List [] of actions taken for this indicator',
            'activity': 'List [] of activity containing this indicator',
            'campaign': 'List [] of campaigns using this indicator',
            'confidence': {
                'rating': 'Low/Medium/High confidence',
                'analyst': 'Analyst who provided this confidence level'
            },
            'impact': {
                'rating': 'Low/Medium/High impact',
                'analyst': 'Analyst who provided this impact level'
            },
            'source': ('List [] of source information about who provided this'
                       ' indicator')
        },
        "jtable_opts": {
            'details_url': 'crits.indicators.views.indicator',
            'details_url_key': 'id',
            'default_sort': "created DESC",
            'searchurl': 'crits.indicators.views.indicators_listing',
            'fields': ["value", "ind_type", "threat_type", "attack_type",
                       "created", "modified", "source", "campaign", "status",
                       "id"],
            'jtopts_fields': ["details", "splunk", "value", "type",
                              "threat_type", "attack_type", "created",
                              "modified", "source", "campaign", "status",
                              "favorite", "actions", "id"],
            'hidden_fields': ["threat_type", "attack_type"],
            'linked_fields': ["value", "source", "campaign", "type", "status"],
            'details_link': 'details',
            'no_sort': ['details', 'splunk'],
        }
    }

    actions = ListField(EmbeddedDocumentField(EmbeddedAction))
    activity = ListField(EmbeddedDocumentField(EmbeddedActivity))
    confidence = EmbeddedDocumentField(EmbeddedConfidence,
                                       default=EmbeddedConfidence())
    impact = EmbeddedDocumentField(EmbeddedImpact,
                                   default=EmbeddedImpact())
    ind_type = StringField(db_field="type")
    threat_type = StringField(default=IndicatorThreatTypes.UNKNOWN)
    attack_type = StringField(default=IndicatorAttackTypes.UNKNOWN)
    value = StringField()

    def migrate(self):
        """
        Migrate to the latest schema version.
        """

        migrate_indicator(self)

    def to_csv(self, fields=[], headers=False):
        """
        Generate a CSV row for this Indicator.

        :param fields: The fields to include.
        :type fields: list
        :param headers: To write column headers into the CSV.
        :type headers: boolean
        :returns: str
        """

        # Fix some of the embedded fields
        # confidence
        if 'confidence' in self._data:
            self.confidence = self.confidence.rating
        # impact
        if 'impact' in self._data:
            self.impact = self.impact.rating
        return super(self.__class__, self).to_csv(fields=fields,headers=headers)

    def set_confidence(self, analyst, rating):
        """
        Set Indicator confidence.

        :param analyst: The user setting the confidence.
        :type analyst: str
        :param rating: The level of confidence.
        :type rating: str ("unknown", "benign", "low", "medium", "high")
        """

        ec = EmbeddedConfidence()
        ec.analyst = analyst
        ec.rating = rating
        self.confidence = ec

    def set_impact(self, analyst, rating):
        """
        Set Indicator impact.

        :param analyst: The user setting the impact.
        :type analyst: str
        :param rating: The level of impact.
        :type rating: str ("unknown", "benign", "low", "medium", "high")
        """

        ei = EmbeddedImpact()
        ei.analyst = analyst
        ei.rating = rating
        self.impact = ei

    def add_action(self, type_, active, analyst, begin_date,
                   end_date, performed_date, reason, date=None):
        """
        Add an action to an Indicator.

        :param type_: The type of action.
        :type type_: str
        :param active: Whether this action is active or not.
        :param active: str ("on", "off")
        :param analyst: The user adding this action.
        :type analyst: str
        :param begin_date: The date this action begins.
        :type begin_date: datetime.datetime
        :param end_date: The date this action ends.
        :type end_date: datetime.datetime
        :param performed_date: The date this action was performed.
        :type performed_date: datetime.datetime
        :param reason: The reason for this action.
        :type reason: str
        :param date: The date this action was added to CRITs.
        :type date: datetime.datetime
        """

        ea = EmbeddedAction()
        ea.action_type = type_
        ea.active = active
        ea.analyst = analyst
        ea.begin_date = begin_date
        ea.end_date = end_date
        ea.performed_date = performed_date
        ea.reason = reason
        if date:
            ea.date = date
        self.actions.append(ea)

    def edit_action(self, type_, active, analyst, begin_date,
                    end_date, performed_date, reason, date=None):
        """
        Edit an action for an Indicator.

        :param type_: The type of action.
        :type type_: str
        :param active: Whether this action is active or not.
        :param active: str ("on", "off")
        :param analyst: The user editing this action.
        :type analyst: str
        :param begin_date: The date this action begins.
        :type begin_date: datetime.datetime
        :param end_date: The date this action ends.
        :type end_date: datetime.datetime
        :param performed_date: The date this action was performed.
        :type performed_date: datetime.datetime
        :param reason: The reason for this action.
        :type reason: str
        :param date: The date this action was added to CRITs.
        :type date: datetime.datetime
        """

        if not date:
            return
        for t in self.actions:
            if t.date == date:
                self.actions.remove(t)
                ea = EmbeddedAction()
                ea.action_type = type_
                ea.active = active
                ea.analyst = analyst
                ea.begin_date = begin_date
                ea.end_date = end_date
                ea.performed_date = performed_date
                ea.reason = reason
                ea.date = date
                self.actions.append(ea)
                break

    def delete_action(self, date=None):
        """
        Delete an action.

        :param date: The date of the action to delete.
        :type date: datetime.datetime
        """

        if not date:
            return
        for t in self.actions:
            if t.date == date:
                self.actions.remove(t)
                break

    def add_activity(self, analyst, start_date, end_date,
                     description, date=None):
        """
        Add activity to an indicator.

        :param analyst: The user adding this activity.
        :type analyst: str
        :param start_date: The date this activity started.
        :type start_date: datetime.datetime
        :param end_date: The date this activity ended.
        :type end_date: datetime.datetime
        :param description: Description of the activity.
        :type description: str
        :param date: The date this activity was entered into CRITs.
        :type date: datetime.datetime
        """

        ea = EmbeddedActivity()
        ea.analyst = analyst
        ea.start_date = start_date
        ea.end_date = end_date
        ea.description = description
        if date:
            ea.date = date
        self.activity.append(ea)

    def edit_activity(self, analyst, start_date, end_date, description,
                      date=None):
        """
        Edit activity for an indicator.

        :param analyst: The user editing this activity.
        :type analyst: str
        :param start_date: The date this activity started.
        :type start_date: datetime.datetime
        :param end_date: The date this activity ended.
        :type end_date: datetime.datetime
        :param description: Description of the activity.
        :type description: str
        :param date: The date this activity was entered into CRITs.
        :type date: datetime.datetime
        """

        if not date:
            return
        for t in self.activity:
            if t.date == date:
                self.activity.remove(t)
                ea = EmbeddedActivity()
                ea.analyst = analyst
                ea.start_date = start_date
                ea.end_date = end_date
                ea.date = date
                ea.description = description
                self.activity.append(ea)
                break

    def delete_activity(self, date=None):
        """
        Delete activity from this indicator.

        :param date: The date of the activity entry to delete.
        :type date: datetime.datetime
        """

        if not date:
            return
        for t in self.activity:
            if t.date == date:
                self.activity.remove(t)
                break
