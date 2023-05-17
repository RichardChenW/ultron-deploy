model_cols = [
    'age_bin',
    'hire_date_bin',
    'emp_time_tra_bin',
    'address_time_tra_bin',
    'bank_time_bin',
    'provider_id _bin',
    'channel_id_bin',
    'routing_number_verify',
    'routing_number_bin',
    'net_monthly_bin',
    'state_final_bin',
    'job_title_size_bin',
    'aff_id_bin',
    'request_amount_bin'
]

MOCK_DATA = {
    "providerId": "string",
    "portfolioId": "string",
    "channelId": "string",
    "createdAt": "string",
    "purchasePrice": "string",
    "channelGrade": "string",
    "request": {
        "referral": {
            "refUrl": "string",
            "ipAddress": "string",
            "affId": "string",
            "subId": "string",
            "test": "string"
        },
        "customer": {
            "personal": {
                "requestAmount": "string",
                "ssn": "string",
                "dob": "1976-06-11",
                "firstName": "string",
                "lastName": "string",
                "address": "string",
                "city": "string",
                "state": "NY",
                "zip": "string",
                "homePhone": "string",
                "otherPhone": "string",
                "dlState": "NY",
                "dlNumber": "string",
                "contactTime": "A",
                "addressMonths": "string",
                "addressYears": "string",
                "rentOrOwn": "O",
                "isMilitary": "false",
                "isCitizen": "string",
                "email": "string",
                "language": "string"
            },
            "employment": {
                "incomeType": "E",
                "payType": "D",
                "empMonths": "string",
                "empYears": "string",
                "empName": "string",
                "empAddress": "string",
                "empCity": "string",
                "empState": "string",
                "empZip": "string",
                "empPhone": "string",
                "empType": "F",
                "hireDate": "string",
                "jobTitle": "string",
                "payFrequency": "B",
                "netMonthly": "string",
                "lastPayDate": "string",
                "nextPayDate": "string",
                "secondPayDate": "string"
            },
            "bank": {
                "bankName": "string",
                "bankPhone": "string",
                "accountType": "C",
                "routingNumber": "string",
                "accountNumber": "string",
                "bankMonths": "string",
                "bankYears": "string"
            },
            "references": "string",
            "userIpAddress": "string"
        }
    }
}
