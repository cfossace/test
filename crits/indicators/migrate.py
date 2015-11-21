from crits.core.crits_mongoengine import EmbeddedCampaign

def migrate_indicator(self):
    """
    Migrate to the latest schema version.
    """

    migrate_2_to_3(self)

def migrate_2_to_3(self):
    """
    Migrate from schema 2 to 3.
    """

    if self.schema_version < 2:
        migrate_1_to_2(self)

    if self.schema_version == 2:
        from crits.core.core_migrate import migrate_analysis_results
        migrate_analysis_results(self)
        self.schema_version = 3
        self.save()
        self.reload()

def migrate_1_to_2(self):
    """
    Migrate from schema 1 to 2.
    """

    if self.schema_version < 1:
        migrate_0_to_1(self)

    if self.schema_version == 1:
        old_analysis = getattr(self.unsupported_attrs, 'old_analysis', None)
        self.activity = []
        self.campaign = []
        if old_analysis:
            # activity
            if 'activity' in old_analysis:
                for a in old_analysis['activity']:
                    (analyst, description) = ('', '')
                    (date, start_date, end_date) = (None, None, None)
                    if 'analyst' in a:
                        analyst = a['analyst']
                    if 'description' in a:
                        description = a['description']
                    if 'date' in a:
                        date = a['date']
                    if 'start_date' in a:
                        start_date = a['start_date']
                    if 'end_date' in a:
                        end_date = a['end_date']
                    self.add_activity(
                        analyst=analyst,
                        start_date=start_date,
                        end_date=end_date,
                        date=date,
                        description=description
                    )
            # campaign
            if 'campaign' in old_analysis:
                for c in old_analysis['campaign']:
                    (analyst, description) = ('', '')
                    (date, confidence, name) = (None, 'low', '')
                    if not 'analyst' in c:
                        c['analyst'] = analyst
                    if not 'description' in c:
                        c['description'] = description
                    if not 'date' in c:
                        c['date'] = date
                    if not 'confidence' in c:
                        c['confidence'] = confidence
                    if not 'name' in c:
                        c['name'] = name
                    ec = EmbeddedCampaign(
                        analyst=c['analyst'],
                        description=c['description'],
                        date=c['date'],
                        confidence=c['confidence'],
                        name=c['name']
                    )
                    self.add_campaign(ec)
            # confidence
            if 'confidence' in old_analysis:
                confidence = old_analysis['confidence']
                (analyst, rating) = ('', 'unknown')
                if 'analyst' in confidence:
                    analyst = confidence['analyst']
                if 'rating' in confidence:
                    rating = confidence['rating']
                self.set_confidence(analyst=analyst, rating=rating)
            # impact
            if 'impact' in old_analysis:
                impact = old_analysis['impact']
                (analyst, rating) = ('', 'unknown')
                if 'analyst' in impact:
                    analyst = impact['analyst']
                if 'rating' in impact:
                    rating = impact['rating']
                self.set_impact(analyst=analyst, rating=rating)
        self.schema_version = 2

def migrate_0_to_1(self):
    """
    Migrate from schema 0 to 1.
    """

    if self.schema_version < 1:
        self.schema_version = 1
