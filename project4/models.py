from .app import db


class telecom_customer_churn(db.Model):
    __tablename__ = 'telecom_customer_churn'

    CustomerID                    = db.Column(db.String(64), primary_key=True)
    Gender                        = db.Column(db.String(64))
    Age                           = db.Column(db.Integer) 
    Married                       = db.Column(db.String(64))
    Number_of_Dependents          = db.Column(db.Integer) 
    city                          = db.Column(db.String(64))
    zipcode                       = db.Column(db.Integer) 
    latitude                      = db.Column(db.Float)
    longtitude                    = db.Column(db.Float)
    NumberofReferrals             = db.Column(db.Integer) 
    tenureinMonths                = db.Column(db.Integer) 
    offer                         = db.Column(db.String(64))
    phoneservice                  = db.Column(db.String(64))
    AvgMonthlyLongDistanceCharges = db.Column(db.Float)
    MultipleLines                 = db.Column(db.String(64))
    InternetService               = db.Column(db.String(64))
    InternetType                  = db.Column(db.String(64))
    AvgMonthlyGBDownload          = db.Column(db.Integer) 
    OnlineSecurity                = db.Column(db.String(64))
    OnlineBackup                  = db.Column(db.String(64))
    DeviceProtectionPlan          = db.Column(db.String(64))
    premiumTechSupport            = db.Column(db.String(64))
    StreamingTV                   = db.Column(db.String(64))
    StreamingMovies               = db.Column(db.String(64))
    streamingmusic                = db.Column(db.String(64))
    unlimitedData                 = db.Column(db.String(64))
    contract                      = db.Column(db.String(64))
    paperlessBilling              = db.Column(db.String(64))
    paymentMethod                 = db.Column(db.String(64))
    MonthlyCharge                 = db.Column(db.Float)
    TotalCharges                  = db.Column(db.Float)
    TotalRefunds                  = db.Column(db.Float)
    TotalExtraDataCharges         = db.Column(db.Float)
    TotalLongDistanceCharges      = db.Column(db.Float)
    TotalRevenue                  = db.Column(db.Float)
    CustomerStatus                = db.Column(db.String(64))
    ChurnCategory                 = db.Column(db.String(64))
    ChurnReason                   = db.Column(db.String(64))

    def __repr__(self):
        return '<telecom_customer_churn %r>' % (self.name)

class telecom_zipcode_population(db.Model):
    __tablename__ = 'telecom_zipcode_population'

   
    population     = db.Column(db.Integer) 
    zipcode        = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<telecom_zipcode_population %r>' % (self.name)